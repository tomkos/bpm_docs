<!-- image -->

# Example 6: Update a business rule group property and publish

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.ArrayList;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.UserDefinedProperty;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example6
{
static Formatter out = new Formatter();

static public String executeExample6()
{
	try
	{
			out.clear();
			out.printlnBold("Business Rule Group before publish:");
			// Retrieve business rule groups by a single property value
			List<BusinessRuleGroup> brgList = BusinessRuleManager
					.getBRGsBySingleProperty("Department",
					QueryOperator.EQUAL,"General", 0, 0);

			if (brgList.size() > 0)
			{
					// Get the first business rule group from the list
					BusinessRuleGroup brg = brgList.get(0);
					// Retrieve the property from the business rule group
					UserDefinedProperty userDefinedProperty =
					(UserDefinedProperty) brg
							.getProperty("Department");

					out.println("Business Rule Group: " + brg.getName());
					out.println("Department Property value: "
					+ brg.getProperty("Department").getValue());
```

```
// Modify the property value in the brg
					// This updates the property value directly in the
					brg object
					userDefinedProperty.setValue("GeneralConfig");
					// Use the original list or create a new list
					// of business rule groups
					List<BusinessRuleGroup> publishList = new
					ArrayList<BusinessRuleGroup>();
					// Add the changed business rule group to the list
					publishList.add(brg);
```

```
// Publish the list with the updated business rule group
					BusinessRuleManager.publish(publishList, true);

					out.println("");

					// Retrieve the business rule group again to verify the
					// changes were published
					out.printlnBold("Business Rule Group after publish:");
					brgList = BusinessRuleManager
					.getBRGsBySingleProperty("Department",
					QueryOperator.EQUAL, "GeneralConfig", 0, 0);
					
					brg = brgList.get(0);

					out.println("Business Rule Group: " + brg.getName());
					// Display the property value to show the change
					out.println("Department Property value: "
					+ brg.getProperty("Department").getValue());
			}
	} catch (BusinessRuleManagementException e)
	{
	e.printStackTrace();
	out.println(e.getMessage());
	}
return out.toString();
}
}
```

## Example

Web browser output for example 6.

```
Executing example6

Business Rule Group before publish:
Business Rule Group: ConfigurationValues
Department Property value: General

Business Rule Group after publish:
Business Rule Group: ConfigurationValues
Department Property value: GeneralConfig
```