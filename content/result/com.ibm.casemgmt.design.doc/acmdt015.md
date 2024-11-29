# Setting up project areas

## About this task

You can define project areas to limit the effects of resetting the test environment because you
might have multiple users in the development environment on multiple projects. The design object
store can have multiple project areas, and each project area corresponds to one test environment.
When you have project areas set up and you reset the test environment from Case Builder, only a single project area is
reset. The entire design object store is not affected, and other Case Builder users who are working on
solutions in the same design object store can continue working without interruption.

For example, you might be a solution provider and have a credit card processing solution that is
ready to test. You also have an insurance solution in your development environment that is still
under development. You can assign the credit card processing solution to a project area so that you
can reset the test environment. When you are done testing, work on the insurance solution that is in
development is not interrupted.

You can assign specific solutions and users to each project area. Users can define and modify
solutions only in the project area that they are assigned to. Users who are not assigned to a
project area cannot log in to Case Builder. Users with access to the
development system are automatically assigned to the default project area.

- You can enter your own connection definition name when you define a regular project area. The
default project area has a predefined connection definition name that you cannot change.
- You can assign user groups to the default project area, but you can assign only individual users
to a regular project area.
- When a user logs on to Case Builder, the user is directed to the
regular project area that they are assigned to. If you want the user to go directly to the default
project area when they log on to Case Builder, you must remove the user from
the regular project area.

While creating the case solution by using Workflow Center or ,
you can select the project area to which the Case Solution belongs. You can use the
project area selection option in the home page to select the project areas
from which the project case solutions are to be displayed in Workflow Center or .

If you used FileNet® Deployment
Manager to
import a legacy solution, the solution is assigned to a default project area, and you cannot see the
legacy solution in Case Builder.
You can use the Case administration client,
or the Manage Project Areas wizard in the Case configuration tool, to assign the solution
to your preferred project area.

- Planning for project areas

Your development environment should have one default project area and zero or more secondary project areas. As you plan your project areas, ensure that you assign the appropriate user privileges when you create the target object store.
- Planning for target environments

Your test environment and production environment each contain one staging object store and typically, multiple target environments. Each target environment consists of one target object store and its associated workflow system, and a shared or dedicated IBM® Content Navigator desktop onto which the target environment is registered.
- Creating a target object store

You must create a target object store for each project area.
- Defining project areas

You can define new, non-default project areas, assign solutions and users to a project area, and remove project areas.
- Managing project areas

Manage project areas and users so that users who are working on different projects in the same environment can do so without interruption.
- Planning for shared or dedicated desktops

You can use a shared desktop to host multiple target environments and solutions. Or you can create extra desktops in IBM® Content Navigator to separate and partition target environments and solutions.
- Configuring case integration

When you are defining a new case project area or target environment, you need to configure case integration with Business Automation Workflow.