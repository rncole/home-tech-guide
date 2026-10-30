# Network server and remote access

The home foundation is a UniFi Dream Machine SE behind an ISP router, with main and IoT networks, and a Synology DS920+ NAS. Synology provides local services and hosts the Home Assistant virtual machine. UniFi Protect handles the camera ecosystem. Macs, iPhones, Apple TVs and HomePods are the principal Apple devices around this network.

## Replicate the foundation

1. Set up the ISP connection and UniFi gateway. If both devices route, understand that there are two NAT boundaries. Reserve stable addresses for key infrastructure.

2. Create a normal device network and, if useful, an IoT network. Add only the cross-network permissions required for management and device integrations. Test one representative device before moving everything.

3. Install and update Synology DSM, create storage and shared folders, and use separate permissions for normal files and service management.

4. Install a supported Home Assistant OS virtual machine in Synology Virtual Machine Manager. Allocate resources appropriate to the workload, connect its network, and pass through the Zigbee coordinator if using USB.

5. Arrange backups of both important NAS data and Home Assistant configuration. A VM snapshot, live database, Git repository and independent backup each cover different failure cases.

## Choose a remote access path per service

Home Assistant has used Nabu Casa remote access with a custom hostname. The provider supplies the service CNAME and certificate-validation CNAME. Follow its generated values and DNS instructions. This is a different path from a Cloudflare Tunnel. [reference 5](09-rollout-and-references.md)

Cloudflare tunnels have also been explored for household services, including Plex. A tunnel connector initiates an outbound connection and can publish a selected service without ordinary inbound port forwarding. Treat this as service-specific plumbing, with appropriate authentication. Check current Cloudflare terms before routing video or large-file traffic through it. [reference 6](09-rollout-and-references.md)

Remote VPN access through UniFi has been worked on, but was not confirmed working end to end. Behind an ISP router, inbound access needs the correct upstream forwarding or supported alternative. A DMZ setting is not a replication requirement. Test from cellular data and prove that both intended home resources and routing work. [reference 3](09-rollout-and-references.md)

## Plex and the television

Plex is part of the media environment, alongside the NAS and Apple TV. A reproducible pattern is a Plex server reading authorized media folders and a Plex client on Apple TV. Exact library paths and remote-streaming settings are deliberately not prescribed here. Start with local playback before adding remote access.

---

[Back to the guide](../README.md)

