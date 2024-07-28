import json
import logging
from datetime import datetime

import boto3

logger = logging.getLogger()

logger.setLevel(logging.INFO)

client = boto3.client("batch")
JOB_QUE_NAME = "main"


def start_job(vendor, market, bucket_name, region):
    response = client.submit_job(
        jobName=f'fetch-fundamentals-for-{vendor}-job-{datetime.now().strftime("%Y-%m-%d-%H_%M")}',
        jobQueue=JOB_QUE_NAME,
        jobDefinition="finclaw-fetch",
        containerOverrides={
            "command": [
                "python",
                "tools/run_fundamentals.py",
                "--vendor",
                vendor,
                "--market",
                market,
                "--storage-type",
                "s3",
                "--bucket-name",
                bucket_name,
                "--region",
                region,
            ],
        },
        timeout={"attemptDurationSeconds": 15000},  # 2hr 10min
    )
    logger.info("Submitted job: {}".format(response["jobId"]))
    logger.info(f"Response: {response}")
    return response


def lambda_handler(event, context):
    resp = start_job(
        event["vendor"], event["market"], event["bucket_name"], event["region"]
    )
    return {"statusCode": 200, "body": json.dumps(resp)}
