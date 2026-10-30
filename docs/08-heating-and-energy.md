# Heating ventilation and energy

The heating system combines an ATAG boiler, a boiler relay, room radiator valves, temperature inputs, schedules and exception modes. The installation has sixteen Sonoff TRVs, plus contact sensors and bathroom controls. Copy the control pattern for your heating system rather than assuming this boiler wiring or hydraulic arrangement applies to yours.

## How the heating rules fit together

Each room has a target from its schedule. Helpers supply winter mode, workday and school-holiday behavior, guest occupancy and away mode. Contact sensors can pause heating for open doors or windows. The aggregate room demand determines whether boiler heat is requested. A dashboard helps show which room is keeping the demand active.

Recent room settings included 20 °C when bedrooms are occupied and 18.5 °C overnight, using the valves’ 0.5 °C steps. A separate minimum-heat routine uses lower fallback targets, including cooler entrance and utility areas. These are household choices, not recommended universal setpoints. Remote room sensors can improve representation, but sensor position and adjacent-room airflow can also explain excessive demand.

1. Start with one room and verify sensor readings, valve response and heat-demand reporting. Confirm the boiler interface and system-specific minimum flow and cycling requirements with the installer.

2. Implement the normal schedule first. Add exception rules with explicit precedence: away, open contact, manual boost, guest mode and baseline schedule must have predictable interactions.

3. Add demand aggregation and inspect what happens when all valves stop asking for heat. Verify sensible behavior after restarts and unavailable sensors.

4. Only then roll out the remaining rooms and tune based on measured temperature and demand history.

## Bathrooms and physical controls

The towel rail combines a scheduled morning boost, humidity-triggered heating and a timed manual override. Shower-state logic and school holidays affect the morning behavior. Manual fan operation has a 20-minute timeout; temporary heating boosts also have explicit cancel and expiry behavior.

Moes four-button Zigbee controls provide physical access. One bathroom uses fan toggle, towel boost, boost cancel and light toggle. A bathroom without a towel rail uses the right buttons for room heating boost and cancel. The point is to trigger centralized scripts so wall buttons and dashboard controls follow the same rules.

## Measure the result

HomeWizard supplies meter consumption data. The heating dashboard explores current and historical temperatures, floor averages, room demand hours and boiler operation. Tariff calculations use timestamped consumption with configured time windows, since meter tariff labels do not necessarily match the contract. Seasonal laundry guidance follows those same windows. Newly added cost estimates still need validation against real readings.

---

[Back to the guide](../README.md)

