from aws_cdk import (
    aws_s3 as s3,
    Stack,
)
from constructs import Construct


class IntutiveS3Stack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(
                            self,
                            "intutive_s3"
                            )
