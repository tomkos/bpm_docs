<!-- image -->

# Implementing an Advanced Integration service in the same process
application or toolkit

## Before you begin

1. Import the process application into Integration Designer.
2. Disassociate the modules from the process application.
3. If there are any artifacts in the default module and library projects
(process\_app\_name\_Implementation and process\_app\_name\_Library),
save these artifacts outside of your workspace. You will merge this
content back into the workspace later.
4. Delete the disassociated default implementation and library modules.
The only artifacts left in the workspace are any disassociated modules.
5. Reimport the process application. This action regenerates the
default projects with a WSDL file for each AIS interface.
6. Rename the interfaces in the library module to give them unique
names. This step is necessary because the advanced integration services
originally came from the same interface.
7. Add any artifacts that you saved in step 3 back into the default
module and library projects, add those back into the projects
8. Publish the process application or modules.

## Procedure

To start the wizard and generate a basic implementation
for a process application, complete the following steps:

1. From the Business Integration view,
expand the process application or toolkit and the Advanced
Integration Services folder. Right-click the service to
be implemented (it is marked unimplemented) and then click Implement.
The Implement Advanced Integration Services wizard
opens.
2. Click This toolkit.
3. Click Next.
4 Select the implementation type from the following listand click Finish . Note: Preferred interaction style determines if a synchronousor asynchronous mode of communication is used. If your Advanced Integrationservice is interacting with modules through imports and exports, checktheir preferred interaction style as it may affect your performanceexpectations. For example, you may select an implementation type ofmicroflow expecting a synchronous communication mode with an immediateresponse. But the implementation may include modules with JMS bindingsthat send data asynchronously which could result in data waiting inqueues.
    - Microflow. Select this option if your
service will start a business process that provides an immediate response.
An export and a business process set to a microflow are created.
    - Long-running business process. Select
this option if your service will start a business process that runs
for an extended time; that is, if it does not provide an immediate
response. An export and a business process set to a long-running process
are created.
    - Java component. Select this option
if your service will be implemented in Java. An export and a Java
component are created.
    - Empty implementation. Select this option
if you have not decided on the implementation you will use. An export
is created but it is not wired to a component in the assembly editor.
Later you can create a mediation flow, state machine, an interaction
with another system through an adapter or some other implementation.
5. You can now see the components in the assembly editor,
and the Advanced Integration service is marked implemented. You must
still develop the implementations because only a skeleton has been
created.
6. Once you have developed your implementation, you must use
the Publish command to update the information
of the corresponding Advanced Integration service in Process Designer.

## Results

When the Advanced Integration service wizard finishes,
the appropriate editor opens in the implementation (an editor such
as BPEL or Java). In the case where no implementation is selected,
the assembly editor opens only if you are in Advanced Mode.
If you are in Simple Mode, the option, Empty
implementation, does not show.

## Related tasks

- Building an Advanced Integration
service