import os
import datetime
from flask import Flask, jsonify, render_template, make_response, abort
from pathlib import Path
from logging import getLogger, FileHandler
# from google.cloud import bigquery
from aws_cdk import (
    core,
    aws_dynamodb as ddb,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

app = Flask(__name__)
JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

logger = getLogger()
handler = FileHandler()
logger.addHandler(handler)


"""
def initial_bq():
    logger.info(f'start to init bq...')
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(Path("~/.var/bq-credtinal.json"))  # todo - something
    # client = bigquery.Client()
    # table_id = ""  # todo - something
    # table = client.get_table(table_id)
    logger.info('end to init bq...')
    return client, table
"""

class


# CLIENT, TABLE = initial_bq()


def insert_row(row):
    errors = CLIENT.insert_rows(TABLE, [row])
    if not errors:
        logger.info("New rows have been added.")
        return "ok"
    else:
        logger.error(f"{errors}")
        return "err"


@app.route('/start_attendance')
def start_attendance():
    return insert_row((datetime.datetime.now(JST), "出勤"))


@app.route('/end_attendance')
def end_attendance():
    return insert_row((datetime.datetime.now(JST), "退勤"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', ports=2346)
