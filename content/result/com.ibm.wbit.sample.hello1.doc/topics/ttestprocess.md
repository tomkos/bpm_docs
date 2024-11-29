<!-- image -->

# Test the module

## About this task

To test the module:

## Procedure

1. In the Business Integration view, expand HelloWorldMediation and
double-click Assembly Diagram. The assembly
diagram opens.
2. Right-click the HelloWorldMediationExport export
component and select Test Component. The integration
test client opens.
3. Provide sample values for the parameters passed to the
export component. To do this, specify values for each of the fields
of the business object by editing cells in the Value column
of the value editor table.  In the Value column
of the value editor table (located in the lower right corner of the
test client), double-click a cell (or start typing in a cell) to enter
edit mode and then enter Mr for title, Phil for firstName,
and Bar for lastName. Tip: Click
the down arrow or press the Enter key after
typing. The value editor is shown in the following figure:
4. At the top of the events list in the test client, click
the Continue icon . The Deployment Location window
 opens.
5 If multiple servers are listed in the Deployment Locationwindow and you intend to select a server other than your original IBM® WorkflowServer server,your test may result in an exception because the HTTP port numberfor the selected server may not match the default port number of 9080that is specified for the HelloServiceImport binding. To determinethe port number of your intended server and (if necessary) changethe port number of the import binding to match it, complete the followingsteps:
    1. In the file system, change to the following folder (where installDir is
the installationl path of the test environment for IBM Integration
Designer and serverProfile is
the name of the server profile): installDir\runtimes\bi\_v8\_stub\profiles\serverProfile\logs
For
example:
C:\Program Files\IBM\WID8\_WTE\runtimes\bi\_v8\_stub\profiles\qwps\logs
    2. Open the file AboutThisProfile.txt in
a text editor.
    3. In the file, locate the HTTP transport port number.
If the HTTP transport port number is not 9080, complete the
following steps to change the port number of the import binding to
match the port number of the HTTP transport port.
    4. Close the AboutThisProfile.txt file.
    5. In the test client, press Cancel to
close the Deployment Location window.
    6. Close the test client and when prompted to save your
changes, click No.
    7. In the Business Integration view, expand the HelloWorldMediation mediation
module and double-click Assembly Diagram. The
assembly diagram opens in the assembly editor.
    8. In the assembly diagram, select the HelloServiceImport import.
    9. Click the Properties tab and
then click the Binding tab. The Binding pane
opens.
    10. In the Address field of the Binding
pane, change the port number of the import binding to match the port
number of the HTTP transport port, as shown in the following figure:
    11. Press Ctrl-S to save your changes
and then close the assembly editor.
    12. Repeat the instructions in this topic, beginning with
step 1.
6. In the Deployment Location window, ensure that the correct
server is selected and click Finish. The User
Login window opens.
7. If you did not change the default user ID and password
of the server during installation, click OK.
Otherwise, type the user ID and password that you specified during
installation and click OK. The test client
code that runs on the server is started, and if necessary any modules
with changes are published, and the test is run. You see events in
the Events list showing execution flowing through
the components in the assembly diagram and fine-grained events of
the execution flowing through the primitives in the mediation request
and response flows. The result returned should be the string "Hello
Mr Phil Bar", as shown here:
8. Optional: You can continue testing. Select the little
down arrow icon beside the third icon in the toolbar above the Events
list and then select Invoke, as shown here: A new Invoke event appears in the events list,
and the original input data for that test shows in the Initial
request parameters value editor. Change Bar to BarAgain and
rerun the test, again by clicking the Continue button.
9. Use File > Close All to close
all open editors. When prompted to save your test client session,
click No.

## Results