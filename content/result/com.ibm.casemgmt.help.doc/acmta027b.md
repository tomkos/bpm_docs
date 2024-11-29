# Deployment of rules fails during solution deployment in IBM Business Automation
Workflow

## Symptoms

When you deploy your case management solution in Business Automation Workflow, you might see an error
similar to the following error: [6/22/18 12:37:14:086 CST] 000001c5 api E
com.ibm.casemgmt.api error FNRPA0624E The rules could not be deployed because of the following
error: An exception occurred in the event handler. Message was: FNRPE0029E:
[RULE\_DEPLOYMENT\_RULE\_DEFINITION]: For case type CC\_Compliant, exception occurred while converting
following rule definition(s): CustomerRatingTable
com.ibm.casemgmt.intgimpl.deploy.handlers.ContinuableStepException: FNRPA0624E The rules could not
be deployed because of the following error: An exception occurred in the event handler. Message was:
FNRPE0029E: [RULE\_DEPLOYMENT\_RULE\_DEFINITION]: For case type CC\_Compliant, exception occurred while
converting following rule definition(s): CustomerRatingTable at
com.ibm.casemgmt.intgimpl.deploy.handlers.ContinuableStepException.createContinuableStepException(ContinuableStepException.java:35)

## Causes

The ODMMessages.jar file, required for the embedded IBM Operational Decision
Manager rules SDK, is missing from the Content Platform Engine directory.

## Resolving the problem

Complete the following steps to copy the required file on your system before you reattempt
solution deployment:

1. Copy the ODMMessages.jar file from the Business Automation Workflow home directory
/opt/ibm/Workflow/v18.0/lib/ext to the external Content Platform Engine directory at
<WAS-home>/lib/ext.
2. Restart the external Content Platform Engine.