<!-- image -->

# Example 14: Handle errors in a rule set

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
import com.ibm.wbiserver.brules.mgmt.ParameterValue;
import com.ibm.wbiserver.brules.mgmt.ValidationException;
import com.ibm.wbiserver.brules.mgmt.problem.Problem;
import
com.ibm.wbiserver.brules.mgmt.problem.ProblemStartDateAfterEndDate;
import com.ibm.wbiserver.brules.mgmt.problem.ValidationError;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleBlock;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSet;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRule;
import
com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetTemplateInstanceRule;

public class Example14 {
static Formatter out = new Formatter();

static public String executeExample14() {
	try {
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

			if (brgList.size() > 0) {
					// Get the first business rule group from the list
					// This should be the only business rule group in the
					list as
					// the combination of target namespace and name are
					unique
					BusinessRuleGroup brg = brgList.get(0);
					out.println("Business Rule Group retrieved");

					// Get the operation of the business rule group that
					// has the business rule that will be modified as
					// the business rules are associated with a specific
					// operation
					Operation op = brg.getOperation("getApprover");

					// Retrieve specific rule by name
					List<BusinessRule> ruleList =
					op.getBusinessRulesByName(
							"getApprover", QueryOperator.EQUAL, 0,
							0);

					// Get the specific rule
					RuleSet ruleSet = (RuleSet) ruleList.get(0);
					out.println("Rule Set retrieved");

					RuleBlock ruleBlock = ruleSet.getFirstRuleBlock();

					Iterator<RuleSetRule> ruleIterator =
					ruleBlock.iterator();

					// Search through the rules to find the rule to
					change
					while (ruleIterator.hasNext()) {
							RuleSetRule rule = ruleIterator.next();

							// Check that the rule was defined with a
							template
							// as it can be changed.
							if (rule instanceof
							RuleSetTemplateInstanceRule) {
								// Get the template rule instance
								RuleSetTemplateInstanceRule
								templateInstance =
								(RuleSetTemplateInstanceRule) rule;
								// Check for the correct template rule
								instance
								if (templateInstance.getName().equals(
										"LargeOrderApprover")) {
```

```
// Get the parameter from the
										template instance
										ParameterValue parameter =
										templateInstance
												.getParameterValue("par
												am1");

										// Set an incorrect value for this
										parameter
										// This will cause a validation
										error
										parameter.setValue("$3500");
										out.println("Incorrect parameter
										value set");
										break;
								}
						}
				}
				// This code should never be reached because of the
				error
				// introduced
				// earlier

				// With the condition value and actions updated, the
				business
				// rule
				// group can be published.
				// Use the original list or create a new list
				// of business rule groups
				List<BusinessRuleGroup> publishList = new
				ArrayList<BusinessRuleGroup>();

				// Add the changed business rule group to the list
				publishList.add(brg);

				// Publish the list with the updated business rule
				group
				BusinessRuleManager.publish(publishList, true);
		}
```

```
} catch (ValidationException e) {
		out.println("Validation Error");

		List<Problem> problems = e.getProblems();

		Iterator<Problem> problemIterator = problems.iterator();

		// Check the list of problems for the appropriate error and
		// perform the appropriate action, for example report error 
                // or correct error
		while (problemIterator.hasNext()) {
				Problem problem = problemIterator.next();
				ValidationError error = problem.getErrorType();

				// Check for specific error value
				if (error == ValidationError.TYPE\_CONVERSION\_ERROR) {
						// Handle this error by reporting the problem
						out
								.println("Problem: Incorrect value
								entered for a parameter");
						return out.toString();
				}
				// else if....
				// Checks can be done for other errors and the
				// appropriate error message or action can be
				performed
				// correct the problem
		}
} catch (BusinessRuleManagementException e) {
		out.println("Error occurred.");
		e.printStackTrace();
}
return out.toString();
}
}
```

## Example

Web browser output for example 14.

```
Executing example14

Business Rule Group retrieved
Rule Set retrieved
Validation Error
Problem: Incorrect value entered for a parameter
```