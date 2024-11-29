<!-- image -->

# Developing a plug-in using the StaffQueryResultPostProcessorPlugin interface

```
public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                                   Task             task,
                                                   int              role,
                                                   Map              context);
```

```
public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                                   Escalation       escalation,
                                                   Task             task,
                                                   int              role,
                                                   Map              context);
```

```
public StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                                   TaskTemplate     template,
                                                   int              role,
                                                   Map              context);
```

```
public StaffQueryResult processStaffQueryResult(StaffQueryResult     originalStaffQueryResult,
                                                   ApplicationComponent applicationComponent,
                                                   int                  role,
                                                   Map                  context);
```

## Parameters

```
Map pacAsMap = (Map) context.get("HTM\_VERB");

// to retrieve the name of the people assignment criteria (PAC)
String pacName = (String) pacAsMap.get("HTM\_VERB\_NAME"); 

// to retrieve the PAC parameter names
Set paramNames = pacAsMap.keySet();

// to retrieve the value of a specific parameter
String paramValue = (String) pacAsMap.get(paramName);
```

```
Object replVarObj = context.get(replVarName);
if (replVarObj instanceof String) 
	    String replVarValue = (String) replVarObj;
if (replVarObj instanceof String[])
	    String[] replVarValues = (String[]) replVarObj;
```

```
String[] removedUserIDs = (String[]) context.get("HTM\_REMOVED\_USERS");
```

## Example: StaffQueryResultPostProcessorPlugin implementation

```
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
```

For more
information about this interface, see the Javadoc.