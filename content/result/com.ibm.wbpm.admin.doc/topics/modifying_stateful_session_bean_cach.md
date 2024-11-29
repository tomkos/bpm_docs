# Modifying the stateful session bean cache

If your IBM® Business Automation Workflow server
has many users connected, the server's heap might grow to huge values.
If you perform a heap dump and analyze it, you can see that a large
part of the heap is occupied by WebWorkflowManager objects nested
in HTTP session objects.

IBM Business Automation Workflow keeps
a cache of stateful session beans (one session bean for each human
service that a user works with). This cache is stored inside the user's
HTTP session. The cache update policy removes a stateful session bean
from the cache if it has not been accessed for more than one hour.
If a user works with multiple human services, many stateful session
beans will be in the cache for this user.

- For human services of user tasks in a business process definition
(BPD) instance, the state of the stateful session bean is saved in
the database with the associated task; therefore, the cache for these
human services is not needed.
- Human services that start directly from Process Portal (exposed
as startable) do not have an associated task; therefore, the cache
is not modified for these services.

To modify the default cache timeout (60 minutes), edit the appropriate 100Custom.xml file
to your topology. For more information about the location of the 100Custom.xml file
that must be updated, see the topic Location of 100Custom configuration files.

```
<web-workflow-manager>
    <session-bean-cache-expiry-timeout merge="replace">timeout in minutes</session-bean-cache-expiry-timeout>
</web-workflow-manager>
```

```
<properties>
    <server>
        <web-workflow-manager>
            <session-bean-cache-expiry-timeout merge="replace">50</session-bean-cache-expiry-timeout>
        </web-workflow-manager>
    </server>
</properties>
```

If your processes run on a cluster, you must make this change for
each cluster member.