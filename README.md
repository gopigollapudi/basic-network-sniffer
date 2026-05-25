# Basic Network Sniffer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Cyber Security](https://img.shields.io/badge/Domain-Cyber%20Security-red)

> A professional Python-based network packet sniffer for capturing and analyzing real-time network traffic using raw sockets.

---

## Overview

The **Basic Network Sniffer** is a Python-based cybersecurity project developed to capture and inspect live network traffic directly from the network interface using raw socket programming.

This project demonstrates:

- Packet sniffing
- Network traffic monitoring
- TCP/IP protocol analysis
- Raw socket programming
- Packet inspection techniques
- Cybersecurity traffic analysis

The sniffer extracts useful information including:

- Source and destination IP addresses
- MAC addresses
- TCP/UDP port numbers
- Protocol types
- ICMP packet information
- Payload data

---

## Key Features

- Real-time packet capturing
- Ethernet frame analysis
- IPv4 packet decoding
- TCP protocol inspection
- UDP protocol inspection
- ICMP packet analysis
- Packet payload extraction
- Hexadecimal and ASCII payload formatting
- Lightweight terminal-based implementation
- Structured and readable packet output

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
| Ethernet | Data Link Layer Protocol |
| IPv4 | Internet Layer Protocol |
| TCP | Transmission Control Protocol |
| UDP | User Datagram Protocol |
| ICMP | Internet Control Message Protocol |

---

## Educational Objectives

- Understand packet sniffing concepts
- Learn network traffic monitoring techniques
- Analyze TCP/IP protocol communication
- Explore raw socket programming
- Perform protocol inspection and analysis
- Understand cybersecurity monitoring fundamentals

---

## Applications

- Network traffic monitoring
- Packet inspection
- Protocol analysis
- Cybersecurity research
- Intrusion detection research
- Ethical hacking practice
- Network security education
- Traffic analysis and debugging

---

## Future Enhancements

- GUI-based packet analyzer
- Protocol-based packet filtering
- PCAP file export support
- Real-time traffic visualization
- Intrusion detection features
- Threat detection mechanisms
- Multi-threaded packet processing
- Scapy integration
- Live dashboard monitoring

---

## Security & Ethical Usage

This project is intended strictly for:

- Educational purposes
- Ethical cybersecurity research
- Authorized network monitoring

Unauthorized packet sniffing or monitoring without proper permission may violate laws and regulations.

---

## Disclaimer

This project is developed solely for educational and ethical cybersecurity learning purposes. The developer is not responsible for any misuse of this tool.

---

## Author

**Gopi Gollapudi**

---

## License

This project is licensed under the MIT License.
