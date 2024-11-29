# Assigning pre- and post-execution scripts

## About this task

In a client-side human service or service flow, you can add pre- and post-execution scripts to
all activities and event nodes that support the pre- and post-execution script function. For
example, start nodes support pre- and post-execution scripts in client-side human services but not
in service flows, while end nodes support pre- and post-execution scripts in both client-side human
services and service flows.

In
the script editor, use standard JavaScript syntax to add the appropriate
pre- or post-execution JavaScript code.

When you add the scripts to a postpone event, the event runs the pre- and post-execution scripts
before saving the execution context and before navigating to the specified URL. Similarly, the end
event in a root client-side human service that is used as a task runs both the pre- and
post-execution scripts before returning the control to the process.

## Procedure

To assign a pre-execution or post-execution script to an activity or event in a
client-side human service or service flow:

1. Open the service that includes the activity or event that requires a pre-execution or
post-execution script.
2. Select the activity or event node in the service flow diagram, and then switch to the
Pre & Post properties.
3. Enter or paste the appropriate JavaScript code in the
Pre-Execution Script section or the Post-Execution
Script section.

For example, assume that you wanted to synchronize a customer's shipping and billing
addresses as part of an order confirmation page that is included in a larger client-side human
service. To achieve this result, you can add a post-execution script that is similar to the
following JavaScript sample code to the order confirmation page. The post-execution script runs
immediately after the execution of the order confirmation page completes and synchronizes the two
addresses.if (tw.local.sameAsShipTo) {
   tw.local.billToAddress = tw.local.shipToAddress;
}When you assign a pre- or post-execution script to an activity or
event, its node in the diagram view includes a circular indicator on the left side (pre-execution)
or on the right side (post-execution).
4. Click Save or Finish Editing.