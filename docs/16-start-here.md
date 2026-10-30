# Start here with a smaller setup

You can reproduce useful parts of this system without purchasing the full household stack. Choose the result you want first, then add only its dependencies.

The three paths below are suggested starting points. They are not additional installed systems or a shopping list of current product recommendations.

## Path one private email and files

**Result:** a stable custom-domain email address and files available on a computer and phone.

Start with:

- A registered domain and access to its DNS.
- A Proton plan supporting the intended mail domain and addresses.
- Proton Mail and Drive on the chosen devices.
- A clear distinction between shared files, offline files and independent backup.

Sequence:

1. Verify the domain and create the receiving addresses.
2. Configure and test MX and mail authentication.
3. Send and receive using the custom address from the phone and computer.
4. Put a small document set in Drive.
5. Test sharing and an offline file.
6. Decide how important files are protected independently.

You do not need a UniFi gateway, NAS, Home Assistant or web application for this path.

Read [Domains and Proton Mail](01-domains-and-email.md), [Proton Drive and VPN](02-storage-and-vpn.md) and [Apple devices and files](12-apple-devices-and-files.md).

## Path two an Apple-friendly smart home

**Result:** one room with useful physical, phone and voice controls.

Start with:

- A supported Home Assistant host.
- A suitable coordinator if using Zigbee.
- One controllable light or switch, one useful sensor and optionally a physical button.
- Apple Home and a suitable home hub for the intended Apple features.

The household uses a Synology VM, but a friend does not need to reproduce that hosting choice merely to automate a room.

Sequence:

1. Prove the device works in Home Assistant.
2. Create one shared action with a clear end or override.
3. Expose the useful control through HomeKit Bridge.
4. Test Apple Home, Siri and the physical button.
5. Add a timer or sensor rule.
6. Inspect restart and unavailable-device behavior.
7. Expand to another room only after the first is understandable.

Whole-house radiator control, a boiler relay and multi-VLAN Matter networking are later milestones. Establish the heating installation's requirements separately before copying that architecture.

Read [Home Assistant](06-home-assistant.md), [Apple Home](07-apple-home-and-media.md) and [Household automations](13-household-automations.md).

## Path three a private custom web application

**Result:** a private page with an API and a persistent record, under your own hostname.

Start with:

- A GitHub repository and a Cloudflare account.
- A domain for the chosen production hostname.
- A minimal Worker and one small data model.
- An access policy for a private application.

Sequence:

1. Serve one page and protect it.
2. Add a create-and-read operation using D1.
3. Validate source through GitHub Actions.
4. Deploy through one deliberate workflow.
5. Attach the custom hostname and test unauthorized access.
6. Add private attachments only if needed.
7. Add email after the manual application works.

Do not start with every helpdesk feature. The full example shows why intake, signatures, retries, reply routing and queued delivery add work beyond the interface.

Read [GitHub and Cloudflare](03-github-and-cloudflare.md) and [the helpdesk example](10-helpdesk-worked-example.md).

## Add a NAS when it solves a storage or server need

A NAS is a useful additional path for local files, media and always-on services. Start with protected shares, one off-site copy and one Plex library playing locally. Add the Home Assistant VM and remote services independently.

The household protects selected NAS data through replication with a family member's DS920. A replica needs its own arrangement and a restore test.

Read [Synology and Plex](11-synology-and-plex.md).

## What costs money

This is a cost-planning map rather than a price quote. Current prices, included allowances and subscription requirements must be checked with the providers.

| Area | Typical initial cost | Ongoing cost or allowance to check |
| --- | --- | --- |
| Domain and mail | Usually little dedicated hardware | Domain renewal and Proton plan |
| Cloud files | Existing devices may suffice | Storage quota and any paid plan |
| Router and Wi-Fi | Gateway, switching and access points as needed | Power, replacement and internet service |
| Home Assistant | Host, coordinator and selected devices | Optional remote-access service, batteries and maintenance |
| Protect | Supported host, recording storage, cameras and sensors | Storage replacement and power; verify optional paid services separately |
| Synology | NAS and disks, plus remote storage arrangement | Power, disks, backup capacity and replacement |
| Plex | Server and playback devices if not already owned | Verify subscription needs for desired features |
| Cloudflare app | Often little local hardware | Workers, D1, R2, Access and usage limits for the selected plans |
| Transactional mail | Sending-domain setup | Provider sending and receiving allowances |

Avoid double-counting shared hardware. A NAS may host both Plex and Home Assistant; an Apple TV may be both media client and a home hub. Shared hardware also creates shared failure dependencies.

## Budget time as well as money

| Layer | Initial work | Ongoing attention |
| --- | --- | --- |
| Email | Domain records, addresses and tests | Renewal, account access and sender changes |
| One room | Pairing, names and a simple rule | Batteries, overrides and occasional troubleshooting |
| Whole-house automation | Rule precedence, equipment behavior and acceptance tests | Seasonal changes, failed devices and updates |
| NAS and media | Storage, permissions, backup and libraries | Health, updates and backup results |
| Web application | Code, access, storage and deployment | Changes, runtime failures, migrations and usage |
| Application email | Intake, sender setup and delivery states | Retries, failures, provider changes and reply routing |

No fixed maintenance-hour estimate is implied. Complexity depends on how many independent systems and exceptions you add.

## A network policy matrix to fill in

The household uses main, IoT, Kids and remote-exit network roles. This table is a planning template, not an export of the deployed firewall.

| Source | Destination | Decision to record |
| --- | --- | --- |
| Main devices | NAS and household controls | Which users and services should be permitted? |
| Home Assistant | IoT devices and Protect | Which integration paths and discovery are required? |
| IoT devices | Main computers or NAS | Which specific exceptions are needed? |
| Kids network | Local media or printer | Which household resources should be reachable? |
| Remote Exit network | Internet | Which tunnel wins and what happens on failure? |
| Included household sources | Proton-selected sites | Which destinations, exclusions and IP families are covered? |
| Remote site | Local private services | Which services are intended to be accessible? |

Translate the decisions into actual supported policies and test them. A separate SSID alone does not enforce the matrix.

## A quick handover for another household member

Keep a small everyday explanation alongside the technical guide:

- How to turn on grouped lights and operate the physical buttons.
- Where Heating Away, Scheduled, Minimum Heat and Off differ.
- How to cancel a boost and see whether a timer is active.
- Where shared files live and how to play media.
- Which app shows cameras and which notifications are critical.
- Who maintains the system and how to report a problem.

This is household usability, not a list of passwords. The most successful first replica is one that another person can use without knowing the architecture.

---

[Maintenance and failures](15-maintenance-and-failures.md) · [Rollout and references](09-rollout-and-references.md) · [Back to the guide](../README.md)
