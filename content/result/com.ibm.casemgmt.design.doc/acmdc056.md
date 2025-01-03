# Importing the audit configuration

## About this task

- The audit configuration might be defined entirely by using the Case administration client to create an audit
configuration package.
- The audit configuration might be partially defined by using the Case administration client and partially defined by
applying manual steps. For example, configuring the audited properties by using the Case administration client is sufficient for support
of the Timeline Visualizer widget to view case history. But integration with the IBM® case analytics tools typically requires additional, manual steps.
- The audit configuration might be entirely defined by manual steps without using the Case administration client.

When a solution is deployed into a test or production environment, the business analyst or
solution developer often assists with designing the audit configuration for the test or production
environment. For assistance with configuring auditing, the solution administrator can also consult
the customized migration and deployment instructions that were developed for migrating the solution
application package.

If the Case administration client was used to implement the
audit configuration design, audit configuration settings are stored in an audit configuration
package file. You can move this file from one environment to another by using the export and import
audit configuration wizards in the Case administration client . For example, you can
create and check your audit configuration in a test environment, run the export audit configuration
wizard, and then import the audit configuration package file into production.

If you manually
set up audit definitions for a solution to support workflow history and analytics extensions, then
you must manually reconfigure the audit definitions in the target environment. You cannot use this
procedure to import the audit configuration. For information, see History and analytics extensions.

## Procedure

To import the audit configuration:

1. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. In the navigation tree in the left pane, select a design
object store and click Solutions.
3. On the Solutions page, click Actions > Import > Audit
Configuration, browse to the exported audit
configuration package file, and complete the wizard steps.
4. After you import the file, view the audit configuration
to ensure that it is correct for the target environment.
5. Apply the audit configuration to the deployed solution.