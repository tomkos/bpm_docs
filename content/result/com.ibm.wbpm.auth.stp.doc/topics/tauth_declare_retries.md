<!-- image -->

# Declaring retries for operations at design time

## About this task

On the properties page of your module, you can set the
retry count on the Asynchronous Retry Count page.
Select the module, display the properties, and select Business Integration > Asynchronous
Retry Count. On your runtime server, when
a system error occurs, asynchronous invocations retry until the retry
count that you set here is reached.

To change the retry count
for more than one project, right-click a module and select Configure
asynchronous retry counts to open a wizard where you can
set retry counts for any of the existing modules. New modules have
a retry count of 0. Existing modules that were created in an earlier
version of Integration Designer have
the same retry count that was previously specified. However, you can
change the asynchronous retry count for new or existing modules to
fit the needs of your application.

When you set the retry count
in the module and install the application, the retry count is specified
for the service bus destination. However, if you specified the JNDI
name of an existing destination on a server, the retry count is not
changed, and the original retry count is kept for that destination.

To
control retries at the operation level, use ServiceInvoke and Callout mediation
primitives.