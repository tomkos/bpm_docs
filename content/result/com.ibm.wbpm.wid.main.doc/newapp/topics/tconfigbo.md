<!-- image -->

# Configuring the business object parsing mode of modules and
libraries

The method by which XML data is parsed at run time on IBM® Workflow
Server is
governed by the business object parsing mode.

The lazy parsing mode performs delayed parsing of input XML data.
Data is processed only when needed. The eager parsing mode loads the
whole XML input data at once, and is compatible with version 6. There
are advantages to using each mode, depending on your application.
The business object parsing mode is set at the module and library
level. Modules and libraries that were created in a version of IBM Integration
Designer before
version 7 will run in the eager parsing mode.

- the parsing mode of existing projects in your workspace
- the parsing mode of dependent projects or other projects in the
same solution

To understand the optimal parsing mode for different types of applications, and to learn about
the implications of changing the parsing mode, read Considerations when choosing the business object parsing mode.

You must configure the business object parsing mode for a complete
solution, or for all the projects in the workspace, rather than configuring
a single module or library. After you configure the solution, you
can further optimize individual projects.

1. Select a solution in the Business Integration View.
2. Right-click and select Configure Business Object Parsing
Mode.
3. Select the modules and libraries for which you want to configure
the parsing mode, and click Next. By default,
the optimal parsing mode for the set of projects is selected.
4. Select the parsing mode and click Finish.Changing
the parsing mode may result in errors in some artifacts, which are
shown in the list of potential problems. You must fix these errors
manually in order to deploy the projects successfully.

1. Select a module or library in the Business Integration View.
2. Right-click and select Configure Business Object Parsing
Mode.
3. Select the modules and libraries for which you want to change
the parsing mode. Click Select All if you want
to configure all the projects in the workspace.
4. Click Next. By default, the optimal parsing
mode for the set of projects is selected.
5. Select the parsing mode and click Finish.Changing
the parsing mode may result in errors in some artifacts, which are
shown in the list of potential problems. You must fix these errors
manually in order to deploy the projects successfully.

You can also set the business object parsing mode of a single module
or library. When you create a new module or library, you have the
option to change the default business object parsing mode. See the
related tasks for more information.