# Application examples and email

The personal applications share GitHub and Cloudflare building blocks, but use different state and access patterns. The [GitHub and Cloudflare chapter](03-github-and-cloudflare.md) explains the platform; the [full helpdesk example](10-helpdesk-worked-example.md) follows a concrete project from source to email delivery.

## A multiplayer card game

One project grew from a physical-game scorekeeper into an optional virtual card game. Its architecture includes a browser interface, Worker APIs, D1 account and history storage, and Durable Objects with WebSockets for live sessions.

The server owns authoritative game state. Clients submit actions; server logic checks turns and moves and distributes updated state. Invitations, resume behavior and notifications add separate concerns beyond card rules.

## The household helpdesk as a full example

The helpdesk uses a private dashboard Worker and a separate signed inbound-webhook Worker. D1 stores tickets, messages, audit records and pending work. Private R2 storage holds attachments. Resend supplies the newer incoming-email and outgoing-message paths.

Scheduled processing separates receiving an event, creating a ticket and sending an acknowledgement. That is a useful contrast with the game's live session coordination: not every app needs Durable Objects or an always-open connection.

The repository contains an earlier direct Cloudflare email-handler implementation as well as the newer webhook path. Some early project documents lag behind the source. The worked example explains the actual entry points and separates implemented code from verified runtime behavior.

[Read the full helpdesk example](10-helpdesk-worked-example.md).

## Keep human email and application email separate

| Function | Example identity | Responsibility |
| --- | --- | --- |
| Human inbox | help@example.com | Proton correspondence |
| Application intake | help@intake.example.com | Incoming-message processing |
| Application sender | help@notifications.example.com | Authenticated transactional sending |
| Private dashboard | helpdesk.example.com | Human authentication through Access |
| Provider webhook | inbound-helpdesk.example.com | Signed machine requests |

A domain name does not establish any of these access or delivery paths by itself.

Leave main-domain mail at Proton. Verify intake directly before forwarding the established support address. Configure the notification sender independently, and test actual reply headers so responses return to the right place.

## Verify each success separately

A webhook accepted by the server is not necessarily a completed ticket. A ticket created in D1 is not necessarily an acknowledgement sent. A provider's sending acceptance is not necessarily delivery to the inbox.

Use stored processing and outbox states to distinguish those steps. Test duplicates, attachments, wrong-ticket replies and provider failure. Keep the human dashboard private while allowing authenticated machine traffic to the separate webhook.

The helpdesk's newer relationship migration begins follow-up and linking schema work. It does not establish that a metrics dashboard, asset management, knowledge base or escalation system is complete.

---

[Back to the guide](../README.md)
