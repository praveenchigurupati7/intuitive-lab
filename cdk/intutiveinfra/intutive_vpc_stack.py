from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct


class IntutiveVpcStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # vpc stack definition
        self.vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.0.0.0/16",
                           # configuration will create 3 groups in 2 AZs = 6 subnets.
                           subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public",
                               cidr_mask=24
                           ), ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                               name="Private",
                               cidr_mask=24
                           )
                           ],
                           # nat gateway
                           nat_gateways=1,
                           )
        # output will be vpc id
        CfnOutput(self, "Output",
                  value=self.vpc.vpc_id)
