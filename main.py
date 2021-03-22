import boto3
import json
import random


def create_crossaccount_bucket(bucket_name):
  sts = boto3.client('sts')

  response = sts.assume_role(
      RoleArn='arn:aws:iam::123495891234:role/AppAccountRole',
      RoleSessionName='bucketRole',
      DurationSeconds=3600,
      ExternalId='SecretExt675765'
  )

  creds = response["Credentials"]

  tempCreds = {
      "accessKeyId": creds["AccessKeyId"],
      "secretAccessKey": creds["SecretAccessKey"],
      "sessionToken": creds["SessionToken"]
  }

  s3 = boto3.client('s3',
                    region_name="us-west-2",
                    aws_access_key_id=tempCreds["accessKeyId"],
                    aws_secret_access_key=tempCreds["secretAccessKey"],
                    aws_session_token=tempCreds["sessionToken"])
  
  resp = s3.create_bucket(
      Bucket=bucket_name,
      CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
  )
  print(resp)

if __name__ == "__main__":
  rn = random.randint(1, 9999)

  bucket_name = "my-shiny-new-bucket-" + str(rn)
  print("bucket_name: ", bucket_name)
  create_crossaccount_bucket(bucket_name)
