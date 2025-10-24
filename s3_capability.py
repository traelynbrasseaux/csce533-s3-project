import argparse

import boto3

""""
    In-class Activity: In this exercise, please create a upload and read functionality of the document using S3 
    upload_to_s3: which uploads object name (file) to the provided bucket_name
    read_from_s3: which downloads object name (file) from the provided bucket_name

"""

s3 = boto3.client('s3')

# name your respective bucket_name here
BUCKET_NAME = "traelyndistributedbucket"


class S3Capability:
    def __init__(self, function):
        self.function = function

    def process(self):
        if self.function == S3Capability.upload_to_s3.__name__:
            self.upload_to_s3()
        elif self.function == S3Capability.read_from_s3.__name__:
            self.read_from_s3()

    def upload_to_s3(self, object_name=None):
        # provide your file path here
        f_name = "test.txt"
        if object_name is None:
            object_name = f_name
        try:
            s3.upload_file(f_name, BUCKET_NAME, object_name)
            print("Successfully uploaded {}, in {}".format(f_name, BUCKET_NAME))
        except Exception as e:
            print("Error in upload {}, in {}, error:{}".format(f_name, BUCKET_NAME, e))

    def read_from_s3(self):
        to_download_object_name = "test.txt"
        downloaded_object = "downloaded_file.txt"
        try:
            s3.download_file(BUCKET_NAME, to_download_object_name, downloaded_object)
            print("Successfully downloaded {}, from {}, path: {}".format(to_download_object_name,
                                                                         BUCKET_NAME,
                                                                         downloaded_object))
        except Exception as e:
            print(
                "Error in download {}, from {}, path: {}, error:{}".format(to_download_object_name,
                                                                           BUCKET_NAME,
                                                                           downloaded_object,
                                                                           e))


if __name__ == "__main__":
    _arg_parser = argparse.ArgumentParser(description="S3 Capability to read and write data")
    _arg_parser.add_argument("-f", "--function_name",
                             action="store",
                             required=True,
                             help="processing function name")

    _arg_value = _arg_parser.parse_args()

    data_analyzer = S3Capability(_arg_value.function_name)
    data_analyzer.process()
