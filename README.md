# CodeAlpha_Basc_Network_Sniffer

A simple Python-based network sniffer that captures and displays Ethernet frames with their source, destination, protocol, and raw data in hexadecimal format. This program requires root permissions to run as it uses raw sockets.

## Features

- Captures Ethernet frames on the network
- Displays source and destination MAC addresses, Ethernet protocol, and raw data
- Formats and displays raw packet data in hexadecimal for easy analysis

## Requirements

- Python 3
- Root permissions (the program requires `sudo` to access raw sockets)

## How It Works

The program uses a raw socket to capture packets from the network interface. It then parses the Ethernet frame headers to extract and display:

- **Source MAC address**
- **Destination MAC address**
- **Ethernet protocol**
- **Raw data** in hexadecimal format

The program runs in an infinite loop, capturing all incoming packets until manually stopped.

## Code Overview

1. **Socket Setup**: Creates a raw socket with `AF_PACKET` and `SOCK_RAW` to capture all network packets.
2. **MAC Address Formatting**: A helper function, `decode`, converts raw MAC addresses to a human-readable format.
3. **Packet Sniffing**: The program continuously listens for packets, extracts relevant headers, and displays information for each packet.

