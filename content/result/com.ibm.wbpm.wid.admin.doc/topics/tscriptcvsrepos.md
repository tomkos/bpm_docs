<!-- image -->

# Creating a script for test cases stored in a CVS repository

## About this task

Your test cases and modules may be stored in a repository
such as CVS.  Since Ant has support for CVS, the test projects and
modules can be extracted from CVS, built, deployed, tested, and undeployed.

The
benefit of using this approach is that you do not need to manually
manage a set of project interchange (PI) files.

## Procedure

1. The script for this case can be seen in Working with scripts. Rather than importing
test cases and modules from a project interchange file, the project
is checked out from a CVS rep
2. Examine the pass/fail results in the returned XML file.
See Example of an XML output file, which
shows an example of the type of output you should expect.  You
are required to have an understanding of CVS commands in this situation as this task
uses the CVS command to run.