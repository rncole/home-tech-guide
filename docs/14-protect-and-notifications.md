# Protect cameras sensors and notifications

UniFi Protect is the household camera and connected-security platform. Its events also become inputs to Home Assistant, allowing security equipment and household automation to cooperate.

The confirmed setup includes Protect cameras and sensors, USL-Smoke smoke/CO alarms, a SuperLink relay on the conventional doorbell and critical phone alerts for doorbell presses and smoke/CO. Exact camera inventory, recorder storage, recording schedules, retention and the application owning each critical alert have not been fully inventoried.

## Separate recording events and responses

| Layer | Responsibility |
| --- | --- |
| Camera or sensor | Captures video or detects a supported condition |
| Protect and recording storage | Manages devices, footage and events as configured |
| Protect phone or browser interface | Views the system with the user's permitted access |
| Home Assistant Protect integration | Exposes supported states and controls for automation |
| Notification rule | Decides what message to send and its urgency |
| Phone and app permissions | Determine how the received notification is presented |

A camera view in Home Assistant is not proof that footage is being retained. A sensor state is not proof that a notification was delivered.

Do not assume Plex or the Synology automatically stores Protect recordings. The recorder and its storage need their own documented configuration.

## A camera setup a friend can reproduce

1. Choose compatible Protect hosting and sufficient recording storage for the intended cameras.
2. Adopt one camera and establish a stable power and network path.
3. Set the camera view and the intended recording behavior.
4. Verify both live viewing and playback of an earlier event.
5. Configure named user access appropriate to who should view or manage cameras.
6. Test phone viewing locally and away from home.
7. Add Home Assistant integration after the basic Protect behavior works.
8. Select only useful entities and events for household automations.

This is a general setup sequence rather than a claim that the household uses continuous recording, motion-only recording or a particular number of retention days.

For a replica, deliberately set the recording mode, storage allocation and viewing permissions. Choose camera placement and framing for the intended household purpose rather than copying another home's layout.

## Protect sensors as automation inputs

Door and window contacts can feed both Protect visibility and Home Assistant rules. The reviewed heating package maps selected contacts to radiator pauses, and hallway motion feeds a lighting rule.

That is a useful division: Protect owns its device integration, while Home Assistant interprets a state in the wider household context. Opening a contact can mean “pause heating in these rooms” without needing Protect to understand the heating timetable.

Keep actual contact state separate from a delayed heating-pause helper. The two-minute open delay and one-minute closing delay are heating policy, not a claim that the physical sensor takes that long to report.

## Smoke and CO alarms

The installed USL-Smoke units detect smoke and CO directly. They provide a local audible warning and report through SuperLink and Protect into Home Assistant.

They are not merely listening for conventional alarms. Other Protect equipment may expose alarm-sound detection, but that is a separate capability.

The household receives critical phone alerts for smoke/CO. The exact app and rule generating those alerts is not yet identified in this guide, so a replica should inspect the actual notification owner rather than enabling duplicate alarms in multiple platforms.

Follow the manufacturer's approved test procedure and verify the local alarm, Protect event, Home Assistant information and phone delivery separately.

## Conventional doorbell with SuperLink relay

An existing doorbell button drives the input of a USL-Relay. A momentary output operates the conventional bell circuit. The relay connects through SuperLink and Protect, and the household receives a critical phone alert when the button is pressed.

This retains an ordinary physical button and bell rather than requiring a replacement video doorbell. The relay has its own supply, and its signal input and bell-switching output have distinct roles.

See [the network chapter](05-network-and-server.md) for the signal path and replication steps. This guide does not provide a universal wiring diagram.

## The household notification map

| Event | Confirmed behavior | Notification owner known here |
| --- | --- | --- |
| Doorbell press | Critical phone alert | Exact app or rule not yet identified |
| Smoke or CO alarm | Critical phone alert | Exact app or rule not yet identified |
| Heavy rain with monitored window open | Home Assistant configuration requests critical interruption level | Home Assistant companion-app action |
| Ordinary rain with monitored window open | Normal configured phone notification | Home Assistant companion-app action |
| Card-game turn | Push and sound confirmed in project use | Web application notification path |
| Helpdesk new request | Queued email acknowledgement implementation | Worker outbox and transactional sender; rollout still needs verification |

Email acknowledgement, browser push, mobile-app push and a local alarm sound are different delivery mechanisms. They should not be treated as interchangeable urgency levels.

The event source also need not be the sending app. A Protect event can trigger another system, while Protect can have its own notifications.

## Test critical alerts as critical alerts

A normal banner is not evidence that critical presentation works. In the responsible app and phone settings, verify the relevant notification permissions and available critical-alert option.

Use an appropriate controlled test:

1. Identify the exact event and which system owns its notification.
2. Confirm that the event appears at the source.
3. Confirm any integration or automation step.
4. Check that the phone receives the correct event text and urgency.
5. Test with the phone locked and away from home.
6. Test the intended behavior under the phone's silent or Focus settings where supported.
7. Check a second event after the first has been dismissed and look for duplicates.

Exact permission screens and platform behavior change; follow current app and iOS instructions. This chapter records the household's confirmed critical-alert behavior without promising that an arbitrary app can request the same privilege.

## Keep notifications useful

Give a message an actionable event and a readable zone. Use stable notification tags or grouping where supported, and distinguish “device unavailable” from “no alarm.”

The current rain alerts include a six-hour snooze. A snooze is appropriate for that nuisance-management use; it is not a reason to apply the same policy to smoke/CO alarms.

Record which app owns each critical event before adding a second response path. Multiple independent paths can be deliberate redundancy, but unexplained duplication makes testing and troubleshooting difficult.

---

[Network and Protect signal paths](05-network-and-server.md) · [Household automation examples](13-household-automations.md) · [Back to the guide](../README.md)
