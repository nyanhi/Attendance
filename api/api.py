import os
import uuid
import json
import boto3
from datetime import datetime, timezone

ddb = boto3.resource("dynamodb")
table = ddb.Table(os.environ["TABLE_NAME"])

JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

HEADERS = {
    "Access-Control-Allow-Origin": "*",
}


def post_start(event, context):
    """
    handler for POST /start
    """
    try:
        item = {
            'item_id': uuid.uuid4().hex,
            'username': 'skatsu',
            'timestamp': datetime.now(JST),
            'month': datetime.now(JST).month,
            'message': '出勤'
        }
        response = table.put_item(Item=item)
        status_code = 201
        resp = {'description': 'Successfully recorded attendance start'}

    except ValueError as e:
        status_code = 400
        resp = {'description': f'Bad request. str{e}'}

    except Exception as e:
        status_code = 500
        resp = {'description': f'str{e}'}

    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": resp
    }


def post_end(event, context):
    """
    handler for POST /end
    """
    try:
        item = {
            'item_id': uuid.uuid4().hex,
            'username': 'skatsu',
            'timestamp': datetime.now(JST),
            'month': datetime.now(JST).month,
            'message': '退勤'
        }
        response = table.put_item(Item=item)
        status_code = 201
        resp = {'description': 'Successfully recorded attendance end'}

    except ValueError as e:
        status_code = 400
        resp = {'description': f'Bad request. str{e}'}

    except Exception as e:
        status_code = 500
        resp = {'description': f'str{e}'}

    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": resp
    }
