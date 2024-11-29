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

## Interface StaffQueryResultPostProcessorPlugin2

- public interface StaffQueryResultPostProcessorPlugin2 This interface allows for the modification of StaffQueryResult data that is computed by the people resolution subsystem of the Human Task Manager. The modified StaffQueryResult data is then used as people assignment for a specific task or escalation role. Using this functionality enables scenarios which require post processing with fine granularity, while optimizing the amount of data kept in the database. It is applicable in any of the following scenarios or combinations thereof: For role specific or task and escalation template specific post processing, ideally, one staff query result is stored in the database per task or escalation template and role. For task and escalation instance specific post processing, ideally, one staff query result is stored in the database per task or escalation instance and role. This interface exposes two methods: The processStaffQueryResult method This method method invokes the custom post processing logic. To facilitate fine-grained post processing decisions, the invocation of this method includes contextual information about: Following post processing contexts are distinguished: The isInstanceSpecific method The custom plugin implementation can control whether the instance specific application contexts (task template based (non ad-hoc) task instance based context, escalation template based (non ad-hoc) escalation instance context) are applied or not. For this purpose, the isInstanceSpecific method is to be implemented accordingly: Note that these decisions can be taken per task template, that is, the plugin implementation can be instance specific in the context of one task template and instance agnostic in the context of another task template. The result of the isInstanceSpecific method is exploited by the Human Task Manager runtime to efficiently store results of post processing. If possible, only one post processing result will be stored per role and task template. Also note that these decisions can be taken only if a task template exists as a common context. In case of ad-hoc task or escalation instances this is not the case. Therefore, for ad-hoc contexts (ad-hoc task instance context, ad-hoc escalation instance context), the isInstanceSpecific method is not invoked since the result has to be 'true' anyway. The PostProcessingContext object Both methods are invoked passing a PostProcessingContext object. This object allows to retrieve contextual information about the assignment reason, the task template, task instance, escalation template, escalation instance, and the application component. See PostProcessingContext for more information. The information available in the post processing context object depends on the method call. Establishing the Post Processing Context in the Custom Plugin Implementation Establish the PostProcessingContext in the implementation of the postProcessStaffQueryResult method as follows: The ApplicationComponent context This context is applicable in the following cases: Plugin instantiation and use of static data The post processor plugin is initialized upon server startup as a singleton. During the life cycle of the plugin, static information can be employed by the custom plugin implementation. Code example The following example illustrates the code for a role specific and instance and template agnostic custom plugin implementation: package com.ibm.task.spi.ppp; import java.util.HashMap; import java.util.Iterator; import java.util.Map; import com.ibm.task.api.WorkItem; import com.ibm.task.spi.StaffQueryResult; import com.ibm.task.spi.StaffQueryResultFactory; import com.ibm.task.spi.UserData; public class MyStaffResultProcessor implements StaffQueryResultPostProcessorPlugin2 { public boolean isInstanceSpecific(PostProcessingContext pppContext) { // post processing logic is not depending on task/escalation instance specifics return false; } // post processing method providing for user substitution that are in the Potential Owner role public StaffQueryResult processStaffQueryResult( StaffQueryResult originalStaffQueryResult, Map peopleQuerySpec, Map peopleQueryVariables, String[] usersRemovedByPeopleQuery, PostProcessingContext pppContext) { StaffQueryResult newStaffQueryResult = null; int assignmentReason = pppContext.getAssignmentReason(); // apply people substitution for potential owners switch (assignmentReason) { case WorkItem.REASON\_POTENTIAL\_OWNER: newStaffQueryResult = substitutePotentialOwners(originalStaffQueryResult); break; default: newStaffQueryResult = originalStaffQueryResult; } return newStaffQueryResult; } // method providing for substitution logic for users in the Potential Owner role private StaffQueryResult substitutePotentialOwners( StaffQueryResult originalStaffQueryResult) { StaffQueryResult newStaffQueryResult = originalStaffQueryResult; StaffQueryResultFactory staffResultFactory = StaffQueryResultFactory .newInstance(); Map userDataMap = originalStaffQueryResult.getUserDataMap(); Map newUserDataMap = new HashMap(); Iterator iterator = userDataMap.keySet().iterator(); while (iterator.hasNext()) { String originalUserId = (String) iterator.next(); // a real substitution logic would contain a lookup, e.g. in a DB, an LDAP directory String substituteUserId = null; if (originalUserId.equals("Edward")) { substituteUserId = "Bob"; } else if (originalUserId.equals("Jack")) { substituteUserId = "John"; } UserData substituteUserData = staffResultFactory.newUserData( substituteUserId, null, null); // include the substitute newUserDataMap.put(substituteUserId, substituteUserData); } if (newUserDataMap.size() > 0) { // create a new StaffQueryResult including the map newStaffQueryResult = StaffQueryResultFactory.newInstance() .newStaffQueryResult(newUserDataMap); } return newStaffQueryResult; } } Since: 7.0.0.2 Version: 7.0.0.2

```
public interface StaffQueryResultPostProcessorPlugin2
```

Using this functionality enables scenarios which require post processing with fine
 granularity, while optimizing the amount of data kept in the database.
 It is applicable in any of the following scenarios or combinations thereof:
 
Role specific post processing: specific post processing is to be applied
 depending on the task or escalation role considered.
 Task and escalation template specific post processing: specific post
 processing is to be applied depending on the task or escalation template
 considered.
 Task and escalation instance specific processing: specific post processing
 is to be applied depending on every task or escalation instance considered.
 

 For role specific or task and escalation template specific post processing,
 ideally, one staff query result is stored in the
 database per task or escalation template and role.
 
 For task and escalation instance specific post processing,
 ideally, one staff query result is stored in the database per
 task or escalation instance and role.
 
 This interface exposes two methods:
 
processStaffQueryResult
 isInstanceSpecific
 

The processStaffQueryResult method

 This method method invokes the custom post processing logic. To
 facilitate fine-grained post processing decisions, the invocation of this
 method includes contextual information about:
 
The people query specification which corresponds to the modeled people
 assignment criteria (name, parameters, and their values) for a specific role
 The specific role and application context in which the role is to be considered
 

 Following post processing contexts are distinguished:
 
Task template context: post processing is provided with information about
 
The task template
 The task template or task instance role (instance creators,
 administrators, readers, editors, potential starters, potential owners)
 
Task template based (non ad-hoc) task instance context: post processing is
 provided with information about
 
The task instance and task template
 The task instance role (administrators, readers, editors,
 potential starters, potential owners)
 
Ad-hoc task instance context: post processing is provided with information
 about
 
The task instance and the application component associated with the task instance
 The task instance role (administrators, readers, editors,
 potential starters, potential owners)
 
Escalation template context: post processing is provided with information
 about
 
The escalation and task template
 The escalation instance role (escalation receivers)
 
Escalation template based (non ad-hoc) escalation instance context: post
 processing is provided with information about
 
The escalation instance and the escalation and task templates
 The escalation role (escalation receivers)
 
Ad-hoc escalation instance context: post processing is provided with
 information about
 
The escalation instance
 The application component associated with the escalation instance
 The escalation role (escalation receivers)
 
Application component context: post processing is provided with
 information about
 
The application component
 The application component role (instance creators)
 

The isInstanceSpecific method

 The custom plugin implementation can control whether the instance
 specific application contexts (task template based (non ad-hoc) task instance based context,
 escalation template based (non ad-hoc) escalation instance context) are applied or not. For this purpose,
 the isInstanceSpecific method is to be implemented accordingly:
 
If post processing should make decisions on the granularity of task
 or escalation instances, isInstanceSpecific should return 'true'.
 If post processing should make decisions on the granularity of task
 templates only, that is, the same decision is granted per role for all task or
 escalation instances associated with the same task template, then
 isInstanceSpecific should return 'false'.
 

 Note that these decisions can be taken per task template, that is, the plugin
 implementation can be instance specific in the context of one task template
 and instance agnostic in the context of another task template.
 
 The result of the isInstanceSpecific method is exploited by the Human Task
 Manager runtime to efficiently store results of post processing. If
 possible, only one post processing result will be stored per role and task
 template.
 
 Also note that these decisions can be taken only if a task template exists as a
 common context. In case of ad-hoc task or escalation instances this is not
 the case. Therefore, for ad-hoc contexts (ad-hoc task instance context, ad-hoc escalation instance context),
 the isInstanceSpecific method is not invoked since the result has to be 'true' anyway.
 
The PostProcessingContext object

 Both methods are invoked passing a PostProcessingContext object. This object
 allows to retrieve contextual information about the
 assignment reason, the task template, task instance, escalation template,
 escalation instance, and the application component. See
 PostProcessingContext for more information.
 
 The information available in the post processing context object depends on the method call.
 
The isInstanceSpecific method is invoked with a post processing context object that
 contains the assignment reason and task template information.
 
The postProcessStaffQueryResult method is invoked with a post processing context object that
 contains the assignment reason and additional information - see below.
 

Establishing the Post Processing Context in the Custom Plugin Implementation

 Establish the PostProcessingContext in the implementation of the postProcessStaffQueryResult
 method as follows:
 
assignmentReason is a task template or task role, taskTemplate!=null, task==null
 

 This means that the task template context applies.
 Available information in the context object: assignmentReason, taskTemplate
 assignmentReason is a task template or task role, taskTemplate!=null, task!=null
 

 This means that the task template based (non ad-hoc) task instance context applies.
 Available information in the context object: assignmentReason, taskTemplate, taskInstance
 assignmentReason is a task template or task role, taskTemplate==null, task!=null, applicationComponent!=null
 

 This means that the ad-hoc task instance context applies.
 Available information in the context object: assignmentReason, taskInstance, applicationComponent
 assignmentReason is Instance Creator role, taskTemplate==null, task==null, applicationComponent!=null
 

 This means that the application component context applies - see below
 Available information in the context object: assignmentReason, applicationComponent
 assignmentReason is an escalation role, escalationTemplate!=null, escalation==null
 

 This means that the escalation template context applies.
 Available information in the context object: assignmentReason, escalationTemplate, taskTemplate
 assignmentReason is an escalation role, escalationTemplate!=null, escalation!=null
 

 This means that the escalation template based (non ad-hoc) escalation instance context applies.
 Available information in the context object: assignmentReason,
 escalationTemplate, taskTemplate, escalationInstance, taskInstance
 assignmentReason is an escalation role, escalationTemplate==null, escalation!=null, applicationComponent!=null
 

 This means that the ad-hoc escalation instance context applies.
 Available information in the context object: assignmentReason,
 escalationInstance, taskInstance, applicationComponent
 

The ApplicationComponent context

 This context is applicable in the following cases:
 
Creation of ad-hoc task templates
 

 The application component associated with the task template defines
 authorization for this action via the application component instance creator role.
 Creation of ad-hoc task instances
 

 The application component associated with the task defines authorization for
 this action via the application component instance creators role.
 Creation of template based task instances
 

 If no instance creator role is defined for a task template, a default
 specification is used. This default is defined for the instance creator role
 of the application component which is associated with the task template.
 

Plugin instantiation and use of static data

 The post processor plugin is initialized upon server startup as a singleton.
 During the life cycle of the plugin, static information can be employed by the
 custom plugin implementation.
 
Code example

 The following example illustrates the code for a role specific and instance
 and template agnostic custom plugin implementation:
 
 package com.ibm.task.spi.ppp;

 import java.util.HashMap;
 import java.util.Iterator;
 import java.util.Map;

 import com.ibm.task.api.WorkItem;
 import com.ibm.task.spi.StaffQueryResult;
 import com.ibm.task.spi.StaffQueryResultFactory;
 import com.ibm.task.spi.UserData;

 public class MyStaffResultProcessor implements
       StaffQueryResultPostProcessorPlugin2
 {
   public boolean isInstanceSpecific(PostProcessingContext pppContext)
   {
       // post processing logic is not depending on task/escalation instance specifics
       return false;
   }

   // post processing method providing for user substitution that are in the Potential Owner role
   public StaffQueryResult processStaffQueryResult(
           StaffQueryResult originalStaffQueryResult,
           Map peopleQuerySpec,
           Map peopleQueryVariables,
           String[] usersRemovedByPeopleQuery,
           PostProcessingContext pppContext)
   {

       StaffQueryResult newStaffQueryResult = null;
       int assignmentReason = pppContext.getAssignmentReason();

       // apply people substitution for potential owners
       switch (assignmentReason)
       {
       case WorkItem.REASON\_POTENTIAL\_OWNER:
           newStaffQueryResult = substitutePotentialOwners(originalStaffQueryResult);
           break;
       default:
           newStaffQueryResult = originalStaffQueryResult;
       }

       return newStaffQueryResult;
   }

   // method providing for substitution logic for users in the Potential Owner role
   private StaffQueryResult substitutePotentialOwners(
           StaffQueryResult originalStaffQueryResult)
   {
       StaffQueryResult newStaffQueryResult = originalStaffQueryResult;
       StaffQueryResultFactory staffResultFactory = StaffQueryResultFactory
               .newInstance();

       Map userDataMap = originalStaffQueryResult.getUserDataMap();
       Map newUserDataMap = new HashMap();
       Iterator iterator = userDataMap.keySet().iterator();

       while (iterator.hasNext())
       {
           String originalUserId = (String) iterator.next();

           // a real substitution logic would contain a lookup, e.g. in a DB, an LDAP directory
           String substituteUserId = null;
           if (originalUserId.equals("Edward"))
           {
               substituteUserId = "Bob";
           }
           else if (originalUserId.equals("Jack"))
           {
               substituteUserId = "John";
           }

           UserData substituteUserData = staffResultFactory.newUserData(
                   substituteUserId,
                   null,
                   null);

           // include the substitute
           newUserDataMap.put(substituteUserId, substituteUserData);
       }

       if (newUserDataMap.size() > 0)
       {
           // create a new StaffQueryResult including the map
           newStaffQueryResult = StaffQueryResultFactory.newInstance()
                   .newStaffQueryResult(newUserDataMap);
       }

       return newStaffQueryResult;
   }
 }

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

boolean
isInstanceSpecific(PostProcessingContext pppContext)
This method is called to determine whether or not post processing is to
 be applied on a per task or escalation instance basis.

StaffQueryResult
processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                       java.util.Map peopleQuerySpec,
                       java.util.Map peopleQueryVariables,
                       java.lang.String[] usersRemovedByPeopleQuery,
                       PostProcessingContext pppContext)
This method is called for post processing the staff query result computed
 by the built-in people resolution of Human Task Manager.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - isInstanceSpecific
boolean isInstanceSpecific(PostProcessingContext pppContext)
This method is called to determine whether or not post processing is to
 be applied on a per task or escalation instance basis. In case processing
 is not instance specific, the modified staff query result is
 shared per role across all task and escalation instances which are
 associated with the same task template.
 
 This method is not invoked for ad-hoc task or escalation instances because for
 these instances an instance specific processing is assumed in all cases.
Parameters:pppContext - The post processing context object to be used. The context contains a
            task template object. See PostProcessingContext.
Returns:true, if post processing is instance specific for the indicated
         context, otherwise, false is returned.
    - processStaffQueryResult
StaffQueryResult processStaffQueryResult(StaffQueryResult originalStaffQueryResult,
                                       java.util.Map peopleQuerySpec,
                                       java.util.Map peopleQueryVariables,
                                       java.lang.String[] usersRemovedByPeopleQuery,
                                       PostProcessingContext pppContext)
This method is called for post processing the staff query result computed
 by the built-in people resolution of Human Task Manager.
Parameters:originalStaffQueryResult - The staff query result computed by the built-in people resolution.peopleQuerySpec - The people assignment criteria (PAC) description considered
            for the current people assignment including name, parameter
            names and values (all of String type) as specified for a
            task or escalation role. To access the PAC name, use in the map
            the key HTM\_VERB\_NAME. To access the value of a parameter use
            in the map the parameter name as key, e.g. "groupName".peopleQueryVariables - The map of replacement variables and their resolved values.
            The resolved value(s) can be of type String or String[].
            Contained are the replacement variables specified in the
            people assignment criteria considered. To access the values
            resolved for a replacement variable, use in the map the name
            of the variable as key, e.g. "htm:task.originator" .usersRemovedByPeopleQuery - The array of user IDs excluded by the specified people
            assignment criteria. The exclusions may be imperative and
            therefore to be considered explicitly, in order to avoid
            accidental re-inclusion via post processing.pppContext - The postProcessingContext object to determine the assignment
            reason and application context being considered. The context
            can contain information about the task template, task
            instance, escalation template, escalation instance,
            application component considered. For access details, see
            PostProcessingContext.
Returns:StaffQueryResult
             The modified staff query result.