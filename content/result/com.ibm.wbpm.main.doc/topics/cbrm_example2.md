<!-- image -->

# Example 2: Retrieve and print business rule groups, rule sets and decision tables

```
import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRule;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Operation;
import com.ibm.wbiserver.brules.mgmt.OperationSelectionRecord;
import com.ibm.wbiserver.brules.mgmt.OperationSelectionRecordList;
import com.ibm.wbiserver.brules.mgmt.Property;
import com.ibm.wbiserver.brules.mgmt.PropertyList;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSet;
public class Example2
{
	status Formatter out = new Formatter();
	static public String executeExample2()
	{
		try
		{
				out.clear();
```

```
// Retrieve all business rule groups
		List<BusinessRuleGroup> brgList = BusinessRuleManager
				.getBRGsByName("DiscountRules",
				QueryOperator.EQUAL, 0, 0);

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
			out.println("Display Name: " +
				brg.getDisplayName());
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
					out.println("Property Name: " +
					prop.getName());
					out.println("Property Value: " +
					prop.getValue());
			}
```

```
List<Operation> opList = brg.getOperations();

			Iterator<Operation> opIterator = opList.iterator();
			Operation op = null;
			out.println("");
			out.printlnBold("Operations");
			// Output operations for the business rule group
			while (opIterator.hasNext())
				{
						op = opIterator.next();
						out.printBold("Operation: ");
						out.println(op.getName());

						// Retrieve the default business rule for the operation
						BusinessRule defaultRule =
						op.getDefaultBusinessRule();
						// If the default rule is found, print out the business rule
						// using the appropriate method for rule type
						if (defaultRule != null)
						{
								out.printlnBold("Default Destination:");
```

```
if (defaultRule instanceof RuleSet)
											out.println(RuleArtifactUtility.
											intRuleSet(defaultRule));
								else
											out.print(RuleArtifactUtility.
											tDecisionTable(defaultRule));
						}
						OperationSelectionRecordList
						opSelectionRecordList = op
								.getOperationSelectionRecordList()
								;

						Iterator<OperationSelectionRecord>
						opSelRecordIterator = opSelectionRecordList
								.iterator();
						OperationSelectionRecord record = null;
```

```
while (opSelRecordIterator.hasNext())
						{
								out.printlnBold("Scheduled
								Destination:");
								record = opSelRecordIterator.next();

								out.println("Start Date: " +
								record.getStartDate()
										+ " - End Date: " +
										record.getEndDate());
								BusinessRule ruleArtifact = record
										.getBusinessRuleTarget();

								if (ruleArtifact instanceof RuleSet)
										out.println(RuleArtifactUtility.pr
										intRuleSet(ruleArtifact));
								else
										out.print(RuleArtifactUtility.prin
										tDecisionTable(ruleArtifact));
							}
				}
		}
		out.println("");
	} catch (BusinessRuleManagementException e)
	{
	e.printStackTrace();
	out.println(e.getMessage());
	return out.toString();
	}
}
```

## Example

Web browser output for example 2.

```
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

Operations
Operation: calculateOrderDiscount
Default Destination:
Rule Set
Name: calculateOrderDiscount
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
Rule: CopyOrder
Display Name: CopyOrder
Description: null
Expanded User Presentation: null
User Presentation: null
Rule: FreeGiftInitialization
Display Name: FreeGiftInitialization
Description: null
Expanded User Presentation: Product ID for Free Gift = 5001AE80 Quantity = 1 Cost =
0.0 Description = Free gift for discounted order
User Presentation: Product ID for Free Gift = {0} Quantity = {1} Cost = {2}
Description = {3}Parameter Name: param0
Parameter Value: 5001AE80
Parameter Name: param1
Parameter Value: 1
Parameter Name: param2
Parameter Value: 0.0
Parameter Name: param3
Parameter Value: Free gift for discounted order
Rule: Rule1
Display Name: Rule1
Description: null
Expanded User Presentation: If customer is gold status, then apply a discount of 20.0
and include a free gift
User Presentation: If customer is {0} status, then apply a discount of {1} and include a
free gift
Parameter Name: param0
Parameter Value: gold
Parameter Name: param1
Parameter Value: 20.0
Rule: Rule2
Display Name: Rule2
Description: null
Expanded User Presentation: If customer.status == silver, then provide a discount of
15.0
User Presentation: If customer.status == {0}, then provide a discount of {1}
Parameter Name: param0
Parameter Value: silver
Parameter Name: param1
Parameter Value: 15.0
Rule: Rule3
Display Name: Rule3
Description: Template for non-gold customers
Expanded User Presentation: If customer.status == bronze, then provide a discount of
10.0
User Presentation: If customer.status == {0}, then provide a discount of {1}
Parameter Name: param0
Parameter Value: bronze
Parameter Name: param1
Parameter Value: 10.0

Operation: calculateShippingDiscount
Default Destination:
Decision Table
Name: calculateShippingDiscount
Namespace: http://BRSamples/com/ibm/websphere/sample/brules

Init Rule: Rule1
Display Name: Rule1
Description: null
Extended User Presentation: null
User Presentation: null
```