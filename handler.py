import boto3

as_group_client = boto3.client(
    'autoscaling'
)


def get_autoscale_groups_openspot(event, context):
    as_groups = as_group_client.describe_auto_scaling_groups()
    as_groups_filtered = []
    for as_group in as_groups['AutoScalingGroups']:
        if as_group.get('Tags')[0].get('Value') == 'enable':
            as_groups_filtered.append(as_group)

    return as_groups_filtered
