#!/bin/bash
#
# Title:s3-upload.sh
#
# Description:
#
# Development Environment: OSX 10.10.5
#
AWS_PROFILE=gsc_braingang
AWS_BUCKET=cfn.braingang.net/vpn1/
#
aws s3 cp vpn-master-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp vpn-ec2-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
aws s3 cp vpn-vpc-v01.json s3://$AWS_BUCKET --profile $AWS_PROFILE
#