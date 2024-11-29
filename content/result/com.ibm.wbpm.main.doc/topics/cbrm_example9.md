<!-- image -->

# Example 9: Schedule another rule for an operation in a business rule group

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.ArrayList;
import java.util.Date;
import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRule;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Operation;
import com.ibm.wbiserver.brules.mgmt.OperationSelectionRecordList;
import com.ibm.wbiserver.brules.mgmt.OperationSelectionRecord;
import com.ibm.wbiserver.brules.mgmt.problem.Problem;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example9 {
static Formatter out = new Formatter();

static public String executeExample9()
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
					out.println("");
					out.printlnBold("Business Rule Group before publish:");
					// Get the first business rule group from the list
					// This should be the only business rule group in the
					list as
					// the combination of target namespace and name are unique
					BusinessRuleGroup brg = brgList.get(0);

					// Get the operation of the business rule group that
					// will have a new business rule scheduled
					Operation op =
					brg.getOperation("calculateShippingDiscount");

					printOperationSelectionRecord(op);
					// Get the list of available business rules for this operation
					List<BusinessRule> ruleList =
					op.getAvailableTargets();

					// Get the first rule in the list as this will be scheduled
					// for the operation
					BusinessRule rule = ruleList.get(0);

					// Get the list of scheduled business rules
					OperationSelectionRecordList opList = op
							.getOperationSelectionRecordList();
					// Create an end date in the future for the business rule
					Date future = new Date();
					long futureTime = future.getTime() + 3600000;
```

```
// Create the new scheduled business rule with the current
					// date which means this rule will become active immediately
					// upon
					// publish and the future date.						
					newOperationSelectionRecord(new Date(),
							new Date(futureTime), rule);
					// Add the new scheduled business rule to the list of
					// scheduled rule
					opList.addOperationSelectionRecord(newRecord);
```

```
// Validate the list to ensure there isn't an overlap
					List<Problem> problems = op.validate();
					if (problems.size() == 0)
					{
							// Use the original list or create a new list
							// of business rule groups
							List<BusinessRuleGroup> publishList = new
							ArrayList<BusinessRuleGroup>();
							// Add the changed business rule group to the list
							publishList.add(brg);
							// Publish the list with the updated business
							rule group
							BusinessRuleManager.publish(publishList, true);
							out.println("");

							// Retrieve the business rule groups again to
							verify the
							// changes were published
							out.printlnBold("Business Rule Group after
							publish:");

							brgList =
							BusinessRuleManager.getBRGsByTNSAndName(
									"http://BRSamples/com/ibm/websphere
									/sample/brules",
									QueryOperator.EQUAL,
									"DiscountRules",
									QueryOperator.EQUAL, 0, 0);
									brg = brgList.get(0);
									
									op =
									brg.getOperation("calculateShippingDiscount");

									printOperationSelectionRecord(op);
							}
							// else handle the validation error
					}
	} catch (BusinessRuleManagementException e)
	{
	e.printStackTrace();
	out.println(e.getMessage());
	}
	return out.toString();
}
/*
Method to print the operation selection record for an operation. The
start date and end date are printed as well as the name of the rule
artifact for the scheduled time.
*/
private static void printOperationSelectionRecord(Operation op)
{
	OperationSelectionRecordList opSelectionRecordList = op
			.getOperationSelectionRecordList();
	Iterator<OperationSelectionRecord> opSelRecordIterator =
	opSelectionRecordList
			.iterator();
	OperationSelectionRecord record = null;
	while (opSelRecordIterator.hasNext())
	{
			out.printlnBold("Scheduled Destination:");
			record = opSelRecordIterator.next();
			out.println("Start Date: " + record.getStartDate()
			+ " - End Date: " + record.getEndDate());
			BusinessRule ruleArtifact = record.getBusinessRuleTarget();
			out.println("Rule: " + ruleArtifact.getName());
			}
	}
}
```

## Example

Web browser output for example 9.

```
Executing example9

Business Rule Group before publish:
Scheduled Destination:
Start Date: Thu Dec 01 00:00:00 CST 2005 - End Date: Sun Dec 25 00:00:00 CST 2005
Rule: calculateShippingDiscountHoliday

Business Rule Group after publish:
Scheduled Destination:
Start Date: Thu Dec 01 00:00:00 CST 2005 - End Date: Sun Dec 25 00:00:00 CST 2005
Rule: calculateShippingDiscountHoliday
Scheduled Destination:
Start Date: Mon Jan 07 21:08:31 CST 2008 - End Date: Mon Jan 07 22:08:31 CST 2008
Rule: calculateShippingDiscount
```