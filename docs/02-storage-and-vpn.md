# Proton Drive and VPN

## Storage across Apple devices

Proton Drive is the private cloud storage part of my toolkit. The Mac and iPhone are the everyday access points. Synology serves a different role: local storage and always-on services. There is no confirmed automatic Proton Drive to Synology synchronization in this setup; do not assume that one protects the other.

1. Install Proton Drive on the Mac and mobile devices, sign in, and create a simple folder structure for documents and shared files.

2. On macOS, put intended cloud files in the Proton Drive location in Finder. Check sync status before assuming an upload is complete. On-demand files may need downloading before offline use. [reference 2](09-rollout-and-references.md)

3. Test access from another device. For a file you need during travel, explicitly make it available offline and test without a connection.

4. Share selected files or folders using Drive’s sharing controls. Keep a separate backup of irreplaceable material: synchronization can also propagate unwanted changes.

## Two different meanings of VPN

Proton VPN provides an outbound path from a device or the home router to the internet. A home VPN server provides an inbound path from a travelling device to the home network. Subscribing to Proton VPN does not, by itself, provide access back to your home services.

I use Proton VPN with UniFi policy routing, including routing selected NAS traffic through the provider. Some destinations need a direct ISP route; a Synology service exception has been useful. The preference has been to manage this through the UniFi interface rather than custom router scripts.

1. For the simplest version, install Proton VPN on the device and confirm ordinary browsing works.

2. For selected home devices, obtain a provider WireGuard profile and import it as a UniFi VPN client. Create a traffic route selecting only the devices or destinations intended to use it. [reference 3](09-rollout-and-references.md)

3. Define whether traffic must stop if the VPN fails, or may use the ordinary internet connection. Test the actual result with the tunnel disconnected.

4. Check public IPv4 and IPv6 addresses from the routed device. An IPv4 route does not prove IPv6 uses the tunnel. In this setup, IPv6 bypass required separate attention; a P2P block was used, which is not equivalent to routing all IPv6 through Proton.

A VPN also changes DNS and filtering behavior. In one troubleshooting case, a UniFi Apple Private Relay content filter contributed to slow browsing. Compare routing, DNS, and filtering separately before blaming an application.

---

[Back to the guide](../README.md)

