<!-- image -->

# Creating task templates and task instances at run time

## About this task

You might want to do this, for example, when the task
definition is not available when the application is deployed, the
tasks that are part of a workflow are not yet known, or you need a
task to cover some ad hoc collaboration between a group of people.

You
can model ad hoc To-do or Collaboration tasks by creating instances
of the com.ibm.task.api.TaskModel class, and using
them to either create a reusable task template, or directly create
a run-once task instance. To create an instance of the TaskModel class,
a set of factory methods is available in the com.ibm.task.api.ClientTaskFactory factory
class. Modeling human tasks at run time is based on the Eclipse Modeling
Framework (EMF).

## Procedure

1. Create an org.eclipse.emf.ecore.resource.ResourceSet using
the createResourceSet factory method.
2. Optional: If you intend to use complex message
types, you can either define them using the org.eclipse.xsd.XSDFactory
that you can get using the factory method getXSDFactory(), or directly
import an existing XML schema using the loadXSDSchema factory
method . To make the complex types available to the Workflow Server, deploy
them as part of an enterprise application.
3. Create or import a Web Services Definition Language (WSDL)
definition of the type javax.wsdl.Definition.  You can
create a new WSDL definition using the createWSDLDefinition method.
Then you can add it a port type and operation. You can also directly
import an existing WSDL definition using the loadWSDLDefinition factory
method.
4. Create the task definition using the createTTask factory
method. If you want to add or manipulate more complex
task elements, you can use the com.ibm.wbit.tel.TaskFactory class
that you can retrieve using the getTaskFactory factory
method .
5. Create the task model using the createTaskModel factory
method, and pass it the resource bundle that you created in the step
1 and which aggregates all other artifacts you created in the meantime.
6. Optional: Validate the model using the TaskModel validate method.

## Results

- Creating runtime tasks that use simple Java types

This example creates a runtime task that uses only simple Java types in its interface, for example, a String object.
- Creating runtime tasks that use complex types

This example creates a runtime task that uses complex types in its interface. The complex types are already defined, that is, the local file system on the client has XSD files that contain the description of the complex types.
- Creating runtime tasks that use an existing interface

This example creates a runtime task that uses an interface that is already defined, that is, the local file system on the client has a file that contains the description of the interface.
- Creating runtime tasks that use an interface from the calling application

This example creates a runtime task that uses an interface that is part of the calling application. For example, the runtime task is created in a Java snippet of a BPEL process and uses an interface from the process application.
- Developing client applications for work baskets and business categories

A set of EJB APIs is provided with the feature pack so that you can develop customized clients for interacting with work baskets and business categories. Client applications access the appropriate session enterprise bean through its home interface.