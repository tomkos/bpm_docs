<!-- image -->

# Example 4: Retrieve business rule groups by multiple properties with OR

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Property;
import com.ibm.wbiserver.brules.mgmt.PropertyList;
import com.ibm.wbiserver.brules.mgmt.query.OrNode;
import com.ibm.wbiserver.brules.mgmt.query.PropertyQueryNode;
import com.ibm.wbiserver.brules.mgmt.query.QueryNodeFactory;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example4
{
static Formatter out = new Formatter();
static public String executeExample4()
{
		try
		{
				out.clear();
```

```
// Retrieve business rule groups based on two conditions
				// Create PropertyQueryNodes for each one condition
				PropertyQueryNode propertyNode1 = QueryNodeFactory
						.createPropertyQueryNode("Department",
						QueryOperator.EQUAL,"Accounting");
				PropertyQueryNode propertyNode2 = QueryNodeFactory
						.createPropertyQueryNode("RuleType",
						QueryOperator.EQUAL,"monetary");
				// Combine the two PropertyQueryNodes with an OR node
				OrNode orNode =
				QueryNodeFactory.createOrNode(propertyNode1,
						propertyNode2);
				// Use orNode in search for business rule groups
				List<BusinessRuleGroup> brgList = BusinessRuleManager
						.getBRGsByProperties(orNode, 0, 0);

				Iterator<BusinessRuleGroup> iterator = brgList.iterator();

				BusinessRuleGroup brg = null;
				// Iterate through the list of business rule groups
				while (iterator.hasNext())
				{
						brg = iterator.next();
						// Output attributes for each business rule group
						out.printlnBold("Business Rule Group");
						out.println("Name: " + brg.getName());
						out.println("Namespace: " +
						brg.getTargetNameSpace());
						out.println("Display Name: " + brg.getDisplayName());
						out.println("Description: " + brg.getDescription());
						out.println("Presentation Time zone: "
								+ brg.getPresentationTimezone());
						out.println("Save Date: " + brg.getSaveDate());

						PropertyList propList = brg.getProperties();

						Iterator<Property> propIterator =
						propList.iterator();
						Property prop = null;
						// Output property names and values
						while (propIterator.hasNext())
						{
								prop = propIterator.next();
								out.println("\t Property Name: " +
								prop.getName());
								out.println("\t Property Value: " +
								prop.getValue());
						}
						out.println("");
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

Web browser output for example 4.

```
Executing example4

Business Rule Group
Name: ApprovalValues
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
Display Name: ApprovalValues
Description: null
Presentation Time zone: LOCAL
Save Date: Sun Jan 06 17:56:51 CST 2008
Property Name: IBMSystemVersion
Property Value: 6.2.0
Property Name: Department
Property Value: Accounting
Property Name: RuleType
Property Value: regulatory
Property Name: IBMSystemTargetNameSpace
Property Value: http://BRSamples/com/ibm/websphere/sample/brules
Property Name: IBMSystemName
Property Value: ApprovalValues
Property Name: IBMSystemDisplayName
Property Value: ApprovalValues

Business Rule Group
Name: DiscountRules
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
Display Name: DiscountRules
Description: null
Presentation Time zone: LOCAL
Save Date: Sun Jan 06 17:56:51 CST 2008
Property Name: Department
Property Value: Accounting
Property Name: IBMSystemVersion
Property Value: 6.2.0
Property Name: RuleType
Property Value: monetary
Property Name: IBMSystemTargetNameSpace
Property Value: http://BRSamples/com/ibm/websphere/sample/brules
Property Name: IBMSystemName
Property Value: DiscountRules
Property Name: IBMSystemDisplayName
Property Value: DiscountRules
```