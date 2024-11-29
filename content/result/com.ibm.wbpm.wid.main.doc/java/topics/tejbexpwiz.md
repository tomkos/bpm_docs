<!-- image -->

# Creating EJB exports using the external service wizard

You can use the external service wizard in IBM® Integration
Designer to
create an EJB export. The external service wizard is a tool used to
create services based on criteria that you provide. It then generates
business objects, interfaces, and import files based on the services
discovered.

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
For EJB exports, select the Inbound processing
option for the direction of binding processing to be used at run time.
After you have made the selection, click Next.
4. Select the module where the generated artifacts should
be saved. You can select an existing module from the drop-down list,
or create a new one by clicking New. After
you have made the selection, click Next.
5. Select an interface to base the binding on by clicking Browse.
From the interface selection window that opens, you can select from
a list of existing interfaces (note that you can sort this list by
using the Show WSDL and Java, Show
WSDL, and Show Java radio buttons).
Or, you can create a new WSDL or Java interface by clicking New.
After you have made the selection, click Next.
Note that if a Java interface is selected, it must be a business interface
and cannot be an EJB local, remote or home interface.
6. From this window, decide whether to create an EJB client
JAR module containing the client interfaces and classes that will
be generated for use in a Java platform application.  Click New to
create a new module, or select an existing one from the drop-down
list. If you decide not to create an EJB client JAR module at this
time, you can create it later from the EJB export binding menu (right-click
the EJB export and select Generate EJB Client Interface).
7. Using the check boxes, indicate if the interfaces in the
EJB client JAR module will be remote or local EJB 3.0 interfaces or
remote EJB 2.1 interfaces.
8. Click Finish to create the EJB export.

## What to do next