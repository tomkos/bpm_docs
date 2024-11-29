<!-- image -->

# Specifying regular debugging or problem determination debugging

## About this task

## Procedure

1. From the Window menu, select Preferences.
The Preferences window opens.
2. In the Preferences window, expand Business Integration and
select debug. The debug page opens.
3 In the debug options radio buttongroup, choose one of the following radio buttons:
    - Select IBM Integration
Designer debugging for
regular debugging of application modules and components. This is the
default selection and you should leave this option selected unless
you need to perform problem determination on the debugger under the
guidance of IBM support personnel.
    - Select Internal debugger debugging to
perform problem determination on the debugger run time code under
the guidance of support personnel.
    - Select System debugging to perform
problem determination on the runtime system code under the guidance
of IBM support personnel. (When this option is selected, certain aspects
of breakpoint processing are ignored, which enables the breakpoint
information to be displayed more quickly.)
4. Click Apply.
5 If you have selected the System debugging option,then you must disable step filtering for all com.ibm.* subclassesby completing the following steps:

1. In the navigation tree of the Preferences window, expand Java and
expand debug.
2. Select Step Filtering. The Step
Filtering page opens.
3. If the Use step filters check
box is selected, then clear the com.ibm.* check
box in the Defined step filters list and click Apply.
6. Click OK to close the Preferences
window.

## What to do next