import boto3
# ! Region should stay static for most instances for AWS
REGION = 'ap-southeast-2'
# ! List of instances wanted to start and stop
INSTANCES = ['i-0c310d5b058a03d57'] #, 'i-0dfc3776a0679fb70'] ! Stop PrintNPaint.NZ
# * Init EC2
EC2 = boto3.client('ec2', region_name=REGION)

# ? Function for *actually* stopping the EC2 instance/s
def lambda_handler(event, context):
    EC2.stop_instances(InstanceIds=INSTANCES)
    print('Stopped these instances: ' + str(INSTANCES))