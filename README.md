# Finclaw

Finclaw is a dedicated tool designed to fetch and
update price data for various assets from multiple vendors.
It has been designed to provide uniform data interface across multiple vendors.

### Principles
- Don't use new libraries unless they are accepted by the industry
- Longevity and simplicity over shortness and complexity

### Vendors supported

- Finnhub
- FMP
- TwelveData


### Running on local
```bash
# Load environment variables defined in .env file
source ./tools/load_env.sh
finclaw grab --start 2023-08-13 --end 2023-09-04 --frequency 1 --include-information p --vendor fmp --market TO
```

### Example usage

```bash
finclaw grab --start 2023-08-13 --end 2023-09-04 --frequency 1 --include-information p --vendor fmp --market TO
```

## (WIP) Infra Setup 
- When creating a job definition make sure the user is marked as Priveleged else it will fail with mount error
```text
VolumeDriver.Create: mounting volume failed: b'mount.nfs4: access denied by server while mounting 127.0.0.1:/'
```