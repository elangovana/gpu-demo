import argparse

import boto3
from datetime import datetime

from boto3.s3.transfer import S3Transfer


def downloadfile(s3bucket, s3key, saveto_localpath):
    client = boto3.client('s3')

    with S3Transfer(client) as transfer:
        transfer.download_file( s3bucket, s3key, saveto_localpath)


def uploadfile(localpath, s3bucket, s3key):
    client = boto3.client('s3')

    with S3Transfer(client) as transfer:
         transfer.upload_file(localpath, s3bucket, s3key)


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