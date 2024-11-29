# Disabling VCS integration

## About this task

Disabling VCS integration stops IBM® Business Automation
Workflow from running the
commit and deliver scripts that are used to copy solution information to the VCS.

## Procedure

To disable VCS integration:

1 Run the following command: BPMConfig -update -de DE\_name -enableVCS false -component CaseManager -profile profile\_name where

```
BPMConfig -update -de DE\_name -enableVCS false -component CaseManager -profile profile\_name
```

    - DE\_name is the name of the IBM Business Automation Workflow development environment
    - profile\_name is the name of the IBM Business Automation Workflow configuration profile
2. Restart the IBM Business Automation Workflow application
server.
3. Optional: 
Remove the files from the sandbox.
IBM Business Automation
Workflow does not remove the files from the sandbox when
you disable VCS integration.

## Results