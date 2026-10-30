# Apple Home presence and television

## Apple Home as the daily control surface

Apple Home and Siri make the system usable without opening an engineering dashboard. The Apple TVs and HomePods also supply home hub capabilities. Home Assistant exposes selected controls through HomeKit Bridge, while retaining the more detailed rules and diagnostics.

One example is a single kitchen light helper that combines a main light switch, cabinet lighting and sink lighting. Apple Home sees one room control even though the underlying devices use different entity types. This is useful for voice commands and an all-off action.

## Presence handoff

The household has a one-touch Heating Away control, connected to Apple Home's last-person-leaves and first-person-arrives automations. Apple handles the presence event; Home Assistant owns the heating transition.

The reviewed implementation is more specific than “turn everything off”:

| Event | Home Assistant action |
| --- | --- |
| Last person leaves while winter scheduling is active | Records that scheduled mode should resume, selects minimum heat and cancels towel holds |
| First person returns after that transition | Reapplies the timetable appropriate to the current time and day |
| Departure while already in Off or Vacation mode | Leaves that operating mode alone; does not record a schedule to restore |
| Restart during an interrupted scheduled absence | Reconciles the stored away state and restoration flag |

Minimum heat uses 16°C generally and 12°C in entrance and utility areas. Automatic boiler-demand control remains available at those targets. This is a temporary setback rather than an unconditional boiler shutdown.

To reproduce the Apple-side connection:

1. Implement and manually test the Heating Away helper and its departure and return actions in Home Assistant.
2. Expose only the household-facing helper through HomeKit Bridge, using a switch-like accessory. Keep internal restoration memory out of Apple Home.
3. Create an Apple Home last-person-leaves automation that turns the away control on.
4. Create a first-person-arrives automation that turns it off.
5. Confirm the participating household members and location settings. Test from the actual phones, then check Home Assistant traces.
6. Test a restart and leaving while already in Off mode, as well as normal departure and return.

Home Assistant remembers whether departure actually interrupted the schedule. Return recalculates the current profile rather than replaying room temperatures saved hours earlier. The Home Assistant configuration does not contain Apple's location automation, so verify both ends of the handoff independently.

Presence is an input, not a complete occupancy model. A guest may remain when tracked phones leave. The current away rule does not check the guest-visiting flag, so that flag should not be mistaken for a presence override.

See [Heating ventilation and energy](08-heating-and-energy.md) for equipment, modes, radiator demand and bathroom rules.

## Apple TV and the actual television

Apple TV has been paired with Home Assistant. The integration can supply media and remote-control functions, depending on the device and app. Add the discovered device or its local address and complete the pairing prompts. Pairing the Apple TV is separate from authorizing the television’s own integration. [reference 9](09-rollout-and-references.md)

A Samsung Frame has also been part of the integration work. If using a television integration, authorize the connection on the TV and verify power and playback behavior independently. Apple TV playback state is not always the same thing as television power state.

Example extension, not a confirmed installed scene: when playback starts after sunset, dim the living room; when paused, raise a low light level. Trigger only on the relevant state transitions, respect manual lighting choices, and test different streaming apps. Keep explicit scene controls for when reported media state is incomplete.

---

[Back to the guide](../README.md)

