import sh
import boto3
import os
import time


def deploy_rds():
    """
    Creates an RDS instance on AWS using environment variables
    """
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBName=os.environ.get('RDS_NAME'),
        DBInstanceIdentifier=os.environ.get('RDS_NAME'),
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='postgres',
        MasterUsername=os.environ.get('RDS_USER'),
        MasterUserPassword='postgres',
        Port=5432,
        PubliclyAccessible=True,
        DeletionProtection=False,
        )
    # print(str(response))
    db = rds.describe_db_instances(DBInstanceIdentifier=os.environ.get('RDS_NAME'))
    counter = 0
    db_endpoint = check_if_rds_deployed(rds, counter)
    db_endpoint = db['DBInstances'][0]['Endpoint']
    print(db_endpoint)

def check_if_rds_deployed(rds, counter):
    db = rds.describe_db_instances(DBInstanceIdentifier=os.environ.get('RDS_NAME'))
    try:
        db_endpoint = db['DBInstances'][0]['Endpoint']
        if not db_endpoint:
            check_if_rds_deployed(rds, counter)
        return db_endpoint
    except KeyError:
        counter += 1
        print('RDS Instance is still spinning up. ' + str(counter) + 'minutes\n')
        time.sleep(60)
        check_if_rds_deployed(rds, counter)


def input_tree():
    user_choice = str(input('Do you want to spin up a database instance (y/n): \n'))
    print('\n')
    if user_choice.lower()[0] == 'y':
        deploy_rds()
    else:
        print('have a nice day')
        return

input_tree()



