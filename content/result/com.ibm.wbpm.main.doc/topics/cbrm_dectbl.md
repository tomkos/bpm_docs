<!-- image -->

# Decision table

Decision tables are similar to decision trees, however they are balanced. Decision tables always
have the same number of conditions to be evaluated and actions to be performed no matter what set of
branches are resolved to true. A decision tree may have one branch with more conditions to evaluate
than another branch.

Decision tables are structured as a tree of nodes and defined by a TreeBlock.
There are different TreeNodes which make up the TreeBlock.
TreeNodes can be condition nodes or action nodes. Condition nodes are the
evaluation branches. At the end of branches, there are action nodes that have the appropriate tree
actions to issue should all of the conditions evaluate to true. There can be any number of levels of
condition nodes, but only one level of action nodes.

<!-- image -->

Decision tables might also have an initialization rule (init rule) which can be issued before the
conditions in the table are checked.

The DecisionTable class provides methods that support the following:

- Retrieve the tree block of tree nodes (condition and action nodes)
- Retrieve the init rule instance
- Retrieve the init rule template if defined

Figure 1. Class diagram of DecisionTable and related classes

<!-- image -->

The TreeBlock of a decision table contains the different condition and action
nodes. Each condition node (ConditionNode) has a term definition
(TreeConditionTermDefinition) and one to n case edges (CaseEdge).
The term definition contains the left operand for the condition expression. The case edges contain
the value definitions which are the different right operands to be used in the condition expression.
For example, in the expression (status == "gold") the term definition would be "status" and "gold"
would be the value definition in the case edge. For all of the case edges in a condition node, they
share the term definition and are only different by the value
(TreeConditionValueDefinition). Continuing with the example, another case edge in
the condition node could have a value "silver". This would be used in an expression too (status ==
"silver"). The only exception to this behavior is if an otherwise has been defined for the condition
node. With an otherwise, there is no value definition as it is used if all other case edges within
the condition node evaluate to false. While an otherwise is not a case edge, it does have a
TreeNode that can be retrieved.

<!-- image -->

For the term definition, the user presentation can be retrieved and used in client applications.
The presentation for the term definition is typically only a representation of the left operand
(status in our example) and does not contain any placeholders. For the case edges, a template can be
used to define the value definition (TreeConditionValueTemplate). A template value
definition instance (TemplateInstanceExpression) holds the parameter values which
are used for execution and can be modified. If an attempt is made to retrieve the value template
definition for a TreeConditionValueDefinition that was not defined with a template,
a null value will be returned. If a template has not been used to define the value condition, a user
presentation can still be retrieved and used in client applications if it was specified at authoring
time.

- Retrieve the root node of the tree
- Retrieve the condition term definitions for the tree block
- Retrieve the action term definitions for the tree block

- Determine if a node is an otherwise clause
- Retrieve the parent node for the current tree node (condition or action node)
- Retrieve the root node of the tree containing the current tree node

- Retrieve the case edges
- Retrieve the term definition
- Retrieve the otherwise case
- Retrieve the templates for the value conditions of the case edges for the condition node
- Add a condition value based on a template to the node
- Remove a condition value based on a template

- Retrieve the list of value templates which are available for the value definition
- Retrieve the child node (condition or action node)
- Retrieve the instance of the template definition associated with the value definition
- Retrieve the value definition directly without retrieving the template
- Set the value for the definition to use a specific template instance definition

- Retrieve the value definition templates defined for the condition node
- Retrieve the user presentation of the condition term

- Retrieve the term definition for the condition node
- Retrieve the condition value definitions for the condition node from all of the case edges
- Retrieve the orientation (row or column)

- Retrieve the specific template instance expression defined for the value
- Retrieve the user

- Retrieve the system ID for the template
- Retrieve the name of the template
- Retrieve the parameters defined for the template
- Retrieve the presentation for the template

- Create a new template condition value instance

- Retrieve the parameters for the template instance
- Retrieve the template (TreeConditionValueTemplate in the case of a case edge in
a decision table) that was used to define the instance

Figure 2. Class diagram for TreeNode and related classes

<!-- image -->

When a new case edge is added to a condition node, the new case edge must use a template to
define the value. For example if a new case edge of "bronze" was to be added for checking 'status',
the appropriate template (TreeConditionValueTemplate) would need to be used to
create a new TemplateInstanceExpression, setting the parameter value to "bronze".

When a new case edge is added, it will also have a child condition node added to it
automatically. This child condition node will contain case edges which are based on the case edge
definitions that have been defined for condition nodes at that same level. If templates or
hard-coded values are used in case edges, they will then be used in the child condition node's case
edges as well. The child condition node that is added automatically will also have its own child
condition nodes created automatically. These child condition nodes will also have child condition
nodes and so on until all levels of condition nodes have been re-created.

Besides the condition nodes, a decision table and more specifically tree block, also contains a
level of action nodes (ActionNode). The action nodes are leaf nodes and reside at
the end of the branch of condition nodes and the case edges. Should all of the condition values in a
line of case edges resolve to true, an action node is reached. The action node will have at least
one action (TreeAction) defined. For the action, there will be a term definition
and value definition. Just as with the condition nodes, the term definition
(TreeActionTermDefinition) is to the left of the expression and the value
definition (TemplateInstanceExpression) is to the right side of the expression. For
example, for the different condition nodes which were checking on the status, there might be actions
to define the discount. If the condition was (status == "gold"), the action can be (discountValue =
0.90). For the action the "discountValue" would be the term definition and the "= 0.90" would be the
value definition.

The term definition of a tree action is shared with other tree actions in other action nodes.
Since every branch of case edges reaches an action, the same term definitions are used. The value
definitions however, can be different per tree action and action node. For example the discountValue
for a status of "gold" can be "0.90"; however the "discountValue" for a status of "silver" can be
"0.95".

Action nodes can have multiple tree actions which have a separate term definition and separate
value definition. For example, if the discount was being determined for a rental car, besides
setting the discountValue, you can also want to assign a specific level of car. Another tree action
could be created to set the "carSize" term to "full size" if the status was "gold" as well as set
the "discountValue" to "0.90".

The value definition in a tree action can be created from a template
(TreeActionValueTemplate). The template definition contains an expression
(TemplateInstanceExpression) which has the parameters for the expression.

Besides changing the parameters, the entire value definition can be modified with a new value
definition instance which is created with another template which was defined for the tree
action.

If a value definition is not created with a template, it cannot be changed. For client
applications, the user presentation can be used in display if it was specified at author time.

For term definitions in tree actions, if a user presentation has been specified, it can also be
used by client applications.

When a new case edge is added to a condition node and the different child condition nodes are
created, action nodes will also be created. Unlike the child condition nodes and case edges which
are created based on the definition of the case edges already defined for that level, action nodes
do not automatically inherit an existing design. Only empty placeholder TreeActions
are created in the action node. A template (TreeActionValueTemplate) must be used
to complete the action definition by creating a TemplateInstanceExpression for at
least one term definition for the action node. Until the tree action is set with a
TemplateInstanceExpression, the tree action will have null values specified for the
user presentation value and template instance value.

When creating a new condition that results in new ActionNodes, the action nodes will be added to
the right of existing actions for the immediate parent condition node. For example if a status of
"ruby" is added to the decision table and should have a specific discount, the condition to check
the status is added at the right of "gold", "silver", and "bronze". The action node for the discount
for "ruby" will be added to the right of the action nodes that correspond to the "gold", "silver"
and "bronze" case edges.

When setting new tree actions for action nodes, an algorithm that looks to the rightmost action
node at the lowest case edge will return the action node with an empty tree action. The tree action
can also be checked that it has null values for the user presentation value and template instance
value. Once the tree action is obtained, it can be set with the correct instance of a
TreeActionValueTemplate.

<!-- image -->

- Retrieve a list of the defined tree actions

- Retrieve a list of the available value templates defined for the tree action
- Retrieve the term definition
- Retrieve the value template instance defined for the tree action
- Retrieve the user presentation for the value if a value template was not used
- Check if the action is a SCA service invocation (isValueNotApplicable method)
- Replace the value template instance with a new instance

- Retrieve the user presentation for the term value definition
- Retrieve a list of the value templates available for the tree action
- Check if the action is a SCA service invocation (isTermNotApplicable
method)

- Retrieve the system ID for the template
- Retrieve the name of the template
- Retrieve the parameters defined for the template
- Retrieve the presentation for the template

- Create a new value template instance from the template definition

- Retrieve the parameters for the template instance
- Retrieve the template (TreeActionValueTemplate in the case of a tree action in
a decision table) which was used to define the instance

Figure 3. Class diagram of TreeAction and related classes

<!-- image -->

The definition of an init rule for a decision table follows the same structure as a rule in a
rule set. The init rule can be defined with a template
(DecisionTableRuleTemplate).

If an init rule was not created at authoring time, it cannot be added once the rule is
deployed.

- Retrieve the name of the rule
- Retrieve the user presentation for the rule
- Retrieve the user presentation for the rule with the different parameters for the rule filled
in

- Retrieve the tree block containing the init rule

- Retrieve the decision table containing the template

Figure 4. Class diagram for DecisionTableRule and related classes

<!-- image -->