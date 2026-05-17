#!/usr/bin/env python3
"""
Simple script demonstrating how to parse a PCAP file and print summary statistics.
This script uses pyshark to iterate through packets in the given capture file and
prints the total number of packets along with a count of the highest layer
protocols observed. You can customize the analysis further to suit your needs.

Usage:
    python analysis.py path/to/your_capture.pcap

You must have pyshark installed:
    pip install pyshark

Note: Parsing large captures can be resource intensive; consider using
PyShark's filtering options to narrow down packets of interest.
"""
import sys

try:
    import pyshark
except ImportError:
    print("pyshark is not installed. Install it with 'pip install pyshark'.")
    sys.exit(1)

def analyze_pcap(pcap_file: str) -> None:
    """Analyze the given pcap file and print protocol statistics."""
    print(f"Opening {pcap_file} ...")
    try:
        capture = pyshark.FileCapture(pcap_file)
    except Exception as e:
        print(f"Error reading {pcap_file}: {e}")
        return

    total_packets = 0
    protocol_counts = {}

    for packet in capture:
        total_packets += 1
        # Highest layer gives the most meaningful protocol for the packet
        highest_layer = packet.highest_layer
        protocol_counts[highest_layer] = protocol_counts.get(highest_layer, 0) + 1

    capture.close()

    print(f"Total packets: {total_packets}")
    print("Protocol counts:")
    for proto, count in sorted(protocol_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"  {proto}: {count}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python analysis.py <pcap_file>")
        sys.exit(1)
    pcap_file = sys.argv[1]
    analyze_pcap(pcap_file)


if __name__ == "__main__":
    main()
