<!-- image -->

# Creating EJB imports using the external service wizard

You can use the external service wizard in IBM® Integration
Designer to
build an EJB import service. The external service wizard is a tool
used to create services based on criteria that you provide. It then
generates business objects, interfaces, and import files based on
the services discovered. The EJB import is created based on an existing
EJB implementation and the newly created import can then be deployed
to IBM Workflow
Server.

## Before you begin

## About this task

## Procedure

1. Launch the external service wizard in IBM Integration
Designer by
clicking File > New > External Service.
2. From the external service wizard window, select JavaEnterprise
JavaBeans Binding and click Next.
Note that you can also launch this wizard by selecting a module in
the business integration (BI) view and right-clicking and selecting New > External Service > Java > Enterprise JavaBeans Binding.
3. The New Enterprise JavaBeans Binding Service window opens.
For EJB imports, select the Outbound processing
option for the direction of binding processing to be used at run time.
After you have made the selection, click Next.
4. Select the module where the generated artifacts should
be saved. You can select an existing module from the drop-down list,
or create a new one by clicking New. You can
also indicate the folder to be used. After you have made the selection,
click Next.
5. Select an available interface from the list. This will
create a reference to an enterprise bean that is accessed through
its local or remote interface. Note that the dependent JAR files have
to exist in the workspace as a Java 2 Platform Enterprise Edition
utility. You can further filter the list of available interfaces using
the All, Remote, or Local options
from the drop-down list.
6. Provide the JNDI name (if it was not automatically discovered)
and click Next or click Finish to
create the EJB import service.
7. If the creation of the EJB import service failed, you will
receive an error message stating Failed to generate interfaces
and business objects. Check the log file.. Review the workspace
error .log file located in %WORKSPACE%\.metadata folder
for details regarding the failure and how to fix it.

## What to do next