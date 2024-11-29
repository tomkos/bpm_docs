<!-- image -->

# Example 10: Modify a parameter value in a template in a rule set

```
package com.ibm.websphere.sample.brules.mgmt;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Operation;
import com.ibm.wbiserver.brules.mgmt.ParameterValue;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSet;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRule;
import
com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetTemplateInstanceRule;
import com.ibm.wbiserver.brules.mgmt.BusinessRule;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleBlock;

public class Example10
{
static Formatter out = new Formatter();

static public String executeExample10()
{
		try
		{
				out.clear();
				
				// Retrieve a business rule group by target namespace and
				name
				List<BusinessRuleGroup> brgList = BusinessRuleManager
						.getBRGsByTNSAndName(
								"http://BRSamples/com/ibm/websphere
								/sample/brules",
								QueryOperator.EQUAL,
								"ApprovalValues",
								QueryOperator.EQUAL, 0, 0);
				if (brgList.size() > 0)
				{
						// Get the first business rule group from the list
						// This should be the only business rule group in the
						list as
						// the combination of target namespace and name are
						unique
						BusinessRuleGroup brg = brgList.get(0);
						// Get the operation of the business rule group that
						// has the business rule that will be modified as
						// the business rules are associated with a specific
						// operation
						Operation op = brg.getOperation("getApprover");
						
						// Get the business rule on the operation that will
						be modified
						List<BusinessRule> ruleList =
						op.getBusinessRulesByName(
								"getApprover", QueryOperator.EQUAL, 0,
								0);

						if (ruleList.size() > 0)
						{
								out.println("");
								out.printlnBold("Rule set before publish:");
								// Get the rule to be modified. Rules are
								unique by
								// target namespace and name, but for this
								example
								// there is only one business rule named
								"getApprover"
								RuleSet ruleSet = (RuleSet) ruleList.get(0);
								out.print(RuleArtifactUtility.printRuleSet(rule
								Set));
```

```
// A rule set has all of the rules defined in a
						rule block
						RuleBlock ruleBlock =
						ruleSet.getFirstRuleBlock();

						Iterator<RuleSetRule> ruleIterator =
						ruleBlock.iterator();

						// Iterate through the rules in the rule block
						to find the
						// rule instance called "LargeOrderApprover"
						while (ruleIterator.hasNext())
						{
								RuleSetRule rule = ruleIterator.next();
```

```
// The rule must have been defined with a
						template
						// in order for it to be changed. Check
						if the current
						// rule is even based on a template.
						if (rule instanceof
						RuleSetTemplateInstanceRule)
						{
```

```
// Get the rule template instance
								RuleSetTemplateInstanceRule
								templateInstance =
								(RuleSetTemplateInstanceRule) rule;

								// Check for the rule instance
								which matches
								// the rule to modify
								if
								(templateInstance.getName().equals(
										"LargeOrderApprover"))
								{
```

```
// Get the parameter from the
										rule instance
										ParameterValue parameter =
										templateInstance
												.getParameterValue("par
												am2");

										// Modify the value of the
										parameter
										parameter.setValue("superviso
										r");
										break;
								}
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
				// Retrieve the business rule groups again to verify
				the
				// changes were published
				out.printlnBold("Rule set after publish:");

				brgList = BusinessRuleManager
						.getBRGsByTNSAndName(
								"http://BRSamples/com/ibm/websphere/sample/brules",
								QueryOperator.EQUAL, "ApprovalValues",
								QueryOperator.EQUAL, 0, 0);

				brg = brgList.get(0);
				op = brg.getOperation("getApprover");
				ruleList = op.getBusinessRulesByName(
						"getApprover", QueryOperator.EQUAL, 0,0);

				ruleSet = (RuleSet) ruleList.get(0);
				out.print(RuleArtifactUtility.printRuleSet(ruleSet));
				}
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

Web browser output for example 10.

```
Executing example10

Rule set before publish:
Rule Set
Name: getApprover
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
Rule: LargeOrderApprover
Display Name: LargeOrderApprover
Description: null
Expanded User Presentation: If the number of items order is above 10 and 
the order is above $5000, then it requires the approval of manager
User Presentation: If the number of items order is above {0} and 
the order is above ${1}, then it requires the approval of {2}
Parameter Name: param0
Parameter Value: 10
Parameter Name: param1
Parameter Value: 5000
Parameter Name: param2
Parameter Value: manager
Rule: DefaultApprover
Display Name: DefaultApprover
Description: null
Expanded User Presentation: approver = peer
User Presentation: approver = {0}
Parameter Name: param0
Parameter Value: peer

Rule set after publish:
Rule Set
Name: getApprover
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
Rule: LargeOrderApprover
Display Name: LargeOrderApprover
Description: null
Expanded User Presentation: If the number of items order is above 10 and 
the order is above $5000, then it requires the approval of supervisor
User Presentation: If the number of items order is above {0} and the order 
is above ${1}, then it requires the approval of {2}
Parameter Name: param0
Parameter Value: 10
Parameter Name: param1
Parameter Value: 5000
Parameter Name: param2
Parameter Value: supervisor
Rule: DefaultApprover
Display Name: DefaultApprover
Description: null
Expanded User Presentation: approver = peer
User Presentation: approver = {0}
Parameter Name: param0
Parameter Value: peer
```