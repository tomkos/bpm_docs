<!-- image -->

# Creating programmatic emulation files

## Before you begin

If your test is invoking a one-way
operation, the test will return a result of Passed, but the emulation
will not actually run unless you have followed the instructions in
the topic "Emulating components and references when invoking one-way
operations".

## About this task

## Procedure

1 Complete one of the following steps: The New Emulator wizard opens to the Emulator page.
    - If you have an existing emulator that you have already defined
as programmatic and you want to create a programmatic emulation file
for it, ensure that the emulator is selected in the Configurations
page of the test suite editor and that Programmatic emulation is
still selected, then click New. (Information
about defining an emulator as programmatic is found in the topic "Defining
emulators as programmatic.")
    - If you do not want to create a programmatic emulation file
for any specific programmatic emulator but you want to create one
that can later be used with one or more new programmatic emulators,
select File > New > Emulator from the workbench
menu bar of the Business Integration perspective.
2 Complete one of the following steps:

- If you want the Project field to display
only component test projects, ensure that the Show only
test projects check box is selected. (It is recommended
that you save your programmatic emulation file in a component test
project because you may not want your testing artifacts to be deployed
to a server with a module.)
- If you want the Project field to display
all available projects, clear the Show only test projects check
box.
3. In the Project field, select the
project where you want to save your programmatic emulation file.
4 If you want to save the test trace in a different folderthan the default Emulators folder, clear the Default checkbox and then complete one of the following steps:

- If you want to save the test trace to an existing folder,
click Browse and then navigate to the folder
and select it.
- If you want to save the test trace to a new folder,
type the name that you want to assign to the new folder in the Folder field.
5. In the Name field, type the name
that you want to assign to the programmatic emulation file.
6. Click Next to open the next page
of the New Emulator wizard.
7 Complete one of the following steps:

- If you are creating a programmatic emulation file for a human
task emulator, ensure that Interface is selected
and then locate and select the interface that you want to emulate
in the Select an interface to emulate list.
(The interface emulator is used to generate the required response
data objects for the human task that will be claimed. By emulating
an interface rather than a component or reference, you can specify
different outputs for the human task.)
- If you are creating a programmatic emulation file for a component
or reference emulator, ensure that Component or reference is
selected and then locate and select the component or reference that
you want to emulate in the Select a component or reference
to emulate list.
8. Click Next. The Java™ Class
page opens.
9. Accept the defaults and click Finish.
The programmatic emulation file is created and the programmatic emulation
editor automatically opens.

## What to do next