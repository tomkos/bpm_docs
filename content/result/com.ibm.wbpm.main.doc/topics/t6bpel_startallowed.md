<!-- image -->

# Determining the BPEL process templates or activities that can be
started

## About this task

When a business process is modeled, the modeler can decide
that only a subset of users can create a process instance from the
process template. This is done by associating an inline invocation
task to a starting activity of the process and by specifying authorization
restrictions on that task. Only the people that are potential starters
or administrators of the task are allowed to create an instance of
the task, and thus an instance of the process template.

If
an inline invocation task is not associated with the starting activity,
or if authorization restrictions are not specified for the task, everybody
can create a process instance using the starting activity.

A
process can have more than one starting activity, each with different
people queries for potential starters or administrators. This means
that a user can be authorized to start a process using activity A
but not using activity B.

## Procedure

1. Use the Business Flow Manager API to create a list of the
current versions of process templates that are in the started state. 
Tip: The queryProcessTemplates method excludes only those process templates that are part of applications
that are not yet started. So, if you use this method without filtering
the results, the method returns all of the versions of the process
templates regardless of which state they are in.
// current timestamp in UTC format, converted to yyyy-mm-ddThh:mm:ss
String now = (new UTCDate()).toXsdString();    
String whereClause = "PROCESS\_TEMPLATE.STATE = 
                      PROCESS\_TEMPLATE.STATE.STATE\_STARTED AND
                      PROCESS\_TEMPLATE.VALID\_FROM = 
                      (SELECT MAX(VALID\_FROM) FROM PROCESS\_TEMPLATE 
                       WHERE NAME=PROCESS\_TEMPLATE.NAME AND 
                       VALID\_FROM <= TS('" + now + "'))";
                                                 
ProcessTemplateData[] processTemplates = process.queryProcessTemplates
                                        ( whereClause, 
                                          "PROCESS\_TEMPLATE.NAME",
                                          (Integer)null, (TimeZone)null);The results are sorted by process template
name.
2. Create the list of process templates and the list of starting
activities for which the user is authorized. The list
of process templates contains those process templates that have a
single starting activity. These activities are either not secured
or the logged-on user is allowed to start them. Alternatively, you
might want to gather the process templates that can be started by
at least one of the starting activities. Tip: A process
administrator can also start a process instance. However,
if Business Flow Manager is using the alternative process administration
mode that restricts process administration to system administrators,
then only users in the BPESystemAdministrator role can perform this
action. Therefore, to get a complete list of templates, you also need
to check whether the logged-on user is an administrator.

List authorizedProcessTemplates = new ArrayList();
List authorizedActivityServiceTemplates = new ArrayList();
3. Determine the starting activities for each of the process
templates. for( int i=0; i<processTemplates.length; i++ )
{
  ProcessTemplateData template = processTemplates[i];
  ActivityServiceTemplateData[] startActivities = 
                 process.getStartActivities(template.getID());
4 For each starting activity, retrieve the ID of the associatedinline invocation task template. for( int j=0; j<startActivities.length; j++ ){ ActivityServiceTemplateData activity = startActivities[j]; TKTID tktid = activity.getTaskTemplateID();

```
for( int j=0; j<startActivities.length; j++ )
{
  ActivityServiceTemplateData activity = startActivities[j];  
  TKTID tktid = activity.getTaskTemplateID();
```

    1. If an invocation task template does not exist, the process
template is not secured by this starting activity.  In this case, everybody can create a process instance using this
start activity. 
boolean isAuthorized = false;
       if ( tktid == null ) 
    {  
      isAuthorized = true; 
      authorizedActivityServiceTemplates.add(activity);      
    }
    2. If an invocation task template exists, use the Human
Task Manager API to check the authorization for the logged-on user.
In the example, the logged-on user is Smith. The logged-on
user must be a potential starter of the invocation task or an administrator. 
if ( tktid != null ) 
    {   
      isAuthorized = 
        task.isUserInRole
            (tkid, "Smith", WorkItem.REASON\_POTENTIAL\_STARTER) || 
        task.isUserInRole(tktid, "Smith", WorkItem.REASON\_ADMINISTRATOR);

      if ( isAuthorized ) 
      {   
        authorizedActivityServiceTemplates.add(activity);
      }
    }If the user has the specified role, or if people
assignment criteria for the role are not specified, the  isUserInRole method returns the value true.
5. Check whether the process can be started using only the
process template name. if ( isAuthorized && startActivities.length == 1 ) 
    {   
      authorizedProcessTemplates.add(template);
    }
6. End the loops.   } // end of loop for each activity service template
}   // end of loop for each process template