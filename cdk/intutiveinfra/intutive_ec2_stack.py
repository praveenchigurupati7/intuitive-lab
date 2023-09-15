from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    Stack,
    CfnOutput
)
import aws_cdk.aws_autoscaling as autoscaling
from constructs import Construct

# ec2 type
ec2_type = "t2.micro"

# Count of instances
count = 2

# Indicate your AMI, no need a specific id in the region
ami_linux = ec2.MachineImage.latest_amazon_linux(
    generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
    edition=ec2.AmazonLinuxEdition.STANDARD,
    virtualization=ec2.AmazonLinuxVirt.HVM,
    storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
)

# metadata script
with open("./user_data/user_data.sh") as f:
    user_data = f.read()


class IntutiveEc2Stack(Stack):

    def __init__(self, scope: Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        print('Creating iam instance role')
        role = iam.Role(self, "IntutiveEc2InstanceRole", assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2FullAccess"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"))
        if not role:
            print('Failed creating iam role')
            return

        print('Creating security group')
        sec_grp = ec2.SecurityGroup(self, 'ec2-sec-grp', vpc=vpc, allow_all_outbound=True)
        if not sec_grp:
            print('Failed finding security group')
            return

        print('Creating inbound firewall rule')
        sec_grp.add_ingress_rule(
            peer=ec2.Peer.ipv4('0.0.0.0/24'),
            description='inbound SSH',
            connection=ec2.Port.tcp(22))

        if not sec_grp:
            print('Failed creating security group')
            return

        # Create Autoscaling Group with fixed 2*EC2 hosts
        self.asg = autoscaling.AutoScalingGroup(self, "IntutiveASG",
                                                vpc=vpc,
                                                instance_type=ec2.InstanceType.of(
                                                    ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
                                                ),
                                                machine_image=ami_linux,
                                                user_data=ec2.UserData.custom(user_data),
                                                desired_capacity=count,
                                                min_capacity=count,
                                                max_capacity=count,
                                                )
        CfnOutput(self, "Output",
                  value=self.asg.auto_scaling_group_name)
