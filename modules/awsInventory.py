import json, socket
from IPy import IP

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