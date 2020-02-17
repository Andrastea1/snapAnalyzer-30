# snapshot -30

Demo project to manage AWS EC@ instance snapshots
## About
This project is a demo and uses boto3 to manage AWS EC2 instance snapshots.

## configuring

shotty uses the config file created by the AWS cli. e.g.

'aws configure --profile shott'


## running

'pipenv run python shotty/shotty.py' <command> <--project =Project>"`

*command is list,start, or stop_instances
*project* is optional
