<!-- image -->

# Using the "-clean" option when starting IBM Integration
Designer

## About this task

## Procedure

1. From a command line, change to the package group installation
directory where you  installed IBM Integration
Designer.
2. Run the command to start IBM Integration
Designer with
the -clean option: wid.exe -clean

## What to do next

- removes and regenerates manifest files.
- removes cached binary files and regenerates them from the newly created manifest files.
- removes and regenerates JXE information.
- removes and regenerates the runtime plug-in registry.

It is a good practice to start IBM Integration
Designer using the -clean option
after applying any Interim Fixes. This will ensure that the plug-in registry is regenerated to
reflect any changes from the applied fixes. This only needs to be done once after applying any
Interim Fix, as running with -clean takes considerable time in regenerating the
plug-in registry.