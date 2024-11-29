<!-- image -->

# Configurations page of the integration test client

<!-- image -->

- 1 Configurations
area
- 2 Control area
- 3 General Properties
- 4 Detailed Properties

## Configurations area

The
Configurations area provides a tree view of your test configurations
and test bucket configurations.

For any given test configuration,
the following information is shown:

- The name of the test configuration.
- The name and version of the process application or toolkit.
- The names of the modules in the test configuration.
- The names of any emulators in each test configuration module.
- The names of any monitors in each test configuration module.

For any given test bucket configuration, one or more of the
following is shown:

- The name of the test bucket configuration.
- The name of the test suite in the test bucket configuration.
- The names of the test cases in the test suite.
- The name of the test configuration in the test suite.
- The name and version of the process application or toolkit.
- The names of the modules in the test configuration.
- The names of any emulators in each test configuration module.
- The names of any monitors in each test configuration module.

In the Configurations area, emulators for references have
the following naming convention:

ComponentName.referenceName

By
comparison, emulators for components have the following naming convention:

ComponentName

And
monitors have the following naming convention:

SourceComponentName.referenceName
- ComponentName

## Control area

| Icon               | Description                                                                                                                                                                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Add                | Opens the New Configuration wizard, with which you can add one of the following test configuration elements to the Configurations page: Test bucket configuration Test configuration Test case process application or toolkit Module Emulator Monitor |
| Remove             | Removes selected test configuration elements from the Configurations page.                                                                                                                                                                            |
| Save Configuration | Opens the Save Configuration window, where you can save test configurations to a test configuration file.                                                                                                                                             |
| Load Configuration | Opens the Load Configuration window, which you can use to load saved test configurations from a test configurations file.                                                                                                                             |
| Save Test Client   | Opens the Save Test Trace window, with which you can save the test trace.                                                                                                                                                                             |

## General Properties

The General
Properties area provides the name and description (if any) of any
test configuration element selected in the Configurations area.

## Detailed Properties

The Detailed
Properties area displays the specific properties of any test configuration
element that is selected in the Configurations area.

<!-- image -->

The Detailed Properties area also contains
a User ID display field and a Logout button.
If security is enabled for your test client server and you have logged
in using a user ID, the User ID field displays
the user ID for the test configuration that is selected in the Configurations
area. You can use the Logout button to manually
log out of the login session.

<!-- image -->

<!-- image -->

<!-- image -->