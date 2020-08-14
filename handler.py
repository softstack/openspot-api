import boto3
import json
import datetime

as_group_client = boto3.client(
    'autoscaling'
)


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


def get_autoscale_groups_openspot(event, context):
    as_groups = as_group_client.describe_auto_scaling_groups()
    return json.dumps(as_groups, default=default)


def enable_openspot_in_autoscale(event, context):
    body = json.loads(event['body'])
    response = as_group_client.create_or_update_tags(
        Tags=[
            {
                'ResourceId': body.get('auto-scaling-group-name'),
                'ResourceType': 'auto-scaling-group',
                'Key': 'openspot',
                'Value': body.get('openspot'),
                'PropagateAtLaunch': True
            },
        ])

    return response
