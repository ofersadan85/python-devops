import boto3
from botocore.exceptions import ClientError

s3_client = boto3.client("s3")
response = s3_client.list_buckets()

print("S3 Buckets:")
for bucket in response["Buckets"]:
    print(f"- {bucket['Name']}")

ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()
try:
    ec2_client.start_instances(InstanceIds=["id1", "id2"])
except ClientError:
    print("No such id")
ec2_client.stop_instances(InstanceIds=["id1", "id2"])
ec2_client.terminate_instances(InstanceIds=["id1", "id2"])
