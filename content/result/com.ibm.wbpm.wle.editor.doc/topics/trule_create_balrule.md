# Creating rules using the rule editor (deprecated)

Traditional: 
You can create
rules using the Business Action Language (BAL) rule editor. The rule editor uses natural language
technology to express business decisions in a form that is readable by humans but can also be run by
a rule service runtime such as the IBM® Operational Decision
Manager Rule Execution Server.

## About this task

You can use the BAL rule editor to build rules, add rule
parts, statements, and fragments, and replace placeholders with variables
and values. Use the completion menu in the editor to insert or edit
constants, values, parts, or fragments of rule statements. While you
are creating or editing rules, the editor highlights errors to help
you identify and resolve problems in your rules.

1. definitions part (optional)
2. if part
3. then part
4. else part (optional)

The
following steps describe how to author a rule using the rule editor.
The rule is implemented in a BAL Rule component as part of a sample
Decision service. The purpose of the sample service created in the
procedure steps is to determine whether approval is required for certain
employee expenses. The sample service is a single-function rule that
can be called from any other service.

## Procedure

1. Make sure you are working in the sample Decision service
that was created in the related topic "Adding a BAL Rule component
to a service."
2. Click the Decisions tab to open
the rule editor.
3. By default, the rule editor opens with an empty BAL rule
window. The rule window contains a basic template for a
simple rule, with one condition (if) and one action (then).
4 Click inside the rule window to begin creating a new rulefrom the template.
    1 Click the condition placeholder, next to if ,to use the Content Assist menu to complete the condition. Double-clicka condition statement in the menu to add that condition to the rule.
        - If the list of conditions is long, you can use the Tree Completer
menu instead of the Content Assist menu to select the condition statement.
With the edit cursor on the <condition> placeholder,
press Ctrl+Shift+Spacebar to open the Tree
Completer menu.
        - If you know the name of the condition you want to insert, start
typing the condition name. The Tree Completer shows all the conditions
that match the name as you type, as shown in the following diagram:
2. Click the action placeholder, next to then, to select from the menu of possible
actions. Double-click an action statement in the menu to add that action to the rule. For
more information about using the menu to select actions, refer to the related topic in the IBM Operational Decision
Manager documentation,
"Inserting a term or a phrase."
5. To add additional rule parts to the rule, click to place
the editor cursor above or below the existing rule content, then press Ctrl+Spacebar to
activate the Content Assist menu.  The Content Assist box
displays a list of valid rule parts. For example, to create a definition
rule part, click before the if condition section, then press Ctrl+Spacebar to
open the Content Assist menu and select definitions.
To create an else rule part, click below the then section
of the rule.
6. To add additional rules to the BAL Rule component, click
the plus symbol at the top of the rule editor window. Each
time you click the plus symbol, a rule editor window is opened. Each
window contains the simple rule template.
7. In a BAL Rule component that contains multiple rules, you
can change the order of the rules. Click the up arrow beside the editing
window to move the rule up one place in the rule order. Click the
down arrow to move the rule down one place in the rule order.
8. The rule editor saves the rules periodically as you are
authoring. To save all the rules in the BAL Rule component
while you are authoring, click Ctrl+S, or click
the Save icon in the Process Designer action
bar.
9. To exit the rule editor, click the exit icon (X)
next to the Decision service name.