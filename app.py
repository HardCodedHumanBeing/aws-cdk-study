#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import(
    Environment
)
from aws_cdk_study.aws_cdk_study_stack import MyArtifactBucketStack
from resource_stacks.custom_vpc import CustomVpcStack

app = cdk.App()

# env_Prod = Environment(account=app.node.try_get_context('env')['prod']['account'],region=app.node.try_get_context('env')['prod']['region'])
# env_Dev = Environment(account=app.node.try_get_context('env')['dev']['account'],region=app.node.try_get_context('env')['dev']['region'])

# MyArtifactBucketStack(app, "myDevStack", env=env_Dev)
# MyArtifactBucketStack(app, "myProdStack", is_prod=True, env=env_Prod)

CustomVpcStack(app,"my-custom-vpc-stack")

app.synth()