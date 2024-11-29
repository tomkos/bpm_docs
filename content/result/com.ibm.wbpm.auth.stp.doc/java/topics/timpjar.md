<!-- image -->

# Adding a Java Archive (JAR) file to a module

## About this task

To add a JAR file to a module, mediation module, or
library:

## Procedure

1 Choose one of the following actions depending on whetherthe JAR file will only be used with one module or library or willbe shared in multiple modules.
    - If the JAR file will be used in only one module, mediation module,
or library, copy the file into a module, mediation module, or library
in the Business Integration view.
    - If the JAR file will be used in multiple modules, mediation modules,
or library, share the JAR file by wrapping it in a Java project so
that many libraries and modules can use the same JAR file at development
time. The next step shows you how to share the JAR file.
2 Optional: Set up dependencies from other modules or librariesto the Java™ project. Use this approach if you wantto allow many libraries and modules to use the same JAR file at developmenttime. During deployment, the Java project will be deployed withthe module.

1. Create a Java project.
2. Copy the JAR file into the Java project.
3. Set up the Java build path of the Java project to contain
this JAR file.
4. Open the dependency editor from the module or library.
5. Add the Java project
in the Java section of the dependencies. Note: Do
not change the Java dependencies for modules and libraries outside
of the dependency editor.
6. Make sure that the Deploy with module or Deploy
with library check box is selected.

During deployment, the Java project will be deployed with
the module.

## Results