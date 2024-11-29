<!-- image -->

# Overview

IBM® Integration
Designer component test projects are packaged as Java 2 Platform
Enterprise Edition web applications and they are typically deployed
to a test environment server for initial processing and debugging.
After these component test projects have been debugged, they are deployed
to a non-UTE (unit test environment) server for subsequent processing.
Typically, this server houses many test cases from many developers.

Because component test projects look just like other applications
when they are installed on a server, it can be difficult to determine
exactly what test cases are installed on a  particular server. Component
Test Explorer solves this problem with a web interface that displays
the component test projects that are on the server as well as the
associated test suites and test cases. Using Component Test Explorer,
you can select and immediately run component test cases on the server.
The results are automatically saved and displayed in the run history.
Additionally, you can schedule test cases to run periodically and
automatically save the results.

Although Component Test Explorer allows you to specify component
and human task emulators in a component test case, you need a global
emulator if the test case has not  been designed for emulation or
a resource that the test case will access is not available. Considering
the test case deployment scenario again, the server housing the test
cases might not contain all of the dependencies that are needed for
the test cases to run successfully. In this case, you can use Component
Test Explorer to create emulators that simulate the behavior of the
missing dependencies.

In another scenario, you might have test cases running on a server
that are not IBM Integration
Designer component
test cases. Therefore, the specified component or human task emulators
are not supported. For example, the test cases can be authored using
another application, but the services being invoked might require
human tasks to be completed. In this case, you can use Component Test
Explorer to create emulators for the human tasks, which allows the
test cases to complete successfully.