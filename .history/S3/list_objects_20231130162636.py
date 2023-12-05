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
    ExpectedBucketOwner='string',
    OptionalObjectAttributes=[
        'RestoreStatus',
    ]
)