#
# Title:sync_bucket.sh
#
# Create destination bucket
# Copy files from source to destination bucket
# Upgrade files to KMS
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin:~/.local/bin; export PATH
#
DST_BUCKET=s3://copy-sink.braingang.net
SRC_BUCKET=s3://lab-production-lab6
AWS_PROFILE=cli_braingang 
KEY_ARN=arn:aws:kms:us-west-2:238461155224:key/98fa57c5-53f1-43b3-8223-b074725aaa3a
#
aws s3 mb $DST_BUCKET --profile=$AWS_PROFILE --region us-west-2
#
aws s3 sync $SRC_BUCKET $DST_BUCKET --profile=$AWS_PROFILE --region us-west-2
#
aws s3 cp $SRC_BUCKET $SRC_BUCKET --recursive --sse-kms-key-id $KEY_ARN --sse aws:kms --profile=$AWS_PROFILE --region us-west-2
#
