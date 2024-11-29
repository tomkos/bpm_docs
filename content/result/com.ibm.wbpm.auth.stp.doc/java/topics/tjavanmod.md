<!-- image -->

# Using a Java project with a module

## About this task

## Procedure

1 Create a Java project. You can createa Java projectfrom the Business Integration view.
    1. Click File > New > Project.
    2. In the New Projects list, select Java > Java project.
    3. Name the project and complete the selections in the wizard.
2. Develop your Java code in that Java project.
3. Add a dependency from a module, mediation module, or library to
this Java project.
To do that in the dependency editor, open the module, mediation module, or
library that will use the Java code. Add the Java project
as a dependent. To always deploy the Java project with the module or library
that you have selected, make sure that the Deploy with Library or Deploy
with Module check box is selected. The dependency editor will
add the Java project to the module's class path. By default,
the dependent Java class is deployed with the module and, in the case
of a library, the dependent Java project is deployed when the library
is deployed with a module. You can choose not to deploy the dependent Java project
with the module or library.