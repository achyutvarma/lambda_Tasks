import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    for bucket in event["buckets"]:
        try:
            s3.delete_bucket(Bucket=bucket)
            print("Bucket deleted successfully!", bucket)

        except Exception as e:
            print("Error deleting bucket:", e)

    return {
        "statusCode": 200,
        "body": json.dumps("Bucket deletion attempted!")
    }
