<!-- image -->

# BusinessFlowManagerService interface

The methods that can be called by the BusinessFlowManagerService
interface depend on the state of the process or the activity and the
authorization of the person that uses the application containing the
method. The main methods for manipulating BPEL process objects are
listed here. For more information about these methods and the other
methods that are available in the BusinessFlowManagerService interface,
see the Javadoc in the com.ibm.bpe.api package.

## Process templates

A process template is
a versioned, deployed, and installed process model that contains the
specification of a BPEL process. It can be instantiated and started
by issuing appropriate requests, for example, sendMessage().
The execution of the process instance is driven automatically by the
server.

| Method                | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| getProcessTemplate    | Retrieves the specified process template.                    |
| queryProcessTemplates | Retrieves process templates that are stored in the database. |

## Process instances

The following API methods
are related to starting process instances.

| Method                     | Description                                                                                                                                                                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| call                       | Creates and runs a microflow.                                                                                                                                                                                                                     |
| callWithReplyContext       | Creates and runs a microflow with a unique starting service or a long-running process with a unique starting service from the specified process template. The call waits asynchronously for the result.                                           |
| callWithUISettings         | Creates and runs a microflow and returns the output message and the client user interface (UI) settings.                                                                                                                                          |
| initiate                   | Creates a process instance and initiates processing of the process instance. Use this method for long-running processes. You can also use this method for microflows that you want to fire and forget.                                            |
| initiateAndSuspend         | Creates a process instance but immediately suspends the further processing of the process instance.                                                                                                                                               |
| initiateAndClaimFirst      | Creates a process instance and claims the first inline human task.                                                                                                                                                                                |
| sendMessage                | Sends the specified message to the specified activity service and process instance. If a process instance with the same correlation set values does not exist, it is created. The process can have either unique or non-unique starting services. |
| getStartActivities         | Returns information about the activities that can start a process instance from the specified process template.                                                                                                                                   |
| getActivityServiceTemplate | Retrieves the specified activity service template.                                                                                                                                                                                                |

| Method               | Description                                                                                                                              |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| suspend              | Suspends the execution of a long-running, parent process instance that is in the running or failing state.                               |
| resume               | Resumes the execution of a long-running, parent process instance that is in the suspended state.                                         |
| restart              | Restarts a long-running, parent process instance that is in the finished, failed, or terminated state.                                   |
| forceTerminate       | Terminates the specified parent process instance, its subprocesses with child autonomy, and its running, claimed, or waiting activities. |
| delete               | Deletes the specified parent process instance and its subprocesses with child autonomy.                                                  |
| query                | Retrieves the properties from the database that match the search criteria.                                                               |
| queryEntities        | Uses query tables to retrieve the properties from the database that match the search criteria.                                           |
| getWaitingActivities | Returns information about the activities that are waiting for a message so that the processing of these activities can continue.         |
| migrate              | Migrates a process instance to the specified newer version of its process model.                                                         |

## Activities

For invoke activities, you can
specify in the process model that these activities continue in error
situations. If the continueOnError flag is set to false and an unhandled
error occurs, the activity is put into the stopped state. A process
administrator can then repair the activity. The continueOnError flag
and the associated repair functions can, for example, be used in a
long-running process where an invoke activity fails occasionally,
but the effort required to model compensation and fault handling is
too high.

The following methods are available for working with
and repairing activities.

| Method                                            | Description                                                                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| claim                                             | Claims a ready activity instance for a user to work on the activity.                                                                                                                                        |
| cancelClaim                                       | Cancels the claim of the activity instance.                                                                                                                                                                 |
| complete                                          | Completes the activity instance.                                                                                                                                                                            |
| completeAndClaimSuccessor                         | Completes the activity instance and claims the next one in the same process instance for the logged-on person.                                                                                              |
| forceComplete                                     | Forces the completion of the following items: An activity instance that is in the running or stopped state. A human task activity that is in the state ready or claimed. A wait activity in state  waiting. |
| forceRetry                                        | Forces the repetition of the following items: An activity instance that is in the running or stopped state. A human task activity that is in the state ready or claimed.                                    |
| forceNavigate, forceForEach, forceLoop, forceJoin | These methods force the navigation of a stopped activity.                                                                                                                                                   |
| skip                                              | Skips processing of the activity.                                                                                                                                                                           |
| jump                                              | Jumps from one activity to the other.                                                                                                                                                                       |
| query                                             | Retrieves the properties from the database that match the search criteria.                                                                                                                                  |
| queryEntities                                     | Uses query tables to retrieve the properties from the database that match the search criteria.                                                                                                              |

## Variables and custom properties

The interface
provides a get and a set method to retrieve and set values for variables.
You can also associate named properties with, and retrieve named properties
from, process and activity instances. Custom property names and values
must be of the java.lang.String type.

| Method                 | Description                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------|
| getVariable            | Retrieves the specified variable.                                                            |
| setVariable            | Sets the specified variable.                                                                 |
| getCustomProperty      | Retrieves the named custom property of the specified activity or process instance.           |
| getCustomProperties    | Retrieves the custom properties of the specified activity or process instance.               |
| getCustomPropertyNames | Retrieves the names of the custom properties for the specified activity or process instance. |
| setCustomProperty      | Stores custom-specific values for the specified activity or process instance.                |