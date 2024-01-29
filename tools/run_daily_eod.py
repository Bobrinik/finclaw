from datetime import datetime, timedelta
import subprocess
import argparse


"""
Example:
    finclaw grab --start 2024-01-17 --end 2024-01-17 --frequency 1  --market TO -ic p -v fmp
    finclaw grab --start 2024-01-17 --end 2024-01-17 --frequency 1  --market-id-code XNYS -ic p -v twelvedata
    
    finclaw grab --start 2024-01-17 --end 2024-01-17 \
    --frequency 1  --market-id-code XNYS -ic p -v twelvedata \
    --storage-type s3 --bucket-name my-bucket-name --region us-east-1
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some named arguments.")

    # Define the named arguments
    parser.add_argument("--start", type=str, help="Start date")
    parser.add_argument("--end", type=str, help="End date")
    parser.add_argument("--vendor", type=str, help="Vendor to use")
    parser.add_argument("--market", type=str, help="Market to grab data from")
    parser.add_argument("--storage-type", type=str, help="What storage backend to use")
    parser.add_argument("--bucket-name", type=str, help="What bucket to use")
    parser.add_argument("--region", type=str, help="What region to use")

    # Parse the arguments
    args = parser.parse_args()
    shared_args = f"--storage-type {args.storage_type} --bucket-name {args.bucket_name} --region {args.region}"
    if args.vendor == "twelvedata":
        subprocess.run(
            f"finclaw grab --start {args.start} --end {args.end} --frequency 1  --market-id-code {args.market} -ic p -v {args.vendor} "
            + shared_args,
            shell=True,
        )
    elif args.vendor == "fmp":
        subprocess.run(
            f"finclaw grab --start {args.start} --end {args.end} --frequency 1  --market {args.market} -ic p -v {args.vendor} "
            + shared_args,
            shell=True,
        )
    else:
        raise not NotImplementedError(f"{args.vendor} not implemented")
