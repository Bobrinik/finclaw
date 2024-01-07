import os
import sys
from datetime import datetime, timedelta
import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple CLI tool for launching fetcher.")
    parser.add_argument("location", help="Pass in .env location")
    args = parser.parse_args()
    print(args.location)
    os.chdir(args.location)

    start = datetime.now().utcnow() - timedelta(days=2)
    end = datetime.now().utcnow()
    print(start)
    print(end)

    subprocess.run(
        f"{sys.executable} -m tradeengine grab --start {start.strftime('%Y-%m-%dT%H:%M:%S')} --end {end.strftime('%Y-%m-%dT%H:%M:%S')} --frequency 1  --market-id-code XNYS -ic p -v twelvedata",
        shell=True)
