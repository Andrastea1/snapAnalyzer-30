import boto3


session = boto3.Session(profile_name = 'shotty')
ec2 = session.resource('ec2')

def list_instances():
        "List ec2 instances"
        for i in ec2.instances.all():
            print(','.join((i.id,i.instance_type,i.placement['AvailabilityZone'],i.state['Name'],i.public_dns_name)))
if __name__== '__main__':
    list_instances()
