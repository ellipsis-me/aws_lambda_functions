import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2 = boto3.client('ec2')
    
    on = "on"
    off = "off"
    state = event.get("state")
    
    if event.get("state") == on:
        ec2.start_instances(
            InstanceIds=[
            event.get("id")
            ]
        )
    elif event.get("state") == off:
        ec2.stop_instances(
            InstanceIds=[
            event.get("id")
            ]
        )
    
    return {
         'statusCode': 200,
         'body': 'OK',
         'event': event
    }

# "event" argument in that case is receiving a dictionary like this {"id":"i-99999999999999999","state":"off"}
# where "id" is the intance id, and "state" is the state that we want, that must be "on" or "off", that function DOES NOT delete instances.