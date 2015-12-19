#! /usr/bin/python
#
# Title: ses.py
# Description:
# Development Environment: OS X 10.10.5/Python 2.7.7
# Author: G.S. Cole (guycole at gmail dot com)
#
import sys
import time
import uuid
import yaml

import boto.ses

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class SesDemo:

    def execute(self):
        start_time = time.time()

        connection = boto.ses.connect_to_region(aws_region, aws_access_key_id=aws_accesskey, aws_secret_access_key=aws_secretkey)
        print connection

        verified = connection.list_verified_email_addresses()
        print verified

        #####
        #####

        status = connection.send_email('digiburo@gmail.com', 'subject', 'body body body', ['guycole@gmail.com'])
        print status

        #####
        #####

        message = MIMEMultipart()
        message['Subject'] = 'Test Subject'
        message['From'] = 'Digi Burro <digiburo@gmail.com>'
        message['To'] = 'guycole@gmail.com'

        html = open('/tmp/html.txt', 'r').read()
        print html

        attachment = MIMEText(html, 'html')
        message.attach(attachment)
        print message

        status = connection.send_raw_email(message.as_string(), source=message['From'], destinations=message['To'])
        print status

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

    driver = SesDemo()
    duration = driver.execute()

print 'stop'
