import json, socket
from IPy import IP
import boto3

class ec2():
    
    def __init__(self):
        self.report = ''
        self.aws_profile = ''

    def inventory(self):

        session = boto3.Session(profile_name=self.aws_profile)
        ec2 = session.client('ec2')

        regions = ec2.describe_regions()

        for region in regions['Regions']:
            ec2 = session.client('ec2', region_name=region['RegionName'])
            interfaces = ec2.describe_network_interfaces()
            for interface in interfaces['NetworkInterfaces']:
                try:
                    self.report += interface['Association']['PublicIp']
                except:
                    continue
        
        return self.report

class eks():
    
    def __init__(self):
        self.file = ''
        self.report = ''


    def inventory(self):

        # get json data related to aws eks ingresses
        f = open(self.file,"r")

        ingresses = json.loads(f.read())

        # analyze ingresses and provide the report: ingress type (private/public) - host - balancer
        for item in ingresses["items"]:
            try:
                host = item['spec']['rules'][0]['host']
                balancer = item['status']['loadBalancer']['ingress'][0]['hostname']
                ingress_type = IP(socket.gethostbyname(balancer)).iptype()
            except Exception as e:
                continue

            self.report += ingress_type + " " + host + " " + balancer + "\n"
        
        return self.report