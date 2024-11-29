# Viewing the status of process instances and applications

## Procedure

1. Open the Process Admin console. In the Process Admin console, the Process Status summary is
displayed in the Server Admin page. It displays status information for
process applications and for process instances that are in the Started, Completed, Late, Executing,
and Failed states.
2. In the Process Status summary, click one of the following time frame buttons to display status
information for process instances and process applications that exist in the selected time
frame:

Option
Description

Today
Displays the status of process instances and process applications for the last 24 hours.
(The default time frame.) 

Week
Displays the status of process instances and process applications for the last seven
days.

Month
Displays the status of process instances and process applications for the last 30
days.

Year
Displays the status of process instances and process applications for the last 365
days.

All-time
Displays the status of the process instances and process applications that have ever existed
on the workflow server.

For example, if you click the Week button, the
Started, Completed, Late,
Executing, and Failed status boxes are automatically
updated to display the status and number of the process instances that existed in the last seven
days.Similarly, in the Process Applications section of the Process Status
summary, the list of process applications is automatically updated to display all of the process
applications that resided on the server in the last seven days. The status icon that precedes each
process application also changes to reflect the current status of the process
application.
3 If you want to see more detailed information about allprocess instances that have the same status (such as all process instancesthat have failed), click one of the following status boxes: The Process Inspector opens and displays a list of allprocess instances that have the same status within the selected timeframe.
    - Started
    - Completed
    - Late
    - Executing
    - Failed
4. If you want to see more detailed information about a specific
process application, click the name of the process application in
the Process Applications section. The Process
Inspector opens and displays a list of the process instances that
originate from the selected process application.
5. If you simply want to open the Process Inspector without displaying any specific process
instances or process applications, click the Open Process Inspector link. The
Process Inspector opens and displays a list of process instances that is sorted in descending order
according to the date of the most recent action.

## What to do next

Optionally, you can embed the Process Status summary in another location. For example, you might
want to embed the Process Status summary in a dashboard or portal to help you aggregate status
information from multiple servers or systems. To embed the Process Status summary in another
location, click the Embed icon in the summary to open the
Embed window, then copy the HTML code from the window and paste it into the web
page where you want the Process Status summary to appear.