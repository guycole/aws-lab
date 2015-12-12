#! /usr/bin/python
#
# Title: sns1.py
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

from boto.sns import SNSConnection


class SnsDemo:

    def discover_topic(self, sns_client, topic_name):
        topics = sns_client.get_all_topics()

        candidates = topics['ListTopicsResponse']['ListTopicsResult']['Topics']
        for candidate in candidates:
            temp = candidate['TopicArn']
            if temp.endswith(topic_name):
                return temp

    def topic_writer(self, sns_client, topic_name, subject, message):
        topic_arn = self.discover_topic(sns_client, topic_name)
        return sns_client.publish(topic_arn, message, subject)

    def execute(self, topic_name):
        start_time = time.time()

        sns_client = SNSConnection(aws_access_key_id=aws_accesskey, aws_secret_access_key=aws_secretkey)
        self.topic_writer(sns_client, topic_name, 'demo subject', 'of all the fishies in the sea the mermaid is the one for me')

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

    driver = SnsDemo()
    duration = driver.execute('sms-me')
    duration = driver.execute('email-me')

print 'stop'
