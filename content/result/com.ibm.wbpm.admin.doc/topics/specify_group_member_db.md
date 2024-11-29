# Specifying that members of a group member cache are retrieved
from the database

## About this task

The configuration setting improves the performance of process application deployment, changes to
group memberships in the Process Admin Console, and internal group membership lookups, for example,
for assignment of roles. It also minimizes the scenarios where an LDAP connection timeout can
occur.

## Procedure

```
<properties>
     <server merge="mergeChildren">                 
          <group-member-cache-source merge="replace">DB</group-member-cache-source>            
     </server>
</properties>
```

## Results

Depending on the user activity in an environment, it might be possible that
the group memberships in the database are not as up-to-date as required when you use the
group-member-cache-source setting. To help resolve this problem, there are scripts
independent of the user login and group-member-cache-source setting that can be
used to update the group memberships. However, depending on the number and complexity of group
memberships, these scripts can run for a long time and must be evaluated carefully. For more information, see Synchronizing group membership by
groups.