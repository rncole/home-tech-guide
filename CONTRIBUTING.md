# Maintaining this guide

Write for someone reproducing a pattern in their own home. Explain purpose, dependencies, integration direction, setup sequence and a simple verification step.

- Distinguish confirmed household use, illustrative examples and work in progress.
- Use example.com and fictional entity names. Never commit credentials, private keys, household addresses, real service URLs, account identifiers, network maps with live addresses, or production data.
- Link to official documentation for changing menus and service limits.
- Document which platform owns an automation. Avoid competing rules in Apple Home and Home Assistant.
- Keep proposed upgrades separate from installed behavior.
- Check relative Markdown links and Mermaid diagrams before merging.

## Structure and editorial rules

- Start readers at docs/getting-started.md and group topics through the README.
- Keep domain and Proton material under services, networking and NAS under infrastructure, household control under home, application development under apps, and maintenance under operations.
- Keep each detailed procedure in one main chapter. Elsewhere, summarize its integration role and link to it.
- Use the Apple Home chapter for presence setup and the heating chapter for heating behavior.
- Use the Protect chapter for alarm and doorbell details, and networking for their connectivity requirements.
- Keep backup and failure procedures in operations; the NAS chapter records the actual replication arrangement.
- When moving content, update internal links and remove obsolete pages rather than retaining forwarding stubs.
- Update previous and next links and the README when changing reading order.
- State whether a claim comes from confirmed use, reviewed source or an example. Keep unresolved live behavior explicit.

This repository is documentation only. It does not deploy services, provision accounts or apply home automation configuration.

## PDF export

When changing chapter order, update export/guide.json as well as README.md and chapter navigation. Run python3 export/build.py --prepare-only to check book links. Review the PDF after changes to tables, figures or layout; export/README.md explains the full build.
