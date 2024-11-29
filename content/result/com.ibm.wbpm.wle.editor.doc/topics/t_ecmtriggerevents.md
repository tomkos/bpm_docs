# Adding a content event to a process

## Before you begin

## About this task

## Procedure

1. Open a process application in the Designer view.
2. Click the plus (+) icon beside Processes and then
select Process. The New Process wizard opens.
3. In the Name field, specify a name for the new process.
4. Click Finish. The new process is displayed in the Process library list
(under Process) and the process opens in the editor.
5. In the canvas, select the existing Start event
or select the Start Event or Intermediate
Event icon in the palette and drag the event to the canvas.
6. Click the Properties tab and then
click Implementation. The Implementation panel
opens.
7. In the Start Event Type or Intermediate Event
Type section, change None to ECM Content.
The event in the diagram changes to display a Content marker icon.
8. Beside the Attached content UCA area in the Event
Properties section, click Select to select an existing content
undercover agent (UCA). For information about creating content UCAs, see Creating and configuring an undercover agent for a content event.
9. In the Properties, click Data Mapping. The Data
Mapping panel opens.
10 Perform the data mapping tasks by completing the followingsteps: For undercover agents that are implemented using a complex variablerather than a service, you can select the complex variable or thetop-level child properties of the variable for mapping or correlation.
    1. Click the variable selector icon on the right side of each field to map each undercover agent
output variable to a local variable in the process.
    2. If you are working with an intermediate event, select the variable that you want to use to
correlate the event with the process instance. The variable selected for correlation is identified
by an assignment symbol (). This correlation ensures that the parameter values of the runtime message are passed to
the correct process instance. (IBM® Business Automation
Workflow
only requires one variable mapping to correlate the event.)
11. Click Save or Finish Editing.