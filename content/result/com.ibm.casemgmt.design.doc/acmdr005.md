# Synchronizing cases with solution data

When you change the case type of a solution and redeploy the solution, the changes are
applied to new case instances. The changes are not applied to running case instances.

- Creating a new folder structure
- Case folder structure changes
- New activities that are added to a case type
- Changes to a container activity (Add or Delete) of subactivities that are associated with a
container
- Changes to activity launch modes (Manual, Automatic, Discretionary, Repeatable)
- Changes to activity-required states (Required, Optional)
- Changes to activity group modes (Inclusive, Exclusive)

The case synchronizer utility processes case instances in batches. The processed case
instance ID is stored in the casesynchronizer.processed file in the path where
the tool is run. If a batch runs without any errors, the tool deletes this file. If errors occur
during the execution of the case synchronizer utility, the tool checks for the case instance IDs and
so on.

| Platform           | File name            | Location                                  |
|--------------------|----------------------|-------------------------------------------|
| AIX®               | caseSynchronizer.sh  | /opt/IBM/CaseManagement                   |
| Linux®             | caseSynchronizer.sh  | /opt/IBM/CaseManagement                   |
| Linux for System z | caseSynchronizer.sh  | /opt/IBM/CaseManagement                   |
| Windows            | caseSynchronizer.bat | C:\Program Files (x86)\IBM\CaseManagement |

## Syntax

caseSynchronizer
command
parameter-list

parameter-list consists of a set of name-value pairs, where each pair has a
parameter and a value, separated by a space.

## Commands

## Parameters

## Examples

- start the case synchronizer for cases of type Accident Report
- update every case instance of that case type
- update the changes that are made to that case type

```
caseSynchronizer launch -cews\_uri http://myserver:9080/wsi/FNCEWS40MTOM 
-username administrator -password mypassword 
-target\_os MyTargetOS -caseType 'ABC\_AccidentReport'
```

```
caseSynchronizer launch -cews\_uri http://myserver:9080/wsi/FNCEWS40MTOM 
-username administrator -password mypassword  -batchSize 2000
-target\_os MyTargetOS -caseType ‘ABC\_AccidentReport' -includedTaskTypes ABC\_VerifyData, ABC\_ProcessClaim
```

```
caseSynchronizer launch -cews\_uri http://myserver:9080/wsi/FNCEWS40MTOM 
-username administrator -password mypassword -threadPoolSize 8
-target\_os MyTargetOS -caseType 'ABC\_AccidentReport' -excludedTaskTypes ABC\_CheckCustomerData, ABC\_ReportClaim
```

It
changes the threadPoolSize to 8 and includes a comma-separated list of activity
types that are excluded or skipped by the case synchronizer utility.

Example 4:

```
caseSynchronizer launch -file /home/user/input\_case\_synchronizer
```

```
caseSynchronizer suspend
```

The number of case instances that
are processed by the case synchronizer can be further filtered by using the
-caseTypeFilter argument. The value in the -caseTypeFilter
argument can be based on any case instance property. The value is used as a search condition for
retrieving the case instances.

```
caseSynchronizer launch -cews\_uri http://myserver:9080/wsi/FNCEWS40MTOM  
-username administrator -password mypassword -target\_os MyTargetOS -caseType 'ABC\_AccidentReport' 
-caseTypeFilter '[ABC\_isValidCustomer] = true AND [ABC\_ClaimAmount] >= 100'
```

## Case Manager REST protocol for the case synchronizer

You can use the Case Manager REST protocol to run the case synchronizer. The following example is
a URI for the POST method:

```
https://host\_name:port\_number/CaseManager/CASEREST/v1/casesynchronizer
```

## Request content

The request for the POST method contains the following parameters in JSON in the body:

```
{
   "command" : "launch -Start the case synchronizer. Required.",
              "suspend -Stop the case synchronizer.",
   "cews\_uri" : "The web services URI used to connect to Content Platform Engine. Required. For example: https://myserver:9080/wsi/FNCEWS40MTOM",
   "username" : "The user ID used to connect to Content Platform Engine. Required.",
   "password" : "The password for the specified user ID used to connect to Content Platform Engine. Required.",
   "target\_os" : "The target object store. Required.",
   "caseType" : "The name of the case type for which the case synchronizer is to be run. Required. If the name of the case type includes spaces, surround the name with single quotation marks. For example: -caseType 'Accident report'",     
   "caseTypeFilter" : "The filter criteria to use when retrieving the case instances to update. This parameter is optional.",
   "includedTaskTypes" : "A comma-separated list of the task type symbolic names to add to the case instances. This parameter is optional.",
   "excludedTaskTypes" : "A comma-separated list of the task type symbolic names to exclude from the update to the case instances. This parameter is optional.",
   "batchSize" : "The number of items to retrieve and process at one time. Optional. If not specified, the default batch size is 1000 items.",  
   "threadPoolSize" : "The number of active threads when processing activities. Optional. The default value is four threads."
}
```

The value of casesynchronizerresult in the response JSON indicates
whether the case synchronizer ran successfully.