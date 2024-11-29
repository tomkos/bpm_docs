# Changing deployment hostname suffix after installation

## Procedure

Try the following steps:

1. Delete the Process Federation Server UMS
registration job.  To find the job, search for pfs-umsregistry-job in
the name.
2 Set the data "UMS\_REGISTERED\_UPDATE *" to false in the following configmaps:
    - cmis-ums-config
    - cpe-ums-config
    - graphql-ums-config
    - icn-ums-config