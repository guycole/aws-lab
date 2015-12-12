#! /usr/bin/python
#
# Title: s3.py
# Description:
# Development Environment: OS X 10.10.5/Python 2.7.7
# Author: G.S. Cole (guycole at gmail dot com)
#
import sys
import time
import uuid
import yaml

from boto.s3.connection import S3Connection
from boto.s3.key import Key

class S3Demo:

    def s3get(self, s3bucket, target):
        s3key = s3bucket.get_key(target)
        s3key.get_contents_to_filename(target)

    def s3list(self, s3bucket):
        result = []

        for key in s3bucket.list():
            if key.size > 0:
                result.append(key.name)

        return result

    def s3write(self, s3bucket, s3filename, local_file):
        s3key = Key(s3bucket)
        s3key.key = s3filename
        s3key.set_contents_from_filename(local_file)

    def execute(self):
        start_time = time.time()

        s3connection = S3Connection(aws_accesskey, aws_secretkey)

        bucket_name = 'test-digiburo-com'
        s3bucket = s3connection.lookup(bucket_name)
        if s3bucket is None:
            print "must create bucket:%s" % bucket_name
#            s3connection.create_bucket(bucket_name)
        else:
            print "bucket exists:%s" % bucket_name

            dirlist = self.s3list(s3bucket)
            print dirlist

            self.s3write(s3bucket, str(uuid.uuid4()), 's3.sh')
            self.s3get(s3bucket, dirlist[0])

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

    driver = S3Demo()
    duration = driver.execute()

print 'stop'
