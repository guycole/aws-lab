#!/bin/bash
#
# Title:s3-upload.sh
#
# Description:
#
# Development Environment: OSX 10.10.5
#
AWS_PROFILE=gsc_braingang
AWS_BUCKET=cfn.braingang.net/code1/
#
aws s3 cp code-git-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp code-master-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp code-pipeline-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp code-sqns-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
#