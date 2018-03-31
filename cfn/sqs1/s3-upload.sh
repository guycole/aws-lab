#!/bin/bash
#
# Title:s3-upload.sh
#
# Description:
#
# Development Environment: OSX 10.10.5
#
AWS_PROFILE=gsc_braingang
AWS_BUCKET=cfn.braingang.net/sqs1/
#
aws s3 cp sqs-master-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp sqs-s3-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp sqs-sns-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
#