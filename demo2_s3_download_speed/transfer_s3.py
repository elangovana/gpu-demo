import argparse
import logging

import boto3
from datetime import datetime

from boto3.s3.transfer import S3Transfer, TransferConfig

FORMAT = '%(asctime)s  %(levelname)s	%(module)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def downloadfile(s3bucket, s3key, saveto_localpath):
    logger.info("Downloading file {} from bucket {}".format(s3key, s3bucket))

    client = boto3.client('s3')

    GB = 1024 ** 3
    MB = 1024 ** 2
    KB = 1024

    config = TransferConfig(
        # The transfer size threshold for which multipart uploads, downloads, and copies will automatically be triggereds
        multipart_threshold=100 * MB,
        # The maximum number of threads that will be making requests to perform a transfer
        max_concurrency=10,
        # The partition size of each part for a multipart transfer
        multipart_chunksize=100 * MB,
        # The maximum amount of read parts that can be queued in memory to be written for a download
        max_io_queue=512,
        #  The max size of each chunk in the io queue
        io_chunksize=4 * MB,
        #  If True, threads will be used when performing S3 transfers
        use_threads=True)

    client.download_file(s3bucket, s3key, saveto_localpath, Config=config)

    logger.info("Completed..")


def uploadfile(localpath, s3bucket, s3key):
    logger.info("Uploading file {} to bucket {}, key {}".format(localpath, s3bucket, s3key))

    client = boto3.client('s3')

    GB = 1024 ** 3
    MB = 1024 ** 2

    config = TransferConfig(
        # The transfer size threshold for which multipart uploads, downloads, and copies will automatically be triggereds
        multipart_threshold=1 * MB,
        # The maximum number of threads that will be making requests to perform a transfer
        max_concurrency=20,
        # The partition size of each part for a multipart transfer
        multipart_chunksize=5 * MB,
        # The maximum amount of read parts that can be queued in memory to be written for a download
        max_io_queue=10,
        #  The max size of each chunk in the io queue
        io_chunksize=1 * MB,
        #  If True, threads will be used when performing S3 transfers
        use_threads=True)

    client.upload_file(localpath, s3bucket, s3key, Config=config)

    logger.info("Completed..")


if __name__ == "__main__":
    UPLOAD_OP = "u"
    DOWNLOAD_OP = "d"
    ops = {UPLOAD_OP, DOWNLOAD_OP}
    parser = argparse.ArgumentParser()

    parser.add_argument("op", choices=ops,
                        help="Enter the operation type. Choose one of these types {}".format(ops))
    parser.add_argument("localpath", help="Enter the local path")
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
