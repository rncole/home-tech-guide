# Application examples and email

## A multiplayer card game

One project grew from a physical-game scorekeeper into an optional virtual card game. Its architecture includes a browser interface, Worker APIs, D1 account and history storage, and Durable Objects with WebSockets for live game sessions. Optional accounts, invitations, saved sessions and push notifications add separate concerns beyond the card rules.

The transferable lesson is to keep authoritative game decisions on the server. Clients submit actions; the server checks whose turn it is, validates the move, updates state, and distributes the result. Persist enough state to resume a session. Browser push uses subscription records and VAPID configuration; the private key remains a server secret.

## A household helpdesk

The newer helpdesk turns messages into tickets, threads replies, stores attachments, and queues acknowledgements. Its design uses Workers, D1 and R2, with a separate transactional email provider for sending. Inbound reliability and queued delivery were still being stabilized at this guide’s date. Follow-ups, metrics, assets, a knowledge base and escalation rules are a development backlog, rather than a finished feature list.

## Keep human email and app email separate

The intended pattern keeps ordinary domain mail at Proton, uses an intake subdomain for machine processing, and authenticates a separate notification subdomain for transactional sending. An existing Proton address can forward into the intake once that path is reliable. The tested intake and production forwarding should not be confused.

1. Leave the main domain MX records at Proton. Configure application intake on a distinct subdomain using the email processing service’s supported routing.

2. Parse incoming mail in server code. Match replies using message identifiers and controlled ticket references, handle attachments and duplicates, and avoid reply loops.

3. Configure the transactional sender, such as Resend, for its own sending subdomain. Add the DNS records it provides and keep its restricted API key in Worker secrets.

4. Record outgoing messages in an outbox and process them with retries and delivery status. Receiving an email, creating a ticket, and sending its acknowledgement are separate success conditions.

5. Before forwarding a real support address, test a new ticket, a threaded reply, duplicate delivery, an attachment, and temporary send failure. Confirm retries do not produce repeated tickets or acknowledgements.

Private dashboards also need authentication and authorization. A custom hostname and HTTPS do not make an app private. Cloudflare Access can provide an access boundary; also check preview and default hostnames so they do not bypass the intended restriction. [reference 4](09-rollout-and-references.md)

---

[Back to the guide](../README.md)

