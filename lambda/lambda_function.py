import json
import csv
import uuid
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = 'bld-tseed-workshop-input-semillero-2026-q3-b'
    source_key = 'sample_users.csv'
    dest_bucket = 'bld-tseed-workshop-output-semillero-2026-q3-b'
    dest_prefix = 'laura_retamal/'

    obj = s3.get_object(Bucket=source_bucket, Key=source_key)
    lines = obj['Body'].read().decode('utf-8').splitlines()

    reader = csv.DictReader(lines)

    for row in reader:
        file_name = dest_prefix + str(uuid.uuid4()) + '.json'
        s3.put_object(
            Bucket=dest_bucket,
            Key=file_name,
            Body=json.dumps(row)
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Done')
    }