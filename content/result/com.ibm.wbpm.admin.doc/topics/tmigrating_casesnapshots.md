# Migrating case snapshots and related process instances

You can migrate process instances and snapshot data for case projects in line
with the traditional Business Automation Workflow process
applications.

- Process instances that originate in case activities have a reference to the case and activity
content objects that are represented as business objects on Business Automation Workflow processes.
- During process migration, the updates to the content object models on the case side apply to
process instances, much like the changes to process variables, along with the changes on the process
model.

## Enabling case instance migration

- If you are in an on-premises environment, add the following snippet to
100Custom.xml in your environment: <server>
  <case-instance-migration-enabled>true</case-instance-migration-enabled>
</server>
- If you are in a container environment, make the following changes: After the case instance migration is enabled inside 100Custom.xml andthe server is restarted, you need to follow the steps in the 'Snapshot and processinstance migration' section:
    - Review your CR and figure out the value of your custom secret name pointed by
lombardi\_custom\_xml\_secret\_name key.
    - Edit the secret, make sure that you have the following key value pair added to the secret with
key name as sensitiveCustomConfig and value as the following XML
snippet. <properties>
   <server>
    <!-- custom properties here -->
    <case-instance-migration-enabled>true</case-instance-migration-enabled>
   </server>
</properties>
    - An administrator needs to complete all the required steps as described in: Snapshot and process instance migration
    - Start the instance migration by using Migrate Inflight Data option in the
Process Admin Console as described in:  Migrating process instances and snapshot data

## Testing the case instance migration in your development environment

Workflow Center

now has a new feature for case projects that enables the testing and debugging of instance migration
from a source snapshot to a target snapshot.

A new Play feature has been added to snapshots, which allows Case Client to be opened in the context
of a given snapshot. To access the Play button:

In the development environment, go to the Snapshots list of a case solution
select the Overflow menu and click Play.

While creating a process instance belonging to a specific snapshot, this feature enables you to
test its behavior before the actual migration. You can then create case instances and underlying
activities in the context of that snapshot in the development environment, rather than creating
process instances in the tip version of the project.