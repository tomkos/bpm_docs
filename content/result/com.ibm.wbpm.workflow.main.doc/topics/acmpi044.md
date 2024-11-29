<!-- image -->

<!-- image -->

<!-- image -->

# Development and production environments

## Development environment

The development environment is typically in a dedicated FileNet P8 domain and includes a design object store where
solutions are stored. You use Case Builder
to define solutions, which are then saved and versioned in the design object store. After you design
a solution, you deploy the solutions into a target environment, and then you can use Case Client to do basic functional testing of your solution
and to customize the user interface.

In addition, the development environment uses project areas in the design object store to isolate
the effects of resetting the test environment. Each project areas has its own target object store
and Content Platform Engine region.

<!-- image -->

## Test environment

The test environment is
for testing the solutions that were created in the development environment.
You might have multiple test environments, for example a performance
testing environment and a pre-production testing environment.

Your test environment can be in a different FileNet P8 domain or in the same FileNet P8 domain as the development environment, but with a
different set of object stores to use for the staging and target object stores. There are no project
areas used in the test environment. Solutions built in the development environment are imported into
the test environment.

<!-- image -->

FileNet Deployment
Manager and other tools are used to migrate
assets that are not managed by IBM Business Automation
Workflow
tools. IBM Workflow
Center interacts with the
solutions in the design object store by using case APIs. The workflow project is exported as a
.zip file from Workflow Center
and, using either online or offline deployment, you import and deploy to IBM Workflow
Server.

## Production environment

The production environment is where your solution is deployed into production for case workers to
process cases.

Your production environment is in a different FileNet P8 domain. In your production environment, you need a
single staging object store where solutions are imported to and deployed from. You also need target
environments to deploy your solutions to. You can deploy many solutions into a single target
environment. Ensure that you have enough system resources for the number of cases that you
anticipate having in each database.

<!-- image -->

FileNet Deployment
Manager can be used to move any assets that
are not created in IBM Business Automation
Workflow between the
FileNet P8 object stores in the production
environment. Workflow Center interacts with the
solutions in the design object store by using case APIs. The workflow project is exported as a
.zip file from Workflow Center
and, using either online or offline deployment, you import and deploy to Workflow Server.

## Required databases and object stores

- The FileNet P8 Global Configuration Data (GCD)
database for each FileNet P8 domain.
- The database for the case management design object store.
- The databases for the target environments. A target environment
consists of one target object store and its associated workflow system.
The target object store and its associated workflow system are collocated
in the target environment database. You can have multiple target environments
in a test and production domain.
- A case history store to record extended case history data.
- A database for IBM Content
Navigator.

You can create new object stores to use with IBM Business Automation
Workflow. You can also take advantage of the documents
and objects that are already contained in an object store by designating an existing object store as
your target object store.