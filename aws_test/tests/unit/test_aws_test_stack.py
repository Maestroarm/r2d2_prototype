import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_test.aws_test_stack import AwsTestStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_test/aws_test_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsTestStack(app, "aws-test")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::Lambda::Function", {
            "Runtime": "python3.9",
            "Handler": "my_lambda.handler",
            "MemorySize": 512,
        })
