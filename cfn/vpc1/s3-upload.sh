#!/bin/bash
#
# Title:s3-upload.sh
#
# Description:
#
# Development Environment: OSX 10.10.5
#
AWS_PROFILE=gsc_braingang
AWS_BUCKET=cfn.braingang.net/vpc1/
#
aws s3 cp vpc-bastion-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp vpc-database-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp vpc-master-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp vpc-vpc-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
#