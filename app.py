#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import(
    Environment
)
from aws_cdk_study.aws_cdk_study_stack import MyArtifactBucketStack

env_Frankfurt = Environment(region="eu-central-1")
env_London = Environment(region="eu-west-2")

app = cdk.App()
MyArtifactBucketStack(app, "myDevStack", env=env_Frankfurt)
MyArtifactBucketStack(app, "myProdStack", is_prod=True, env=env_London)

app.synth()
