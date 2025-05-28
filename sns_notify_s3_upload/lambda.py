import json
import boto3
import urllib.parse

sns = boto3.client('sns')

# Replace with your actual SNS Topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:your-region:your-account-id:FileUploadNotifications'

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        
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
            print("Error sending notification:", str(e))
            raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }
