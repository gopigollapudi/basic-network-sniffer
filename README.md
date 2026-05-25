# Basic Network Sniffer

A professional Python-based Network Packet Sniffer designed to capture and analyze live network traffic using raw sockets.

## Features

- Real-time packet capturing
- Ethernet frame analysis
- IPv4 packet decoding
- TCP, UDP, and ICMP protocol analysis
- Source and destination IP extraction
- Packet payload inspection
- Hexadecimal and ASCII payload formatting

---

## Technologies Used

- Python 3
- socket
- struct
- textwrap

---

## Project Structure

basic-network-sniffer/
│
├── sniffer.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore

---

## Installation

# Clone Repository
git clone https://github.com/your-username/basic-network-sniffer.git

`md id="y6xg0x"
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux-orange)

# Basic Network Sniffer

# Move to Project Directory
cd basic-network-sniffer

# Run the Project 
Linux
 sudo python3 sniffer.py
 
# Run the Project 
Windows
Open Command Prompt as Administrator
python sniffer.py

# Sample Output

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

# Educational Objectives

- Packet Sniffing
- Network Traffic Monitoring
- TCP/IP Protocol Understanding
- Raw Socket Programming
- Protocol Analysis
- Cyber Security Fundamentals

---

# Future Improvements

- GUI Interface
- Packet Filtering
- PCAP File Export
- Intrusion Detection Features
- Real-time Traffic Visualization

---

# Author

Gopi Gollapudi

---

# License

This project is licensed under the MIT License.

---

# requirements.txt

```txt
# No external libraries required
