# Creating or upgrading a target object store for test or production
environments

## Before you begin

## About this task

- Deployed solution folder: A folder structure for a deployed solution
in the target object store. Case instances are created under this
structure.
- Case class:  A representation for a case type in a solution.
- Document class: A representation for a type of document in a solution.
- Property template: A definition of a property type.
- Activity class: A definition of an activity type.
- Subscription: A case or activity event condition to corresponding Content Platform Engine event actions.

## Procedure

To create or upgrade a target object store for your test
or production environment:

1. For a new target environment, if you did not previously
create an object store, create one in IBM®
FileNet® P8.
For information, see Defining object stores and Creating an object store.
2. For a new target environment, if you did not previously
create a workflow system, create one now.
For information,
see Creating a workflow system.
3 For a new target environment or an upgraded target environment,convert the object store to a case management target object store.
    1. Start the IBM Business Automation
Workflow
Case administration client .
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
server
is the IBM Content
Navigator
server name or IP address.
port is the
IBM Content
Navigator port
number.
    2. In the navigation tree in the left pane, right-click
the object store, select Convert to Target Object Store,
and complete the wizard steps.

## What to do next

1. Define and register the target environment. See Defining and registering target environments.
2. Optional: If you plan to use the Timeline Visualizer widget to view case history in the
solutions that you deploy to this target environment, set up a case history store before you migrate
and deploy the solutions. See Preparing a database for the case history store and Timeline Visualizer widget.
3. Optional: If you plan to use the IBM Case Monitor Dashboard to view business activity data for
cases and activities in the solutions that you deploy to this target environment, set up a Case Analyzer store before you migrate and deploy the solutions.
4. Configure indexes for the target object store indexes. See Configuring production target object store indexes.