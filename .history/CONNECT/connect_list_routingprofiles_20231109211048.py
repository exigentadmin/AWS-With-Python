import boto3
import json

#list all groups using client
connect = boto3.client('connect') #Connect
response = connect.list_routing_profiles(
    InstanceId='67faf965-78f3-49d8-a49a-f98a2b061700'
)

#response from aws is a dict
response_json = json.dumps(response, indent = 4) #convert dict to json

#print(response)
print(response_json)

'''
queue_list = response['QueueSummaryList'] #set variable equal to the QueueSummaryList list

#print(queue_list)

total_queues = 0

for arn in queue_list:
    length = len(arn['Arn'])
    arn_pure = (arn['Arn'])[length - 36:]
    print(arn_pure)
    total_queues += 1
    #print(arn['Arn'])

print('\nTotal queues ', total_queues)
'''


