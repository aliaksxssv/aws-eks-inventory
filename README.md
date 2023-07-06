# aws-eks-inventory

1. Authorize in AWS account

$ aws configure sso

2. Update kubeconfig

$ aws eks update-kubeconfig --region us-west-2 --name pandadoc-infra-main --profile infra-admin

3. Get AWS EKS ingresses across all namespaces

$ kubectl get --all-namespaces ingress -o json > ingress.json 

4. Create report from json

$ python3 ./main.py ingress.json