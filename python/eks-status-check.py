import boto3

eks_client = boto3.client('eks')

clusters = eks_client.list_clusters()['clusters']

for cluster in clusters:
    response = eks_client.describe_cluster(
        name=cluster
    )
    cluster_inf = response['cluster']
    cluster_status = cluster_inf['status']
    cluster_endpoint = cluster_inf['endpoint']
    cluster_version = cluster_inf['version']
    print(cluster_status)
