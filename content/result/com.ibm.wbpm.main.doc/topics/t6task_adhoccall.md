<!-- image -->

# Creating runtime tasks that use an interface from the calling application

## About this task

## Procedure

1. Access the ClientTaskFactory and create a resource set to contain
the definitions of the new task model. ClientTaskFactory factory = ClientTaskFactory.newInstance(); 

// specify the context class loader so that following resources are found
ResourceSet resourceSet = factory.createResourceSet
              ( Thread.currentThread().getContextClassLoader() );
2. Access the WSDL definition and the descriptions of your operations.
Specify the path within the containing package JAR file. 
Definition definition = factory.loadWSDLDefinition( resourceSet, 
                          "com/ibm/workflow/metaflow/interface.wsdl" ); 
                      PortType portType = definition.getPortType( 
                      new QName( definition.getTargetNamespace(), "doItPT" ) );
Operation operation = portType.getOperation
                                  ("doIt", (String)null, (String)null);
3. Create the EMF model of your new human task. If you
are creating a task instance, a valid-from date (UTCDate) is not required.
TTask humanTask = factory.createTTask( resourceSet, 
                                       TTaskKinds.HTASK\_LITERAL, 
                                       "TestTask", 
                                       new UTCDate( "2005-01-01T00:00:00" ), 
                                       "http://www.ibm.com/task/test/", 
                                       portType, 
                                       operation );This
step initializes the properties of the task model with default values.
4. Modify the properties of your human task model. // use the methods from the com.ibm.wbit.tel package, for example,
humanTask.setBusinessRelevance( TBoolean, YES\_LITERAL );

// retrieve the task factory to create or modify composite task elements
TaskFactory taskFactory = factory.getTaskFactory();

// specify escalation settings
TVerb verb = taskFactory.createTVerb();
verb.setName("John");

// create escalationReceiver and add verb
TEscalationReceiver escalationReceiver = 
                    taskFactory.createTEscalationReceiver();
escalationReceiver.setVerb(verb);

// create escalation and add escalation receiver 
TEscalation escalation = taskFactory.createTEscalation();
escalation.setEscalationReceiver(escalationReceiver);
5. Create the task model that contains all the resource definitions.
TaskModel taskModel = ClientTaskFactory.createTaskModel( resourceSet );
6. Validate the task model and correct any validation problems that
are found. ValidationProblem[] validationProblems = taskModel.validate();
7 Create the runtime task instance or template. Usethe HumanTaskManagerService interface to create the task instance or the tasktemplate. You must provide an application name that contains the data typedefinitions so that they can be accessed.
    - The following snippet creates a task instance:task.createTask( taskModel, "WorkflowApplication", "HTM" );
    - The following snippet creates a task template:task.createTaskTemplate( taskModel, "WorkflowApplication" );

## Results

If a runtime task instance is created, it can now be started. If
a runtime task template is created, you can now create task instances from
the template.