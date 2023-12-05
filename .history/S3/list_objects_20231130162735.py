import boto3
import json
import pprint
import yaml

client = boto3.client('s3')

response = client.list_objects(
    Bucket='string',
    Delimiter='string',
    EncodingType='url',
    Marker='string',
    MaxKeys=123,
    Prefix='string',
    RequestPayer='requester',
    ExpectedBucketOwner='daba336d32200a86d417709556615a3fc4854309d085aa694c3618e4ad6f3e32',
    OptionalObjectAttributes=[
        'RestoreStatus',
    ]
)