# Setting up target environments

## About this task

In test and production environments, you deploy solutions in target environments. The first time
that you run the Case configuration tool to configure the
production environment after you install IBM® Business Automation
Workflow, you must define and register at least one target environment. Later, you can use the Case administration client to define additional target environments
iteratively as needed to support your solutions.

You can deploy one solution or many
solutions into a single target environment. Ensure that you have enough
system resources for the number of cases that you anticipate having
in each database.

For the simplest configuration, deploy all
of your solutions in a single target environment. In this configuration,
all of the solutions share a single Content Platform Engine target object store
and a single workflow system.

To separate the workload among
databases, you can deploy each solution or a few solutions into a
separate target environment. In this configuration, each solution
or group of solutions is provided with a dedicated Content Platform Engine target object store
and workflow system. This configuration provides data separation between
the solutions, which allows for greater flexibility in database operations,
database maintenance, and assigning security privileges.

If
you configure multiple test and production environments, and you configure
multiple IBM
FileNet® P8 domains,
ensure that each target environment is on the same domain as its corresponding
staging object store.

It is a best practice to
create a case management master group to use for assigning access to object stores at the time that
you create the object store. Give this group Use object store permission. You
can grant new users access to the object store by adding them to the master group. This approach can
prevent issues with changing security on an established object store.

- Creating or upgrading a target object store for test or production environments

A target object store is required for each target environment in the test and production domains.
- Creating custom desktops

You can use extra desktops in IBM Content Navigator to group target environments and solutions. This approach makes it possible to separate groups of solution users that are based on roles, organizations, or location.
- Defining and registering target environments

You can define target environments for a test environment or production environment by using the Case configuration tool or the Case administration client. After you define a target environment definition, you must register it before you can use it.
- Configuring Case integration for target environment

When you are defining a new target environment for a production environment, you need to configure Case integration against the object store that is associated with the target environment.
- Managing target environment definitions

Use the Case administration client to view and edit properties that were defined for a target environment or to delete a target environment definition.
- Indexing event logs for older case types to enable case health analysis of work items

Business Automation Workflow obtains information about overdue work items for a case type from the Content Platform Engine event logs. After you configure the target object store in your environment, the event logs for the case types are automatically indexed in new solutions. For solutions that were created before you configured the target object store, you must manually index the event log for each case type in your existing solutions and for any case types you subsequently add to the solutions. If you do not index the event logs, no work item analysis is done for these case types.