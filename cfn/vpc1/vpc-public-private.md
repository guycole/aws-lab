# VPC Public Private

* Introduction

Demonstrate Cloud Formation of an AWS VPC w/the following features:

    * VPC (192.168.0.0)
    * public (192.168.1.0) subnet
    * private (192.168.2.0) subnet
    * bastion EC2 instance (SSH only)
    * simulated "web" EC2 instance
    * simulated "db" EC2 instance
    * IAM rule for s3 access
    * NAT gateway to allow private subnet outside access
    
* Tour
    
You will need a EC2 keypair to use this script.
    
    * line 36-75 Create IAM role/policy for S3 access from EC2
    * line 77-88 Define VPC
    * line 90-106 Define internet gateway and attach to VPC
    * line 108-126 Define NAT Gateway, needed for private subnet to enjoy internet access
    * line 128-169 Define private subnet, route table, route and associate route to subnet
    * line 171-212 Define public subnet, route table, route and associate route to subnet
    * line 214-223 Define bastion security group, SSH only
    * line 225-254 Define bastion EC2 instance
    * line 256-266 Define web security group, HTTP to world, SSH to public subnet
    * line 268-296 Define web EC2 instance
    * line 298-310 Define DB security group 
    * line 312-340 Define DB EC2 instance