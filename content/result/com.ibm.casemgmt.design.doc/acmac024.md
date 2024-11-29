# Configuring case features from the command line

## About this task

Your case management system includes a development environment for creating and testing case
management solutions and a production environment for working with running case management
solutions. You must configure both environments.

Configuring
the development environment includes configuring Case Builder and Case Client. Configuring the production
environment includes configuring Case Client.

You can use the BPMConfig tool to create a profile for each development environment instance and
a profile for each production environment instance. The information for a profile is collected in
XML files in the form of properties and values that describe the associated configuration and
deployment tasks. Three XML files contain the information that is common to all tasks in the
profile, and each configuration task in the profile has one configuration XML file. Provide values
for the profile properties that are specific to each configuration at your site, such as the
application server name.

The XML files are stored in a directory that is unique to a profile. Because the profile name is
used for both the directory name and the file name of the configuration profile file, you must
provide a profile name that is a valid directory name for your operating system. By default, the
profiles are stored in the
install\_root/CaseManagement/configure/profiles directory
where install\_root is the location where IBM® Business Automation
Workflow is installed.

- Configuring the case development environment by using the command line

You must configure the development environment before you create and deploy you case solutions. You use the development environment to create, modify, and test solutions before you move them into a production environment. You can use the command line to configure the development environment.
- Adding users to the default project area by using the command line

You must add at least one user to the default project area. Users cannot log into Case Builder until they are added to a project area.
- Configuring the production environment by using the command line

You must configure the production environment before you deploy your solutions to that production environment. You configure the production environment after you configure the development environment.
- Defining and modifying project areas by using the command line

You use project areas to limit the effects of resetting the test environment. You can define new project areas, define a default project area, assign solutions and users to a project area, and remove project areas by using the command line.
- Creating a list of object store properties and document classes by using the command line

You can reuse existing Content Platform Engine properties and document classes in your case management solutions. You can use the command line to create text files that provide the information from a target object store that you need for reusing existing properties and document classes.
- Copying an existing case solution by using the command line

You can copy an existing solution to quickly begin designing a new solution that is based on the existing solution. You can use the command line to create the copy.
- Creating a solution from a template by using the command line

You can create a solution that is based on a solution template to quickly begin designing a new solution. The template provides a basic design for your solution, and you can customize the new solution later in Case Builder. You can use the command line to create the solution. Your administrator determines the templates that are available in an object store.
- Converting a solution to a template by using the command line

You can convert a solution to a template by using the command line. You use templates to quickly create new solutions that are based on the same design as the template. The template contains all the solution design information, but you cannot edit a template directly or create running cases from a template.
- Exporting a case solution package by using the command line

You must export the case management solution package from the development environment domain before you can move the solution to the production environment domain. You can use the command line to export the solution package.
- Importing a case solution package by using the command line

You must import the case management solution package into the production environment design object store before you can deploy the solution to the production environment domain.
- Importing a solution from a manifest by using the command line

You can deploy an IBM Business Automation Workflow Case solution from a version control system (VCS) into a production environment or a different development environment. You must first extract the solution manifest from the VCS. You then use this manifest to import the solution into the design object store in the new environment before you can deploy the solution to the environment domain.
- Generating the object store data map by using the command line

Generate the object store data map for mapping the object stores that are contained in a solution package to the appropriate object stores in the target environment.
- Creating and enabling a Case Analyzer store by using the command line

You must create and enable a Case Analyzer store if you want to use IBM Case Monitor Dashboard. The createCaseAnalyzerStore command creates and enables the event export store for the IBM Case Monitor Dashboard.
- Creating and enabling a case history store by using the command line

You must create and enable an event export store if you want to use extended case history features. For example, if you want to view the progression of a case over time by using the Timeline Visualizer widget, you must create and enable a case history store.
- Applying a security configuration by using the command line

After you create a security configuration by using the IBM Business Automation Workflow Case administration client , you can apply the security configuration by using the command line. You must specify a target environment if the solution is in a production environment.
- Exporting a security configuration by using the command line

You must export the case management security configuration from one domain (such as the   testing or development environment) before you can move the security configuration to another   domain (such as the production environment). You can use the command line to export one or more   security configurations.
- Importing a security configuration by using the command line

If you exported the security configuration package file for a solution when you migrated   the solution package, import the file after you deploy the solution in the target environment to   apply the security settings to the solution. You can use the command line to import the security   configuration package.
- Applying an audit configuration by using the command line

After you create an audit configuration by using the IBM Business Automation Workflow Case administration client , you can apply the audit configuration by using the command line. You must specify a target environment if the solution is in a production environment.
- Exporting an audit configuration by using the command line

You must export a case management audit configuration from one domain (such as the testing or development environment) before you can move the audit configuration to another domain (such as the production environment). You can use the command line to export one or more audit configurations.
- Importing an audit configuration by using the command line

If you exported the audit configuration package file for a solution when you migrated   the solution package, import the file after you deploy the solution in the target environment to   apply the audit settings to the solution. You can use the command line to import the audit   configuration package.