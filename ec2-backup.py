import boto3
import datetime

def lambda_handler(event, context):
    # Initialize the AWS EC2 client
    ec2 = boto3.client('ec2')
    
    # Define a list of EC2 instance IDs to be backed up
    instance_ids = ['i-XXXXXXXXXXXXXXXXX', 'i-YYYYYYYYYYYYYYYYY']  # Replace with your instance IDs
    
    # Create a backup (AMI) of each EC2 instance
    for instance_id in instance_ids:
        # Generate a unique name for the AMI
        ami_name = f'Backup-{instance_id}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'
        
        # Create the AMI (backup)
        response = ec2.create_image(InstanceId=instance_id, Name=ami_name, NoReboot=True)
        
        # Optionally, you can tag the created AMI for better organization
        ec2.create_tags(Resources=[response['ImageId']], Tags=[{'Key': 'Backup', 'Value': 'Yes'}])
        
        print(f"Created backup {response['ImageId']} for instance {instance_id}")
    
    return {
        'statusCode': 200,
        'body': 'EC2 instance backup completed successfully.'
    }
