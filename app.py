import os
import datetime
from aws_cdk import (
    core,
    aws_dynamodb as ddb,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')


class AttendanceRecord(core.Stack):
    def __init__(self, scope: core.App, name: str, **kwargs):
        super.__init__(scope, name, **kwargs)

        table = ddb.Table(
            self, "Timestamps",
            partition_key=ddb.Attribute(
                name="timestamp",
                type=ddb.AttributeType.STRING
            ),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        common_params = {
            "runtime": _lambda.Runtime.PYTHON_3_7,
            "environment": {
                "TABLE_NAME": table.table_name
            }
        }

        post_start_lambda = _lambda.Function(
            self, "PostStart",
            code=_lambda.Code.from_asset('api'),
            handler='api.post_start',
            memory_size=512,
            timeout=core.Duration.seconds(10),
            **common_params
        )

        post_end_lambda = _lambda.Function(
            self, "PostEnd",
            code=_lambda.Code.from_asset('api'),
            handler='api.post_end',
            memory_size=512,
            timeout=core.Duration.seconds(10),
            **common_params
        )

        # grant permissions
        table.grant_read_write_data(post_start_lambda)
        table.grant_read_write_data(post_end_lambda)

        api = apigw.RestApi(
            self, "AttendanceApi",
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=apigw.Cors.ALL_METHODS,
            )
        )

        start = api.root.add_resource('start')
        start.add.method(
            'POST',
            apigw.LambdaIntegration(post_start_lambda)
        )

        end = api.root.add_resource('end')
        end.add.method(
            'POST',
            apigw.LambdaIntegration(post_end_lambda)
        )


app = core.App()
AttendanceRecord(
    app, "AttendanceRecord",
    env={
        "region": os.environ["CDK_DEFAULT_REGION"],
        "account": os.environ["CDK_DEFAULT_ACCOUNT"],
    }
)

app.synth()

