<!-- image -->

# Calling other BPEL processes

## Before you begin

## About this task

Your BPEL process can call other services, including other
BPEL processes. There are scenarios in which it is important that
the calling BPEL process (parent) knows that the called service
is another BPEL process. For example, you want to manage the lifecycle
 of the processes, so that if the parent process is terminated, all
subprocesses are stopped.

Another important example of when
awareness of the nature of the called service is required is in late
binding. In a late binding scenario a particular part of the overall
process is modeled as a subprocess, but the integration developer
is aware that in the future this part of the process may change. A
good example would be when a decision point in the business model
is reached; today the decision is made by a member of staff (a human
task would be required) but in the future the decision may be automated
(a microflow could be used). By modeling this decision as a subprocess,
the parent process does not have to be modified when this change is
made. The new subprocess can be seamlessly introduced.

Many
BPEL processes can be reused as part of larger BPEL processes. You
can build a set of useful subprocesses that can be reused to facilitate
rapid development of complex BPEL processes. Take the following steps
to call one BPEL process from another. Below we outline the steps
to call a subprocess from a parent process.

For lifecycle management
the parent and subprocess should be part of the same
module. For late binding they should belong to different modules.

## Procedure

1 Add a reference partner SubprocessPartner to theBPEL process parent that points to the interface that is usedby the process subprocess .
    1. In the tray, select the plus sign beside Reference
Partners.
    2. Select the interface that corresponds to the subprocess
from the list of matching interfaces.
2. Add an Invoke activity to the parent business
process by dragging the reference partner to the canvas.
3. Enter the details for the Invoke activity
in the details page. Provide any necessary variables.
4 Optional: In order to control the lifecycleof the subprocess:

1. In the parent process, in the Details property
of the process, make sure that the Bind the lifecycle to
the invoking BPEL process check box is cleared.
2. In the subprocess process, in the Details property
of the process, make sure that the Bind the lifecycle to
the invoking BPEL process check box is selected.
3. Open the assembly diagram.
4. Add parent and subprocess to the assembly
diagram and create a wire between them.
5 Optional: To enable late binding versioning:

1. In the tray select the reference partner subprocess
and in the properties view enter subprocess in the Process
template field.
2. Open the assembly diagram of the module with the parent process.
3. Add parent to the assembly diagram.
4. Open the assembly diagram of the module with the subprocess process.
5. Add subprocess to the assembly diagram.
6. In the assembly diagram of subprocess,
generate an SCA Binding export. Right-click subprocess in
the assembly diagram, select Generate Export > SCA Binding.