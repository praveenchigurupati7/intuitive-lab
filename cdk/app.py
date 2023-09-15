#!/usr/bin/env python3

from aws_cdk import App

from intutiveinfra.intutive_vpc_stack import IntutiveVpcStack
from intutiveinfra.intutive_ec2_stack import IntutiveEc2Stack
from intutiveinfra.intutive_s3_stack import IntutiveS3Stack

app = App()

vpc_stack = IntutiveVpcStack(app, "cdk-vpc")
ec2_stack = IntutiveEc2Stack(app, "cdk-ec2",
                             vpc=vpc_stack.vpc)
s3_stack = IntutiveS3Stack(app, "cdk-s3")

app.synth()
