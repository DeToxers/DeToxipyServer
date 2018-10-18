import sh
import boto
import os

rds_conn = boto.rds.connect_to_region('us-west-2')
db = rds_conn.create_dbinstance(os.environ.get('RDS_NAME'), 20, 'db.t2.micro', os.environ.get('RDS_USER'), os.environ.get('RDS_PASSWORD'))
db = rds_conn.get_all_dbinstances(os.environ.get('RDS_NAME'))[0]
while db.status != 'available':
    print('waiting for rds to spin up.\n')

