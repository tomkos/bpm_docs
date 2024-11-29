<!-- image -->

# Example 8: Change the default business rule for a business rule group

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRule;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Operation;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example8
{
static Formatter out = new Formatter();

static public String executeExample8()
{
		try
		{
				out.clear();

		// Retrieve a business rule group by target namespace and name
		List<BusinessRuleGroup> brgList = BusinessRuleManager
				.getBRGsByTNSAndName(
						"http://BRSamples/com/ibm/websphere
						/sample/brules",
						QueryOperator.EQUAL,
						"DiscountRules",
						QueryOperator.EQUAL, 0, 0);

		if (brgList.size() > 0)
		{
				out.printlnBold("Business Rule Group before publish:");
				// Get the first business rule group from the list
				// This should be the only business rule group in the list as
				// the combination of target namespace and name are unique
				BusinessRuleGroup brg = brgList.get(0);

				out.print("Business Rule Group: ");
				out.println(brg.getName());

				// Get the operation of the business rule group that
				// will have its default business rule updated
				Operation op =
				brg.getOperation("calculateShippingDiscount");
```

```
// Retrieve the default business rule for the operation
				BusinessRule defaultRule =
				op.getDefaultBusinessRule();
				out.print("Default Rule: ");
				out.println(defaultRule.getName());

				// Get the list of available business rules for this
				operation
				List<BusinessRule> ruleList =
				op.getAvailableTargets();

				Iterator<BusinessRule> iterator =
				ruleList.iterator();
				BusinessRule rule = null;

				// Find a business rule that is different from the
				current
				// default
				// business rule
				while (iterator.hasNext())
				{
						rule = iterator.next();
						if
						(!defaultRule.getName().equals(rule.getName()))
						{
```

```
// Set the default business rule to be a
								// different business rule
								// This change is to the operation object
								// directly
								op.setDefaultBusinessRule(rule);
								break;
						}
				}
				// Use the original list or create a new list
				// of business rule groups
				List<BusinessRuleGroup> publishList = new
				ArrayList<BusinessRuleGroup>();
				// Add the changed business rule group to the list
				publishList.add(brg);
				// Publish the list with the updated business rule
				group
				BusinessRuleManager.publish(publishList, true);

				out.println("");

				// Retrieve the business rule groups again to verify the
				// changes were published

				out.printlnBold("Business Rule Group after publish:");
				brgList = BusinessRuleManager
				.getBRGsByTNSAndName(
						"http://BRSamples/com/ibm/websphere/sample/brules",
						QueryOperator.EQUAL, "DiscountRules",
						QueryOperator.EQUAL, 0, 0);

				brg = brgList.get(0);
				out.println("Business Rule Group: " + brg.getName());
				op = brg.getOperation("calculateShippingDiscount");

				// Retrieve the default business rule for the operation
				defaultRule = op.getDefaultBusinessRule();
				out.print("Default Rule: ");
				out.println(defaultRule.getName());
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

Web browser output for example 8.

```
Executing example8

Business Rule Group before publish:
Business Rule Group: DiscountRules
Default Rule: calculateShippingDiscount

Business Rule Group after publish:
Business Rule Group: DiscountRules
Default Rule: calculateShippingDiscountHoliday
```