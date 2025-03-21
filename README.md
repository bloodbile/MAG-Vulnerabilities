# 🎀 MAG Vulnerabilities 🎀
## Overview
The web interface of the MAG 250 & MAG 254 IPTV Box contains a critical unauthenticated remote file download vulnerability due to insufficient input validation at the /portaledit.html endpoint. The endpoint allows users to input a URL into the "url" field, intended for external management portals. However, due to insufficient input validation, it allows for any URL to be entered. As a result, an attacker can input malicious URLs pointing to external sources, potentially hosting malware binaries. Additionally, a separate vulnerability allows unauthenticated attackers to trigger a system reboot via a POST request to the /cgi-bin/power.cgi endpoint with the payload;
{'power_type': '2'}
## Impact
By chaining these vulnerabilities, an attacker can enter malicious URLs for the device to process upon system startup, and force retrieval & execution of those URLs by triggering an unauthenticated system reboot, leading to potential malware installation or further exploitation of the device.

![concept.gif](https://raw.githubusercontent.com/bloodbile/MAG-Vulnerabilities/refs/heads/main/concept.gif)
