# Home Assistant and device protocols

Home Assistant is the integration and automation engine. Apple Home provides familiar controls and Siri. Devices join through their appropriate integration; Home Assistant combines their states into rules. Most of the heating and bathroom logic lives in Home Assistant so it can coordinate devices from different manufacturers.

| Technology | How it fits | Examples |
| --- | --- | --- |
| Zigbee | Local mesh through a coordinator and ZHA | Sonoff radiator valves, Moes buttons and sensors |
| Wi-Fi or Ethernet | IP devices through native integrations | Media players, network systems and some switches |
| Matter over Thread | Matter controller plus a Thread border router | IKEA KAJPLATS lighting |
| HomeKit Bridge | Exports selected Home Assistant entities | Lights, switches and household controls in Apple Home |

## Replicate the integration layer

1. Boot Home Assistant OS and complete onboarding. Establish a stable local address and install the mobile companion app.

2. Add the Zigbee coordinator to ZHA, then pair a small set of devices. Use clear names by room and function. Put the coordinator where interference and radio coverage are manageable.

3. Add native integrations such as Apple TV and HomeWizard. Verify state changes in Home Assistant before writing rules around them.

4. Create helpers for shared modes, timers and overrides. Group multiple physical lights into one useful room control. Add a dashboard that makes both current state and exceptions visible.

5. Add HomeKit Bridge and expose a deliberate list of entities to Apple Home. This is the direction from Home Assistant to Apple Home; HomeKit Device is a different integration for bringing compatible accessories into Home Assistant. [reference 7](09-rollout-and-references.md)

## Matter Thread and the IPv6 lesson

Matter is an application protocol; Thread is a low-power IPv6 network. A Thread border router connects that mesh to the home IP network. Suitable Apple TVs and HomePods provide this role, alongside their Apple Home hub functions. The Apple TV media integration does not itself configure the Thread network. [reference 8](09-rollout-and-references.md)

Pair with the supported phone and Home Assistant commissioning flow, or use Matter multi-admin sharing from an existing controller. Make sure the correct Thread credentials are available. Do not factory-reset everything just because discovery stalls.

In this household, enabling IPv6 on the IoT network resolved a Matter pairing problem. Also check multicast discovery and firewall paths between the phone, controller and border router. Local IPv6 support for Matter is distinct from allowing unrestricted public IPv6 traffic around a VPN policy. [reference 8](09-rollout-and-references.md)

---

[Back to the guide](../README.md)

