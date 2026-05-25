# Basic Network Sniffer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux-orange)
![Status](https://img.shields.io/badge/Status-Active-success)

> A professional Python-based network packet sniffer for capturing and analyzing live network traffic using raw sockets.

---

## Overview

The **Basic Network Sniffer** is a Python-based cybersecurity project designed to capture and analyze real-time network traffic directly from the network interface using raw sockets.

This project provides practical exposure to:

- Packet sniffing techniques
- Network traffic monitoring
- TCP/IP protocol analysis
- Raw socket programming
- Cybersecurity traffic inspection

The sniffer extracts and displays useful packet information such as:

- Source and Destination IP Addresses
- MAC Addresses
- Protocol Types
- TCP/UDP Port Numbers
- ICMP Information
- Packet Payload Data

---

## Features

- Real-time packet capturing
- Ethernet frame analysis
- IPv4 packet decoding
- TCP protocol analysis
- UDP protocol analysis
- ICMP packet inspection
- Packet payload extraction
- Hexadecimal and ASCII payload formatting
- Structured terminal-based output
- Lightweight and efficient implementation

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core Programming Language |
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
Packet Capture
       ↓
Protocol Analyzer
       ↓
Formatted Output
```

---

## Project Structure

```bash
basic-network-sniffer/
│
├── sniffer.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── screenshots/
│   └── terminal-output.png
└── diagrams/
    └── architecture.png
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/gopigollapudi/basic-network-sniffer.git
```

---

### Move to Project Directory

```bash
cd basic-network-sniffer
```

---

## Running the Application

### Linux

Run the program using root privileges:

```bash
sudo python3 sniffer.py
```

---

### Windows

Open Command Prompt as Administrator and run:

```bash
python sniffer.py
```

> Note: Raw socket support is limited on Windows systems.

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

## Supported Protocols

| Protocol | Description |
|---|---|
| Ethernet | Data Link Layer Protocol |
| IPv4 | Internet Layer Protocol |
| TCP | Transmission Control Protocol |
| UDP | User Datagram Protocol |
| ICMP | Internet Control Message Protocol |

---

## Educational Objectives

- Packet Sniffing
- Network Traffic Monitoring
- TCP/IP Protocol Understanding
- Raw Socket Programming
- Protocol Analysis
- Cyber Security Fundamentals

---

## Applications

- Network Traffic Monitoring
- Packet Inspection
- Protocol Learning
- Cyber Security Research
- Intrusion Detection Research
- Ethical Hacking Practice
- Network Security Education

---

## Future Improvements

- GUI Interface
- Packet Filtering
- PCAP File Export
- Intrusion Detection Features
- Real-time Traffic Visualization
- Multi-threaded Packet Processing
- Protocol-based Filtering
- Scapy Integration

---

## Security & Ethical Usage

This project is intended strictly for:

- Educational Purposes
- Ethical Cyber Security Research
- Authorized Network Monitoring

Unauthorized packet sniffing on networks without proper permission may violate legal and ethical guidelines.

---

## Author

**Gopi Gollapudi**

---

## License

This project is licensed under the MIT License.

---

## requirements.txt

```txt
# Python Standard Libraries Used
socket
struct
textwrap
```
