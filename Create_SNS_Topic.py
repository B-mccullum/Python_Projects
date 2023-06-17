import boto3

topic_name = "week_15_topic"

def create_sns_topic(topic_name):
    # Create an SNS client with the desired region
    sns = boto3.client('sns', region_name='us-east-1')
    
    # Create a new SNS topic
    response = sns.create_topic(Name=topic_name)
    
    # Extract the topic ARN from the response
    topic_arn = response['TopicArn']
    
    # Return the topic ARN
    return topic_arn

# Call the create_sns_topic function to create a new SNS topic
topic_arn = create_sns_topic(topic_name)

# Print the SNS topic ARN
print(f"SNS topic ARN is: {topic_arn}")

