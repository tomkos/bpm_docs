<!-- image -->

# Shared people assignments

The sharing of results applies only if a people assignment criteria
definition contains fixed parameter values. Such values, for example,
the name of a group: cn=group1, cn=groups, imply
that the corresponding people query result is the same, regardless
of the task instance context in which the people query is resolved.

If the people assignment criteria definition contains replacement
variables, the sharing scope is reduced to people assignments that
have the same replacement variable values. For example, a parameter
value can depend on parts of the input message of a task. Because
different task instances can have different input messages, the parameter
values for the people queries differ, too.

If you post process people query results, sharing does not apply
to these results by default. To enable the sharing of post-processed
results, complete the following steps in the administrative console:

1. Click Servers > Clusters > WebSphere application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer, and click Human Task Manager.
2. In the Additional Properties section, click Custom
Properties and change the value of the Staff.PostProcessorPlugin.EnableResultSharing custom
property to true, then save your
changes
3. Restart the server or cluster to make the changes effective.

<!-- image -->