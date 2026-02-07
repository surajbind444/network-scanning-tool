
# network-scanning-tool
=======
# Network Scanning Tool (Python)

## Overview
A Python-based network scanning tool developed in Kali Linux.  
The tool performs TCP port scanning using socket programming and integrates Nmap to identify open ports and running services.

## Tools & Technologies
- Python 3
- Socket Programming
- Nmap
- python-nmap
- Kali Linux

## Features
- Identifies open TCP ports
- Detects running services on target hosts
- Uses virtual environment for dependency management
- Designed for ethical and educational use

## Files
- socket_scanner.py – Basic TCP port scanner
- nmap_scanner.py – Advanced scanner with Nmap integration

## Usage
````bash
source venv/bin/activate
python socket_scanner.py
python nmap_scanner.py

