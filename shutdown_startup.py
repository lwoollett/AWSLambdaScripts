import boto3
# ! Region should stay static for most instances for AWS
REGION = 'ap-southeast-2'
# ! List of instances wanted to start and stop
# , 'i-0c310d5b058a03d57'] ! Stop PrintNPaint.NZ
INSTANCES = ['i-0dfc3776a0679fb70']
# * Init EC2
EC2 = boto3.client('ec2', region_name=REGION)

# ? Function for *actually* starting the EC2 instance/s
def lambda_startup(event, context):
    EC2.start_instances(InstanceIds=INSTANCES)
    print('Start these instances: ' + str(INSTANCES))


# ? Function for *actually* stopping the EC2 instance/s
def lambda_shutdown(event, context):
    EC2.stop_instances(InstanceIds=INSTANCES)
    print('Stopped these instances: ' + str(INSTANCES))

def lambda_handler(event, context):
    if(event["type"] == "shutdown"): lambda_shutdown(None, None)
    else: lambda_startup(None, None)
    print("Event:")
    print(event)
    print("Context:")
    print(context)