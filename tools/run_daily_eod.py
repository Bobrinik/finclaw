from datetime import datetime, timedelta
import subprocess
import argparse


"""
Example:
    finclaw grab --start 2024-01-17 --end 2024-01-17 --frequency 1  --market TO -ic p -v fmp
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process some named arguments.")

    # Define the named arguments
    parser.add_argument('--start', type=str, help='Your name')
    parser.add_argument('--end', type=int, help='Your age')
    parser.add_argument('--vendor', type=str, help='Country of residence')

    # Parse the arguments
    args = parser.parse_args()

    subprocess.run(
        f"finclaw grab --start {args.start} --end {args.end} --frequency 1  --market TO -ic p -v {args.vendor}",
        shell=True)
