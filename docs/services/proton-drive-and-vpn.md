# Proton Drive and VPN

Online services · [Guide contents](../../README.md) · [Previous](domains-and-email.md) · [Next](../infrastructure/network.md)

## Storage across Apple devices

Proton Drive is the private cloud storage part of my toolkit. The Mac and iPhone are the everyday access points. Synology serves a different role: local storage and always-on services. There is no confirmed automatic Proton Drive to Synology synchronization in this setup; do not assume that one protects the other.

1. Install Proton Drive on the Mac and mobile devices, sign in, and create a simple folder structure for documents and shared files.

2. On macOS, put intended cloud files in the Proton Drive location in Finder. Check sync status before assuming an upload is complete. On-demand files may need downloading before offline use. [reference 2](../references.md)

3. Test access from another device. For a file you need during travel, explicitly make it available offline and test without a connection.

4. Share selected files or folders using Drive’s sharing controls. Keep a separate backup of irreplaceable material: synchronization can also propagate unwanted changes.

## Device VPN and home network routing

Proton VPN supplies an outbound internet path. It does not by itself provide remote access back into the home. Start by installing the supported app on one device and testing ordinary browsing.

The household also uses Proton as a router-hosted VPN client for selected sites across included household users and for selected NAS traffic. That configuration belongs in the [network chapter](../infrastructure/network.md), alongside source-based remote-exit Wi-Fi, rule precedence, direct exceptions, and the observed IPv6 bypass issue.

For either approach, decide whether a failed tunnel should block or permit fallback. Check actual IPv4, IPv6 and DNS behavior rather than relying only on a connected indicator. A device-level VPN can change how traffic interacts with router policies.

---

[Guide contents](../../README.md) · [Previous](domains-and-email.md) · [Next](../infrastructure/network.md)
