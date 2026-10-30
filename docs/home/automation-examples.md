# Household automation examples

Smart home and daily use · [Guide contents](../../README.md) · [Previous](heating-and-energy.md) · [Next](protect-and-notifications.md)

The home automation extends beyond heating. Its common pattern is a useful event, a few explicit conditions, a shared action and a predictable end or override. This chapter describes selected rules in the reviewed Home Assistant configuration; it does not claim they have all been observed live during this documentation update.

## Kitchen lighting as one household control

Three lighting circuits are combined into a single on/off light: the main kitchen switch, cabinet lights and sink lighting.

The template sends commands to the correct entity type for each component. It reports on if any component is on. It reports available only when all three have recognized on/off states.

To reproduce, identify the actual circuits, create the helper or template and test all-on and all-off. Then expose that one useful control through HomeKit Bridge. Retain individual controls where separate use is useful.

This is an interface simplification, not rewiring or a requirement that all bulbs use the same protocol.

## Hallway motion lighting

The reviewed upstairs hallway automation uses a motion sensor, light switch and the sun state.

| Situation | Behavior |
| --- | --- |
| Motion begins after sunset | Turns the hallway light on |
| Nighttime with no motion for five minutes | Turns the light off |
| Daytime with no motion for fifteen minutes | Turns the light off |
| Light has remained on for the relevant interval | Rechecks the no-motion condition |
| Sunrise or sunset | Rechecks under the new day/night rule |

It does not automatically turn the light on for daytime motion. The longer daytime timeout can still clear a light someone turned on manually.

For a replica, start with sensor state and light response, then add the day/night conditions. Test repeated movement, a person standing still and a manually operated light. A motion sensor is not a perfect occupancy detector.

## Blinds with schedule heat shading and manual hold

A hallway blind uses sun state, time, a temperature input and a window contact.

| Condition | Requested position |
| --- | --- |
| Sun below horizon, before 07:00 or at/after 21:00 | Closed |
| Daytime temperature above 28°C | Closed |
| Daytime temperature above 25°C up to 28°C | Half open |
| Other valid daytime reading | Open |

These are the configured thresholds, not universal recommendations. The generic temperature entity's physical location should be verified before interpreting it as indoor or outdoor temperature.

Automatic closing or partial shading requires the associated window to have been closed for thirty seconds. Opening is not subject to the same closed-window condition.

A manual HomeKit operation sets a hold. Temperature and window updates do not immediately undo that choice. The next sunrise, sunset, 07:00 or 21:00 schedule trigger clears the hold and lets normal calculation resume.

This is a useful model for overrides: define when automation may take back control. Do not make a manual command compete with a temperature trigger every few minutes.

## Rain alerts for open windows

The contact-pause package also includes upstairs-window rain alerts. It checks open contacts against current and forecast precipitation.

The reviewed configuration distinguishes ordinary rain from heavier rain, uses critical interruption level for the heavy-rain notification, and includes a six-hour snooze helper and timer. A periodic heavy-rain reminder is separate from the initial event.

The current thresholds include precipitation or forecast values above 0.1 and a heavy-rain check above 5 in the configured weather entities' units. Verify what those entities represent before copying the numbers.

The message identifies which monitored windows are open. In a replica, use clear room names rather than raw entity identifiers.

To test, check each window's state first, then a controlled notification and snooze expiry. Do not change real sensor history simply to manufacture a rain event.

## Rain-aware garden watering

Planter watering runs a daily check at 06:00 and requires at least thirty-six hours since the recorded previous watering, unless that timestamp is missing.

It uses recent rainfall and forecast values:

| Condition | Action |
| --- | --- |
| At least 8 mm recorded in the prior 24 hours | Skip |
| At least 8 mm forecast for the day | Skip |
| At least 3 mm in the short-term forecast total | Skip |
| At least 70% chance and at least 4 mm forecast for the day | Reduced nine-minute watering |
| None of the above | Normal eighteen-minute watering |

The automation waits for the valve's reported on state, runs the chosen duration, requests off and waits for confirmation before updating the last-watered timestamp. A separate rule requests shutoff if the valve remains on for thirty minutes.

That checks reported state, not measured water flow. A separate software timeout also depends on Home Assistant running. For a replica, establish the valve's own behavior on lost power or communications and test a short supervised cycle before the full duration.

Missing weather values in the current rule fall back to zero. That can permit watering rather than conservatively skipping it. Document this behavior and tune it intentionally for the installation.

## Coffee socket auto-off

The coffee pot's smart socket is commanded off after being reported on for one hour. This rule is present independently of the proposed alarm-triggered morning routine.

The plug changes power availability; it does not prove the coffee machine can safely or reliably start brewing when power returns. Check the actual appliance behavior and switching suitability before reproducing any automatic-on routine.

The current one-hour state-duration trigger is not an independently verified hardware cutoff. Restart behavior needs testing; a continuously running software timer should not be assumed to survive every interruption.

## A complete bathroom scenario

This example follows the existing fan and towel logic. Assume normal winter scheduling and automatic heating are enabled, the sensors are valid and no manual towel hold is active.

1. Bathroom humidity rises more than ten percentage points above the dining-room reference.
2. The fan high rule can request high ventilation. Its off-to-on transition starts the twenty-minute timer.
3. The primary bathroom's high condition persists for twenty seconds, so the towel logic recognizes a shower.
4. The shower latch is set and a thirty-minute towel countdown starts. The towel target becomes 28°C.
5. The towel valve may report demand. The boiler relay still obeys its confirmation and minimum-off timing.
6. Continuing humidity does not continually restart the towel countdown.
7. At the fan timer's expiry, high ventilation remains if either bathroom is still above the configured humidity threshold; otherwise high is released.
8. At the towel countdown's expiry, the normal schedule is recalculated.
9. Dry conditions later rearm shower detection. The fan's separate normal dry rule requires both bathrooms below the dry threshold for fifteen minutes when its timer is idle.

The timers are independent. The fan can run longer than the towel boost, or the towel can finish while the room remains humid.

Manual controls fit around that sequence: the primary bathroom boost button starts the shared towel countdown when permitted; cancel clears the boost and hold and restores the schedule when enabled. A qualifying manual setpoint hold protects that choice from routine scheduling. Selecting away/minimum heat cancels the relevant towel overrides.

See [Heating ventilation and energy](heating-and-energy.md) for the detailed precedence, morning-shower latch and restart handling.

## Reuse the design pattern

For another household automation, document five things:

- What starts it.
- What permissions and valid data it requires.
- Which common script or action changes the equipment.
- What ends or cancels it.
- What happens after restart or missing data.

That explanation is more useful to a friend than a large YAML block with household-specific entity IDs.

---

[Guide contents](../../README.md) · [Previous](heating-and-energy.md) · [Next](protect-and-notifications.md)
