import subprocess
import argparse


"""
Example:
    finclaw grab --start 2024-02-28 --end 2024-06-06 --frequency 1  --market XTSE -ic bs,cf,ic --vendor fmp
    
    Fetches balance sheet, cashflow and income statement
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some named arguments.")

    # Define the named arguments
    parser.add_argument("--vendor", type=str, help="Vendor to use")
    parser.add_argument("--market", type=str, help="Market to grab data from")
    parser.add_argument("--storage-type", type=str, help="What storage backend to use")
    parser.add_argument("--bucket-name", type=str, help="What bucket to use")
    parser.add_argument("--region", type=str, help="What region to use")

    # Parse the arguments
    args = parser.parse_args()
    shared_args = f"--storage-type {args.storage_type} --bucket-name {args.bucket_name} --region {args.region}"
    if args.vendor == "twelvedata":
        raise ValueError("Fundamental data for TwelveData is not supported")
    elif args.vendor == "fmp":
        # finclaw grab --start 2024-02-28 --end 2024-06-06 --frequency 1  --market XTSE -ic bs,cf,ic --vendor fmp
        subprocess.run(
            f"finclaw grab --start 2024-02-28 --end  2024-06-06 --frequency 1  --market {args.market} -ic bs,ic,cf -v {args.vendor} "
            + shared_args,
            shell=True,
        )
    else:
        raise not NotImplementedError(f"{args.vendor} not implemented")
