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

This project demonstrates the fundamentals of:

- Packet Sniffing
- Network Traffic Monitoring
- TCP/IP Protocol Analysis
- Raw Socket Programming
- Packet Inspection Techniques
- Cyber Security Traffic Analysis

The sniffer captures and analyzes packets in real time and extracts useful information including:

- Source and Destination IP Addresses
- MAC Addresses
- TCP/UDP Port Numbers
- Protocol Types
- ICMP Packet Information
- Payload Data

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
├── LICENSE
├── .gitignore
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

---

### Navigate to the Project Directory

```bash
cd basic-network-sniffer
```

---

## Running the Application

### Linux

Run the program with root privileges:

```bash
sudo python3 sniffer.py
```

---

### Windows

Open Command Prompt as Administrator and execute:

```bash
python sniffer.py
```

> Note: Raw socket support is limited on Windows operating systems.

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

- Understand packet sniffing concepts
- Learn network traffic monitoring techniques
- Analyze TCP/IP protocol communication
- Explore raw socket programming
- Perform protocol inspection and analysis
- Understand cybersecurity monitoring fundamentals

---

## Applications

- Network Traffic Monitoring
- Packet Inspection
- Protocol Analysis
- Cyber Security Research
- Intrusion Detection Research
- Ethical Hacking Practice
- Network Security Education
- Traffic Analysis and Debugging

---

## Future Enhancements

- GUI-based Packet Analyzer
- Protocol-based Packet Filtering
- PCAP File Export Support
- Real-time Traffic Visualization
- Intrusion Detection Features
- Threat Detection Mechanisms
- Multi-threaded Packet Processing
- Scapy Integration
- Live Dashboard Monitoring

---

## Security & Ethical Usage

This project is intended strictly for:

- Educational Purposes
- Ethical Cyber Security Research
- Authorized Network Monitoring

Unauthorized packet sniffing or monitoring without proper permission may violate laws and regulations.

---

## Disclaimer

This project is developed solely for educational and ethical cybersecurity learning purposes. The developer is not responsible for any misuse of this tool.

---

## Screenshots

Add your terminal output screenshots inside:

```bash
screenshots/
```

Example:

```bash
screenshots/terminal-output.png
```

Then display it using:

```md
![Sample Output](screenshots/terminal-output.png)
```

---

## requirements.txt

```txt
# No external dependencies required
```

---

## Author

**Gopi Gollapudi**

---

## License

This project is licensed under the MIT License.
