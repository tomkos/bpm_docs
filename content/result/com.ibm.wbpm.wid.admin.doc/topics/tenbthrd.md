<!-- image -->

# Changing integration debugger thread filters

## About this task

## Procedure

1. From the Window menu, select Preferences.
The Preferences window opens.
2. In the left frame of the Preferences window, expand Run/Debug and
expand Java and Mixed Language Debug, then
select Thread Filters. The Thread Filters page
opens.
3 If you want to want to ensure that the recommended threadfiltering preferences are set for the integration debugger, completethe following steps:
    1. Ensure that the Apply thread filters check
box is selected. (Note that if you wanted to show all threads,
you would clear the check box.)
    2. Ensure that the Java Threads check
box is selected. This thread filter will filter the Java™ threads
of IBM Business Automation
Workflow from
the Debug view in the Debug perspective. When Java threads
are filtered, they will not appear in the Debug view unless a debug
event occurs within them, such as a breakpoint.
    3. Ensure that the WBI Thread Filter check
box is not selected. This will enable IBM Integration
Designer threads
to be displayed in the Debug view.
    4. Click OK.