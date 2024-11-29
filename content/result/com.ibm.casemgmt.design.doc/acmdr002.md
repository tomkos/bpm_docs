# Validating preconditions

Using commands, you can run the precondition checker utility to validate preconditions
after changing property preconditions for an existing activity. The precondition checker looks for
activities that were created before the precondition changed and evaluates the updated activity. If
the new precondition is met, the activity status changes to working status.

Alternatively, you can use the Case Manager REST
protocol to run the precondition checker rather than using commands to run it.

## Precondition checker utility

- The criteria changes for an activity with a A property condition is met
precondition.
- The precondition changes from A document is filed in the case or
A case property is updated to A property condition is
met.
- Or, any precondition changes to No precondition.

| Platform           | File name               | Location                                                                                                        |
|--------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| AIX®               | preconditionChecker.sh  | /opt/IBM/CaseManagement                                                                                         |
| Linux®             | preconditionChecker.sh  | /opt/IBM/CaseManagement                                                                                         |
| Linux for System z | preconditionChecker.sh  | /opt/IBM/CaseManagement                                                                                         |
| Windows            | preconditionChecker.bat | C:\Program Files\IBM\CaseManagement for a fresh installC:\Program Files (x86)\IBM\CaseManagement for an upgrade |

## Syntax

preconditionChecker
command
parameter
value

## Commands

## Parameters

```
preconditionChecker launch -cews\_uri http://myserver:9080/wsi/FNCEWS40MTOM 
-username administrator -password mypassword 
-target\_os MyTargetOS -solution 'credit card dispute'
```

## Case Manager REST protocol for the precondition
checker

You can use the Case Manager REST protocol to run the precondition checker. The following example
is a URI for the POST method:

```
https://host\_name:port\_number/CaseManager/CASEREST/v1/preconditionchecker
```

## Request content

The request for the POST method contains the following parameters in JSON in the body:

```
{
  "command" : "launch -Start the precondition checker utility. Required."
              "suspend -Stop the precondition checker utility.",
   "cews\_uri" : "The web services URI used to connect to Content Platform Engine. Required. For example: https: //myserver:9080/wsi/FNCEWS40MTOM",
   "username" : "The user ID used to connect to Content Platform Engine. Required.",
   "password" : "The password for the specified user ID used to connect to Content Platform Engine. Required.",
   "target\_os" : "The target object store. Required.",     
   "solution" : "The name of the solution that the precondition checker will check. Optional. If no solution is specified, the precondition checker API checks all deployed solutions." 
   "batchSize" : "The number of items to retrieve and process at one time. Optional. If not specified, the default batch size is 1000 items.",  
   "threadPoolSize" : "The number of active threads when processing activities. Optional. The default value is four threads."
}
```

The value of preconditioncheckerresult in the response JSON
indicates whether the precondition checker ran successfully.