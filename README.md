# Basic Network Sniffer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Cyber Security](https://img.shields.io/badge/Domain-Cyber%20Security-red)

> A professional Python-based network packet sniffer for capturing and analyzing real-time network traffic using raw sockets.

---

## Overview

The **Basic Network Sniffer** is a cybersecurity project developed in Python to capture and inspect live network traffic directly from the network interface.

This project demonstrates packet sniffing, TCP/IP protocol analysis, raw socket programming, and basic cybersecurity traffic inspection.

The sniffer displays useful packet information such as:

- Source and destination IP addresses
- Source and destination MAC addresses
- TCP/UDP port numbers
- Protocol types
- ICMP packet details
- Packet payload data

---

## Key Features

- Real-time packet capturing
- Ethernet frame analysis
- IPv4 packet decoding
- TCP packet inspection
- UDP packet inspection
- ICMP packet analysis
- Payload extraction
- Hexadecimal and ASCII payload formatting
- Lightweight terminal-based output

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| socket | Raw packet capturing |
| struct | Binary packet parsing |
| textwrap | Payload formatting |

---

## Project Architecture

```text
Network Interface
       ↓
Raw Socket
       ↓
Packet Capture Engine
       ↓
Protocol Analyzer
       ↓
Packet Formatter
       ↓
Terminal Output
```

---

## Project Structure

```bash
basic-network-sniffer/
│
├── sniffer.py
├── README.md
├── requirements.txt
├── License
├── screenshots/
│   └── terminal-output.png
└── diagrams/
    └── architecture.png
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/gopigollapudi/basic-network-sniffer.git
```

### Navigate to the Project Directory

```bash
cd basic-network-sniffer
```

---

## Running the Application

### Linux

```bash
sudo python3 sniffer.py
```

### Windows

Open Command Prompt as Administrator and run:

```bash
python sniffer.py
```

> Note: Raw socket support is limited on Windows. Linux is recommended.

---

## Sample Output

```text
Ethernet Frame:
 - Destination: FF:FF:FF:FF:FF:FF
 - Source: 00:0C:29:AB:CD:EF
 - Protocol: 8

IPv4 Packet:
 - Version: 4
 - Header Length: 20
 - TTL: 64
 - Protocol: 6
 - Source: 192.168.1.5
 - Target: 142.250.183.78

TCP Segment:
 - Source Port: 52314
 - Destination Port: 443
```

---

## Screenshots

![Terminal Output](screenshots/terminal-output.png)

---

## Supported Protocols

| Protocol | Description |
|---|---|
| Ethernet | Data Link Layer protocol |
| IPv4 | Internet Layer protocol |
| TCP | Transmission Control Protocol |
| UDP | User Datagram Protocol |
| ICMP | Internet Control Message Protocol |

---

## Educational Objectives

- Understand packet sniffing concepts
- Learn network traffic monitoring
- Analyze TCP/IP communication
- Explore raw socket programming
- Perform protocol inspection
- Understand cybersecurity monitoring fundamentals

---

## Applications

- Network traffic monitoring
- Packet inspection
- Protocol analysis
- Cybersecurity research
- Intrusion detection learning
- Ethical hacking practice
- Network security education

---

## Future Enhancements

- GUI-based packet analyzer
- Protocol-based packet filtering
- PCAP file export
- Real-time traffic visualization
- Intrusion detection features
- Threat detection mechanisms
- Multi-threaded packet processing
- Scapy integration

---

## Security & Ethical Usage

This project is intended strictly for:

- Educational purposes
- Ethical cybersecurity research
- Authorized network monitoring

Unauthorized packet sniffing or monitoring without permission may violate laws and regulations.

---

## Disclaimer

This project is developed only for educational and ethical cybersecurity learning. The developer is not responsible for any misuse of this tool.

---

## Author

**Gopi Gollapudi**

---

## License

This project is licensed under the MIT License.
