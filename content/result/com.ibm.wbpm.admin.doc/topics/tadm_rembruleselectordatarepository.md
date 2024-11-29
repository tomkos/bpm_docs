<!-- image -->

# Removing business rule and selector data from the repository

## Before you begin

## About this task

When you install an application containing business rule or selector artifacts, the server stores
these artifacts in database tables so that you can dynamically update them without changing the
application. This also allows other servers to share these artifacts. When you uninstall an
application, the server does not automatically remove these artifacts from the database tables
because the application may still be installed and running on another server. Deleting the artifacts
from the database causes the other running copies of the application to fail when they try to use
business rules or selectors.

To remove unneeded business rule and selector artifacts from the repository, perform the
following steps.

## Procedure

1. Locate the following database tables from which you will delete rows:

BYTESTORE
The main table that contains the business rule and selector artifacts
BYTESTOREOVERFLOW
The overflow table for the main table
APPTIMESTAMP
The table that holds a timestamp of installed applications that contain business rule and
selector artifacts
CUSTPROPERTIES
The table that holds custom user-defined properties and system properties for a business rules
group, rule set, or decision table.
2 Using the tools for your database platform, follow these steps to delete all business rule andselector artifacts for a given application:
    1. Find all of the rows in the BYTESTORE table where the APPNAME column is
the same as the name of the application.
    2. Record the values of the primary key columns for all of the rows found. The primary key columns
for the BYTESTORE table are ARTIFACTTNS, ARTIFACTNAME, and
ARTIFACTTYPE.
    3. Delete the rows found in step 2a from the BYTESTORE table.
    4. For each set of primary key values recorded in step 2b, find the rows in the BYTESTOREOVERFLOW
table that have the same values in the corresponding columns.

Note: For a given set of primary key values, there may be zero, one, or more than one row in the
BYTESTOREOVERFLOW table.
    5. Delete the rows found in step 2d from the BYTESTOREOVERFLOW table.
    6. For each set of primary key values recorded in step 2b, find the rows in the CUSTPROPERTIES
table that have the same values in the corresponding columns.
    7. Delete the rows found in step 2f from the CUSTPROPERTIES table.
    8. Delete the row in the APPTIMESTAMP table where the APPNAME column equals
the name of the application.

## Results