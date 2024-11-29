<!-- image -->

# Populate the module

## About this task

To populate the module:

## Procedure

1. If the assembly editor is not currently open for the HelloWorldProcess
module, expand the HelloWorldProcess module
in the Projects section of the Business Integration
view, then double-click Assembly Diagram to
open the assembly editor.
2. In the palette of the assembly editor, click the Process component
and then drag it to the editor canvas.
3. In the canvas, click the new process component and then
rename it to HelloWorldProcess and press the Enter key.
Note: If you accidentally double-click the process component,
an Open window will open to ask you whether you want to implement
the component now. If the Open window appears, click No (or
press the Esc key).
4. In the canvas, click the new HelloWorldProcess component
to display the hover bar above the component, then click the circled I icon
to open the Add Interface window.
5. In the Matching interfaces list,
select HelloWorldProcess and click OK.
The new HelloWorldProcess interface is added
to the HelloWorldProcess component, as shown
in the following figure:
6. Drag Human task from the palette
to the canvas.
7. Rename the new human task component to HelloWorldTask.
8. Using essentially the same steps that you used to add an
interface to the HelloWorldProcess component, add the interface HelloWorldTask to
the new human task component.
9. Wire the HelloWorldProcess process
component to the HelloWorldTask human task
component and click OK. When the Add
Wire window opens, click OK. Here
is what you should have so far:
10. Press Ctrl-S to save your work.
11. In the Projects section of the Business
Integration view, expand the HelloWorldMediation project
and the Assembly Diagram category, then select HelloWorldMediationExport and
drag it to the assembly editor canvas for the HelloWorldProcess module.
The Component Creation window opens.
12. Select Import with SCA Binding and
click OK. An SCA import component is generated
that can be used to invoke the module from the Hello World Part 1
sample.
13. Rename the new import to HelloWorldImport.
14. Wire the HelloWorldProcess process
component to the HelloWorldImport import. When
the Add Wire window opens, click OK.
Your assembly diagram should now look like this:
15. By default, the assembly editor canvas is in automatic
layout mode and each component is positioned automatically. However,
if you manually adjust the position of a component, the automatic
layout capability is switched off. Look on the status line at the
bottom of the workbench to see whether automatic layout is on or off.
If the status is off, you can turn automatic
layout on again by right-clicking in the assembly editor canvas and
selecting Automatic Layout, as shown in the
following figure:Alternatively, you can leave automatic layout off and perform
a one-time layout by selecting Layout Contents.
16. Save the contents of the assembly editor.