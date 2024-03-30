from aws_cdk import (
    App,
    Stack
)
from aws_cdk import(
    aws_s3 as s3
)
from constructs import Construct

class MyFirstCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self,
            "myBucketId", 
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED
        )
