<!-- image -->

# Limitations for component testing

A known limitation is:

- Component test projects experience build problems when two or
more instances of the same resource are detected

This limitation is discussed in the following section.

## Component test projects experience build problems
when two or more instances of the same resource are detected

For
a component test project to successfully reference modules (using
emulators or other test resources), it needs to be able to access
the WSDL and XSD files that are associated with the modules. If one
or more WSDL files reside in the modules rather than in libraries,
the component test project cannot directly reference the modules.
In this situation, the WSDL and XSD files are automatically copied
over to the component test project, which enables the component test
project to access the files and successfully reference the modules.

For
each WSDL file that is automatically copied over to a component test
project, a source folder is automatically created. When a build occurs,
WSDL and XSD files in each source folder are copied to a single output
folder. This can cause the following problems:

- Two or more instances of the same resource may exist with the
same name but with a different case, which prevents the component
test project from building. This problem is often accompanied by the
following error message:The project was not built
due to "A resource exists with a different case: '<path\_to\_resource>'."
Fix the problem, then try refreshing this project and building it
since it may be inconsistent.
- Two or more instances of the same WSDL or XSD file may exist with
the same name and same case. The next time that a reference is created
from the component test project to the associated module, the correct
instance of the WSDL or XSD file may be inadvertently overwritten
by an incorrect instance.

To resolve these problems, you can use refactoring to move
your WSDL files from the modules to libraries. This is the recommended
solution because it is a best practice to place WSDL files in libraries
rather than in modules. (The refactoring tool will help you move any
XSD files or other resources that are associated with the WSDL files.)

If
there is some reason why you cannot use refactoring to move your WSDL
files from modules to libraries, you can resolve the problems using
one of the following approaches:

- Create another test project for the emulator that is causing the
problem and move any tests that you need to the new project. (This
approach may not be possible if you have a single test that needs
the WSDL files that are experiencing name conflicts.)
- In the module that you are testing, rename the folder that is
causing the problem. (Alternatively, you can change the path to the
folder and retain the original folder name.)