#! /opt/local/bin/python
#
# Title: cognito1.py
# Description:
# Development Environment: OS X 10.10.5/Python 2.7.7
# Author: G.S. Cole (guycole at gmail dot com)
#
import json
import sys
import time
import yaml

import boto3

class CognitoDemo:

    def execute(self):
        start_time = time.time()

        client = boto3.client('cognito-idp', region_name = aws_region, aws_access_key_id = aws_access_key, aws_secret_access_key = aws_secret_key)
        print client

        raw_list = client.list_user_pools(NextToken='bogus', MaxResults=50)
        user_pool_list = raw_list['UserPools']
        for user_pool in user_pool_list:
            print user_pool
        print '-x-x-x-x-x-x-'
        raw_list = client.list_users(UserPoolId='us-west-2_sVsFWampV')
        user_list = raw_list['Users']
        for user in user_list:
            print user
        print '-x-x-x-x-x-x-'

#        print boto.cognito.identity.regions()
#
#        identity = boto.cognito.identity.connect_to_region(aws_region, aws_access_key_id=aws_accesskey, aws_secret_access_key=aws_secretkey)
#        print identity
#
#        pool_list = identity.list_user_pools(50)
#        print pool_list
#
#        for pool in pool_list:
#            print pool
#
#        fresh_pool = identity.create_identity_pool('fresh_pool', True)
#        print fresh_pool
#        fresh_pool_id = fresh_pool['IdentityPoolId']
#        print fresh_pool_id

#        print identity.describe_identity_pool(fresh_pool_id)

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
    aws_access_key = configuration['awsAccessKey']
    aws_secret_key = configuration['awsSecretKey']

    driver = CognitoDemo()
    duration = driver.execute()

print 'stop'
