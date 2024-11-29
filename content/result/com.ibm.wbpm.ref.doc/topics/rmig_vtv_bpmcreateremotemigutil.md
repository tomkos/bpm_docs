# BPMCreateRemoteMigrationUtilities command-line utility

The BPMCreateRemoteMigrationUtilities command
creates the archive file specified by the archive\_file\_name parameter
containing all of the commands and their prerequisites that must be
run on the system containing the source profile to be migrated.

## Prerequisites

On Linux or UNIX platforms, ensure that all extracted files have execute permission for the
logged-in user. Otherwise, use the chmod command to grant execute permission for
all extracted files.

## Location

The BPMCreateRemoteMigrationUtilities command-line utility is in the
install\_root/bin directory on the new system.

The location of the archive file is displayed when you run the
BPMCreateRemoteMigrationUtilities command. By default, the archive file is in the
install\_root/util/migration/scripts directory.

## Syntax

```
BPMCreateRemoteMigrationUtilities 
full\_path\_and\_archive\_file\_name
```

```
BPMCreateRemoteMigrationUtilities 
full\_path\_and\_archive\_file\_name 
32bit
```

## Parameters

## Examples

```
BPMCreateRemoteMigrationUtilities remoteMigrationUtilities.zip
```

```
BPMCreateRemoteMigrationUtilities remoteMigrationUtilities-32bit.zip 32bit
```