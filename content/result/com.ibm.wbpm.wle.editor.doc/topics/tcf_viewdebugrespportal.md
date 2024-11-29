# Tips for debugging views in Process Portal

## Before you begin

Before you start debugging your views, you must enable JavaScript debugging in Process Portal. See
Enabling tracing for coaches. You should also ensure that the client-side human
service containing the views that you want to test is either exposed as a startable service or is
contained in a BPD which is exposed to start in the Process Portal.

Use the view debugging tips that correspond to your chosen browser.

## Internet Explorer 11

1. Log in to Process Portal.
2. Open the Developer tools from the tool bar or by pressing F12 and go to the Debugger tool.
3. In Process Portal, launch the client-side human service or BPD that contains the view that you want
to test.
4. The Internet Explorer Debugger tool stops at a debugger statement at the beginning of the coach
initialization. You can see the generated page for the coach.
5. Locate the view lifecycle method code and set breakpoints as required.
6. Continue normal JavaScript debugging in the Internet Explorer Debugger tool.

## Google Chrome

1. Log in to Process Portal.
2. Open the Google Chrome Debugger (F12).
3. In Process Portal, claim your task or start the exposed client-side human service that you want to
test.
4. When Chrome Debugger stops at a debugger statement at the beginning of the coach initialization,
click Resume script execution.
5. Click Refresh in the browser.
6 When Chrome Debugger stops again, click Resume script execution to allowthe debugger tool to continue when you see (engine.setTitle("Portal"); ORengine.setTitle("Work"); ). Follow the debugger statement until you see thegenerated page for your coach.
    - For a task, click Resume script execution until the debugger tool stops
at the page that contains the line engine.setTitle("<your\_coach\_title>");.
Follow the debugger statement in the code.
    - For an exposed client-side human service, restart the human service in Process Portal after
the browser refresh. The debugger tool will stop at the page that contains the line
engine.setTitle("<your\_coach\_title>");. Follow the debugger statement in the
code.Tip:  For the rare case when the page source is still not displayed when the
debugger stops, click Work in the navigation section and restart the human
service or reclaim the task.
7. Set breakpoints in your view lifecycle method as required.
8. Continue normal JavaScript debugging in the Chrome Debugger tool.

## Mozilla Firefox

1. Log in to Process Portal.
2. Open the Firefox Debugger.
3. In Process Portal, launch the client-side human service or BPD that contains the view that you
want to test.
4. The Firefox Debugger tool stops at a debugger statement at the beginning of the coach
initialization. You can see the generated page for the coach. Note: You might encounter an issue
where Firefox Debugger does not display the generated page for your coach. If this occurs, click
Click to resume in the Debugger tab, then right-click on the coach and select This Frame > Reload Frame to reload the coach iFrame.
5. Locate the view lifecycle method code and set breakpoints as required.
6. Continue normal JavaScript debugging in the Firefox Debugger tool.