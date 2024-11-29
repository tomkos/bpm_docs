<!-- image -->

# Populating CVS with the required artifacts

## Before you begin

## About this task

To populate CVS with the required artifacts:

## Procedure

1. Ensure that your component test project does not include
any SCA modules as utility JAR files. Component test projects can
only contain libraries.
2. Check your component test project into CVS.
3 If your component test project has dependencies on WSDL,XSD, or Java interface files that are not contained in a library thatis referenced by the component test project, complete the followingsteps: It is necessary to check the WSDL, XSD, and Java interface filesinto CVS because the component test project needs them at run timefor the creation of the types required to run the tests. Checkingthese files into CVS enables you to work with the test artifacts withouthaving the associated modules in the workspace.
    1. In the Business Integration view, expand your component
test project. The WSDL, XSD, and Java interface files are automatically
copied into the following source folder under the component test project
(where ModuleName is the name of the associated module): ModuleNamedependencies
    2. Check the WSDL, XSD, and Java interface files into CVS.
4 In the Physical Resources view, expand your component testproject and check the generated Java class files for your test suitesinto CVS. Depending on whether you specified a folder for your testsuites when you created them, the generated Java class files willhave the following file names:

- test.TestSuiteName.java
- tablesFor\_test.TestSuiteName\_DataTable.java
- FolderName.test.TestSuiteName.java
- FolderName.tablesFor\_test.TestSuiteName\_DataTable.java
5 Create a file to catalog your test suites by completingthe following steps: You will need the information in the TestSuiteList.xml fileto configure the scripts that perform the batch testing of your componenttest projects.

1. In the workbench, run a search for the test suites in
your component test project.
2. Generate an XML file named TestSuiteList.xml that contains
the names of the test suites and their corresponding class names and
test cases.
3. Check the TestSuiteList.xml file into CVS.