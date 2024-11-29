<!-- image -->

# Example 11: Add a new rule from a template to a rule set

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
import com.ibm.wbiserver.brules.mgmt.Parameter;
import com.ibm.wbiserver.brules.mgmt.ParameterValue;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleBlock;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSet;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRuleTemplate;
import
com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetTemplateInstanceRule;

public class Example11
{
static Formatter out = new Formatter();

static public String executeExample11()
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
				"getApprover", QueryOperator.EQUAL, 0,0);

			if (ruleList.size() > 0)
			{
				out.println("");
				out.printlnBold("Rule set before publish:");
				// Get the rule to be modified. Rules are unique by
				// target namespace and name, but for this example
				// there is only one business rule named
				"getApprover"
				RuleSet ruleSet = (RuleSet) ruleList.get(0);
				out.print(RuleArtifactUtility.printRuleSet(rule
				Set));
```

```
// Get the list of rule templates
				ListRuleSetRuleTemplate> ruleTemplates =
				ruleSet
					.getRuleTemplates();

				Iterator<RuleSetRuleTemplate> templateIterator
				= ruleTemplates
					.iterator();

				while (templateIterator.hasNext())
				{
					RuleSetRuleTemplate template =
					templateIterator.next();

					// Locate the template to use to create a
					new rule
					if
					(template.getName().equals("Template\_Larg
					eOrder"))
					{
```

```
// Create a list for the parameters
					for this template
					// rule instance
					List<ParameterValue> paramList =
					new ArrayList<ParameterValue>();

					// From the template definition,
					get a specific parameter
					// and set the value
					Parameter param =
					template.getParameter("param0");
					ParameterValue paramValue = param
						.createParameterValue("
						20");

					// Add parameter to the list
					paramList.add(paramValue);

					// Get the next parameter and set
					the value
					param = template.getParameter("param1");
					paramValue = 
					param.createParameterValue("7500");

					// Add parameter to the list
					paramList.add(paramValue);

					// Get the next parameter and set
					the value
					param =
					template.getParameter("param2");
						paramValue = param
						.createParameterValue("
						2nd-line manager");

					// Add parameter to the list
					paramList.add(paramValue);
```

```
// Create the template rule
					instance with the parameter
					// list
					RuleSetTemplateInstanceRule
						templateInstance = template
						.createRuleFromTemplate
						("ExtraLargeOrder",
						paramList);
					// Get the ruleblock for the rule
						set
					RuleBlock ruleBlock =
					ruleSet.getFirstRuleBlock();
```

```
// Add the template rule to the
					ruleblock
					ruleBlock.addRule(templateInstance)
					;
																
					break;
					}
				}

				// Use the original list or create a new list
				// of business rule groups
				List<BusinessRuleGroup> publishList = new
				ArrayList<BusinessRuleGroup>();

				// Add the changed business rule group to the
				list
				publishList.add(brg);

				// Publish the list with the updated business
				rule group
				BusinessRuleManager.publish(publishList, true);

				out.println("");

				// Retrieve the business rule groups again to
				verify the
				// changes were published
				out.printlnBold("Rule set after publish:");

				brgList = BusinessRuleManager
				.getBRGsByTNSAndName(
						"http://BRSamples/com/ibm/websphere
						/sample/brules",
						QueryOperator.EQUAL,
						"ApprovalValues",
						QueryOperator.EQUAL, 0, 0);

				brg = brgList.get(0);
				op = brg.getOperation("getApprover");
				ruleList = op.getBusinessRulesByName(
									"getApprover", QueryOperator.EQUAL,
									0, 0);

				ruleSet = (RuleSet) ruleList.get(0);
				out.print(RuleArtifactUtility.printRuleSet(rule
				Set));
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

Web browser output for example 11.

```
Executing example11

Rule set before publish:
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
Rule: ExtraLargeOrder
Display Name:
Description: null
Expanded User Presentation: If the number of items order is above 20 and 
the order is above $7500, then it requires the approval of 2nd-line manager
User Presentation: If the number of items order is above {0} and the order 
is above ${1}, then it requires the approval of {2}
Parameter Name: param0
Parameter Value: 20
Parameter Name: param1
Parameter Value: 7500
Parameter Name: param2
Parameter Value: 2nd-line manager
```