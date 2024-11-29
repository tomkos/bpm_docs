# Event catalog pattern query fails on a Windows system

## Cause

The percent character (%)
is a reserved character in the Windows command-line
interface and is not passed properly to the eventcatalog command.

## Remedy

```
eventcatalog -listdefinitions -name EVENT%% -pattern
```