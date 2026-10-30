# Domains and Proton Mail

My custom domain provides an identity that can stay the same when the services behind it change. Proton hosts the human email inboxes. Cloudflare handles DNS and web application routing. GitHub stores application source code; it is not the mail provider or the runtime for these apps.

## One domain with several destinations

| Example name | Destination | What decides it |
| --- | --- | --- |
| person@example.com | Proton Mail | MX records for example.com |
| game.example.com | Cloudflare application | Application custom domain and DNS |
| home.example.com | Home Assistant remote service | Remote service DNS instructions |
| help@intake.example.com | Application email intake | MX and email routing for intake subdomain |
| notifications.example.com | Transactional sender | Sender verification and authentication records |

Email and websites coexist because DNS has different record types and names. Changing a website hostname does not require moving your inbox. Keep the root domain mail records pointing to Proton when adding application hosting.

## Replicate the email setup

1. Register a domain and choose a Proton plan that supports the required custom domains and addresses. Put DNS management at Cloudflare if following this architecture; the registrar can remain elsewhere.

2. Add the domain inside Proton Mail. Publish its ownership verification record in Cloudflare DNS, then create the addresses that should receive mail.

3. Follow Proton’s current wizard for MX, SPF, DKIM and DMARC. Use the exact values it generates. Mail-related CNAME records should follow the provider’s DNS-only instructions, rather than being treated as proxied web traffic.

4. Check domain verification in Proton. Test incoming and outgoing mail with an unrelated provider and inspect authentication results before relying on the address.

## What the DNS records do

MX selects the receiving mail service. SPF identifies authorized sending infrastructure. DKIM signs messages. DMARC defines how receivers should treat mail that fails aligned authentication. Publish one SPF policy at each hostname and combine authorized senders as required, rather than adding competing SPF records. [reference 1](09-rollout-and-references.md)

Create purpose-specific addresses for household contact, project support, or privacy requests. These can feed the same inbox, or separate users where needed. An additional address is not automatically a separate mailbox or login.

---

[Back to the guide](../README.md)

