# Apple Home presence and television

## Apple Home as the daily control surface

Apple Home and Siri make the system usable without opening an engineering dashboard. The Apple TVs and HomePods also supply home hub capabilities. Home Assistant exposes selected controls through HomeKit Bridge, while retaining the more detailed rules and diagnostics.

One example is a single kitchen light helper that combines a main light switch, cabinet lighting and sink lighting. Apple Home sees one room control even though the underlying devices use different entity types. This is useful for voice commands and an all-off action.

## Presence handoff

The household has a one-touch away control, connected to Apple Home’s last-person-leaves and first-person-arrives automations. Apple Home detects the household presence event; the exposed Home Assistant control changes the heating mode; Home Assistant applies the room rules.

1. Create an away helper or equivalent control in Home Assistant. Define what entering away mode does to the heating and what returning home should restore.

2. Expose a compatible switch-like control through HomeKit Bridge. Verify that operating it manually changes Home Assistant’s state.

3. In Apple Home, create the last-person-leaves automation to activate away mode and the first-person-arrives automation to clear it. Configure the participating household members and required location settings.

4. On return, recalculate the current schedule, guest settings and overrides rather than restoring every room to an arbitrary fixed temperature. Test both transitions with a manual fallback available.

Presence is an input, not a complete occupancy model. Guests may remain when the tracked phones leave. Give guest mode a clear policy and make away state visible so someone can correct an unexpected result.

## Apple TV and the actual television

Apple TV has been paired with Home Assistant. The integration can supply media and remote-control functions, depending on the device and app. Add the discovered device or its local address and complete the pairing prompts. Pairing the Apple TV is separate from authorizing the television’s own integration. [reference 9](09-rollout-and-references.md)

A Samsung Frame has also been part of the integration work. If using a television integration, authorize the connection on the TV and verify power and playback behavior independently. Apple TV playback state is not always the same thing as television power state.

Example extension, not a confirmed installed scene: when playback starts after sunset, dim the living room; when paused, raise a low light level. Trigger only on the relevant state transitions, respect manual lighting choices, and test different streaming apps. Keep explicit scene controls for when reported media state is incomplete.

---

[Back to the guide](../README.md)

