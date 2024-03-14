# Title: consumer.py
# Description: drain SQS 
# Development Environment: macOS 14.4/Python 3.9.6
# Author: G.S. Cole (guycole at gmail dot com)
#
import boto3
import json
import sys

import yaml
from yaml.loader import SafeLoader

class Consumer:

    def execute(self, queue_name: str):
        print("execute")

        sqs = boto3.resource('sqs')

        queue = sqs.get_queue_by_name(QueueName=queue_name)
        print(queue.url)

        loop_flag = True
        while loop_flag:
            loop_flag = False
            messages = queue.receive_messages(MessageAttributeNames=["All"], MaxNumberOfMessages=5, WaitTimeSeconds=5,)
            for msg in messages:
                loop_flag = True
                print(f"received: {msg.message_id} {msg.body}")
                msg.delete()

print("consumer start")

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


    consumer = Consumer()
    consumer.execute(configuration["queue"],)

print("consumer stop")

# ;;; Local Variables: ***
# ;;; mode:python ***
# ;;; End: ***