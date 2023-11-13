from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct


class IacDccStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ec2.CfnKeyPair(
            self,
            id="DCC-KEY_PAIR",
            key_name="ec2-ssh-key"
        )

        vpc = ec2.Vpc(
            self,
            id="DCC-VPC",
            max_azs=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC
                )
            ]
        )

        instance = ec2.Instance(
            self,
            id="DCC-EC2",
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            instance_type=ec2.InstanceType("t2.micro"),
            key_name="ec2-ssh-key",
            vpc=vpc,
            # role=""
        )

        instance.connections.allow_from_any_ipv4(ec2.Port.tcp(22))
