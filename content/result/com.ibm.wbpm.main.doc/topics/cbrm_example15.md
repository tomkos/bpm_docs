<!-- image -->

# Example 15: Handle errors in a business rule group

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
import com.ibm.wbiserver.brules.mgmt.OperationSelectionRecord;
import com.ibm.wbiserver.brules.mgmt.OperationSelectionRecordList;
import com.ibm.wbiserver.brules.mgmt.ParameterValue;
import com.ibm.wbiserver.brules.mgmt.ValidationException;
import com.ibm.wbiserver.brules.mgmt.problem.Problem;
import
com.ibm.wbiserver.brules.mgmt.problem.ProblemStartDateAfterEndDate;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleBlock;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSet;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRule;
import
com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetTemplateInstanceRule;

public class Example15
{
static Formatter out = new Formatter();

static public String executeExample15()
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
			while (ruleIterator.hasNext())
			{
				RuleSetRule rule = ruleIterator.next();

				// Check that the rule was defined with a
				template
				// as it can be changed.
				if (rule instanceof
				RuleSetTemplateInstanceRule)
				{
					// Get the template rule instance
					RuleSetTemplateInstanceRule
					templateInstance =
					(RuleSetTemplateInstanceRule) rule;

					// Check for the correct template rule
					instance
					if (templateInstance.getName().equals(
							"LargeOrderApprover"))
					{
						// Get the parameter from the
						template instance
						ParameterValue parameter =
						templateInstance
							.getParameterValue("par
							am1");

						// Set the value for this parameter
						// This value is in the correct
						format and will
						// not cause a validation error
						parameter.setValue("4000");
						out.println("Rule set parameter
						value on set correctly");
						break;
						}
				}
		}
```

```
// Validate the changes made the rule set
						List<Problem> problems = ruleSet.validate();
						out.println("Rule set validated");

						// No errors should occur for this test case, however,
						// check if there are problems and then
						// perform the correct action to recover or report 
						// the error
						if (problems != null)
						{
							Iterator<Problem> problemIterator =
							problems.iterator();

							while (problemIterator.hasNext())
							{
								Problem problem = problemIterator.next();

								if (problem instanceof
								ProblemStartDateAfterEndDate)
								{
									out
									.println("Incorrect
										value entered for a
											parameter");
									return out.toString();
								}
							}
						} else
						{
							out.println("No problems found for the rule
							set");
						}
						// Get the list of available rule targets
						List<BusinessRule> ruleList2 =
						op.getAvailableTargets();

						// Get the first rule that will be scheduled
						incorrectly
						BusinessRule rule = ruleList2.get(0);

						// The error condition will be to set the end time
						for a
						// scheduled rule to be 1 hour before the start time
						// This will cause a validation error
						Date future = new Date();
						long futureTime = future.getTime() - 360000;

						// Get the operation selection list to add the
						incorrectly
						// scheduled item
						OperationSelectionRecordList opList = op
						.getOperationSelectionRecordList();

						// Create a new scheduled rule instance
						// No error is thrown until validated or a publish
						// occurs as more changes might be made
						OperationSelectionRecord newRecord = opList
							.newOperationSelectionRecord(new Date(),
							new Date(
							futureTime), rule);
```

```
// Add the scheduled rule instance to the operation
						// No error here either
						opList.addOperationSelectionRecord(newRecord);
						out.println("New selection record added with
						incorrect schedule");

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
			} catch (ValidationException e) {
			out.println("Validation Error");

			List<Problem> problems = e.getProblems();

			Iterator<Problem> problemIterator = problems.iterator();
			// There might be multiple problems
			// Go through the problems and handle each one or
			// report the problem
			while (problemIterator.hasNext())
			{
				Problem problem = problemIterator.next();

				// Each problem is a different type that can be
				compared
				if (problem instanceof ProblemStartDateAfterEndDate)
				{
					out
					.println("Rule schedule is
						incorrect. Start date is after end
						date.");
					return out.toString();
					}
				// else if....
				// Checks can be done for other errors and the
				// appropriate error message or action can be
				performed
				// correct the problem
		}
	}catch (BusinessRuleManagementException e)
	{
		out.println("Error occurred.");
		e.printStackTrace();
	}
	return out.toString();
	}
}
```

## Example

Web browser output for example 15.

```
Executing example15

Business Rule Group retrieved
Rule Set retrieved
Rule set parameter value on set correctly
Rule set validated
Validation Error
Rule schedule is incorrect. Start date is after end date.
```