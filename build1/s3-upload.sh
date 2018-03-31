#!/bin/bash
#
# Title:s3-upload.sh
#
# Description:
#
# Development Environment: OSX 10.10.5
#
AWS_PROFILE=gsc_braingang
AWS_BUCKET=killme.braingang.net
#
rm -f demo1_input.zip
zip -r demo1_input.zip buildspec.yml src
#
aws s3 cp demo1_input.zip s3://$AWS_BUCKET --profile $AWS_PROFILE
#