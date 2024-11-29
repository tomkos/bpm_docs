<!-- image -->

# Late binding calls the wrong version of a subprocess

## Reason

A common reason for late binding using the wrong version of a subprocess is that the module
that contains the subprocess does not have a Service Component Architecture (SCA) export. Without an
export, processes in other modules are not visible to the parent process and it always invokes the
version of the subprocess that is in the same module.

## Resolution