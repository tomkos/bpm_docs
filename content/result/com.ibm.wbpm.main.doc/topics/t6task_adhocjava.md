<!-- image -->

# Creating runtime tasks that use simple Java types

## About this task

## Procedure

1. Access the ClientTaskFactory and create a resource set to contain
the definitions of the new task model. ClientTaskFactory factory = ClientTaskFactory.newInstance(); 
ResourceSet resourceSet = factory.createResourceSet();
2. Create the WSDL definition and add the descriptions of your operations.
// create the WSDL interface
Definition definition = factory.createWSDLDefinition
         ( resourceSet, new QName( "http://www.ibm.com/task/test/", "test" ) );
    
// create a port type
PortType portType = factory.createPortType( definition, "doItPT" );

// create an operation; the input and output messages are of type String: 
// a fault message is not specified
Operation operation = factory.createOperation
        ( definition, portType, "doIt", 
          new QName( "http://www.w3.org/2001/XMLSchema", "string" ),
          new QName( "http://www.w3.org/2001/XMLSchema", "string" ), 
          (Map)null );
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
7 Create the runtime task instance or template. Usethe HumanTaskManagerService interface to create the task instance or the tasktemplate. Because the application uses simple Java types only, you do notneed to specify an application name.
    - The following snippet creates a task instance:atask.createTask( taskModel, (String)null, "HTM" );
    - The following snippet creates a task template:task.createTaskTemplate( taskModel, (String)null );

## Results

If a runtime task instance is created, it can now be started. If
a runtime task template is created, you can now create task instances from
the template.