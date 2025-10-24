# CSCE 533 S3 Capability Project

## Successful Execution
```
tbbti@TraesLaptop MINGW64 ~/csce533_test (main)
$ python s3_capability.py --function_name upload_to_s3
Successfully uploaded test.txt, in traelyndistributedbucket

tbbti@TraesLaptop MINGW64 ~/csce533_test (main)
$ python s3_capability.py --function_name read_from_s3
Successfully downloaded test.txt, from traelyndistributedbucket, path: downloaded_file.txt

tbbti@TraesLaptop MINGW64 ~/csce533_test (main)
$ cat downloaded_file.txt
This is my test file for CSCE 533.

tbbti@TraesLaptop MINGW64 ~/csce533_test (main)
$
```
