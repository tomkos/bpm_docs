<!-- image -->

# Modifying decision table entries

## Before you begin

## About this task

## Procedure

1 Edit the value by typing over the existing value in the input field or by clicking the downarrow that appears in the field and selecting a value from the drop-down list. Restriction:
    - The initialization rule will only be displayed in the decision table if it is included in the
business rule definition that was designed in IBM® Integration
Designer. Only one initialization action rule can be
associated with a single template, but the action rule can have multiple action expressions in
it.
    - The otherwise condition will only be displayed in the decision table if it is
included in the business rule definition that was designed in IBM Integration
Designer. You cannot add or remove the
otherwise condition in the business process rules manager; however, you can incorporate
actions defined with templates for the otherwise condition.
2. Click Special actions and select an action.

Note: Selecting an option for reordering the columns or rows only affects the visual presentation of
the table and has no effect on the order in which the conditions and actions are processed.
3. Click Save.

## Results

The rule is modified locally and is ready to be published to the repository. For more
information, see Publishing and reverting business rules.