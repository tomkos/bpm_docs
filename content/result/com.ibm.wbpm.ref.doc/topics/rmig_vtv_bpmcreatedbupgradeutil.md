# BPMCreateDatabaseUpgradeUtilities command-line utility
(deprecated)

The BPMCreateDatabaseUpgradeUtilities command creates the archive file
specified by the archive\_file\_name parameter that contains all of the commands
and their prerequisites that need to be invoked on the database system where the database upgrade is
to be performed.

The location of the archive file is displayed when you run the
BPMCreateDatabaseUpgradeUtilities command. By default, the archive file is in the
install\_root/util/migration directory.

## Prerequisites

For the network deployment environment, this command must be run on the machine that has the
deployment manager profile.

## Location

The BPMCreateDatabaseUpgradeUtilities command-line utility is in the
target\_install\_root/bin directory.

Errors are logged in the snapshot directory in a file whose name begins with
BPMCreateDatabaseUpgradeUtilities and ends with
.error.

## Syntax

```
BPMCreateDatabaseUpgradeUtilities 
archive\_file\_name 
snapshot\_directory
```

## Parameters

## Examples

Create the archive containing the remote migration utilities:

- BPMCreateDatabaseUpgradeUtilities.sh upgradeUtilities.zip /MigrationSnapshots/ProcSrv01
- BPMCreateDatabaseUpgradeUtilities upgradeUtilities.zip c:\MigrationSnapshots\ProcSrv01