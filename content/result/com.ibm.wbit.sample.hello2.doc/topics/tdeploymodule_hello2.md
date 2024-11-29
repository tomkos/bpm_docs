<!-- image -->

# Deploy and test the modules

## About this task

To deploy and test the modules:

## Procedure

1. In the Business Integration view, right-click the HelloWorldPart2 integration
solution and select Test > Test Solution, as
shown here:   The
integration test client opens.
2. In the test client, click the Configurations tab.
The Configurations page opens and lists all of the modules in your
solution. Ensure that only the HelloWorldProcess module
is expanded, as shown here:   The
Configurations page is where you can configure your test session,
such as identifying the modules to include in the test, which ensures
that the modules are deployed and up-to-date on the server. (By launching
the test client from an integration solution, the modules are pre-populated
in the test configuration.)
3. You can also configure your test session so that variable
data is shown for each event when a process is tested, which can be
very helpful. Under the Fine-Grained Traces category
of the module, select HelloWorldProcess. On
the right side of the Configurations page, you see all of the variables
in the selected business process. Click Select All,
as shown here:  Another useful capability (which is not explored in this sample)
is the emulation of components and imports, which means that you do
not actually need to run them during your testing. This capability
encompasses the testing of human task components, where you can emulate
different users and claim and complete the tasks. Note: You
can also save your integration test client sessions to reuse them
at another time.
4. Click the Events tab. In the Detailed
Properties section, specify the module and component that you want
to test: namely, the HelloWorldProcess module
and the HelloWorldProcess process. In the value
editor, specify a value of male for the gender variable.
The Detailed Properties section should look like the following figure:
5. At the top of the Events area, click the Continue icon . The Deployment Location
window opens, as shown here:If you have different servers defined, you could choose to
deploy your modules to different servers. However, for the purposes
of this sample, simply click Finish to accept
the default server associations. The User Login window opens.
6. If you did not change the default user ID and password
for the server when you installed it, simply click OK.
(The default user ID and password are both admin.)
However, if you did change the default user ID or password
when you installed the server, specify the user ID and password and
then click OK. The server is started
(if required) and all of the modules in the test configuration are
deployed or republished as necessary, as shown here:Finally,
the actual test begins to run. In the Events area
of the test client, you can see events that display the execution
path through the components in the assembly diagram. You can also
see fine-grained trace events that display the execution path through
the activities in the business process, as shown in the following
figure: At this point, the execution
pauses. The Request event (highlighted in the
figure) is appended with the text (HelloWorldProcess ->
HelloWorldTask:getName), which indicates that the component HelloWorldProcess has
invoked the component HelloWorldTask through
its getName operation. The Request event is
currently the last event in the Events area, which means that the
process is waiting for user input...yours! There is a to-do task that
is waiting to be claimed and completed before the test can continue.
In the following steps, you will locate and process the to-do task.
7. In the Servers view, right-click
your server and select Launch > Business Process Choreographer
Explorer. The Business Process Choreographer Explorer
opens in the built-in web browser.
8. When you are prompted for a user name and password, specify
the user name and password that you have been using for administration
and for which you are specified as the only potential owner for the
human task. By default, the user name and password are both admin.
9. Click Login. The My To-dos page
opens. This page contains a list of to-do tasks for the user name
that you used to log in to the Business Process Choreographer Explorer,
as shown here:Remember, it is possible for multiple people to see the same
to-do task if they are part of the same Potential Owners list. However,
once a person claims a to-do task, only that person will be able to
see it.
10. Select the check box in front of the HelloWorldTask task
and then click the Work on button to claim
the task. The Task Message page opens and displays a form that contains
the input parameter data as well as the prompts used for specifying
the output parameter data, as shown here:
11. In the Task Message page, specify phil in
the firstName field and specify bar in
the lastName field, then click the Complete button
to complete your to-do task. The My To-dos page opens again, but the
to-do task no longer appears.
12. At the top of the Business Process Choreographer Explorer,
click Logout and then close the browser window.
Note: This web user interface is the default one supplied
for your convenience. There is also another supplied user interface
for human tasks in the Business Space, which you can also launch from
the Servers view. As well, you can create your own user interfaces
for processing human tasks. This can be done by starting from scratch
and using only the business process and human task APIs that IBM supplies,
or you can get a head start on your custom user interface by using Generate
Human Task User Interface in the module. For each task,
a default form will be generated if no customized forms are found.
You can optionally create and customize the forms for each task in
the User Interface section of the human task editor.
13. In the workbench, click the HelloService\_Test tab
to refocus the integration test client. You will note that the test
automatically continued and ran to completion. In the value editor,
you can see the contents that were returned for the result output
variable, as shown in the figure below: In the Events area,
you can also see the fine-grained trace event flow for the business
process as well as the request and response mediation flows from the
mediation module in the Hello World Part 1 sample, as shown in the
following figure:
14. In the Events area, click the Reply fine-grained
trace event to see the contents of the business process variables
as they existed at that point in the execution path, as shown in the
following figure:
15. Optional: If you want, you can perform some additional
testing. At the top of the Events area, click the drop-down arrow
beside the Invoke icon and then select Invoke,
as shown here: A
new Invoke event is displayed in the Events
area and the original input data for the earlier test is displayed
in the Initial request parameters value editor.
In the value editor, change male to female and
then click the Continue icon to run the test
again. You will need to once again launch Business Process Choreographer
Explorer to claim the task and you should again specify phil as
the given name and bar as the family name for
the output parameters. When you complete the task in Business Process
Choreographer Explorer, you should see a result of Hello
Ms phil bar returned in the test client.
16. Use File > Close All to close all
of the open editors. When a Save Test Trace window asks whether you
want to save your changes, click No.

## Results