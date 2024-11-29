# Tips for debugging view lifecycle method inside client-side human services

1. Open the client-side human service that contains the page that uses the views you want to
debug.
2. Click Debug
 in the upper-right corner. The inspector opens, pausing on the first step of the
client-side human service after the Start event.
3. When the client-side human service playback window launches, follow the browser-specific tips to
add breakpoints and debug the lifecycle method for your views.

## Internet Explorer 11

1. Open the Developer tools from the tool bar or by pressing F12
and go to the Debugger tool.
2. In the Inspector, click Step Over
 to
move to the page that you want to test, then click Step Into

begin debugging the page.
3. The Internet Explorer Debugger tool stops at a debugger statement at the beginning of the page
initialization. You can see the generated page for the page.
4. Locate the view lifecycle method code and set breakpoints as required.
5. Continue normal JavaScript debugging in the Internet Explorer
Debugger tool.

## Google Chrome

1. Open the Google Chrome Developer tools.
2. In the Inspector, click Step Over
 to
move to the page that you want to test, then click Step Into

begin debugging the page.
3. The Google Chrome Debugger tool stops at a debugger statement at the beginning of the page
initialization. You can see the generated page for the page. Note: You might encounter an issue
where Chrome Debugger does not display the generated page for the first page in a client-side human
service. If this occurs, click Resume script execution in the Sources tab,
wait until the page is loaded, then close and re-open the browser debugger. Next, click  again in the Inspector to restart the debugging process. If the browser debugger is closed,
re-open it. This causes the Chrome debugger to refresh and properly display the generated page for
the first page.
4. Locate the view lifecycle method code and set breakpoints as required.
5. Continue normal JavaScript debugging in the Chrome Debugger tool.

## Mozilla Firefox

1. Open the Firefox Debugger.
2. In the Inspector, click Step Over
 to
move to the page that you want to test, then click Step Into

begin debugging the page.
3. The Firefox Debugger tool stops at a debugger statement at the beginning of the page
initialization. You can see the generated page for the page. Note: You might encounter an issue
where Firefox Debugger does not display the generated page for your page. If this occurs, click
Click to resume in the Firefox Debugger tab, then right-click on the playback
window and select This Frame > Reload Frame to reload the page iFrame.
4. Locate the view lifecycle method code and set breakpoints as required.
5. Continue normal JavaScript debugging in the Firefox Debugger tool.