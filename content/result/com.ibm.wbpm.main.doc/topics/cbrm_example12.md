<!-- image -->

# Example 12: Modify a template in a decision table by changing a parameter value and then
publish

The easiest way to modify conditions and actions in a decision table is to use unique names for
the templates at each condition level and for each action. The unique names can be searched for and
then changes can be made to template instances defined with the template. When changes are made to a
template instance of a particular template, all of the condition values defined with that template
at that level will be updated. For action expressions, each instance is unique and a change to one
does not change others.

For this example, there are a number of additional methods that were created to simplify the
locating of a specific case edge for update, finding the specific parameter value, and finding the
action expression defined with a specific template.

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Vector;

import com.ibm.wbiserver.brules.mgmt.BusinessRule;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleGroup;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManagementException;
import com.ibm.wbiserver.brules.mgmt.BusinessRuleManager;
import com.ibm.wbiserver.brules.mgmt.Operation;
import com.ibm.wbiserver.brules.mgmt.ParameterValue;
import com.ibm.wbiserver.brules.mgmt.Template;
import com.ibm.wbiserver.brules.mgmt.dtable.ActionNode;
import com.ibm.wbiserver.brules.mgmt.dtable.CaseEdge;
import com.ibm.wbiserver.brules.mgmt.dtable.ConditionNode;
import com.ibm.wbiserver.brules.mgmt.dtable.DecisionTable;
import com.ibm.wbiserver.brules.mgmt.dtable.TemplateInstanceExpression;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeAction;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeBlock;
import
com.ibm.wbiserver.brules.mgmt.dtable.TreeConditionValueDefinition;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeNode;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example12 {
static Formatter out = new Formatter();

static public String executeExample12()
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
				"ConfigurationValues",
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
				Operation op = brg.getOperation("getMessages");

				// Get all business rules available for this
				operation
				List<BusinessRule> ruleList =
				op.getAvailableTargets();

				// For this operation there is only 1 business rule
				and
				// it is the business that we want to update
				DecisionTable decisionTable = (DecisionTable)
				ruleList.get(0);
				out.println("");
				out.printlnBold("Decision table before publish:");
				out
					.print(RuleArtifactUtility
					.printDecisionTable(decisionT
						able));
```

```
// Get the tree block that contains all of the
				conditions
				// and actions for the decision table
				TreeBlock treeBlock = decisionTable.getTreeBlock();
				// From the tree block, get the tree node which is
				the
				// starting point for navigating through the decision
				table
				TreeNode treeNode = treeBlock.getRootNode();
```

```
// Find the case edge at level 1 below the root with
				// specific template with a parameter value that has
				// a specific name. Since we are starting at the top,
				// the current depth is 0
				CaseEdge caseEdge = getCaseEdge(treeNode, "param0",
				"Condition Value Template 2.1", 1, 0);
```

```
if (caseEdge != null)
				{
					// Case edge was found. Get the value
					definition of the
					// case edge
					TreeConditionValueDefinition condition =
						caseEdge
						.getValueDefinition();
					// Get the condition expression defined with a
						template
						TemplateInstanceExpression conditionExpression
						= condition
							.getConditionValueTemplateInstance(
					);
```

```
// Get the template for the expression
					Template conditionTemplate =
					conditionExpression
						.getTemplate();

						// Check that template is correct as it is
						possible to have
						// multiple templates for a condition value,
						but only one
						// applied
						if (conditionTemplate.getName().equals(
							"Condition Value Template 2.1"))
						{
							// Get the parameter value
							ParameterValue parameterValue =
							getParameterValue("param0",
								conditionExpression);

							// Set the new parameter value
							parameterValue.setValue("info");
						}
```

```
ConditionNode conditionNode = (ConditionNode)
						treeNode;

						// Get the case edges tree node
						ListCaseEdge> caseEdges =
						conditionNode.getCaseEdges();

						// Create a list to hold all of the action
						expressions that
						// also need to be updated. Because every
						action is
						// independent of other action even though the
						template is
						// shared, all must be updated.
						List<TemplateInstanceExpression> expressions =
						new Vector<TemplateInstanceExpression>();

						// Retrieve all of the expressions
						for (CaseEdge edge : caseEdges)
						{
								getActionExpressions("Action Value
								Template 1", edge,
								expressions);
						}
```

```
// Update the correct parameter in each
						expression
						for (TemplateInstanceExpression expression 				
						expressions)
						{
							for (ParameterValue parameterValue :
							expression
								.getParameterValues())
							{
								// Check for correct parameter
								although there is
								// only one paramater in our
								template
								if
									(parameterValue.getParameter().getN
									ame().equals("param0")) {
										String value =
										parameterValue.getValue();
										parameterValue.setValue("Info
										"
										+
										value.substring(value.
										indexOf(":"),
										value.length()));
							}
					}
			}
			// With the condition value and actions
			updated, the
			// business rule group can be published.
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
			out.printlnBold("Decision table after
			publish:");

			brgList =
			BusinessRuleManager.getBRGsByTNSAndName(
				"http://BRSamples/com/ibm/websphere
				/sample/brules",
				QueryOperator.EQUAL,
				"ConfigurationValues",
				QueryOperator.EQUAL, 0, 0);

			brg = brgList.get(0);
			op = brg.getOperation("getMessages");
			ruleList = op.getAvailableTargets();
		
			decisionTable = (DecisionTable)
			ruleList.get(0);
			out.print(RuleArtifactUtility
				.printDecisionTable(decisionTable))
				;
				}
			}
	} catch (BusinessRuleManagementException e)
	{
			e.printStackTrace();
			out.println(e.getMessage());
	}
	return out.toString();
}

/*
Method to recursively navigate through a decision table and locate a
case
edge that has a template with a specific name and contains a specific
parameter to change. This method assumes that the level(depth) in the
decesion table of the value that is to be changed is known and the
current level(currentDepth) is tracked *
*/
static private CaseEdge getCaseEdge(TreeNode node, String pName,
		String templateName, int depth, int currentDepth)
{
	// Check if the current node is an action. This is an indication
	// that this branch of the decision table has been exhausted
	// looking for the case edge
	if (node instanceof ActionNode)
	{
		return null;
	}

	// Get the case edges for this node
	List<CaseEdge> caseEdges = ((ConditionNode) node).getCaseEdges();
	for (CaseEdge caseEdge : caseEdges)
	{

	// Check if the correct level has been reached
	if (currentDepth < depth)
		{
			// Move down one level and then call getCaseEdge
			again
			// to process that level
			currentDepth++;
			return getCaseEdge(caseEdge.getChildNode(), pName,
				templateName, depth, currentDepth);
		} else
		{
			// The correct level has been reached. Get the
			condition in
			// order to check the templates on that condition on
			whether
			// they match the template sought
			TreeConditionValueDefinition condition = caseEdge
				.getValueDefinition();

			// Get the expression for the condition which has
			been defined
			// with a template
			TemplateInstanceExpression expression = condition
				.getConditionValueTemplateInstance();
			// Get the template from the expression
						Template template = expression.getTemplate();

			// Check if this is the template sought
				if (template.getName().equals(templateName))
				{
					// The template is found to match
						return caseEdge;
				} else
					caseEdge = null;
			}
	}
	return null;
}

/*
This method will check the different parameter values for an expression
and if the correct one is found, return that parameter value.
*/
private static ParameterValue getParameterValue(String pName,
		TemplateInstanceExpression expression)
{
	// Check that the expression is not null as null would indicate
	// that the expression that was passed in was probably not
	defined
	// with a template and does not have any parameters to check.
	if (expression != null) {
		// Get the parameter values for the expression
		List<ParameterValue> parameterValues = expression
				.getParameterValues();

		for (ParameterValue parameterValue : parameterValues)
		{
			// For the different parameters, check that it
			matches the
			// parameter value sought

			if
				(parameterValue.getParameter().getName().equals(pName
			))
			{
				// Return the parameter value that matched
						return parameterValue;
			}
		}
	}
return null;
}
/*
This method finds all of the action expressions that are
defined with a specific template. It recursively works through
a case edge and adds action expressions that match to the
expressions parameter.
*/

private static void getActionExpressions(String templateName,
CaseEdge next, List<TemplateInstanceExpression>
expressions)
{
	ActionNode actionNode = null;
	TreeNode treeNode = next.getChildNode();
		
	// Check if the current node is at the action node level
	if (treeNode instanceof ConditionNode)
	{
		List<CaseEdge> caseEdges = ((ConditionNode) treeNode)
			.getCaseEdges();

		Iterator<CaseEdge> caseEdgesIterator =
		caseEdges.iterator();

		// Work through all case edges to find the action
		// expressions
		while (caseEdgesIterator.hasNext())
			{
				getActionExpressions(templateName,
				caseEdgesIterator.next(),
					expressions);
			}
	} else {
			// ActionNode found
			actionNode = (ActionNode) treeNode;

			List<TreeAction> treeActions = actionNode.getTreeActions();
			// Check that there is at least one treeAction specified
			for
			// the expression and work through the expressions checking
			// if the expressions have been created with the specific
			// template.
			if (!treeActions.isEmpty())
			{

				Iterator<TreeAction> iterator =
				treeActions.iterator();

			while (iterator.hasNext())
				{
					TreeAction treeAction = iterator.next();
					TemplateInstanceExpression expression =
					treeAction
						.getValueTemplateInstance();

					Template template = expression.getTemplate();

					if (template.getName().equals(templateName))
					{
						// Expression found with matching
						template
						expressions.add(expression);
					}
				}
			}
		}
	}
}
```

## Example

Web browser output for example 12.

```
Executing example12

Rule set before publish:
Decision Table
Name: getMessages
Namespace: http://BRSamples/com/ibm/websphere/sample/brules

Decision table after publish:
Decision Table
Name: getMessages
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
```