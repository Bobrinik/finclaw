from datetime import datetime, timedelta
import subprocess

if __name__ == '__main__':
    start = datetime.now().utcnow() - timedelta(days=1)
    end = datetime.now().utcnow()

    subprocess.run(
        f"finclaw grab --start {start.strftime('%Y-%m-%dT%H:%M:%S')} --end {end.strftime('%Y-%m-%dT%H:%M:%S')} --frequency 1  --market TO -ic p -v fmp",
        shell=True)
