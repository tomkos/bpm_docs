# Migrating artifacts

- If you are migrating from IBM Business Process Manager
 Enterprise
Service Bus or migrating from an AdvancedOnly deployment environment, you don't need to migrate
IBM Workflow
Center.
- If you are migrating from IBM Business Process Manager
Standard or IBM Business Process Manager
Express or a Standard
deployment environment, you don't need to migrate IBM Integration
Designer artifacts.

1. Install and configure a new environment as the target for the artifact migration. This
environment can run while also running the source environment.
2 Import and migrate the applications from the source environment.
    - For snapshot content, see Migrating Process Center artifacts.
    - For advanced content, see Migrating IBM Integration Designer artifacts.
3. Optional: Update the migrated applications to use new capability that is delivered in IBM Business Automation Workflow
24.x.
4. Manually deploy the migrated applications from the development tools to the target
environment.
5. Optional: Run both environments in parallel so that business process instances
and human task instances that are in progress finish in the source environment and new instances
start in the target environment. In some cases, you can use IBM Process Federation
Server to get one view
of your tasks.
6. Shut down and remove the source environment when it is no longer needed.

1. Import the project interchange file into Integration Designer.
2. From the Project menu, select Business Integration Projects and click Regenerate Deploy Code and Reinstall on Servers.
3. Select Regenerate XSLT files for XML maps. Leave Clean projects selected as default.
4. Click OK to start the regeneration process (this may take some time). Once complete, re-deploy your module with the updates.

- Installing IBM Business Automation Workflow for artifact migration

Before you begin artifact migration, install and configure IBM Business Automation Workflow 24.x on a different computer, or in a different directory on the same computer as your previous version.
- Migrating Workflow Center (previously Process Center) artifacts

You can export artifacts from previous versions of Workflow Center (Process Center) and import them into your new version.
- Migrating IBM Integration Designer artifacts

You can migrate artifacts from previous versions of IBM Integration Designer or WebSphere® Integration Developer to IBM Integration Designer 24.x. Migrating to IBM Integration Designer 24.x preserves the basic structure of your existing applications with minimal required reconfiguration.

## Related information

- Deprecated and removed features of IBM Business Automation Workflow