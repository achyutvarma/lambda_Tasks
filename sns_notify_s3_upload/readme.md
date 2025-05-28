# Create an SNS Topic
- Go to Amazon SNS.
- Create a new topic (type: Standard).
- Name it something like FileUploadNotifications.
- Create a subscription to this topic:
- Protocol: Email
- Endpoint: your email address

Confirm the subscription by clicking the link sent to your email.

# B. Create an IAM Role for Lambda
- Ensure the Lambda function has permissions for:
- Reading from S3
- Publishing to SNS

IAM Role Permissions (example policy):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    },
    {
      "Effect": "Allow",
      "Action": "sns:Publish",
      "Resource": "arn:aws:sns:your-region:your-account-id:FileUploadNotifications"
    }
  ]
}
'''

# C. Configure S3 Bucket Notification
- Go to your S3 bucket.
- In the Properties tab, scroll to Event notifications.
- Create a new event:
- Name: SendSNSNotification
- Event type: PUT (for file upload)
- Destination: Lambda Function

- Choose your Lambda function.

# Test and Verify
Upload a file to your specified S3 bucket.

You should receive an email from the SNS topic within a few seconds.

