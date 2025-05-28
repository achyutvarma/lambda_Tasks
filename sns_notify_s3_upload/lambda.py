import json
import boto3
import urllib.parse

sns = boto3.client('sns')

# Replace with your actual SNS Topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:your-region:your-account-id:FileUploadNotifications'

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    for record in event['Records']:         # An S3-triggered Lambda event may have multiple records (files uploaded in a batch).
                                            # This loop handles each one individually.
        bucket = record['s3']['bucket']['name']  # Extract Bucket and File Info

        key = urllib.parse.unquote_plus(record['s3']['object']['key'])  #Used to decode URL-encoded strings. S3 object keys may contain special characters encoded (e.g., spaces become %20).
        
        message = f"A new file has been uploaded to your S3 bucket:\n\nBucket: {bucket}\nFile: {key}"
        subject = "S3 File Upload Notification"
        
        try:
            response = sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject=subject
            )
            print("Notification sent. Message ID:", response['MessageId'])
        except Exception as e:
            print("Error sending notification:", str(e))  # If something goes wrong (like SNS not reachable, permissions issue, etc.), the exception is caught and logged.
                                                          # raise e re-throws the error so Lambda knows it failed.raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }
