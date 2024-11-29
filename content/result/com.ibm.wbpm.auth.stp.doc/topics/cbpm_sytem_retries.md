<!-- image -->

# Controlling system retries

For example, if you know that a service might become unavailable
for a short time for maintenance, you might want to design your application
to store requests, and to be able to retry when the service is available
again after the maintenance.  However, a retry of an operation in
some scenarios might cause negative results, especially if the underlying
component or service is not transactional.

In Integration Designer,
you have visibility and control over the retries that you plan for
run time on the process server.

When you use an asynchronous invocation and a runtime error occurs,
retries might occur. You can set the asynchronous retry count for
a module. When you deploy the module, the retry count takes effect.
When necessary, administrators can change module retry settings at
run time using the configSCAAsyncRetryCount command.

When you use mediations, you can specify retries at the operation
level using the service invocation primitive and the callout primitive.
The retry behavior of the mediation primitives overrides the asynchronous
retry count, even if you do not specify retries.

When working with long-running BPEL processes, and you want to
have several activities participate in the same transaction, retries
might occur.

If an application is updated from the administrative console
or from Integration Designer,
event sequencing and store and forward changes are not included. If
you want the retry count to be updated with event sequencing and store
and forward changes, you must redeploy the application or use the configSCAAsyncRetryCount command.

- Asynchronous retry count for modules

Asynchronous invocations in the runtime server involve using a queue, which is a service integration bus destination.
- Mediation flow retries

In the Mediation Flow editor, the mediation primitives ServiceInvoke and Callout have retry properties (Retry on, Retry count Retry delay(second)) that you can use to control retries when a service operation is invoked. The mediation retry logic overrides the underlying asynchronous retry logic on the service integration bus destinations.
- BPEL process retries

If you are deploying to IBM® Workflow Server and using BPEL, the transaction attributes for the Commit before, Commit after and Participates settings provide performance hints to the process engine, attempting to invoke the activity (with other activities) in a global transaction.
- Declaring retries for operations at design time

Declare retry counts for operations when you are designing in Integration Designer.