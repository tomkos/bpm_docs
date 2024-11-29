<!-- image -->

# Test the module

## About this task

To test the module, follow these steps:

## Procedure

1. Copy the customer.txt file into
the c:\flatfiles\inboundevents directory.
2. Check the contents of the c:\flatfiles\inboundevents directory.
The input file, customer.txt, should be removed
from the folder once it has been processed by your application.
3. Check the c:\flatfiles\outputdir directory.
You should see a list of files with a file name matching this pattern: Customer.<sequence
number>.txt. The content of each file is a single customer
data record. You will also see a sequencing file indicating the customer
records processed.
4. In the c:\flatfiles\inboundarchive directory,
you should see your original file with a timestamp suffix. For example, customer.txt.<timestamp>.success.
5. If you want to test again, put the customer.txt file
into the c:\flatfiles\inboundevents directory
again. This file and the directory structure are discussed in Create the directories and input file.

## Results

Stop the server, which otherwise
will continue to run. Right-click IBM Workflow
Server again
and from the context menu click Stop.