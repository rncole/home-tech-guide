# Maintenance backups and failure behavior

Keeping it running · [Guide contents](../../README.md) · [Previous](../apps/helpdesk-example.md) · [Next](../references.md)

This chapter describes how to keep the combined setup understandable and dependable. It is a maintenance and dependency guide, not a recovery manual containing private access details.

The confirmed off-site backup arrangement uses a family member's **Synology DS920**, with replication between that system and the household NAS. The exact package, data selection, schedule, direction of each job and retained versions are not established here.

## Document the replication arrangement

For each job, record privately:

| Item | Why it matters |
| --- | --- |
| Source and destination | Makes the protected copy and restore location explicit |
| Included shares or application data | Establishes what is actually protected |
| Frequency and last successful run | Shows how much recent work could be absent |
| Version or snapshot retention | Determines whether an earlier state can be recovered |
| Deletion handling | Establishes whether unwanted deletions propagate |
| Credentials and encryption-key custody | Determines who can operate or restore the backup |
| Restore-test result | Proves more than a completed transfer |

These fields describe what a replica needs, not a claim that the household's replication uses bidirectional synchronization or a specific Synology package.

A second NAS at another home provides a different physical location. It does not automatically protect files that were never included in a job, phone data, Proton Drive or Cloudflare D1/R2.

## Distinguish the data protection layers

| Layer | Protects or records | Separate check required |
| --- | --- | --- |
| NAS disk redundancy | Selected disk-failure scenarios | Actual storage layout and health |
| Local snapshots where configured | Earlier filesystem states | Retention and same-device exposure |
| Family-NAS replication | Selected data at another site | Job coverage, versioning and restoration |
| Home Assistant backup | Supported HA configuration and data | Copy location and usable restore |
| GitHub history | Selected source and configuration text | Runtime data and secrets are elsewhere |
| Cloud storage synchronization | Files across cloud clients | Independent protection against unwanted change |
| Application database or object protection | Cloudflare application state | Provider capabilities and chosen exports or backups |

Do a small test restore to a separate location. Check the recovered file, not only the task log. For applications, a useful restore also needs compatible code, schema and any separately retained configuration.

## Suggested maintenance rhythm

The following is a suggested operating routine, not an inventory of already scheduled household tasks.

| When | Useful check |
| --- | --- |
| After a meaningful change | Verify the affected user flow and inspect errors |
| Periodically | Review failed backup and replication jobs, storage health and service availability |
| Before major updates | Confirm a recent usable backup and note affected dependencies |
| After NAS restart | Check Home Assistant VM, coordinator access, Plex and network services |
| After router or VLAN changes | Check discovery, device control, remote paths and IPv4/IPv6 routing |
| At season or calendar changes | Review heating profiles, school holidays and electricity time windows |
| Before certificate or domain expiry | Verify renewal status, installation and correct service use |
| Occasionally | Perform restore and notification tests |

Update related systems deliberately. Changing DSM, Home Assistant and routing simultaneously makes it harder to explain a new fault.

## Certificates and custom domains

Certificate issuance, renewal, installation and service reload are distinct steps. A successful renewal task does not prove that the application is presenting the renewed certificate.

The household has worked with DSM certificate configuration, custom hostnames and provider-managed remote access. Earlier certificate scripts and tasks should not be treated as a verified current renewal system without checking the actual service path.

For each service, record who manages its certificate: the hosted platform, remote-access provider or a local process. Remove obsolete task dependencies only after identifying what currently uses them.

Keep domain renewal and DNS access maintained. A domain connects many independent services even though they are hosted in different places.

## What depends on what

| Failure or outage | Likely affected behavior | What must not be assumed |
| --- | --- | --- |
| Home internet unavailable | Cloud apps, remote access, cloud weather, email and remote notification paths | That every local integration stops, or that all local integrations continue |
| NAS unavailable or restarting | Home Assistant VM, native Plex and NAS shares | That only storage is affected |
| Home Assistant unavailable | Central heating coordination, shared scripts, sensor synchronization and HA timers | That wall scene buttons still execute HA actions |
| Zigbee coordinator unavailable | ZHA communication and central control of paired devices | That a valve's last state equals a safe fallback |
| Protect host or SuperLink gateway unavailable | Network visibility and related event paths | That a connected-security alert will still reach the phone |
| Proton tunnel unavailable | Policy-routed traffic | Whether a rule blocks or falls back without testing |
| Inter-site tunnel unavailable | Remote-exit Wi-Fi and site-dependent services | That ordinary main-network traffic must fail too |
| Family NAS or remote link unavailable | Replication and remote family services | That the last remote copy is current |
| Cloudflare application unavailable | Helpdesk or game access and processing | That a GitHub copy contains the runtime data |
| Transactional email provider unavailable | Intake or outgoing delivery | That a stored ticket means its acknowledgement arrived |
| Phone offline or permissions changed | Remote notification presentation | That an event log proves the phone alerted |

These are dependency expectations and test prompts, not a claim of measured failover for every component.

## Local operation and independent controls

Some functions can remain local when the internet is down: Zigbee communication with Home Assistant, local IP device access and local Plex playback can be possible while their local dependencies remain healthy. Authentication and service-specific cloud dependencies can still matter.

USL-Smoke alarms have their own local detection and audible warning. Network reporting is an additional chain. Their installation and self-test requirements remain those of the alarm manufacturer.

The doorbell's relay action, local bell and phone alert should be tested independently. Do not assume that a smart relay preserves the original bell function under every gateway or power failure.

Heating valves can have their own local controls, but the reviewed boiler-demand coordination depends on Home Assistant. This guide does not establish an independent fallback thermostat or a verified heating failover arrangement.

## Timer and restart behavior

The towel package explicitly reconciles restored countdowns and schedule state after startup. The away package also reconciles saved mode-restoration state.

Other rules use state-duration triggers or delays. Those should not be described as persistent hardware safety timers. Garden watering's separate thirty-minute software shutoff, coffee's one-hour auto-off and the fan timer all deserve controlled restart testing.

For a replica, classify each timer: persistent state, reconstructed deadline, or a running automation that can be interrupted. Define the intended response when an expiry occurs while the automation host is offline.

## Power and UPS

A UniFi UPS has been discussed and UPS-related entities have appeared in the wider inventory. Its actual load, connected equipment, runtime and automated shutdown behavior have not been confirmed.

To document a replica, list which gateway, switches, access points, NAS and gateways receive backup power. Then determine whether supported shutdown coordination exists. Powering the NAS alone does not keep notifications working if the network loses power.

No specific outage endurance is claimed for this household.

## A small failure test is more useful than a promise

Choose one reversible test at a time: interrupt a test VPN route, restart the VM during a nonessential timer, disconnect a noncritical sensor, or restore a sample file from replication.

Record the observed result and restore normal operation. Avoid manufacturing alarm or heating faults simply to fill in a table.

The goal is a short list of proven behaviors and remaining assumptions. Keep private recovery instructions elsewhere.

---

[Guide contents](../../README.md) · [Previous](../apps/helpdesk-example.md) · [Next](../references.md)
