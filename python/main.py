import boto3
import schedule

ec2_client = boto3.client('ec2')

instances = ec2_client.describe_instances()


def check_instance_status():
    statuses = ec2_client.describe_instance_status(IncludeAllInstances=True)["InstanceStatuses"]
    for status in statuses:
        ins_status = status['InstanceStatus']['Status']
        sys_status = status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        print(f"Instance {status['InstanceId']} is {state} with instance status is {ins_status} and system status is {sys_status}")

check_instance_status()

# schedule.every(5).minutes.do(check_instance_status)
#
# while True:
#     schedule.run_pending()
