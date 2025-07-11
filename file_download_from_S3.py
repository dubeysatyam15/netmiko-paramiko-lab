import boto3

s3_client = boto3.client('s3', region_name='ap-south-1')

bucket_name = 'bomregionbucket'

with open("C:\\Users\\dubey\\Downloads\\paramiko\\file.txt", 'r') as f:
    reader = f.read().splitlines()
    for item in reader:
        response = s3_client.get_object(Bucket=bucket_name, Key=item)
        data = response['Body'].read()
        # Save the object locally with the same name
        with open(item, 'wb') as out_file:
            out_file.write(data)
        print(f"Downloaded: {item}")

