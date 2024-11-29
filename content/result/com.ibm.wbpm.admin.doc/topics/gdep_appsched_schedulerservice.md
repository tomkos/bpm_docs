<!-- image -->

# Administering the Application Scheduler

Additionally, you can generate scheduler entries during the migration of a
WebSphere® InterChange Server repository that includes
WebSphere InterChange Server scheduler entries. (See the
topic on Migrating from WebSphere InterChange Server).
Use the Application Scheduler panel in the administrative console to administer these migrated
scheduler entries as well.

In a stand-alone server environment, the Application Scheduler is automatically installed. When
you create the stand-alone server profile, the Application Scheduler is installed and configured on
that server.

In a Network Deployment environment, the Application Scheduler is automatically installed for
every managed server and cluster member created; no additional action is needed.

In WebSphere InterChange Server, an
application that contained collaboration objects or connectors could be started, paused, and stopped
at the component level (that is, a component could be stopped while the remainder of the application
was allowed to continue). In IBM Business Automation Workflow,
scheduling of events is provided through the Application Scheduler. The Application Scheduler allows
you to start and stop processes at the application level.