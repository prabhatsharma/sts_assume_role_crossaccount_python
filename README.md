# STS Assume role example

We will create a bucket in Data account from AppAccount using cross account IAM roles.

AWS Accounts

1. Primary account with application (AppCcount) - 987658241234
1. Account with S3 bucket (DataAccount) - 123495891234

Below are the steps

## In DataAccount

1. Create a cross account IAM role in DataAccount that trusts AppAccount

Name this role - AppAccountRole

Attach AmazonS3FullAccess policy to the role

ExternalID - SecretExt675765

Trust policy:

<pre>
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::987658241234:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "SecretExt675765"
        }
      }
    }
  ]
}
</pre>

RoleArn should look like:

arn:aws:iam::123495891234:role/AppAccountRole

## In AppAccount

Run the program main.py

python main.py


