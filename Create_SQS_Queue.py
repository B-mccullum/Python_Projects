import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Specify a unique name for your queue
queue_name = 'wk-15-project'

# Create the SQS queue
response = sqs.create_queue(
    QueueName=queue_name,
    Attributes={
        'DelaySeconds': '0',
        'VisibilityTimeout': '30',
        # Add any other desired attributes
    }
)

# Get the URL of the newly created queue
queue_url = response['QueueUrl']

