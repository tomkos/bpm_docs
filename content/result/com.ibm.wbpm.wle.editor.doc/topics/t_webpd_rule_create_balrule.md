# Using action rules in the Process Designer

## Before you begin

## About this task

You can use the BAL rule editor to build rules, add rule
parts, statements, and fragments, and replace placeholders with variables
and values. Use the completion menu in the editor to insert or edit
constants, values, parts, or fragments of rule statements. While you
are creating or editing rules, the editor highlights errors to help
you identify and resolve problems in your rules.

The rule editor uses natural language technology to express business decisions in a form that is
readable by humans but could also be run by a rule service runtime such as the IBM® Operational Decision
Manager Rule Execution Server.

1. definitions part (optional)
2. if part
3. then part
4. else part (optional)

## Procedure

The following steps describe how to add a simple action
rule to an existing Decision task by using the decision editor.

1. Click the Decisions tab to open
the rules editor.
2. Select the your Decision task.
3. Click inside the rule window to begin creating a new rule
from the template. By default, the rule editor opens with
a basic template for a simple rule, with one condition (if)
and one action (then). For example, you can enter the following
rule definition, if expense is more than 5000 then set requireApproval
to true ;.
4 Click the condition placeholder, next to if , touse the Content Assist menu to complete the condition. Click a conditionstatement in the menu to add that condition to the rule.
    - If the list of conditions is long, you can use the Hierarchical
View menu instead of the Content Assist menu to select the condition
statement. To activate the Hierarchical View, click on the Toggle
Hierachical View icon while the Content Assist menu is
open, or press Ctrl+Shift+Spacebar.
    - If you know the name of the condition that you want to insert,
start typing the condition name. The Content Assist shows all the
conditions that match the name as you type.
    - The rule can reference service flow variables, for example, expense and requireApproval.
5. To select from the menu of possible actions, click the action placeholder, next to then.
Click an action statement in the menu to add that action to the rule.
For more information about using the menu to select actions, refer to the related topic in the
IBM Operational Decision
Manager documentation: Inserting a term or a phrase.
6. To add additional rule parts to the rule, click to place
the editor cursor above or below the existing rule content, then press Ctrl+Spacebar to
activate the Content Assist menu.  The Content Assist box
displays a list of valid rule parts. For example, to create a definition
rule part, click before the if condition section, then press Ctrl+Spacebar to
open the Content Assist menu and select definitions.
To create an else rule part, click below the then section
of the rule.
7. To add additional rules to the decision, click one of the
rule plus symbols beside the rule editor window. Each
time you click a plus symbol, a rule editor window is opened. Each
window contains the simple rule template.
8. In a decision that contains multiple rules, you can change
the order of the rules. Click the up arrow beside the editing window
to move the rule up one place in the rule order. Click the down arrow
to move the rule down one place in the rule order.
9. The rule editor saves the rules periodically as you are
authoring. To save all the rules in the decision while
you are authoring, press Ctrl+S, or click Finish
editing .

## Results

- Action Rules
- Rules Embedded capabilities and limitations
- Restricted characters in element names and vocabulary labels

- Business rule parts and structure in the Process Designer

Business rules, such as action rules or decision tables, express business policy statements using a predefined business vocabulary that can be interpreted by a computer. Rules authored in the Business Action Language (BAL) are also easily readable by humans.