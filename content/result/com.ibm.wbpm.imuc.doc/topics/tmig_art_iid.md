# Migrating IBM Integration
Designer artifacts

## About this task

If you migrate the target runtime environment to IBM Business Automation
Workflow 24.x, you can run
the applications that you previously deployed, even if you do not migrate Integration Designer or
WebSphere
Integration Developer. However, if you want to edit the applications, you must also migrate Integration Designer or
WebSphere Integration Developer to a compatible version so the major versions of the two
products match.

Instead of migrating the source artifacts individually, you should import your
existing projects into a new workspace after you install.

- Migrating source artifacts

IBM Integration Designer source artifact migration refers to the process of importing a project interchange (PI) created in an older version of IBM Integration Designer or WebSphere Integration Developer into a newer version of IBM Integration Designer.
- Migrating generated Java EE staging projects

When you import a project interchange file that contains modules from a previous version of IBM Integration Designer or WebSphere Integration Developer, a migration wizard is automatically launched in IBM Integration Designer 24.x. If the project interchange file contains any generated Java Platform, Enterprise Edition staging projects (such as EJB, Web, or App projects), the migration wizard contains a page to help you migrate the projects.
- Migrating server runtime targets

When you import a project interchange file that contains modules from a previous version of IBM Integration Designer or WebSphere Integration Developer, a migration wizard is automatically launched in IBM Integration Designer 24.x. If the project interchange file contains any projects that target a previous version of the server runtime, the migration wizard contains a wizard page that enables you to automatically update the projects to target the current server runtime of Integration Designer.
- Considerations for the IBM Integration Designer migration process

When you migrate from a previous version of Integration Designer or WebSphere Integration Developer to IBM Integration Designer 24.x, most of the migration is done automatically. However, there are a number of considerations to be aware of that might require additional manual configuration.