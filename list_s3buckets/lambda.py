import boto3
import json

def lambda_handler(event, context):
    s3=boto3.resource('s3')
    bucket_names = []
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_names.append(bucket.name)
    return {
        'statusCode': 200,                           
        'body': json.dumps(bucket_names)
    }


# output
Status: Succeeded
Test Event Name: Test

Response:
{
  "statusCode": 200,
  "body": "[\"mkldnjkmdlcmklnjln\", \"newawwsbucket266666666\"]"
}
