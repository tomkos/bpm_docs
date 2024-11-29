- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface StaffQueryResultPostProcessorPlugin

- public interface StaffQueryResultPostProcessorPlugin This interface provides for methods that allow to modify StaffQueryResult data. This plug-in provides for methods to post process staff result data on different levels. That means, for different roles different methods are called. Example: This is a sample list, it is not complete. Note: The plug-in is available once per installation, so all tasks use this plug-in, that is, the staff results for all tasks are filtered by this plug-in. Code Sample: (handles the Editor role of a certain task with name "SpecialTask")import java.util.Collection;import java.util.Locale;import java.util.Map;import com.ibm.task.api.ApplicationComponent;import com.ibm.task.api.Escalation;import com.ibm.task.api.EscalationTemplate;import com.ibm.task.api.Task;import com.ibm.task.api.TaskTemplate;import com.ibm.task.spi.StaffQueryResult;import com.ibm.task.spi.StaffQueryResultFactory;import com.ibm.task.spi.StaffQueryResultPostProcessorPlugin;import com.ibm.task.spi.UserData;public class MyStaffResultProcessor implements StaffQueryResultPostProcessorPlugin{ public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult, ApplicationComponent applicationComponent, int role, Map context) { return(originalStaffQueryResult); } public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult, Escalation escalation, Task task, int role, Map context) { return(originalStaffQueryResult); } public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult, EscalationTemplate template, int role, Map context) { return(originalStaffQueryResult); } public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult, Task task, int role, Map context) { StaffQueryResult newStaffQueryResult = originalStaffQueryResult; StaffQueryResultFactory staffResultFactory = StaffQueryResultFactory.newInstance(); if (role == com.ibm.task.api.WorkItem.REASON\_EDITOR && task.getName() != null && task.getName().equals("SpecialTask")) { Map userDataMap; UserData userDataObj; // get the user data map from passed staff query result and clear // the map. Then add a new Editor (new UserData instance) userDataMap = newStaffQueryResult.getUserDataMap(); userDataMap.clear(); userDataObj = staffResultFactory.newUserData("MyEditor", new Locale("en-US"), "MyEditor@company.com"); userDataMap.put(userDataObj.getUserName(), userDataObj); } return(newStaffQueryResult); } public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult, TaskTemplate template, int role, Map context) { return(originalStaffQueryResult); } } // end of class MyStaffResultProcessor Register this plug-in by adding a Custom Property with name "Staff.PostProcessorPlugin" to the Human Task Container on the AdminConsole. The value for this Custom property is the name of your implementing class. Since: 6.0.2 Version: 6.1.0

```
public interface StaffQueryResultPostProcessorPlugin
```

This plug-in provides for methods to post process staff result data on
 different levels. That means, for different roles different methods are
 called.

 Example:
 
Potential Creator: processStaffQueryResult(StaffQueryResult, TaskTemplate, int, Map);
Potential Owner: processStaffQueryResult(StaffQueryResult, Task, int, Map);
Escalation Receiver: processStaffQueryResult(StaffQueryResult, Escalation, Task, int, Map);

This is a sample list, it is not complete.

Note: The plug-in is available once per installation, so all tasks
 use this plug-in, that is, the staff results for all tasks are filtered by
 this plug-in.
 
Code Sample: (handles the Editor role of a certain task with name
 "SpecialTask")

import java.util.Collection;
import java.util.Locale;
import java.util.Map;
import com.ibm.task.api.ApplicationComponent;
import com.ibm.task.api.Escalation;
import com.ibm.task.api.EscalationTemplate;
import com.ibm.task.api.Task;
import com.ibm.task.api.TaskTemplate;
import com.ibm.task.spi.StaffQueryResult;
import com.ibm.task.spi.StaffQueryResultFactory;
import com.ibm.task.spi.StaffQueryResultPostProcessorPlugin;
import com.ibm.task.spi.UserData;

public class MyStaffResultProcessor implements StaffQueryResultPostProcessorPlugin
{
    public StaffQueryResult processStaffQueryResult(StaffQueryResult     originalStaffQueryResult,
                                                    ApplicationComponent applicationComponent,
                                                    int                  role,
                                                    Map                  context)
    { return(originalStaffQueryResult); }
 
    public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                                    Escalation       escalation,
                                                    Task             task,
                                                    int              role,
                                                    Map              context)
    { return(originalStaffQueryResult); } 
 
    public StaffQueryResult processStaffQueryResult(StaffQueryResult   originalStaffQueryResult,
                                                    EscalationTemplate template,
                                                    int                role,
                                                    Map                context)
     { return(originalStaffQueryResult); } 
 
    public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                                    Task             task,
                                                    int              role,
                                                    Map              context)
    {
       StaffQueryResult        newStaffQueryResult = originalStaffQueryResult;
       StaffQueryResultFactory staffResultFactory  = StaffQueryResultFactory.newInstance();
 
       if (role           == com.ibm.task.api.WorkItem.REASON\_EDITOR &&
           task.getName() != null                                    &&
           task.getName().equals("SpecialTask"))
       {
          Map      userDataMap;
          UserData userDataObj; 
 
          // get the user data map from passed staff query result and clear 
          // the map. Then add a new Editor (new UserData instance)
          userDataMap = newStaffQueryResult.getUserDataMap();
          userDataMap.clear();
          
          userDataObj = staffResultFactory.newUserData("MyEditor", 
                                                       new Locale("en-US"), 
                                                       "MyEditor@company.com");
          userDataMap.put(userDataObj.getUserName(), userDataObj);
       }
       return(newStaffQueryResult);
    }
 
    public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                                    TaskTemplate     template,
                                                    int              role,
                                                    Map              context)
    { return(originalStaffQueryResult); }
 } // end of class MyStaffResultProcessor

 Register this plug-in by adding a Custom Property with name
 "Staff.PostProcessorPlugin" to the Human Task Container on the AdminConsole.
 The value for this Custom property is the name of your implementing class.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT1
    - Method Summary

Methods 

Modifier and Type
Method and Description

StaffQueryResult
processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                       ApplicationComponent applicationComponent,
                       int role,
                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on the
 ApplicationComponent, for example 'Potential Creator'.

StaffQueryResult
processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                       Escalation escalation,
                       Task task,
                       int role,
                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on
 escalations, for example 'Escalation Receivers'.

StaffQueryResult
processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                       EscalationTemplate template,
                       int role,
                       java.util.Map context)
For future use.

StaffQueryResult
processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                       Task task,
                       int role,
                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on
 tasks, for example 'Readers, Potential Owner, Admins, Editors, ...'.

StaffQueryResult
processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                       TaskTemplate template,
                       int role,
                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on
 task templates, for example 'Readers, Potential Owner, Admins, Editors, 
 etc.'.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT1
static final java.lang.String COPYRIGHT1
See Also:Constant Field Values

- Method Detail

### Method Detail

    - processStaffQueryResult
StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                       ApplicationComponent applicationComponent,
                                       int role,
                                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on the
 ApplicationComponent, for example 'Potential Creator'.
 
 It is called when an ad-hoc task template or ad-hoc task instance is 
 being created. It also can be called for a deployed task templates if 
 that template does not define Potential Creators.
Parameters:originalStaffQueryResult - the original result of the staff queryapplicationComponent - application component data (API object)role - enum for the assignment reason (POTENTIAL\_INSTANCE\_CREATORS)context - additional context to be passed to the plugin (primarily for extensibility)
Returns:modified StaffQueryResult
    - processStaffQueryResult
StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                       Escalation escalation,
                                       Task task,
                                       int role,
                                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on
 escalations, for example 'Escalation Receivers'.
 
 It is called when an escalation is fired and the escalation receivers are 
 being determined.
Parameters:originalStaffQueryResult - the original result of the staff queryescalation - escalation data (API object)task - task data (API object)role - enum for the assignment reason (i.e. ESCALATION\_RECEIVER, ..context - additional context to be passed to the plugin (primarily for extensibility)
Returns:modified StaffQueryResult
    - processStaffQueryResult
StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                       EscalationTemplate template,
                                       int role,
                                       java.util.Map context)
For future use.
Parameters:originalStaffQueryResult - the original result of the staff querytemplate - escalation template data (API object)role - enum for the assignment reason (i.e. ESCALATION\_RECEIVER, ..context - additional context to be passed to the plugin (primarily for extensibility)
Returns:modified StaffQueryResult
    - processStaffQueryResult
StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                       Task task,
                                       int role,
                                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on
 tasks, for example 'Readers, Potential Owner, Admins, Editors, ...'.
 
 It is called when a task is started and the role members for admins, 
 readers, editors. etc. are being determined.
Parameters:originalStaffQueryResult - the original result of the staff querytask - task data (API object)role - enum for the assignment reason (i.e. POTENTIAL\_OWNER, ADMINISTRATOR, ..context - additional context to be passed to the plugin (primarily for extensibility)
Returns:modified StaffQueryResult
    - processStaffQueryResult
StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                       TaskTemplate template,
                                       int role,
                                       java.util.Map context)
This method is called when the StaffQueryResult is queried for a role on
 task templates, for example 'Readers, Potential Owner, Admins, Editors, 
 etc.'.
 
 It is called when a task is created and the role members for admins, 
 readers and potential creators are being determined. It can be also 
 called when the API method 'isUserInRole(TKTID, user, role)' is invoked.
Parameters:originalStaffQueryResult - the original result of the staff querytemplate - task template data (API object)role - enum for the assignment reason (i.e. POTENTIAL\_OWNER, ADMINISTRATOR, ..context - additional context to be passed to the plugin (primarily for extensibility)
Returns:modified StaffQueryResult