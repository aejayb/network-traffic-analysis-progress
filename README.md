# Network Traffic Analysis Learning Journey

## Overview

This repository chronicles a hands‑on learning exercise in network traffic analysis guided by an AI agent.  As part of my cybersecurity training through the SANS Applied Cybersecurity School (ACS), I leveraged ChatGPT in Agent Mode to simulate a mentor who challenged my assumptions and guided me through progressively deeper inspection of live network traffic.  The goal of this repository is to demonstrate both my technical growth and the effective use of AI assistance to accelerate skill development.

Recruiters and mentors reviewing this repository will see evidence of self‑driven learning, curiosity and documentation skills—qualities that translate directly into success in security operations, threat hunting and network analysis roles.

## What We Accomplished

Throughout this exercise, the AI agent and I worked together to:

1. **Select the correct capture interface** – We discussed the purpose of each network adapter (Wi‑Fi, virtual NAT/host‑only, loopback) and chose the VMware **Host‑Only** adapter for clean lab captures.  This ensured that the traffic we analyzed was relevant (Kali ↔ Windows VM) instead of noisy internet chatter.

2. **Baseline normal traffic** – By capturing on my Wi‑Fi adapter, we inspected typical web traffic and learned why most packets appear as `QUIC Protected Payload` or TLS application data.  This reinforced the reality that modern traffic is encrypted and must be analyzed through metadata and behaviour rather than plaintext.

3. **Investigate DNS queries** – We filtered for DNS and learned to follow a domain resolution from query (`A` for IPv4, `AAAA` for IPv6) to response and pivot into subsequent communication.  For example, we resolved `huggingface.co` to its IPs and then filtered the capture to follow TLS handshakes and QUIC sessions to that host.

4. **Dissect a full HTTPS session** – We captured a complete interaction with a web server and analyzed it phase by phase: TCP three‑way handshake, TLS Client/Server Hello (identifying SNI), encrypted application data exchange and graceful connection teardown.  This exercise deepened my understanding of how secure sessions are established and maintained.

5. **Form investigative questions** – The agent pushed me to ask “who initiated this traffic?”, “why is this domain contacted?”, and “is this normal?” instead of passively reading packets.  Adopting this analytical mindset is crucial for real‑world threat hunting and SOC work.

6. **Develop supporting tooling** – As part of this project, I created `analysis.py`, a small Python script that uses [`pyshark`](https://github.com/KimiNewt/pyshark) to parse pcap files and provide simple protocol statistics.  This script demonstrates my ability to extend my analysis beyond the Wireshark GUI and begin automating routine tasks.

## Files in This Repository

| File         | Purpose                                                                      |
|-------------|-------------------------------------------------------------------------------|
| `README.md` | This document, describing the learning journey and context for reviewers.      |
| `analysis.py` | Example Python script showing how to parse a pcap file and count protocols. |

## How This Showcases My Potential

This project underscores my adaptability and eagerness to learn emerging tools.  By actively collaborating with an AI mentor, I was able to:

- **Translate complex concepts into practice**: I didn’t just read about TCP or TLS—I captured, filtered and examined live packets, building muscle memory that will transfer to real SOC environments.
- **Communicate clearly**: Documenting each step in a professional manner highlights my ability to convey technical findings to non‑technical stakeholders—a key skill when interfacing with management or clients.
- **Leverage automation**: Incorporating a Python script hints at my drive to automate repetitive tasks and continue growing as a cybersecurity practitioner.

I am excited to apply these skills to real‑world challenges and to continue leveraging AI responsibly in my professional development.

---

If you have any questions about this learning exercise or my interest in network security, feel free to reach out.  Thank you for reviewing my work!
