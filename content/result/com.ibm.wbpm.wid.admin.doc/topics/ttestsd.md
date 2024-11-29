<!-- image -->

# Using Ant scripts for testing in headless IBM Workflow
Server

## About this task

Although headless IBM Workflow
Server 
is the recommended test environment, there are several kinds  of artifacts
that cannot be successfully tested in this environment  and you should
use headless IBM Integration
Designer instead.
 These artifacts are described in the "Limitations" topic.

The
 following topics describe how to use Ant scripts for testing in the
 headless environment of IBM Business Automation
Workflow:

- Overview of testing with Ant scripts in headless IBM Business Automation Workflow

If you have created component test projects, test suites, and test cases in IBM Integration Designer, you can use Ant scripts in conjunction with the serviceDeploy and wsadmin tools to automatically build, deploy, and test your projects in the headless (command line) batch processing environment of IBM Business Automation Workflow.
- Populating CVS with the required artifacts

If you are using CVS as your team repository, you need to ensure that the repository contains the required artifacts to support batch processing of component test projects before you can build, deploy, and test the projects in a headless batch processing environment.
- Configuring an Ant script

An Ant script is used to initiate several tasks in the batch processing of component test projects, such as the building, deploying, and testing of the projects. You can create your own Ant script or modify the one that is displayed in this topic. By convention, the Ant script is named build.xml.
- Running the Ant script

When you have finished configuring the Ant script, you are ready to run it.
- Viewing the XML output file

When you finish your component testing, an XML output file is generated. You can view the XML output file to determine the results of your testing and see what tests cases passed or failed. The output file lists the tests that passed and failed and provides the start and stop times, which helps you spot performance problems. The start time and stop time of the entire test suite and each test case is listed in microseconds. These start and stop times are helpful in diagnosing applications with performance problems, such as a lengthy time period linked to a specific function that is a possible source of a bottleneck.
- Additional servlet tasks

The servlet interface enables you to query test suites and test cases and run whole tests, partial tests, and specific test cases. The servlet is generated into the web project of the component test project. The servlet APIs can be incorporated in the script or used on a stand-alone basis. If used on a stand-alone basis, the application must be already deployed and the server running.
- Examples of files used in batch component testing

Several different types of files are typically used to perform batch processing of component test projects in a command-line environment, such as Ant scripts and XSD files.
- Limitations of batch testing in headless IBM Business Automation Workflow

From time to time, you may encounter some limitations in performing batch component testing in the headless environment of IBM Business Automation Workflow. In many situations, you can successfully work around these limitations.