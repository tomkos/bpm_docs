<!-- image -->

# RuleArtifactUtility class

```
package com.ibm.websphere.sample.brules.mgmt;

import java.util.Iterator;
import java.util.List;

import com.ibm.wbiserver.brules.mgmt.BusinessRule;
import com.ibm.wbiserver.brules.mgmt.Parameter;
import com.ibm.wbiserver.brules.mgmt.ParameterValue;
import com.ibm.wbiserver.brules.mgmt.RuleTemplate;
import com.ibm.wbiserver.brules.mgmt.Template;
import com.ibm.wbiserver.brules.mgmt.dtable.ActionNode;
import com.ibm.wbiserver.brules.mgmt.dtable.CaseEdge;
import com.ibm.wbiserver.brules.mgmt.dtable.ConditionNode;
import com.ibm.wbiserver.brules.mgmt.dtable.DecisionTable;
import com.ibm.wbiserver.brules.mgmt.dtable.DecisionTableRule;
import com.ibm.wbiserver.brules.mgmt.dtable.DecisionTableTemplateInstanceRule;
import com.ibm.wbiserver.brules.mgmt.dtable.TemplateInstanceExpression;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeAction;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeActionTermDefinition;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeBlock;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeConditionTermDefinition;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeConditionValueDefinition;
import com.ibm.wbiserver.brules.mgmt.dtable.TreeNode;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleBlock;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSet;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRule;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetRuleTemplate;
import com.ibm.wbiserver.brules.mgmt.ruleset.RuleSetTemplateInstanceRule;

public class RuleArtifactUtility
{
		static Formatter out = new Formatter();

		/*
		Method to print out a decision table with the conditions and
		actions printed out in a HTML tabular format. The conditions
		and actions are printed out with a separate method that
		recursively works through the case edges of the decision
		tables.
		*/

		public static String printDecisionTable(BusinessRule
		ruleArtifact)
		{
				out.clear();
				out.printlnBold("Decision Table");
				DecisionTable decisionTable = (DecisionTable)	ruleArtifact;
				out.println("Name: " + decisionTable.getName());
				out.println("Namespace: " +
				decisionTable.getTargetNameSpace());
				
				// Output the init rule for the decision table before
				// working through the table of conditions and actions
				DecisionTableRule initRule =
				decisionTable.getInitRule();
				if (initRule != null)
				{
						out.printBold("Init Rule: ");
						out.println(initRule.getName());
						out.println("Display Name: " +
						initRule.getDisplayName());
						out.println("Description: " +
						initRule.getDescription());
						// The expanded user presentation will automatically populate the
						// presentation with the parameter	values and can be used for
						// display if the init rule was defined with a template. If no
						// template was defined the 	expanded user presentation
						// is the same as the regular presentation.
						out.println("Extended User
						Presentation: "
								+
						initRule.getExpandedUserPresentation());
						// The regular user presentation will have placeholders in the
						// string where the parameter can be substituted
						// if the init rule was defined with a template
						// If the rule was not defined with a template, the user
						// presentation will only
						// be a string without placeholders. The placeholders are of a
						// format of {n} where n is the index (zero-based) of the parameter in the template.
						// This value can be used to create an interface for editing where there	are
						// fields with the parameter values available for editing
						out.println("User Presentation: " +
						initRule.getUserPresentation());
						// Init rules might be defined with or without a template
						// Check to make sure a template	was used before trying
						// to access the parameters
						if (initRule instanceofDecisionTableTemplateInstanceRule)
						{
								DecisionTableTemplateInstanceRule
								templateInstance =
								(DecisionTableTemplateInstanceRule) 
								initRule;

								RuleTemplate template =
								templateInstance.getRuleTemplate();

								List<Parameter>
								parameters =
								template.getParameters();
								Iterator<Parameter>
								paramIterator =
								parameters.iterator();

								Parameter parameter =
								null;

								while
								(paramIterator.hasNext()) {
								parameter =
								paramIterator.next();

								out.println("Parameter
								Name: " +
								parameter.getName());
								out.println("Parameter
								Value: "
								+
								templateInstance.getParameterValue
								(parameter.getName()));
								}
						}
				}
				// For the rest of the decision table, start at the root and
				// recursively work through the different case edges and
				// actions
				TreeBlock treeBlock =
				decisionTable.getTreeBlock();
				TreeNode treeNode = treeBlock.getRootNode();

				printDecisionTableConditionsAndActions(treeNode, 0);
				out.println("");
				return out.toString();
		}
		//*Method to recursively work through the case edges and print out the conditions and actions.*
		static private void printDecisionTableConditionsAndActions(
				TreeNode treeNode, int indent)
		{
				out.print("<table border=\"1\">");
				if (treeNode instanceof ConditionNode)
				{
						// Get the case edges for the current TreeNode
						// and for each case edge print out the conditions
						ConditionNode conditionNode =
						(ConditionNode) treeNode;

						List<CaseEdge> caseEdges =
						conditionNode.getCaseEdges();
						Iterator<CaseEdge> caseEdgeIterator
						= caseEdges.iterator();

						CaseEdge caseEdge = null;

						while (caseEdgeIterator.hasNext())
						{
								out.print("<tr>");
								// If this is the start	of the conditions for the
								// condition node, 	print out the condition term
								if (indent == 0)
								{
								out.print("<td>");

								TreeConditionTermDefinition 
								termDefinition =
								conditionNode.getTermDefinition();

								out.print(termDefinition.getUserPresentation());
								out.print("</td>");
								indent++;
								} else {
								// After the condition term has been printed for a
								// case edge skip for	the rest of the case edges
								out.print("<td></td>");
								}

								caseEdge =
								caseEdgeIterator.next()
								;

								out.print("<td>");

								// Check if the	caseEdge is defined by a template
								if
								(caseEdge.getValueDefinition() != null)
								{
								TemplateInstanceExpression templateInstance =
								caseEdge.getValueTemplateInstance();

								out.println(templateInstance.
								getExpandedUserPresentation());

								TreeConditionValueDefinition valueDef =
								caseEdge.getValueDefinition();

								out.println(valueDef.getUserPresentation());

								Template template =
								templateInstance.getTemplate();

								// Get the parameters	for the template definition and
								// print out the parameter names and	values
								List<Parameter>
								parameters =
								template.getParameters();
								Iterator<Parameter>
								paramIterator =
								parameters.iterator();

								List<ParameterValue>
								parameterValues =
								templateInstance
								.getParameterValues();
								Iterator<ParameterValue
								> paramValues =
								parameterValues.iterator();

								Parameter parameter =
								null;
								ParameterValue
								parameterValue = null;

								while
								(paramIterator.hasNext() &&
								paramValues.hasNext())
								{
								parameter =
								paramIterator.next();
								parameterValue =
								paramValues.next();

								out.println("Parameter
								Name: " +
								parameter.getName());
								out.println("Parameter
								Value: "
										+
								parameterValue.getValue());
								}
								}

								out.print("</td><td>");
								// Print the child node	for the caseEdge
								printDecisionTableConditionsAndActions
								(caseEdge.getChildNode(),	0);

								out.print("</td></tr>")
								;
								}

								// Add Otherwise condition if it	exists
								TreeNode otherwise =
								conditionNode.getOtherwiseCase();

								if (otherwise != null)
								{
										out.print("<tr><td></td>
										<td>Otherwise</td><td>
										");
										// Print the OtherwiseConditionNode
										printDecisionTableConditionsAndActions (otherwise, 0);
										out.print("</td></td>")
										;
								}
								out.print("</table>");
						} else {
								// ActionNode has been found and different logic is needed
								// to print out the TreeActions
								ActionNode actionNode =
								(ActionNode) treeNode;
								List<TreeAction> treeActions =
								actionNode.getTreeActions();

								Iterator<TreeAction>
								treeActionIterator =
								treeActions.iterator();

								TreeAction treeAction = null;

								// The ActionNode can contain multiple TreeActions to
								// print out
								while
								(treeActionIterator.hasNext())
								{
										out.print("<tr>");
										treeAction =
										treeActionIterator.next
										();

										TreeActionTermDefinition treeActionTerm =
										treeAction.getTermDefinition();

										if (indent == 0) {
										out.print("<td>");
										out.print(treeActionTerm.getUserPresentation()
										);
										out.print("</td>");
										}
										out.print("<td>");
										TemplateInstanceExpression templateInstance =
										treeAction.getValueTemplateInstance();

										// Check that a template was specified	for
										// the TreeAction	before working with the
										// parameter name and	values
										if (templateInstance !=
										null) {
										out.println(templateInstance.
										getExpandedUserPresentation());

										Template template =
										templateInstance.getTemplate();

										List<Parameter>
										parameters =
										template.getParameters();

										Iterator<Parameter>
										paramIterator =
										parameters.iterator();

										List<ParameterValue>
										parameterValues =
										templateInstance
										.getParameterValues();
										Iterator<ParameterValue
										> paramValues =
										parameterValues
										.iterator();

										Parameter parameter =
										null;
										ParameterValue
										parameterValue = null;

										while
										(paramIterator.hasNext() &&
										paramValues.hasNext())
										{
										{parameter =
										paramIterator.next();
										parameterValue =
										paramValues.next();

										out.println(" Parameter
										Name: " +
										parameter.getName());
										out.println(" Parameter	Value: "
										+
										parameterValue.getValue());

										}
										} else
										{
										// If a template was not used, the only item	that is
										// available is the	UserPresentation if it was
										// specified when the	rule was created
										out.print(treeAction.getValueUserPresentation( ));
										}

										out.print("</td></tr>")
										;
								}
								out.print("</table>");
						}
				}
				/*
						Method to print out a rule set
				*/
		public static String printRuleSet(BusinessRuleruleArtifact)
		{
					out.clear();
					out.printlnBold("Rule Set");
					RuleSet ruleSet = (RuleSet) ruleArtifact;
					out.println("Name: " + ruleSet.getName());
					out.println("Namespace: " +
					ruleSet.getTargetNameSpace());

					// The rules in a rule set are contained in a	rule block
					RuleBlock ruleBlock =
					ruleSet.getFirstRuleBlock();

					Iterator<RuleSetRule> ruleIterator =
					ruleBlock.iterator();

					RuleSetRule rule = null;

					// Iterate through the rules in the rule block.
					while (ruleIterator.hasNext())
					{
							rule = ruleIterator.next();
							out.printBold("Rule: ");
							out.println(rule.getName());
							out.println("Display Name: " +
							rule.getDisplayName());
							out.println("Description: " +
							rule.getDescription());
							// The expanded user presentation will automatically populate the
							// presentation with the parameter values and can be used for
							// display if the rule was defined	with a template. If no
							// template was defined the expanded user presentation
							// is the same as the regular presentation.
							out.println("Expanded User Presentation: "
									+
							rule.getExpandedUserPresentation());
							// The regular user presentation	will have placeholders in the
							// string where the parameter can	be substituted if the rule
							// was defined with a template. If the rule was not defined with
							// a template, the user	presentation will only be a string
							// without placeholders. The	placeholders are of a format of {n}
							// where n is the index (zerobased) of the parameter in the
							// template. This value can be used to create an interface for
							// editing where there are fields	with the parameter values
							// available for editing
							out.println("User Presentation: " +
							rule.getUserPresentation());

							// Check if the rule was defined	with a template
							if (rule instanceof
							RuleSetTemplateInstanceRule) {
									RuleSetTemplateInstance
									Rule templateInstance =
									(RuleSetTemplateInstanceRule) rule;

									RuleSetRuleTemplate
									template =
									templateInstance
									.getRuleSetRuleTemplate
									();

									List<Parameter>
									parameters =
									template.getParameters();
									Iterator<Parameter>
									paramIterator =
									parameters.iterator();

									Parameter parameter =
									null;

									// Retrieve all of the parameters
									// and output the name and value
									while
									(paramIterator.hasNext())
									{
									parameter =
									paramIterator.next();

									out.println("Parameter
									Name: " +
									parameter.getName());
									out.println("Parameter
									Value: "
											+
									templateInstance.getParameterValue(
									parameter.getName()).getValue());
									}
							}
					}
					out.println("");
					return out.toString();
			}
}
```