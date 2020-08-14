import boto3

as_group_client = boto3.client(
    'autoscaling'
)


def get_autoscale_groups_openspot(event, context):
    as_groups = as_group_client.describe_auto_scaling_groups()
    return as_groups


def enable_openspot_in_autoscale(event, context):

    openspot_status = event['data']['openspot']

    if openspot_status == 'enable':
        response = as_group_client.create_or_update_tags(
            Tags=[
                {
                    'ResourceId':  event['data']['ResourceId'],
                    'ResourceType': 'auto-scaling-group',
                    'Key': 'openspot',
                    'Value': openspot_status,
                    'PropagateAtLaunch': True
                },
            ])
        return response
    else:
        return 'Nothing to do'

