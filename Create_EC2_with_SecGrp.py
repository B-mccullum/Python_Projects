import boto3

# Define your AWS access key ID and secret access key
aws_access_key_id = "Enter Access Key ID"
aws_secret_access_key = "Enter Secret Access Key ID"

# Specify the region and EC2 instance details
region = 'us-east-1'
ami_id = 'ami-053b0d53c279acc90'  # Replace with the ID of the Ubuntu AMI in your desired region
instance_type = 't2.micro'

# Define the security group rules
security_group_name = 'MySecurityGroup'
security_group_rules = [
    {
        'FromPort': 8080,
        'ToPort': 8080,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    },
    {
        'FromPort': 22,
        'ToPort': 22,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    },
    {
        'FromPort': 443,
        'ToPort': 443,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    },
    {
        'FromPort': 80,
        'ToPort': 80,
        'IpProtocol': 'tcp',
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    }
]

# Create an EC2 resource and security group
ec2 = boto3.resource('ec2', region_name=region,
                     aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key)

# Create the security group
security_group = ec2.create_security_group(
    GroupName=security_group_name,
    Description='Allow inbound traffic on ports 8080, 22, 443, and 80 from any source',
    VpcId='Enter VPC ID'  # Replace with your VPC ID
)

# Authorize the inbound traffic for each rule
for rule in security_group_rules:
    security_group.authorize_ingress(
        CidrIp=rule['IpRanges'][0]['CidrIp'],
        FromPort=rule['FromPort'],
        ToPort=rule['ToPort'],
        IpProtocol=rule['IpProtocol']
    )

# Launch the EC2 instance with the specified security group
instances = ec2.create_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    SecurityGroupIds=[security_group.group_id],
    MinCount=1,
    MaxCount=1
)

# Print the instance IDs of the created instances
for instance in instances:
    print("Created instance ID:", instance.id)

