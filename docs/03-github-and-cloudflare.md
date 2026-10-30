# GitHub and Cloudflare applications

My web projects use GitHub to store and review code and Cloudflare to run it. The helpdesk is a concrete example: a private browser dashboard, APIs, database, attachments and email handling, hosted independently of the home NAS.

The [full helpdesk worked example](10-helpdesk-worked-example.md) follows the actual project structure using sanitized names. This chapter explains the shared building blocks and development workflow.

## What lives where

| Component | Responsibility | Helpdesk example |
| --- | --- | --- |
| GitHub repository | Source, history, branches, reviews and automation definitions | JavaScript, SQL migrations, Wrangler configuration and workflows |
| GitHub Actions | Runs checks and deployment commands | Validate code, deploy Workers and manually apply database migrations |
| Cloudflare Workers | Executes server-side application code | Dashboard/API Worker and separate inbound webhook Worker |
| Browser interface | Renders controls and calls APIs | Dashboard HTML and JavaScript served by the main Worker |
| D1 | Persists structured records | Tickets, messages, audit entries and delivery queues |
| R2 | Stores object bytes | Private attachments; D1 holds metadata |
| Cloudflare Access | Authenticates permitted dashboard users at the edge | Protects the administrator hostname |
| Cloudflare DNS and custom domains | Connect friendly names to applications | helpdesk.example.com and inbound-helpdesk.example.com |
| Resend | Transactional email and the newer receiving path | Incoming-email webhooks and outgoing acknowledgements |
| Proton Mail | Human correspondence | Main-domain inbox and an eventual tested forwarding route |

A private repository does not make a deployed website private. A custom hostname and HTTPS do not provide user authorization. Each layer has its own purpose.

## Pages versus Workers

Pages is one way to host a website; Workers can also serve a browser interface and implement its API. There is no requirement to use both for every app.

The inspected helpdesk uses **Workers**. Its main entry imports the dashboard interface and returns HTML for the root route. API routes in the same Worker read and write D1 and R2. A second Worker handles inbound provider webhooks.

The multiplayer card-game project additionally uses Durable Objects and WebSockets for shared live sessions. The helpdesk does not need that pattern simply because another project uses it.

## Repository structure explains the application

The helpdesk contains:

| Path | Purpose |
| --- | --- |
| `src/index.js` | Main HTTP routes, authorization gate and scheduled outbox entry |
| `src/ui.js` | Browser dashboard |
| `src/email-intake.js` | Earlier direct email-handler intake implementation |
| `src/outbox-processor.js` | Scheduled acknowledgement processing |
| `src/mail-templates.js` | Message content generation |
| `webhook/` | Separate inbound webhook Worker, validation and deployment configuration |
| `migrations/` | Versioned SQL changes |
| `test/` | Automated tests |
| `.github/workflows/` | Validation, deployment and migration automation |
| `wrangler.toml` | Main Worker entry point, bindings, domain and schedule |
| `docs/` | Setup notes, some written at earlier implementation stages |

These paths are useful reading order: start with configuration and entry points, follow a request into storage, then inspect workflows to see how the code reaches Cloudflare.

## Bindings connect code to managed services

A binding gives Worker code a named handle to a Cloudflare resource. In the helpdesk, `DB` is D1 and `ATTACHMENTS` is R2. The two Workers bind to the same application database and attachment bucket.

Ordinary variables describe behavior or public configuration, such as an application label or feature flag. Secrets hold credentials such as mail API keys. A GitHub deployment token belongs in Actions secrets; a runtime email credential belongs in the relevant Worker's secret store.

A database ID is configuration, not a substitute for a credential, but this shareable guide still uses placeholders. Never copy the original project's private account values into a replica.

## A minimal sanitized Wrangler example

This illustrates the main helpdesk structure. It is not the complete source or a ready deployment.

```toml
name = "household-helpdesk"
main = "src/index.js"
compatibility_date = "2026-10-29"
workers_dev = false
preview_urls = false

[[routes]]
pattern = "helpdesk.example.com"
custom_domain = true

[[d1_databases]]
binding = "DB"
database_name = "household-helpdesk"
database_id = "REPLACE_WITH_YOUR_DATABASE_ID"
migrations_dir = "migrations"

[[r2_buckets]]
binding = "ATTACHMENTS"
bucket_name = "household-helpdesk-attachments"

[triggers]
crons = ["*/5 * * * *"]
```

Create the resources first and substitute your own identifiers. The actual project also has application variables and separately configured secrets. A declared binding does not create a populated database or prove its migrations have run.

Disabling default Worker and preview URLs helps keep the private helpdesk from acquiring unintended alternative entry points. Other projects may deliberately use authenticated previews; make that choice per application.

## Separate checks deployment and migrations

The helpdesk's workflows illustrate three different jobs:

| Workflow | Trigger and gate | What it does |
| --- | --- | --- |
| Source validation | Pushes and pull requests | Syntax checks, tests and Wrangler packaging dry run |
| Main deployment | Main-branch pushes or manual run; deployment variable must allow it | Deploys the main Worker |
| Inbound deployment | Manual run; a separate variable must allow it | Deploys from the webhook subdirectory |
| Database migration | Manual run | Applies pending SQL migrations to remote D1 |

Deployment and migration are deliberately separate. Merging code that expects a new table will not create that table just because the Worker deployed successfully.

The deployment workflows use an Actions production environment and Cloudflare credentials stored in repository secrets. The current main deployment validates its entry and UI files before running Wrangler. The wider validation workflow covers more checks. Inspect all relevant workflow results rather than equating one green job with complete validation.

A deployment gate prevents an accidental run before infrastructure is ready; it is not application authentication. Similarly, `ACCESS_ENABLED=true` does not configure Cloudflare Access.

## The development cycle

1. Define a small change and its expected behavior.
2. Create a branch and edit source or SQL as needed.
3. Run checks and open a pull request.
4. Review code, migration effects and the relevant workflow results.
5. Test in a suitable development environment, with separate resources where needed.
6. Merge after review, then run any explicitly required migration and deployment steps in their intended order.
7. Verify the deployed application through its real access path.

I use ChatGPT to help inspect code, implement changes, explain logs and prepare reviews. GitHub retains the concrete changes. A generated explanation should be checked against code and runtime behavior, especially where older comments remain in the project.

For a stateful app, rolling back code does not necessarily reverse database changes or undo outgoing email. Design compatible schema transitions and test side effects separately.

## What code deployment does not finish

A successful Worker deployment does not by itself establish:

- The intended Access policy and identity allowlist.
- The correct database schema and application data.
- Mail-sending domain verification or inbox routing.
- Runtime secrets and feature flags.
- A provider webhook subscription and signature secret.
- Correct custom-domain access and disabled alternative routes.
- End-to-end delivery, attachment access or retry recovery.

Wrangler can manage a configured custom-domain binding during deployment. That is different from moving Proton MX records, configuring a mail provider, or creating an Access application.

## Choose one deployment owner

Cloudflare repository builds and GitHub Actions are both possible deployment approaches. The helpdesk's inspected implementation uses GitHub Actions. Do not enable a second independent production deploy path without understanding which settings and environments each one owns.

For an initial project, the simplest useful milestone is one protected page with a small API. Add the database, attachments and mail after each earlier layer works.

See [the helpdesk worked example](10-helpdesk-worked-example.md) for the complete integration sequence and [application examples and email](04-applications-and-email.md) for the comparison with live multiplayer.

## Official reference points

- [Cloudflare Workers documentation](https://developers.cloudflare.com/workers/)
- [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/)
- [D1 documentation](https://developers.cloudflare.com/d1/)
- [R2 documentation](https://developers.cloudflare.com/r2/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

The application-specific descriptions above are based on inspected repository source, not a live Cloudflare account audit. Follow current provider instructions for changing menus and permissions.

---

[Back to the guide](../README.md)
