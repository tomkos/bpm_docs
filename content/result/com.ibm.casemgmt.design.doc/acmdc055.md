# Importing the security configuration

## About this task

- The security configuration might be defined entirely by using the Case administration client to create a security
configuration package.
- The security configuration might be partially defined by using the Case administration client and partially defined by
applying manual steps.
- The security configuration might be entirely defined by manual steps without using the Case administration client.

When a solution is deployed into a test or production environment, the business analyst or
solution developer often assists with designing the security configuration for the test or
production environment. For assistance with configuring security, the solution administrator can
also consult the customized migration and deployment instructions that were developed for migrating
the solution application package.

If the Case administration client was used to implement the
security configuration design, security configuration settings are stored in a security
configuration package file. You can move this file from one environment to another by using the
export and import security configuration wizards in the Case administration client . For example, you can
create and check your security configuration in a test environment, run the export security
configuration wizard, and then import the security configuration package file into
production.

If you manually set up the security configuration for the solution, then you must
manually reapply the security configuration in the target environment. You cannot use this procedure
to import and apply the security configuration.

## Procedure

To import the security configuration package file:

1. Start the Case administration client.
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
where
server is the IBM® Content
Navigator IP address or
fully qualified server name, and 
port is the
IBM Content
Navigator port
number.
2. In the navigation tree in the left pane, select a design
object store and click Solutions.
3. On the Solutions page, click Actions > Import > Security
Configuration, browse to the exported security
configuration package file, and complete the wizard steps.
4. After you import the file, view the security configuration
to ensure that it is correct for the target environment.
5. Apply the security configuration to the deployed solution.