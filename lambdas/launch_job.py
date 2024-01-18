import boto3
from datetime import datetime, timedelta
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('batch')
JOB_QUE_NAME = "main"

start = datetime.now().utcnow() - timedelta(days=1)
end = datetime.now().utcnow()
start = start.strftime('%Y-%m-%dT%H:%M:%S')
end = end.strftime('%Y-%m-%dT%H:%M:%S')


def start_job(vendor, market):
    response = client.submit_job(
        jobName=f'fetch-{vendor}-job-{datetime.now().strftime("%Y-%m-%d-%H_%M")}',
        jobQueue=JOB_QUE_NAME,
        jobDefinition='finclaw-fetch',
        containerOverrides={
            'command': [
                'python', 'tools/run_daily_eod.py', '--start', start, '--end', end, '--vendor', vendor, '--market',
                market
            ],
        }
    )
    logger.info("Submitted job: {}".format(response['jobId']))
    logger.info(f"Response: {response}")


def lambda_handler(event, context):
    resp = start_job(event["vendor"], event["market"])
    return {
        'statusCode': 200,
        'body': json.dumps(resp)
    }
