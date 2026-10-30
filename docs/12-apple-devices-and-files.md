# Apple devices everyday controls and files

Apple devices provide the everyday interface to the wider setup. Macs are working computers and access points for files and administration. iPhones provide mobile apps, presence inputs and notifications. HomePods provide Siri and Apple Home hub capabilities. Apple TV provides media playback and, on suitable hardware, home hub and Thread border-router functions.

Home Assistant remains the integration and rule engine. Proton supplies email, storage and outbound VPN services. Synology supplies local storage, Plex and the Home Assistant VM. Using Apple devices does not require moving all these services into Apple's ecosystem.

## Which interface to use

| Task | Everyday interface | System doing the underlying work |
| --- | --- | --- |
| Turn a room's grouped lights on or off | Apple Home, Siri or a physical button | Home Assistant and the actual switches or lights |
| Start a timed bathroom boost | Physical scene button or household control | Home Assistant timer and heating scripts |
| Change household away state | Apple Home presence or manual away control | Home Assistant mode transition |
| Watch Plex media | Plex app on Apple TV | Synology Plex server and storage |
| Read custom-domain mail | Proton app or web interface | Proton Mail |
| Open cloud files | Proton Drive app or supported file interface | Proton Drive |
| Work with NAS files | A permitted network-share connection | Synology |
| Check detailed automation behavior | Home Assistant dashboard and traces | Home Assistant |
| Receive urgent household events | Phone notifications | The configured alerting application and service |

The advantage is familiarity. A household member can say a useful room name or press a button without needing to know whether the device is Zigbee, Wi-Fi or a relay.

## Make names and room controls useful

Expose a curated set of Home Assistant entities through HomeKit Bridge. Prefer controls with a clear household meaning over every diagnostic switch.

The kitchen illustrates this: one light control operates the main light switch, cabinet lighting and sink lighting. It presents a single on/off action while the underlying components keep their separate interfaces. The reviewed template reports on when any constituent is on and requires all three to have known states before reporting availability.

Keep ordinary controls distinct from administration. A helper that says “Heating Away” is useful in Apple Home; an internal timer-restoration flag generally is not.

To reproduce:

1. Get the underlying device working in Home Assistant.
2. Create the room helper or shared action.
3. Test it in Home Assistant.
4. Expose the intended entity through HomeKit Bridge.
5. Give it a concise name and room in Apple Home.
6. Test both touch control and Siri, including an unavailable component.
7. Avoid exposing a device twice through competing native and bridged paths without a deliberate reason.

The actual exported list is a deployment choice. The guide does not assume every helper visible in Home Assistant also appears in Apple Home.

## HomePods Apple TV and Thread

The household includes Apple TVs, second-generation HomePods and HomePod minis. A suitable living-room Apple TV has been the preferred home hub. Compatible Apple equipment can also provide a Thread border router.

These are separate roles:

- The Apple home hub supports Apple Home automation and access.
- A Thread border router links Thread devices with the home IP network.
- The Apple TV media integration exposes playback and remote-control capabilities to Home Assistant.
- HomeKit Bridge exposes selected Home Assistant entities to Apple Home.

Pairing the media integration does not itself provision a Thread network. Follow the supported commissioning path and verify local IPv6 and discovery, especially across network boundaries.

See [Home Assistant and device protocols](06-home-assistant.md).

## Presence and household exceptions

Apple Home's last-person-leaves and first-person-arrives automations operate the Heating Away control. Home Assistant selects minimum heat and later restores the current schedule if departure interrupted scheduled mode.

This avoids copying all the room logic into Apple Home. It also leaves a manual control for a mistaken presence event.

A guest without a tracked phone can still be home when the last tracked person leaves. The existing guest-heating flag is not itself an override of the reviewed away rule. Establish the household policy explicitly.

See [Apple Home presence and television](07-apple-home-and-media.md) for the exact handoff.

## Shortcuts as an optional event source

An iPhone Wake Up alarm triggering towel heating and coffee has been discussed as a possible extension. Starting when the alarm rings was the desired trigger. This is not established as an installed workflow in the reviewed configuration.

A replica could use an appropriate personal automation to call one Home Assistant script, while that script retains the mode checks and timeout behavior. Personal phone automations should supply intent rather than bypass the heating rules.

Keep this separate from the existing scheduled towel preheat and confirmed coffee auto-off.

## Decide where files belong

The confirmed toolkit contains Proton Drive and Synology. Exact folder assignments and the household's use of iCloud Drive, Photos or device backup have not been inventoried. The table below is a decision framework, not a claim that every row is already configured.

| Need | Suitable role to assign | Question to answer |
| --- | --- | --- |
| Small files needed away from home | Cloud storage such as Proton Drive | Which folders should sync and be available offline? |
| Large media libraries | NAS storage | Which server indexes them and who may change them? |
| Shared household documents | Explicitly shared folder or cloud location | Who owns the authoritative copy? |
| Apple-specific synchronization | iCloud features if deliberately used | Which data is synced and is any independent backup needed? |
| Off-site NAS protection | Replication to the family DS920 | Which data and versions are included? |

Do not assume that using iCloud or Proton Drive makes every Mac folder backed up. Likewise, a file visible through a network share normally lives on the NAS, not automatically on the Mac.

For each important category, decide:

1. Where the authoritative copy lives.
2. Which devices can access it.
3. Whether a local or cloud copy is required offline.
4. Who can edit or delete it.
5. What protects it from deletion or failure.

Avoid putting the same working folder under overlapping sync tools without testing the interaction.

## A practical file workflow

For a replica, keep one small shared document collection in the chosen cloud location and a separate NAS media collection. Test a cloud file from the phone, a NAS share from the Mac and a Plex item from Apple TV.

Then test offline access deliberately. A cloud placeholder is not a downloaded file, and NAS access away from home depends on the chosen remote path.

The household's confirmed NAS backup arrangement is replication with a family member's DS920. This does not establish automatic protection of every phone, Mac, cloud folder or Cloudflare application database. See [Maintenance backups and failure behavior](15-maintenance-and-failures.md).

## Verify the daily experience

A useful household acceptance test is simple: can another person turn on the kitchen lights, cancel a boost, understand the away state, watch media, find a shared file and recognize an important alert without opening an administrator console?

Use that test to decide what belongs in Apple Home and what can stay in the detailed dashboard.

---

[Household automation examples](13-household-automations.md) · [Protect and notifications](14-protect-and-notifications.md) · [Back to the guide](../README.md)
