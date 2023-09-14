from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class AwsTestStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self,
            "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,  # Specify the runtime
            handler="my_lambda.handler",  # Replace with your actual handler function
            code=_lambda.Code.from_asset("lambda"),  # Path to your Lambda code directory,
            memory_size=512,
        )

        my_lambda.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE
        )