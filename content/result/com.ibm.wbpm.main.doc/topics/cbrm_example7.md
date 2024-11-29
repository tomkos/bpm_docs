<!-- image -->

# Example 7: Update properties in multiple business rule groups and publish

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.UserDefinedProperty;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example7
{
static Formatter out = new Formatter();

static public String executeExample7()
{
		try
		{
				out.clear();
				out.printlnBold("Business Rule Group before publish:");
				// Retrieve business rule groups by a single property value
				List<BusinessRuleGroup> brgList = BusinessRuleManager
						.getBRGsBySingleProperty("Department", 
						QueryOperator.EQUAL, "Accounting", 0, 0);

				Iterator<BusinessRuleGroup> iterator = brgList.iterator();

				BusinessRuleGroup brg = null;
				
				// Use the original list or create a new list
				// of business rule groups
				List<BusinessRuleGroup> publishList = new
				ArrayList<BusinessRuleGroup>();

				// Iterate through all of the business rule groups and
				// modify the property
				while (iterator.hasNext())
				{
						// Retrieve the property from the business rule group
						brg = iterator.next();
						
						out.println("Business Rule Group: " + brg.getName());

						// Retrieve the property from the business rule group
						UserDefinedProperty prop = (UserDefinedProperty) brg
								.getProperty("Department");
						out.println("Department Property value: "
						+
						brg.getProperty("Department").getValue())
						;

						// Modify the property value in the brg
						// This updates the property value directly in the
						brg object
						prop.setValue("Finance");
```

```
// Add the changed business rule group to the list
						publishList.add(brg);
						}

						// Publish the list with the updated business rule
						group
						BusinessRuleManager.publish(publishList, true);

						out.println("");

						// Retrieve the business rule groups again to verify the
						// changes were published
						out.printlnBold("Business Rule Group after
						publish:");

						brgList = BusinessRuleManager
								.getBRGsBySingleProperty("Department",
								QueryOperator.EQUAL,
								"Finance", 0, 0);
						iterator = brgList.iterator();

						while (iterator.hasNext())
						{
								brg = iterator.next();
								out.println("Business Rule Group: " +
								brg.getName());
								out.println("Department Property value: "
									+
									brg.getProperty("Department").getVa
									lue());
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

Web browser output for example 7.

```
Executing example7

Business Rule Group before publish:
Business Rule Group: ApprovalValues
Department Property value: Accounting
Business Rule Group: DiscountRules
Department Property value: Accounting

Business Rule Group after publish:
Business Rule Group: ApprovalValues
Department Property value: Finance
Business Rule Group: DiscountRules
Department Property value: Finance
```