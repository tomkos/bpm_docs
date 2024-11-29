# BPMMigrationStatus command-line utility

The BPMMigrationStatus command displays the status of all the migrations that
are in progress or complete on the current system. Each migration is uniquely identified by the
source install root, the source profile name, the snapshot directory of the source profile, the
target install root, and the target profile name.

## Location

The BPMMigrationStatus command-line utility is in the
target\_install\_root/bin directory.

## Syntax

```
BPMMigrationStatus 
[-clean]
```

## Parameters

## Examples

Examine the migration
status on the current system:

- BPMMigrationStatus.sh
- BPMMigrationStatus.bat

Clean up and remove all prior migration status information
from the current system:

- BPMMigrationStatus.sh -clean
- BPMMigrationStatus.bat -clean