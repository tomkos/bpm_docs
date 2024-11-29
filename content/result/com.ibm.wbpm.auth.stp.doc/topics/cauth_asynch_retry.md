<!-- image -->

# Asynchronous retry count for modules

Clients typically determine the calling style, but some components,
such as long-running processes, human tasks, and message bindings
(WebSphere MQ, MQ JMS, generic JMS, and JMS imports) are always invoked
asynchronously. Also, you can indicate how components are to be invoked
by setting the preferred interaction style. Asynchronous invocations
typically involve a transaction boundary, and when an error occurs,
system retries are possible.

A service integration bus destination is created when a business
module or a mediation module is deployed. Service integration bus
destinations handle asynchronous invocations in a module. Also, service
integration buses destinations are created for asynchronously invoked
components when store and forward or event sequencing qualifiers are
specified and when a JMS import or export has destination properties
defined in the binding. The Maximum failed deliveries per
message setting for service integration bus destinations
defines the number of retries when a runtime error occurs.

In Integration Designer,
you have visibility and control over the retries for service integration
bus destinations that are created when the applications are deployed.
You can set the asynchronous retry count for a module. The retry count
indicates the number of times that the system retries asynchronous
events at run time at the project level. When you deploy your application,
the retry count is used to correctly set the service integration bus
destination Maximum failed deliveries per message value.

Administrators can create destinations for WebSphere MQ, MQ JMS,
generic JMS, and JMS message bindings, and they can define the maximum
failed deliveries per message value at that time. The maximum failed
deliveries value is not affected by the asynchronous retry count for
a module or by the configSCAAsyncRetryCount command.

You can set the retry count on the properties page of your module,
or you can change the retry count for more than one module using the Configure
Asynchronous Retry Count wizard. When a system error occurs,
asynchronous invocations retry until the configured retry count is
reached. New modules are created with a retry count of zero. Modules
from earlier versions keep existing retry settings during migration.
(In earlier versions, modules were created with a retry count of 4.)

At run time, you can see the retries for each service integration
bus by selecting Service integration > Buses on the administrative console
and then looking at the destinations for the SCA system bus, or the
SCA application bus if you have a JMS import or export.

Administrators can use the configSCAAsyncRetryCount command
to change the asynchronous retry count for a module, all modules in
a server, or all modules in a deployment target. The command changes
the retry count for the destinations that are created when the application
is deployed. For example, if there is unintended or unwanted behavior
in an application, you might want to have administrators turn off
the retry settings, until you change the application and redeploy.

When planning your application, consider when hop reduction can
occur and how it affects the error logic in your application. For
example, when a JMS export is used, hop reduction causes the first
component invocation to use the JMS destination and not the SCA module
destination. Therefore, a runtime error can flow back to the JMS destination
where its retry logic is invoked. If retries occur there, the performance
hop is removed and the module destination is used. Now if a runtime
error occurs, it flows back to the SCA module destination where its
retry logic is invoked. Depending on how retries are configured, when
the last retry fails, failures from the module destination go to the
failed event manager and failures from the JMS destination go to its
default error destination. For information about hop reduction and
destinations, see Retry configuration.