<!-- image -->

# Asynchronous parallel processing

Figure 1. Branched aggregation block

<!-- image -->

1. Specify the Invocation style property on each Service Invoke mediation primitive to be
Async, as shown in Figure 2. Figure 2. Service invoke mediation primitive property details
2. If the mediation flow component is configured to run under a Global Transaction, ensure that the
component Reference that is associated with the Service Invoke mediation primitive has a qualifier
for Asynchronous invocation that is set to  Call, as shown in Figure 3.Figure 3. Setting the Asynchronous invocation qualifier

If a global Transaction is configured, and the Asynchronous invocation setting is
Commit, then request messages are never sent, because the service request
cannot be sent until the transaction commits.
3. An additional step of configuration is required when the aggregation block processes in Iterate
mode. Using the Fan Out mediation primitive you can specify the number of concurrent unprocessed
requests that can be made before the response messages are processed. By specifying an integer value
in the Check for asynchronous responses after 
X
messages have been fired field, as shown in Figure 4, the runtime completes
the processing of X requests and then processes the response messages before
further iterations are processed. This way you can restrict the number of parallel requests being
processed by back-end services, such as the Payroll and HR services. To process all entries within
the array before the handling of any response messages, select Check for asynchronous
responses after all messages have been fired.Figure 4. Setting the number of requests that should be processed

By using the Invocation style and Asynchronous invocation settings both Payroll and HR services
are called before either of the response messages being processed.