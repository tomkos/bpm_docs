<!-- image -->

# Example 5: Retrieve business rule groups with a complex query

More examples of business rule group queries are available in the appendix.

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Property;
import com.ibm.wbiserver.brules.mgmt.PropertyList;
import com.ibm.wbiserver.brules.mgmt.query.AndNode;
import com.ibm.wbiserver.brules.mgmt.query.OrNode;
import com.ibm.wbiserver.brules.mgmt.query.PropertyQueryNode;
import com.ibm.wbiserver.brules.mgmt.query.QueryNodeFactory;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example5
{
static Formatter out = new Formatter();
static public String executeExample5()
{
		try
		{
				out.clear();

				// Retrieve business rule groups based on three conditions where
				// two of the conditions are combined in an OR node
				// Create PropertyQueryNodes for each condition for the OR node
				PropertyQueryNode propertyNode1 = QueryNodeFactory
						.createPropertyQueryNode("Department",
						QueryOperator.EQUAL,"General");
				PropertyQueryNode propertyNode2 = QueryNodeFactory
						.createPropertyQueryNode("MissingProperty",
				QueryOperator.EQUAL, "SomeValue");
				// Combine the two PropertyQueryNodes with an OR node
				OrNode orNode =
				QueryNodeFactory.createOrNode(propertyNode1, propertyNode2);
				// Create the third PropertyQueryNode
						PropertyQueryNode propertyNode3 = QueryNodeFactory
						.createPropertyQueryNode("RuleType",
				QueryOperator.EQUAL,"messages");
```

```
// Combine OR node with third PropertyQueryNode with
				AndNode AndNode andNode =
				QueryNodeFactory.createAndNode(propertyNode3, orNode);

				List<BusinessRuleGroup> brgList = BusinessRuleManager
						.getBRGsByProperties(andNode, 0, 0);

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
				}
			} 		catch (BusinessRuleManagementException e)
		{
		e.printStackTrace();
		out.println(e.getMessage());
		}
	return out.toString();
	}
}
```

## Example

Web browser output for example 5.

```
Executing example5

Business Rule Group
Name: ConfigurationValues
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
Display Name: ConfigurationValues
Description: null
Presentation Time zone: LOCAL
Save Date: Sun Jan 06 17:56:51 CST 2008
Property Name: IBMSystemVersion
Property Value: 6.2.0
Property Name: Department
Property Value: General
Property Name: RuleType
Property Value: messages
Property Name: IBMSystemTargetNameSpace
Property Value: http://BRSamples/com/ibm/websphere/sample/brules
Property Name: IBMSystemName
Property Value: ConfigurationValues
Property Name: IBMSystemDisplayName
Property Value: ConfigurationValues
```