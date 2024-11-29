<!-- image -->

# Replacing a stand-alone task with an inline task in the BPEL
process

## Procedure

1. In the assembly editor, delete the existing interface between
the human task component and the BPEL process.
2. Delete the component.
3. In the BPEL process component, right-click the invoke activity
that originally connected to the human task component, and clickChange type > Human task.
4. In the Details tab of the human
task, clickNew.
5. Select the interface that was used between the original
business process component and the human task component.
6. Define the settings for the human task.
7. From the main menu, click Project > Clean.