<!-- image -->

# Developing a plug-in using the StaffQueryResultPostProcessorPlugin2 interface

## Parameters

- The task template.
- One of the following work item assignment reasons: Instance creator,
administrator, reader, editor, potential starter, or potential owner.

- The escalation template.
- The work item assignment reason: Escalation receiver.

- The task template.
- The task instance.
- One of the following work item assignment reasons: Administrator,
reader, editor, potential starter, or potential owner.

- The task instance.
- The application component associated with the task instance.
- One of the following work item assignment reasons: Administrator,
reader, editor, potential starter, or potential owner.

- The task template.
- The task instance.
- The escalation template.
- The escalation instance.
- The work item assignment reason: Escalation receiver.

- The escalation instance.
- The task instance that is associated with the escalation.
- The application component associated with the escalation instance.
- The work item assignment reason: Escalation receiver.

- The application component.
- The work item assignment reason: Instance creator.

## Example: StaffQueryResultPostProcessorPlugin2 implementation

```
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
        // post processing logic is not depending on task/escalation
        // instance specifics
        return false;
    }

    // post processing method providing for user substitution that are
    // in the Potential Owner role
    public StaffQueryResult processStaffQueryResult(
            StaffQueryResult originalStaffQueryResult,
            Map peopleQuerySpec,
            Map peopleQueryVariable,
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

    // method providing for substitution logic for users in the Potential Owner
    // role
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

            // a real substitution logic would contain a lookup, for example in a database,
            // an LDAP directory
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
```

For more information about
this interface, see the Javadoc.