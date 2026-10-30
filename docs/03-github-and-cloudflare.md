# GitHub and Cloudflare applications

My personal web projects use GitHub for code and Cloudflare for running it. The browser loads the interface from Cloudflare; requests to an API execute server-side code there. These apps do not require an always-on computer in the house.

| Component | Role in the setup |
| --- | --- |
| GitHub repository | Source files, change history, branches and pull requests |
| Cloudflare Pages or static assets | Delivers the browser interface |
| Cloudflare Workers | Runs APIs and application logic |
| D1 | Stores structured records such as users or tickets |
| Durable Objects | Coordinates shared live session state where used |
| R2 | Stores objects such as attachments where used |
| Cloudflare DNS and custom domains | Connects a friendly hostname to the deployed application |

## Replicate a small application

1. Create a GitHub repository with a working minimal app and a README. Keep credentials out of source files.

2. Choose a deployment model: Pages for a suitable site, or Workers with static assets and server code. Connect the repository to Cloudflare builds, or deploy through GitHub Actions. Use one clear production deployment owner.

3. Set the actual build and deployment commands for that project. For a Worker this may include Wrangler; do not copy blank build settings from a different app without checking its requirements.

4. Create required D1 databases, object storage, or Durable Object bindings. Apply database migrations to the correct environment and keep preview data separate from production.

5. Add secrets in the runtime or deployment secret store. Only intentionally public configuration belongs in browser code. Test the preview, then attach app.example.com using the platform’s custom-domain flow. [reference 4](09-rollout-and-references.md)

6. Test authentication, mobile layout, data persistence and failure paths. Merge through a pull request after validation and verify the production deployment.

## The change workflow

The usual cycle is a feature branch, a focused change, validation, a preview, review, and merge. Cloudflare preview builds have been useful for trying changes on a phone before releasing them. A successful build proves packaging; it does not prove that login, email, migrations, or live multiplayer works.

I use ChatGPT as a development collaborator to inspect code, explain failures, and implement changes through this workflow. The repository remains the source of truth. Review generated changes and validate behavior before merging.

---

[Back to the guide](../README.md)

