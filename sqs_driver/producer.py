# Title: producer.py
# Description: write traffic to SQS
# Development Environment: macOS 14.4/Python 3.9.6
# Author: G.S. Cole (guycole at gmail dot com)
#
import boto3
import json
import sys

import yaml
from yaml.loader import SafeLoader

class Producer:

    def execute(self, queue_name: str, limit:int):
        print("execute")

        sqs = boto3.resource('sqs')

        queue = sqs.get_queue_by_name(QueueName=queue_name)
        print(queue.url)

        payload = {}

        for ndx in range(limit):
            payload["message"] = f"message {ndx}"
            json_payload = json.dumps(payload)
            print(json_payload)
            response = queue.send_message(MessageBody=json_payload)
            rmd = response["ResponseMetadata"]
            if rmd["HTTPStatusCode"] != 200:
                print("queue write failure")
                return

print("production start")

#
# argv[1] = configuration filename
#
if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_file_name = sys.argv[1]
    else:
        config_file_name = "config.yaml"

    with open(config_file_name, "r", encoding="utf-8") as stream:
        try:
            configuration = yaml.load(stream, Loader=SafeLoader)
        except yaml.YAMLError as exc:
            print(exc)


    producer = Producer()
    producer.execute(configuration["queue"], configuration["population"],)

print("production stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***