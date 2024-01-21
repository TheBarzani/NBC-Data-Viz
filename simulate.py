import json
import time

def simulate_real_time_data(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for i in range(len(data)-1):
        current_record = data[i]
        next_record = data[i+1]

        # Extract TimeStampEpoch values
        current_timestamp = int(current_record["TimeStampEpoch"])
        next_timestamp = int(next_record["TimeStampEpoch"])

        # Calculate time difference in seconds
        time_difference = next_timestamp - current_timestamp

        print(json.dumps(current_record, indent=2))

        # Sleep for the time difference before processing the next record
        time.sleep(time_difference/ 1000000000)

if __name__ == "__main__":
    json_file_path = "data/Exchange_1.json"  # Replace with the actual path to your JSON file
    # simulate_real_time_data(json_file_path)
