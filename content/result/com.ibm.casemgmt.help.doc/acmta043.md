# Cannot deploy a solution with business rules if transaction
timeout value is too low

## Symptoms

When you deploy a solution that contains rules, the
following error message is returned:

FNRPA0624E The
rules could not be deployed because of the following error: A transaction
problem has occurred. Message was: ; nested exception is: com.ibm.websphere.csi.CSITransactionRolledbackException:
Transaction marked rollbackonly 7/19/13 11:14:06 PM PDT FNRPA0093E
The previous error was caused by: A transaction problem has occurred.
Message was: ; nested exception is: com.ibm.websphere.csi.CSITransactionRolledbackException:
Transaction marked rollbackonly

## Causes

## Resolving the problem

1. Go to the Application servers > server1 > Transaction service page in the WebSphere® Application
Server administrative console.
2. Increase the value of the Total transaction lifetime timeout setting to a
higher value, such as 300 seconds.

After the solution is successfully deployed, change the value
of the transaction timeout setting back to the previous value.