import boto3

s3 = boto3.client("s3")

filename = 'upload.py'
with open(filename, 'rb') as data:
    response = s3.upload_fileobj(data, 'bmoores3bucket' , filename)

    print(response)