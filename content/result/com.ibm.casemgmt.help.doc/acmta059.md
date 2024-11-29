# Configuring the object stores failed

## Symptoms

An
error occurs while running Configure the Case Management Object Stores.
The task fails because of the following error:

The
case management add-ons cannot be installed in Content Engine. The
installation of the AddOn 5.3.2 Case Manager Target Object Store Extensions
into the object store TOS failed. The installation report follows:
PostImportScriptMethod failed with exception: There was an error running
the script. Message was: Wrapped com.filenet.api.exception.EngineRuntimeException:
FNRCE0075E: E\_TRANSACTION\_FAILURE: A transaction failure has occurred
due to an invalid state or timeout. The current transaction state
is STATUS\_MARKED\_ROLLBACK and it was expected to be active failedBatchItem=0
(#256).

## Causes

## Resolving the problem

- Servers > Server Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > Transaction service > Total transaction lifetime timeout
- Servers > Server Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > Transaction service > Maximum transaction lifetime timeout
- Servers > Server Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > ORB service > Request
timeout
- Servers > Server Types > WebSphere application servers > Configuration
tab > Container Settings > Container
Services > ORB service > Locate
request timeoutNote: For WebSphere Application
Server Version 8.5.2,
the maximum value for the locate request timeout is 300.
- Resources > JDBC > Data sources >  [Content Engine or
Case Manager data source name]  > Connection Pool
properties > Connection timeout
- Resources > JDBC > Data sources >  [Content Engine or
Case Manager XA data source name] > Connection
Pool properties > Connection timeout