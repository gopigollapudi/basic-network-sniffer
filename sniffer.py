# Basic Network Sniffer — Complete GitHub Project Structure

## Project Folder Structure

```bash
basic-network-sniffer/
│
├── sniffer.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── screenshots/
    └── sample-output.png
```

---

# 1. sniffer.py

```python
import socket
import struct
import textwrap

TAB_1 = "\t - "
TAB_2 = "\t\t - "
TAB_3 = "\t\t\t - "

DATA_TAB_1 = "\t "
DATA_TAB_2 = "\t\t "
DATA_TAB_3 = "\t\t\t "


# =========================
# Main Function
# =========================
def main():

    try:
        conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

        print("Network Sniffer Started...\n")

        while True:

            raw_data, addr = conn.recvfrom(65536)

            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)

            print("\nEthernet Frame:")
            print(
                TAB_1 +
                f"Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}"
            )

            if eth_proto == 8:

                ipv4_info = ipv4_packet(data)

                if ipv4_info is None:
                    continue

                version, header_length, ttl, proto, src, target, data = ipv4_info

                print(TAB_1 + "IPv4 Packet:")
                print(
                    TAB_2 +
                    f"Version: {version}, Header Length: {header_length}, TTL: {ttl}"
                )

                print(
                    TAB_2 +
                    f"Protocol: {proto}, Source: {src}, Target: {target}"
                )

                # ICMP
                if proto == 1:

                    icmp_info = icmp_packet(data)

                    if icmp_info:
                        icmp_type, code, checksum, data = icmp_info

                        print(TAB_1 + "ICMP Packet:")
                        print(
                            TAB_2 +
                            f"Type: {icmp_type}, Code: {code}, Checksum: {checksum}"
                        )

                # TCP
                elif proto == 6:

                    tcp_info = tcp_segment(data)

                    if tcp_info:

                        (
                            src_port,
                            dest_port,
                            sequence,
                            acknowledgement,
                            flag_urg,
                            flag_ack,
                            flag_psh,
                            flag_rst,
                            flag_syn,
                            flag_fin,
                            data
                        ) = tcp_info

                        print(TAB_1 + "TCP Segment:")

                        print(
                            TAB_2 +
                            f"Source Port: {src_port}, Destination Port: {dest_port}"
                        )

                        print(
                            TAB_2 +
                            f"Sequence: {sequence}, Acknowledgement: {acknowledgement}"
                        )

                        print(TAB_2 + "Flags:")

                        print(
                            TAB_3 +
                            f"URG: {flag_urg}, ACK: {flag_ack}, "
                            f"PSH: {flag_psh}, RST: {flag_rst}, "
                            f"SYN: {flag_syn}, FIN: {flag_fin}"
                        )

                        print(TAB_2 + "Data:")
                        print(format_multi_line(DATA_TAB_3, data))

                # UDP
                elif proto == 17:

                    udp_info = udp_packet(data)

                    if udp_info:

                        src_port, dest_port, length, data = udp_info

                        print(TAB_1 + "UDP Segment:")

                        print(
                            TAB_2 +
                            f"Source Port: {src_port}, "
                            f"Destination Port: {dest_port}, "
                            f"Length: {length}"
                        )

                        print(TAB_2 + "Data:")
                        print(format_multi_line(DATA_TAB_3, data))

                else:
                    print(TAB_1 + "Other IPv4 Data:")
                    print(format_multi_line(DATA_TAB_2, data))

    except PermissionError:
        print("Run the program as Administrator or Root.")

    except KeyboardInterrupt:
        print("\nProgram Stopped.")

    except Exception as e:
        print(f"Error: {e}")


# =========================
# Ethernet Frame
# =========================
def ethernet_frame(data):

    if len(data) < 14:
        return None, None, None, None

    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])

    return (
        get_mac_addr(dest_mac),
        get_mac_addr(src_mac),
        socket.htons(proto),
        data[14:]
    )


# =========================
# Format MAC Address
# =========================
def get_mac_addr(bytes_addr):

    bytes_str = map('{:02x}'.format, bytes_addr)

    return ':'.join(bytes_str).upper()


# =========================
# IPv4 Packet
# =========================
def ipv4_packet(data):

    if len(data) < 20:
        return None

    version_header_length = data[0]

    version = version_header_length >> 4

    header_length = (version_header_length & 15) * 4

    ttl, proto, src, target = struct.unpack(
        '! 8x B B 2x 4s 4s',
        data[:20]
    )

    return (
        version,
        header_length,
        ttl,
        proto,
        ipv4(src),
        ipv4(target),
        data[header_length:]
    )


# =========================
# Format IPv4 Address
# =========================
def ipv4(addr):

    return '.'.join(map(str, addr))


# =========================
# ICMP Packet
# =========================
def icmp_packet(data):

    if len(data) < 4:
        return None

    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])

    return icmp_type, code, checksum, data[4:]


# =========================
# TCP Segment
# =========================
def tcp_segment(data):

    if len(data) < 14:
        return None

    (
        src_port,
        dest_port,
        sequence,
        acknowledgement,
        offset_reserved_flags
    ) = struct.unpack('! H H L L H', data[:14])

    offset = (offset_reserved_flags >> 12) * 4

    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1

    return (
        src_port,
        dest_port,
        sequence,
        acknowledgement,
        flag_urg,
        flag_ack,
        flag_psh,
        flag_rst,
        flag_syn,
        flag_fin,
        data[offset:]
    )


# =========================
# UDP Segment
# =========================
def udp_packet(data):

    if len(data) < 8:
        return None

    src_port, dest_port, length, checksum = struct.unpack(
        '! H H H H',
        data[:8]
    )

    return src_port, dest_port, length, data[8:]


# =========================
# Format Multi-line Data
# =========================
def format_multi_line(prefix, string, size=20):

    if isinstance(string, bytes):

        lines = []

        for i in range(0, len(string), size):

            chunk = string[i:i + size]

            hex_part = ' '.join(f'{byte:02x}' for byte in chunk)

            text_part = ''.join(
                chr(byte) if 32 <= byte <= 126 else '.'
                for byte in chunk
            )

            lines.append(
                f"{prefix} {hex_part.ljust(size * 3)}  {text_part}"
            )

        return '\n'.join(lines)

    return textwrap.fill(
        string,
        width=80,
        initial_indent=prefix,
        subsequent_indent=prefix
    )


# =========================
# Run Program
# =========================
main()
```

---

# 2. README.md

````markdown
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

### Clone Repository

```bash
git clone https://github.com/your-username/basic-network-sniffer.git
````

### Move to Project Directory

```bash
cd basic-network-sniffer
```

---

## Run the Project

### Linux

```bash
sudo python3 sniffer.py
```

### Windows

Run Command Prompt as Administrator.

```bash
python sniffer.py
```

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
```

---

## Educational Objectives

* Packet Sniffing
* Network Traffic Monitoring
* TCP/IP Protocol Understanding
* Raw Socket Programming
* Protocol Analysis
* Cyber Security Fundamentals

---

## Future Improvements

* GUI Interface
* Packet Filtering
* PCAP File Export
* Intrusion Detection Features
* Real-time Traffic Visualization

---

## Author

Gopi Gollapudi

---

## License

This project is licensed under the MIT License.

````

---

# 3. requirements.txt

```txt
# No external libraries required
````

---

# 4. .gitignore

```gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
.env
venv/
.env/
.vscode/
.idea/
*.log
```

---

# 5. LICENSE

```text
MIT License

Copyright (c) 2026 Gopi Gollapudi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

# GitHub Upload Commands

```bash
git init
git add .
git commit -m "Initial Commit - Basic Network Sniffer"
git branch -M main
git remote add origin https://github.com/your-username/basic-network-sniffer.git
git push -u origin main
```

---

# Recommended GitHub Repository Details

## Repository Name

```text
basic-network-sniffer
```

## Description

```text
Professional Python-based network packet sniffer for capturing and analyzing live network traffic using raw sockets.
```

## Topics/Tags

```text
python
cyber-security
network-sniffer
packet-analyzer
socket-programming
ethical-hacking
network-security
packet-sniffing
```
