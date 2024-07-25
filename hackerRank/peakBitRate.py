from dataclasses import dataclass
import re
import sys

@dataclass
class Transfer:
    start_time: int
    end_time: int
    bitrate: int

def find_peak_bitrate(transfers):
    events = []

    # Create events for all start and end times
    for transfer in transfers:
        events.append((transfer.start_time, transfer.bitrate))
        events.append((transfer.end_time, -transfer.bitrate))
    
    # Sort events first by time, and then by type of event (start before end if times are the same)
    events.sort()

    max_bitrate = 0
    current_bitrate = 0

    print(events)
    # Traverse through events to calculate peak bitrate
    for time, bitrate_change in events:
        current_bitrate += bitrate_change
        max_bitrate = max(max_bitrate, current_bitrate)
    
    return max_bitrate

def parse_transfers(lines):
    transfer_re = re.compile(r"^\s*(\d+)\s+--+\s+(\d+)\s+--+\s+(\d+)\s*$")
    for line in lines:
        match = transfer_re.match(line)
        if match is None:
            raise ValueError(f"Invalid input line: {line}")
        start_time = int(match.group(1))
        end_time = int(match.group(2))
        bitrate = int(match.group(3))
        yield Transfer(start_time, end_time, bitrate)

if __name__ == "__main__":
    # Hardcoded test data
    test_data = [
        "1 --- 3 --- 3",
        "2 --- 5 --- 5",
        "4 --- 6 --- 4",
        "9 --- 10 --- 10",
        "11 --- 12 --- 12"

    ]
    
    # Parsing the hardcoded test data
    transfers = list(parse_transfers(test_data))
    
    # Calculate and print the peak bitrate
    print(find_peak_bitrate(transfers))  # Expected output: 9