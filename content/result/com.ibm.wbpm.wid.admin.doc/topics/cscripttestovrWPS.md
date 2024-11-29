<!-- image -->

# Overview of testing with Ant scripts in headless IBM Business Automation
Workflow

Although Ant scripts are not strictly required for running tests
in a headless batch processing environment, there are several advantages
to using them. For example, Ant scripts enable you to automatically
and simultaneously test numerous large applications that are inherently
complex or constantly changing. They also allow you to run as many
tests as you want or need in the off-hours, which reduces the load
on computing systems and enables developers to focus on development
activities when they are at work.

However, perhaps the most important reason for using Ant scripts
is that you can configure an Ant script to automatically perform multiple
tasks that would otherwise need to be performed manually, such as:

- Checking component test projects out of a team repository like
CVS.
- Zipping up the projects into a project interchange file.
- Importing the project interchange file into the IBM Integration
Designer workspace.
- Building the projects using serviceDeploy.
- Starting the server.
- Deploying the projects to the server using wsadmin.
- Running the tests using servlet tasks.
- Removing the projects from the server using wsadmin.

In WebSphere Integration Developer version 7.0 or later, component test projects are full-fledged SCA modules. This enables you to test your component test projects in the headless batch processing environment of IBM Business Automation
Workflow and use the capabilities of the serviceDeploy and wsadmin tools. If you have pre-v7.0 component test projects that you want to test in headless IBM Business Automation
Workflow, you can import them into IBM Integration
Designer and a migration wizard will be automatically launched to enable you to convert the component test projects to version 7 SCA modules.

Although headless IBM Business Automation
Workflow is the recommended test environment, there are several kinds of artifacts that cannot be successfully tested in this environment and you should use headless IBM Integration
Designer instead. These artifacts are described in the "Limitations" topic.