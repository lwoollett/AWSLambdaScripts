import boto3
REGION = 'ap-southeast-2'
INSTANCES = ['i-0c310d5b058a03d57', 'i-0dfc3776a0679fb70']
EC2 = boto3.client('ec2', region_name=REGION)

def lambda_handler(event, context):
    EC2.start_instances(InstanceIds=INSTANCES)
    print('Started instances: ' + str(INSTANCES))