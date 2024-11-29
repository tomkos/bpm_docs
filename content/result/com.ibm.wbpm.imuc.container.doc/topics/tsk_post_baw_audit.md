# Enabling the audit log

## Procedure

1. By default, the audit log is disabled. To enable it, add the following configuration in
your CR.  The following example uses baw\_configuration for Workflow
Runtime.baw\_configuration:
    ## audit log configuration
    audit\_log:
        ## Whether to enable Process Admin Console audit log. Default value is false.
        enable: true
2. For the list of parameters, see the audit parameters listed in IBM Business Automation Workflow Runtime and
Workstream Services parameters