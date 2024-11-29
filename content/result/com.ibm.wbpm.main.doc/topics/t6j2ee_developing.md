<!-- image -->

# Developing EJB client applications for BPEL processes and human
tasks

## About this task

- Manage the lifecycle of processes and tasks from starting them
through to deleting them when they complete
- Repair activities and processes
- Manage and distribute the workload over members of a work group

- BusinessFlowManagerService interface provides the methods for
BPEL process applications
- HumanTaskManagerService interface provides the methods for task-based
applications

For more information on the EJB APIs, see the Javadoc
in the com.ibm.bpe.api package and the com.ibm.task.api package.

The
following steps provide an overview of the actions you need to take
to develop an EJB client application.

## Procedure

1. Decide on the functionality that the application is to
provide.
2. Decide which of the session beans that you are going to
use. Depending on the scenarios that you want to implement
with your application, you can use one, or both, of the session beans.
3. Determine the authorization authorities needed by users
of the application.  The users of your application must
be assigned the appropriate authorization roles to call the methods
that you include in your application, and to view the objects and
the attributes of these objects that these methods return. When an
instance of the appropriate session bean is created, WebSphere® Application
Server associates
a context with the instance. The context contains information about
the caller's principal ID, group membership list, and roles. This
information is used to check the caller's authorization for each call. 
The
Javadoc contains authorization information for each of the methods.
4. Decide how to render the application. The
EJB APIs can be called locally or remotely.
5 Develop the application.
    1. Access the EJB API.
    2 Use the EJB API to interact with processes or tasks.
        - Query the data.
        - Work with the data.

- Accessing the EJB APIs

The Enterprise JavaBeans (EJB) APIs are provided as two stateless session enterprise beans. BPEL process applications and task applications access the appropriate session enterprise bean through the home interface of the bean.
- Developing applications for BPEL processes

A BPEL process is a set of business-related activities that are invoked in a specific sequence to achieve a business goal. Examples are provided that show how you might develop applications for typical actions on processes.
- Developing applications for human tasks

A task is the means by which components invoke humans as services or by which humans invoke services. Examples of typical applications for human tasks are provided.
- Developing applications for BPEL processes and human tasks

People are involved in most business process scenarios. For example, a business process requires people interaction when the process is started or administered, or when human task activities are performed. To support these scenarios, you need to use both the Business Flow Manager API and the Human Task Manager API.
- Handling exceptions and faults

A BPEL process might encounter a fault at different points in the process.