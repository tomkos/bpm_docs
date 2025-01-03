# Exporting solution assets

Use Workflow Center or Case administration client to migrate Business Automation Workflow solutions.

To export legacy solutions that haven't been promoted to IBM® Business Automation
Workflow, you must use the Case administration client.

To export case solution projects, or promoted solutions, you must use Workflow Center to
export a snapshot
.twx or .zip package.

- Exporting solution assets from a design object store

You can use Workflow Center or Case administration client to export solution assets from the design object store. This export process creates a solution package that contains all the assets that were created for the solution in Case Builder.
- Exporting solution assets from a version control system (VCS)

If you delivered solution assets to a version control system (VCS), you can use the delivery label to export the solution assets and solution manifest from the VCS. You then can migrate and deploy the solution assets to a new environment.
- Exporting the security configuration

Security configuration settings are contained within a package file that is dedicated to security configuration. To transfer these settings between environments, use the security configuration wizards for export and import that are found in the administration client. For instance, you can develop and validate your security configuration in a test environment. To do so, run the security configuration wizard for export, and then, import the security configuration package file into the production environment.
- Exporting the audit configuration

If you configure auditing for a solution, you can view and analyze the case history for the solution. You can transfer audit configuration settings between environments by using the audit configuration wizards available in the Case administration client. Create and verify your audit configuration in a test environment. Then use the audit configuration wizard to export the settings and import them into the production environment.