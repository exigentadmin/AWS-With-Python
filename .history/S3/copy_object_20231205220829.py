import boto3

client = boto3.client('s3')


response = client.copy_object(
    Bucket='exigent-test-lambda-trigger',
    CopySource='/exigent-test-lambda-trigger/Level1/Level2/UHG/New-Text-Document00:00:00.txt',
    Key='New-Text-Document00:00:00.txt',
)

print(response)