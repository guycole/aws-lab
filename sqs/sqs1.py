#! /usr/bin/python
#
# Title: sqs1.py
# Description:
# Development Environment: OS X 10.10.5/Python 2.7.7
# Author: G.S. Cole (guycole at gmail dot com)
#
import datetime
import json
import os
import rfc822
import sys
import time
import uuid
import yaml

from email import utils

from boto import connect_sqs
from boto.sqs.message import RawMessage

class SqsDemo:
    def rfc822_now(self):
        now_tuple = datetime.datetime.now().timetuple()
        now_time = time.mktime(now_tuple)
        return utils.formatdate(now_time)

    def log_payload(self, task_id, priority, facility, message):
        data = {
            'time_stamp_rfc822': self.rfc822_now(),
            'task_id': str(task_id),
            'priority': str(priority),
            'facility': str(facility),
            'message': str(message)
        }

        message = RawMessage()
        message.set_body(json.dumps(data))
        return message

    def q_lookup(self, q_name):
        sqs_connection = connect_sqs(aws_accesskey, aws_secretkey)
        return sqs_connection.lookup(q_name)

    def q_delete(self, qqq, message):
        qqq.delete_message(message)

    def q_writer(self, qqq, payload):
        status = qqq.write(payload)

    def q_reader(self, qqq):
        print 'reader'
        qqq.set_message_class(RawMessage)
        result_set = qqq.get_messages()
        print len(result_set)
        print result_set

        for result in result_set:
            print result.get_body()
            temp = json.loads(result.get_body())
            print temp

            self.q_delete(qqq, result)

    def execute(self, q_name, task_id):
        start_time = time.time()

        qqq = self.q_lookup(q_name)

        payload = self.log_payload(task_id, 'notice', 'witness', 'application start')
        self.q_writer(qqq, payload)

        self.q_reader(qqq)

        stop_time = time.time()
        return stop_time - start_time

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    if len(sys.argv) > 1:
        yaml_filename = sys.argv[1]
    else:
        yaml_filename = 'config.yaml'

    configuration = yaml.load(file(yaml_filename))

    aws_region = configuration['awsRegion']
    aws_accesskey = configuration['awsAccessKey']
    aws_secretkey = configuration['awsSecretKey']

#    aws_accesskey = 'bogus'
#    aws_secretkey = 'bogus'

    driver = SqsDemo()
    duration = driver.execute('TestQueue', uuid.uuid4())

print 'stop'