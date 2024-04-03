from aws_cdk import (
    aws_ec2 as ec2,
    CfnOutput,
    Stack
)
from constructs import Construct

class CustomVpcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        prod_configs = self.node.try_get_context('env')['prod']
        custom_vpc = ec2.Vpc(self,
                             "customVpcId",
                             cidr=prod_configs['vpc_config']['vpc_cidr'],
                             max_azs=2,
                             nat_gateways=1,
                             subnet_configuration=[
                                 ec2.SubnetConfiguration(name="public", cidr_mask=prod_configs['vpc_config']['subnet_mask'],
                                                         subnet_type=ec2.SubnetType.PUBLIC),
                                 ec2.SubnetConfiguration(name="private", cidr_mask=prod_configs['vpc_config']['subnet_mask'],
                                                         subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS),
                                 ec2.SubnetConfiguration(name="isolated", cidr_mask=prod_configs['vpc_config']['subnet_mask'],
                                                         subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS)
                             ]
                             )
        CfnOutput(self,
                  "outputCustomVpcId",
                  value=custom_vpc.vpc_id,
                  export_name="customVpcId")