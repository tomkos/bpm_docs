<!-- image -->

# Creating custom selectors

## About this task

## Procedure

1. Create the components that will be the target of the selector
after the selection has been made. Any IBM® Business Automation
Workflow component
can be used as the outcome of the selector choice. You need as many
components as you will have possible outcomes. These components should
all share an interface.
2 Create a CustomSelector Java™ class. This is the class that will make the decision about which componentto select.
    1. Open the New Java Class wizard.
Select your Module in the Business Integration view, right-click
and select New > Other > Java > Class and
then click Next.
    2. In the Source Folder field browse
to the current module folder.
    3. Enter com.ibm.customselectors in the Package field.
    4. Enter an appropriate name for the Java class, for example CustomSelector.
    5. Open the Implemented interfaces selection panel.
Click the Add button.
    6. In the Choose interfaces field
of the Implemented interfaces selection panel type com.ibm.wbiserver.common.selection.S,
and choose SelectionAlgorithm in the Matching
types field when it appears. Click OK.
    7. Click Finish.
    8. Augment the generated code with new code that will provide
the new custom selection logic.
3 Create a new selector component.

1. Apply the same interface to the new selector that you
used for the target components.
2. Choose one of the target IBM Business Automation
Workflow components
as the Default Rule Logic.
3. Save and close the new selector.
4 Edit the code of the new selector to replace the default Java class with your custom code.

1. In the Business Integration view, right-click the selector
and click Show Files. This
opens the Physical Resources view, which displays the generated files
for the project.
2. Right-click the filename.sel file,
and select Open With > Text Editor.
3. Find the line of code: <Selector>com.ibm.wbiservers.common.selection.GenericSelector</Selector>  and
replace it with <Selector>com.ibm.customselectors.CustomSelector</Selector> where CustomSelector is
the name you gave to your Java class.
4. Save and close the selector file.
5. Add the selector and all of the target components to the
assembly diagram.

## Results

## Related concepts

- Rule group editor
- Using rule set names in a rule group

## Related tasks

- Specifying the rule logic for a rule group
- Scheduling rules using the rule group editor
- Customizing algorithms for date and time selection