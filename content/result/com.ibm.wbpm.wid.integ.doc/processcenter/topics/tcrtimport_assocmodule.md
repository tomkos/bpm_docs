<!-- image -->

# Creating an import to call a process in an associated module

## Before you begin

For imports that start or interact with a process from a Service Component
Architecture (SCA) module, the authenticated user role must have at least deployer and monitor
roles.

## Procedure

To create an import to start or interact with a process from a module
that is associated with a process application or toolkit, follow these steps:

1 From the Business Integration view, expand the process application andright-click the process you want to call. The available processes are listed underProcesses . Select Create Import . Alternately, on theassembly editor palette you can expand Outbound Imports , and then selectProcess , drag it onto the canvas and select the process from the dialog box.You can also do one of the following procedures:
    - If you are working on the assembly diagram, you can drag the process from the Business
Integration perspective onto the assembly editor canvas. It displays the Create
Import dialog.
    - If you are working in the BEPL editor and want to call a process from BPEL, drag the processfrom the Business Integration perspective directly into the BPEL editor:
        - If the process contains a None Start Event and does not contain any start or intermediatemessage events:
            - If the BPEL process is long running, the SCA import is created with a request-response
interface.
            - If the BPEL process is a microflow, the SCA import is created with a one-way interface.
    - If the process contains a Start or Intermediate Message Event, or if there is no None Start
Event, a dialog opens that explains that you must create the SCA Import manually by adding the
process to the assembly diagram.
2 In the Create Import window, all the exposed process interfaces arelisted. Select any combination of one or more interfaces for the Import. An import is created and added to the assembly editor canvas.

- The Available request-response interfaces section lists interfaces
that call the process and receive its outputs as a response from the process when it
completes.
- The Available one-way interfaces section lists interfaces that call
the process or interact with an existing process. For one-way interfaces, there is no response
returned from the process.