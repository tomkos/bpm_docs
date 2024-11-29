<!-- image -->

# Example 13: Add a condition value and actions to a decision table

When adding a condition value to a condition node, you are adding a case edge. The new case edge
is added at the end of the list of case edges. For the condition value, you must specify a template
instance expression that has the appropriate parameter values set. In order to specify the template
instance expression you will have to use a specific template. It is recommended to give
the template names at each condition node level unique names in order to retrieve the correct
templates for that type of condition. If a single template definition is used, it may make it
difficult to determine at which level the condition is being added.

When setting the condition value in a condition node, this will add the condition value with the
same template instance to all condition nodes at the same level. This is done as the decision table
is balanced. Also as part of the adding a new condition value, new action nodes will be added. These
action nodes have tree actions that have null values specified for the user presentation and
template instance expression. Because the condition value can be added to a condition node that does
not have an action node as a child node, the addition of a condition node may result in a large
number of action nodes. The number of action nodes is based upon the level the condition node is
added and the number of condition nodes at that level and the number of condition nodes at each
child level.

In order to find the action nodes that have been created, a search of action nodes with tree
actions that have null user presentation and template instance expression may be performed. A
TreeActionValueTemplate can be used to create an expression that can be set into
the TreeAction. This pattern would need to be repeated for all new action
nodes.

For this example two methods were provided to assist in setting up the new tree actions.
getEmptyActionNode recursively looks for an empty action node from the current
condition node and getParameterValue returns the value of a parameter that was specified by
name.

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
import com.ibm.wbiserver.brules.mgmt.Template;
import com.ibm.wbiserver.brules.mgmt.ValidationException;
import com.ibm.wbiserver.brules.mgmt.dtable.ActionNode;
import com.ibm.wbiserver.brules.mgmt.dtable.CaseEdge;
import com.ibm.wbiserver.brules.mgmt.dtable.ConditionNode;
import com.ibm.wbiserver.brules.mgmt.dtable.DecisionTable;
import com.ibm.wbiserver.brules.mgmt.dtable.TemplateInstanceExpression;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeAction;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeActionTermDefinition;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeActionValueTemplate;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeBlock;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeConditionValueTemplate;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeNode;
import com.ibm.wbiserver.brules.mgmt.problem.Problem;
import com.ibm.wbiserver.brules.mgmt.query.QueryOperator;

public class Example13
{
	static Formatter out = new Formatter();

	static public String executeExample13()
	{
		try
		{
			out.clear();

			// Retrieve a business rule group by target namespace
			// and name
			List<BusinessRuleGroup> brgList = BusinessRuleManager
				.getBRGsByTNSAndName(
			"http://BRSamples/com/ibm/websphere/sample/brules",
					QueryOperator.EQUAL,"ConfigurationValues",
					QueryOperator.EQUAL, 0, 0);

			if (brgList.size() > 0)
				{
					// Get the first business rule group from the
					// list. This should be the only business
					// rule group in the list as the combination
					// of target namespace and name are unique
					BusinessRuleGroup brg = brgList.get(0);

					// Get the operation of the business rule
					// group that has the business rule that will
					// be modified as the business rules are
					// associated with a specific operation
					Operation op = brg.getOperation("getMessages");

					// Get all business rules available for
					// this operation
					List<BusinessRule> ruleList =
						op.getAvailableTargets();

					// For this operation there is only 1 business
					// rule and it is the business that we want
					// to update

					DecisionTable decisionTable = (DecisionTable)
						ruleList.get(0);
						out.printlnBold("Decision table before
						publish:");
						out.print(RuleArtifactUtility
						.printDecisionTable(decisionTable));
```

```
// Get the tree block that contains all of
					// the conditions and actions for the decision
					// table
					TreeBlock treeBlock =
						decisionTable.getTreeBlock();

					// From the tree block, get the tree node which
					// is the starting point for navigating through
					// the decision table
					ConditionNode conditionNode = (ConditionNode)
						treeBlock.getRootNode();

					// Get the case edges for this node which is
					// the first level of conditions
					List<CaseEdge> caseEdges =
						conditionNode.getCaseEdges();

					// Get the case edge which will have the new
					// condition added
					CaseEdge caseEdge = caseEdges.get(0);

					// For the case edge get the condition node in
					// order to retrieve the templates for the
					// condition
					conditionNode = (ConditionNode)
									caseEdge.getChildNode();

					// Get the templates for the condition
					List<TreeConditionValueTemplate>
						treeValueConditionTemplates = conditionNode
						.getAvailableValueTemplates();

					Iterator<TreeConditionValueTemplate>
						treeValueConditionTemplateIterator =
						treeValueConditionTemplates.iterator();

					TreeConditionValueTemplate conditionTemplate =
						null;
```

```
// Find the template that should be used
						while
					(treeValueConditionTemplateIterator.hasNext())
					{
						conditionTemplate =
							treeValueConditionTemplateIterator
								.next();
						if (conditionTemplate.getName().equals(
							"Condition Value Template
							2.1"))
							{
								// Template found
								break;
							}
							conditionTemplate = null;
					}
					if (conditionTemplate != null)
					{
```

```
// Get the parameter definition from the
					// template
					Parameter conditionParameter =
					conditionTemplate.getParameter("param0");

					// Create a parameter value instance to
					// be used in a new condition template
					// instance
					ParameterValue conditionParameterValue =
							conditionParameter
							.createParameterValue("fatal");

					List<ParameterValue>
							conditionParameterValues = new
							ArrayList<ParameterValue>();

					// Add the parameter value to a list

					conditionParameterValues
						.add(conditionParameterValue);

					// Create a new condition template
					// instance with the parameter value
					TemplateInstanceExpression
						newConditionValue =
						conditionTemplate
							.createTemplateInstanceExpression(c
						onditionParameterValues);
					// Add the condition template instance to
					// this condition node
					conditionNode

					.addConditionValueToThisLevel(newConditionValue);
					// When a condition node is added there
					// are new action nodes that are created
					// and empty. These must be filled with
					// action template instances. By
					// searching for each empty action
					// node from the parent level, all of the
					// new empty action nodes can be found.
					conditionNode = (ConditionNode)
					conditionNode.getParentNode();
```

```
// Get the case edges for the parent node
					caseEdges = conditionNode.getCaseEdges();

					Iterator<CaseEdge> caseEdgesIterator =
					caseEdges.iterator();

					while (caseEdgesIterator.hasNext())
					{
						// For each case edge, retrieve an
						// empty action node if it exists
						ActionNode actionNode =
						getEmptyActionNode(caseEdgesIterator
						.next());

						// Check if all actions are filled
						if (actionNode != null)
						{
```

```
// Get the list of tree
							// actions. These
							// are not the actual
							// actions, but the
							// placeholders for the
							// actions
							List<TreeAction>
							treeActionList = actionNode
								.getTreeActions();

							List<TreeActionTermDefinition>
							treeActionTermDefinitions =
								treeBlock
							.getTreeActionTermDefinitions();

							List<TreeActionValueTemplate>
								treeActionValueTemplates =
								treeActionTermDefinitions
								.get(0).getValueTemplates();

							TreeActionValueTemplate
								actionTemplate = null;

							for (TreeActionValueTemplate
									tempActionTemplate :
									treeActionValueTemplates)
									{

									if
									(tempActionTemplate.get
										Name().equals(
										"Action Value
										Template 1"))
										{
											actionTemplate =
											tempActionTemplate;
											break;
										}
									}

									if (actionTemplate != null)
									{
										// Get another action
										// that is under
										// the parent condition
										// node in order
										// to use the value as
										// the basis for
										// the error message in
										// the new
										// action node. Move up
										// to the
										// parent condition
										// node first
										ConditionNode
										parentNode =
										(ConditionNode)
										actionNode
											.getParentNode();

										// Get the first case
										// edge of the
										// parent node as this
										// action will
										// always be filled in
										// as new actions
										// are added to the end
										// of the case
										// edge list.
										CaseEdge caseE =
											parentNode.getCas
											eEdges().get(
											0);

										// The child node is an
										// action node
										// and at the same
										// level as the new
										// action node.
										ActionNode aNode =
										(ActionNode) caseE
											.getChildNode();

										// Get the list of tree
										// actions
										TreeAction
											existingTreeAction =
											aNode
											.getTreeActions()
											.get(0);

										// Get the template
										// instance
										// expression for the
										// tree action
										// from which you can
										// retrieve the
										// parameter

										TemplateInstanceExpression
										existingExpression =
											existingTreeAction
											.getValueTemplateInstance();

										ParameterValue
										existingParameterValue =
										getParameterValue(
												"param0",
										existingExpression);

										String actionValue =
										existingParameterValue
											.getValue();

										// Create the new
										// message from the
										// message of the
										// existing
										// tree action
										actionValue = "Fatal"
												+
										actionValue.substring(actionValue
											.indexOf(":"), actionValue
											.length());
											Parameter
											actionParameter =
											actionTemplate
											.getParameter("param0");

											// Get the parameter
											// from the template
											ParameterValue
											actionParameterValue =
												actionParameter
											.createParameterValue(actionValue);

											// Add the parameter to
											// a list of templates
											List<ParameterValue>
											actionParameterValues = new
											ArrayList<ParameterValue>();

									actionParameterValues.add(actionParameterValue);

											// Create a new tree
											// action instance

										TemplateInstanceExpression
											treeAction = actionTemplate
					.createTemplateInstanceExpression(actionParameterValues);

										// Set the tree action
										// in the action node
										// by setting it in the
										// tree action list
```

```
treeActionList.get(0)
										.setValueTemplateInstance(
										treeAction);
										}
									}
							}
				}
				// With the condition value and actions
				// updated, the business rule group can be
				// published.
				// Use the original list or create a new list
				// of business rule groups
					List<BusinessRuleGroup> publishList = new
						ArrayList<BusinessRuleGroup>();

				// Add the changed business rule group to the
				// list
					publishList.add(brg);

				// Publish the list with the updated business
				// rule group

				BusinessRuleManager.publish(publishList, true);

				brgList =
					BusinessRuleManager.getBRGsByTNSAndName(
					"http://BRSamples/com/ibm/websphere/sample/brules",
					QueryOperator.EQUAL, "ConfigurationValues",
					QueryOperator.EQUAL, 0, 0);
					brg = brgList.get(0);
					op = brg.getOperation("getMessages");
					ruleList = op.getAvailableTargets();
					decisionTable = (DecisionTable)
						ruleList.get(0);
					out.printlnBold("Decision table after
						publish:");
					out
						.print(RuleArtifactUtility
							.printDecisionTable(decisionTable));
				}
		} catch (ValidationException e)
		{
			List<Problem> problems = e.getProblems();

			out.println("Problem = " +
			problems.get(0).getErrorType().name());

			e.printStackTrace();
			out.println(e.getMessage());
		} catch (BusinessRuleManagementException e)
		{
			e.printStackTrace();
			out.println(e.getMessage());
		}
		return out.toString();
	}

	/*
	* This method searches from the current case edge for any
	* action nodes that have empty tree actions. An empty
	* action node is found by looking at the end of the list
	* of case edges and checking if the action node has tree
	* actions that have both a null user presentation and
	* TemplateInstanceExpression.
	*/
	private static ActionNode getEmptyActionNode(CaseEdge next)
	{
		ActionNode actionNode = null;
		TreeNode treeNode = next.getChildNode();

	if (treeNode instanceof ConditionNode)
	{
		List<CaseEdge> caseEdges = ((ConditionNode) treeNode)
			.getCaseEdges();

		if (caseEdges.size() > 1)
		{
			// Get rightmost case-edge as the new
			// condition and thus empty actions are at the
			// end of the case edges
			actionNode = getEmptyActionNode(caseEdges
				.get(caseEdges.size() - 1));

			if (actionNode != null)
			{
				return actionNode;
			}
	}
	} else
	{
		actionNode = (ActionNode) treeNode;

		List<TreeAction> treeActions =
		actionNode.getTreeActions();

		if (!treeActions.isEmpty())
		{
		if
		((treeActions.get(0).getValueUserPresentation() == null)
			&&
		(treeActions.get(0).getValueTemplateInstance() == null))
			{
				return actionNode;
			}
		}	
			`actionNode = null;
		}
		return actionNode;
	}
	/*
	* This method will check the different parameter values for an
	* expression and if the correct one is found, return that
	* parameter value.
	*/
	private static ParameterValue getParameterValue(String pName,
			TemplateInstanceExpression expression)
	{
		ParameterValue parameterValue = null;

		// Check that the expression is not null as null would
		// indicate that the expression that was passed in was
		// probably not defined with a template and does not have
		// any parameters to check.
		if (expression != null)
		{
			// Get the parameter vlues for the expression
			List<ParameterValue> parameterValues = expression
				.getParameterValues();
			Iterator<ParameterValue> parameterIterator =
				parameterValues
				.iterator();

			// For the different parameters, check that it
			// matches the parameter value sought
			while (parameterIterator.hasNext())
			{
				parameterValue = parameterIterator.next();

				if
				(parameterValue.getParameter().getName().equals(pName))
				{
				// Return the parameter value that
				// matched
				return parameterValue;
				}
		}
	}
	return parameterValue;
}
}
```

## Example

Web browser output for example 13.

```
Executing example13

Decision table before publish:
Decision Table
Name: getMessages
Namespace: http://BRSamples/com/ibm/websphere/sample/brules

Decision table after publish:
Decision Table
Name: getMessages
Namespace: http://BRSamples/com/ibm/websphere/sample/brules
```