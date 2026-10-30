# A practical rollout and references

## Build in a useful order

1. Domain and email: get Proton mail delivery and authentication working before adding app email.

2. Files and device VPN: establish Proton Drive use and test offline files; add Proton VPN on one device before router-wide policies.

3. Home foundation: establish stable networking, NAS storage and a Home Assistant instance with backups.

4. One room: pair a light, sensor and button, then expose only useful controls to Apple Home.

5. Household rules: add presence and a timed override before attempting a whole-house heating system.

6. One web app: deploy a minimal project from GitHub to Cloudflare, test previews, then add its domain and storage.

7. Advanced features: add transactional mail, live sessions, private dashboards and cost calculations when the simpler paths are proven.

## What to keep documented

Keep a short service inventory, which system owns each rule, a list of DNS record purposes, and a record of manual versus automatic deployment steps. Save configuration and migration history in Git. Keep secrets and live personal data outside repositories. For Home Assistant, pull merged configuration into the running system, validate it, and reload the relevant part where supported; some changes require a restart.

This guide describes architecture and replication, not a live account audit. Proton Drive folder choices, specific Plex settings, some TV scenes, and unfinished remote-access and helpdesk work are not represented as verified production configurations. Service menus and plan limits change; use the provider links for the current details.

## Official setup references

[1] Proton custom domains and mail authentication
https://proton.me/support/custom-domain
https://proton.me/support/anti-spoofing-custom-domain

[2] Proton Drive on macOS
https://proton.me/support/proton-drive-macos-setup
https://proton.me/support/proton-drive-macos-on-demand-sync

[3] UniFi VPN client and remote access
https://help.ui.com/hc/en-us/articles/16357883221015-UniFi-Gateway-WireGuard-VPN-Client
https://help.ui.com/hc/en-us/articles/30050679793431-UniFi-Remote-Access-VPN-and-Port-Forwarding

[4] Cloudflare Worker custom domains
https://developers.cloudflare.com/workers/configuration/routing/custom-domains/

[5] Nabu Casa custom-domain remote access
https://github.com/NabuCasa/support/blob/main/src/cloud/remote-access/remote-access-with-custom-domain.md

[6] Cloudflare Tunnel service considerations
https://developers.cloudflare.com/cloudflare-one/faq/cloudflare-tunnels-faq/

[7] Home Assistant HomeKit Bridge
https://www.home-assistant.io/integrations/homekit/

[8] Home Assistant Matter and Thread
https://www.home-assistant.io/integrations/matter/
https://www.home-assistant.io/integrations/thread/

[9] Home Assistant Apple TV
https://www.home-assistant.io/integrations/apple_tv/

---

[Back to the guide](../README.md)

