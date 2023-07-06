import json, socket, sys
from IPy import IP

# get json data related to aws eks ingresses
file_name = sys.argv[1]
f = open(file_name,"r")

ingresses = json.loads(f.read())

# analyze ingresses and provide the report: ingress type (private/public) - host - balancer
for item in ingresses["items"]:
    try:
        host = item['spec']['rules'][0]['host']
        balancer = item['status']['loadBalancer']['ingress'][0]['hostname']
        ingress_type = IP(socket.gethostbyname(balancer)).iptype()
    except Exception as e:
        continue

    print(ingress_type + " " + host + " " + balancer)
