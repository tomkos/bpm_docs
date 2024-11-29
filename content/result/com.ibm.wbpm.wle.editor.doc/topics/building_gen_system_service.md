# Building a General System service in the desktop Process Designer (deprecated)

## Before you begin

General system services are likely to be called directly
from a BPD or from a Human Service. General System services can include
only basic service components, such as scripts, and cannot contain
Coaches or integration steps (Web Service integration, Java integration,
or Content integration). General System services can be nested within
any other type of service.

## Procedure

To create a General System service, perform the following
steps.

1. Open the desktop Process Designer.
2. Open a process application in the Designer view.
3. Click the plus sign next to Implementation,
and then click General System Service.
4. In New Service, enter a name for
the service and click Finish. IBM Process
Designer displays
the diagram of the service with the default Start Event and End Event
components.
5. If you do not want to automatically synchronize shared business objects that are inputs to this
service when the business object is changed in other instances, switch to
Overview and clear Automatically sync shared business
objects.

Important: Nested services inherit the synchronization behavior of the starting service.
In addition, if you have a service that runs custom logic and then explicitly saves your shared
business objects, always clear the automatic synchronization option. Otherwise, the shared business
object is automatically saved and the code in your service will not run.