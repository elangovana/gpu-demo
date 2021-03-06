import argparse

import boto3
from datetime import datetime
import logging

FORMAT = '%(asctime)s  %(levelname)s	%(module)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

def downloadfile(s3bucket, s3key, saveto_localpath):
    logger.info("Downloading file {} from bucket {}".format(s3key, s3bucket))

    s3 = boto3.resource('s3')
    s3.Bucket(s3bucket).download_file(s3key, saveto_localpath)

    logger.info("Completed..")

def uploadfile(localpath, s3bucket, s3key):
    logger.info("Uploading file {} to bucket {}, key {}".format(localpath, s3bucket, s3key))

    s3 = boto3.resource('s3')

    with open(localpath, 'rb') as data:
        s3.Bucket(s3bucket).put_object(Key=s3key, Body=data)

    logger.info("Completed..")


if __name__ == "__main__":
    UPLOAD_OP = "u"
    DOWNLOAD_OP = "d"
    ops = {UPLOAD_OP, DOWNLOAD_OP}
    parser = argparse.ArgumentParser()

    parser.add_argument("op", choices=ops,
                        help="Enter the operation type. Choose one of these types {}".format(ops))
    parser.add_argument("localpath", help="Enter the localpath")
    parser.add_argument("s3bucket", help="Enter bucket name")
    parser.add_argument("s3key", help="Enter object key")

    args = parser.parse_args()

    localpath = args.localpath
    s3bucket = args.s3bucket
    s3key = args.s3key

    exec_start_time = datetime.now()
    if args.op == UPLOAD_OP:
        uploadfile(localpath, s3bucket, s3key)
    else:
        downloadfile(s3bucket, s3key, localpath)
    exec_end_time = datetime.now()

    # Compute total execution time
    exec_time = (exec_end_time - exec_start_time)
    print("Total time in seconds is: {}".format(exec_time.total_seconds()))