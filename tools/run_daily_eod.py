from datetime import datetime, timedelta
import subprocess
import argparse


"""
Example:
    finclaw grab --start 2024-01-17 --end 2024-01-17 --frequency 1  --market TO -ic p -v fmp
    finclaw grab --start 2024-01-17 --end 2024-01-17 --frequency 1  --market-id-code XNYS -ic p -v twelvedata
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process some named arguments.")

    # Define the named arguments
    parser.add_argument('--start', type=str, help='Start date')
    parser.add_argument('--end', type=str, help='End date')
    parser.add_argument('--vendor', type=str, help='Vendor to use')
    parser.add_argument('--market', type=str, help='Market to grab data from')
    # Parse the arguments
    args = parser.parse_args()

    if args.vendor == "twelvedata":
        subprocess.run(
            f"finclaw grab --start {args.start} --end {args.end} --frequency 1  --market-id-code {args.market} -ic p -v {args.vendor}",
            shell=True)
    elif args.vendor == "fmp":
        subprocess.run(
            f"finclaw grab --start {args.start} --end {args.end} --frequency 1  --market {args.market} -ic p -v {args.vendor}",
            shell=True)
    else:
        raise not NotImplementedError(f"{args.vendor} not implemented")

