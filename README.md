# Basic Network Sniffer

## Overview

This project implements a basic network packet sniffer using Python and the Scapy library. The program captures network packets in real time and extracts useful information such as source IP address, destination IP address, protocol type, and packet payload. This project demonstrates the fundamentals of network packet analysis and how data travels across a network.

---

## Objective

The objective of this project is to:

* Capture live network packets.
* Analyze packet headers.
* Display source and destination IP addresses.
* Identify the protocol used by each packet.
* Understand the basics of network traffic monitoring.

---

## Technologies Used

* Python 3
* Scapy Library

---

## Project Files

* **sniff.py** – Python program for capturing and analyzing network packets.
* **README.md** – Documentation explaining the project and source code.

---

## Code Explanation

### Importing Scapy

The program imports the required Scapy modules that provide packet capturing and packet analysis functionality.

```python
from scapy.all import *
```

---

### Packet Processing Function

A callback function is created to process every captured packet. It checks whether the packet contains an IP layer before extracting useful information.

```python
def packet_callback(packet):
```

---

### Displaying Packet Information

For each packet, the program displays:

* Source IP Address
* Destination IP Address
* Protocol Number
* Packet Payload (if available)

This information helps understand communication between devices on a network.

---

### Packet Capture

The `sniff()` function continuously captures network traffic and passes each packet to the callback function for processing.

Example:

```python
sniff(prn=packet_callback, count=20)
```

* `prn` specifies the function used to process packets.
* `count=20` captures 20 packets before stopping.

---

## Sample Output

```text
Source IP: 192.168.1.10
Destination IP: 142.250.193.78
Protocol: TCP

Source IP: 192.168.1.10
Destination IP: 8.8.8.8
Protocol: UDP
```

---

## Learning Outcomes

After completing this project, I learned:

* Basics of packet sniffing
* Structure of network packets
* IP addressing
* Network protocols
* Using Scapy for packet analysis
* Python programming for cybersecurity applications

---

## Conclusion

This project provides a basic understanding of packet sniffing and network traffic analysis using Python. It demonstrates how Scapy can be used to inspect packets and extract useful networking information, making it a valuable introduction to network security concepts.
