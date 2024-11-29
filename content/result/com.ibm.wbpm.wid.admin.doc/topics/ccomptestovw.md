<!-- image -->

# Component testing

The test suite editor is fully integrated into the workbench, which
enables you to navigate through the Business Integration view and
other views while using the editor. It is also closely integrated
with the assembly editor and you can open the assembly editor from
the test suite editor. The primary launch point for the test suite
editor is the Business Integration view. You can open multiple instances
of the test suite editor and use them to define your test suites and
test cases.

Before you work with the test suite editor and perform component
testing, you should have experience with unit testing and the integration
test client. The component testing documentation largely extends the
unit testing documentation, so you should familiarize yourself with
the topics on unit testing.

- Component test
projects
- Test suites
- Test cases
- Test variations
- Test bucket
configurations
- Events

These concepts are discussed in the following sections.

## Component test projects

A component test project is a container for test suites. Generally,
the first step in performing component testing is to create a component
test project.

In version 7.0 and later, component test projects
are created as SCA modules. You can import your 6.2x component test
projects into IBM® Integration
Designer version
7.x, the component test projects are automatically migrated to version
7.x specifications and you can test them like a version 7.x component
test project. If you used WebSphere Integration Developer version
6.2x to generate an EAR file from component test projects and other
artifacts, you can deploy and run the EAR file on IBM Integration
Designer version
7.x without performing any manual migration tasks.

## Test suites

A test suite
is a collection of one or more test cases. When you create a test
suite, you can choose from one of the following test patterns:

- Operation-level testing
- Scenario-based testing

In operation-level testing, a separate test case is
created for each operation that you select for component testing.
In scenario-based testing, a single test case is created for
all of the operations that you select for component testing.

## Test cases

You can think
of a test case as being a container for multiple operations that you
have selected for testing. Test cases enable you to automate and simultaneously
test the operations in the integration test client. Test data for
test cases is defined in the test data table, which contains a set
of named variables that can be used for either input or output in
the test case invocations.

## Test variations

A test
variation is a specific set of variable values for a test case. Although
each test case is automatically assigned a default test variation,
you can create multiple test variations for a test case that each
contain a different set of variable values. When a test case is run,
all of the test variations for the test case are run unless one of
the test variations fails.

## Test bucket configurations

A test bucket configuration is a set of specific test suites and
test cases that are run together in the same test session.

## Events

In addition to the standard
events that are generated in the integration test client when you
are unit testing, such as the Invoke and Return events, component
testing adds the following events in the integration test client:

| Event type     | Description                                                                                                                                                                                                                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Run Test       | An informational event that is generated when you select Run Test menu item from either the integration test client or the Business Integration view. The event informs you whether the component test passed or failed. It also presents statistics on the total number of test cases that were run and the number that passed, failed, or were flagged with an error. |
| Test Suite     | An informational event that informs you whether the test suite has passed or failed the test run. It also presents statistics on the total number of test cases that were run and the number that passed, failed, or were flagged with an error.                                                                                                                        |
| Test Case      | An informational event that informs you whether the test case has passed or failed the test run.                                                                                                                                                                                                                                                                        |
| Test Variation | An informational event that informs you whether the test variation has passed or failed the test run.                                                                                                                                                                                                                                                                   |

- Test suite editor

In IBM Integration Designer, the test suite editor is the designated tool for editing test suites. It features a rich user interface that enables you to easily manage your test suites and test cases. The test suite editor has been designed to closely resemble the test client, which helps you easily transition from using one tool to the other.
- Setting preferences for the test suite editor

By default, the user-definable preferences for the test suite editor are already optimized for working with test suites and test cases. However, in the course of your testing activities, you may find that you want to change some preferences.
- Getting started: Top-down testing of test cases

In component testing, you use the test suite editor and associated wizards to create and define test cases that consist of multiple operations, which enables you to automate and simultaneously test the operations in the integration test client. In top-down testing, you define test cases by selecting components and operations for testing and then you run the test cases in the integration test client. (In bottom-up testing, you use integration test client invocations to define test cases.)
- Managing test suites

IBM Integration Designer provides numerous tools for managing your test suites, such as wizards for creating component test projects and test suites and a test suite editor for editing your test suites.
- Specifying dependencies for component test projects

In WebSphere Integration Developer version 7 and later, component test projects are full-fledged SCA modules. This allows you to use the dependency editor to specify Java libraries as dependencies for component test projects. If a component test project is being used to test a module that has a dependency on an SCA library, the SCA library will automatically be displayed in the dependency editor.
- Running test suites

In IBM Integration Designer, you can select one or more component test projects, test suites, or test cases to run and test in the integration test client. For example, you can select one or more component test projects and all of the test suites and associated test cases contained in the projects will be tested. Or you can select one or more individual test suites or test cases from multiple component test projects.
- Automating tests using Ant scripts

If you want to automate your testing of component test projects, test suites, and test cases, you can use Ant scripts to invoke the headless (command line) batch processing environments of either IBM Integration Designer or IBM Workflow Server. Ant scripts enable you to automatically perform numerous tasks in batch processing environments, such as building, deploying, and testing your component test projects. The headless environments are used exclusively to perform batch processing of Integration Designer modules. You cannot use these headless environments to deploy modules contained in process applications or toolkits to either a IBM Workflow Center server or a process server on Workflow Center.
- Testing with the Component Test Explorer

The Component Test Explorer enables you to manage and run  test cases that have been deployed to either a test environment server or a stand-alone server. Much like the Business Process Choreographer Explorer, the Component Test Explorer is a web client that you can invoke and run from either inside or outside of IBM Integration Designer.
- Limitations for component testing

From time to time, you may encounter some limitations in testing components. In most situations, you can successfully work around these limitations.