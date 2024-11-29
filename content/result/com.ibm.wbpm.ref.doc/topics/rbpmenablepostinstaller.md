<!-- image -->

# BPMEnablePostInstaller command-line utility

The BPMEnablePostInstaller command runs the required scripts for all the fixes
that are installed during an upgrade.

## Prerequisites

Run this command only when you are instructed to while you are following the steps to install an
upgrade in a swinging profiles environment.

Run this command on the computer that has the deployment manager profile and also on each
separate computer that has a managed node.

## Location

The BPMEnablePostInstaller command-line utility is in the
install\_root\_24.x/bin
directory.

The log file is in
install\_root\_/logs/postinstall/BPMEnablePostInstaller\_timestamp.log.

## Syntax

```
install\_root\_24.x/bin/BPMEnablePostInstaller 
-ifix [interim\_fix\_name,interim\_fix\_name, ... ]
```

## Parameters

## Examples

- BPMEnablePostInstaller -iFix
- BPMEnablePostInstaller.sh -ifix 8.6.10019001-WS-BPM-IFJR00000