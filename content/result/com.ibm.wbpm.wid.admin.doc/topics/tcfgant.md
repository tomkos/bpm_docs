<!-- image -->

# Configuring an Ant script

## About this task

## Procedure

1. Define the properties for your environment.
2. Check the component test projects out of CVS.
3. Zip up the projects into a project interchange file.
4. Build the projects.
5. Start the server.
6. Deploy the projects to the server.
7. Specify a "Get" operation to run the tests using servlet
tasks.
8. Remove the projects from the server.
9. Stop the server.

## Example

The code fragment below shows the contents of an example
Ant script named build.xml that is used to perform automated testing
of the Hello World Part 1 sample of IBM® Integration
Designer.
The script invokes extraction and build operations for the projects
being tested. For this reason, the script has a dependency on one
of the following conditions:

- The existence of a workspace that contains IBM Integration
Designer modules.
- The use of CVS as a source code repository.

Furthermore, the script depends on the complete impor action
of the Hello World Part 1 sample and the creation of a component test
project and test suite.

```
<!-- Sample component test script for use with IBM Business Automation
Workflow --> <project name="Automated Test Case Run" basedir="." default="run">  1     <!-- Modules, libraries, and test projects being tested -->
    <property name="module1" value="HelloWorldMediation" />
    <property name="module2" value="HelloService" />
    <property name="library1" value="HelloWorldLibrary" />
    <property name="testproject1" value="HelloWorldTest" />

 2  <!-- The following sections contain property settings -->

    <!-- Server properties -->
    <property name="wps.home" value="C:/WID75\_WTE/runtimes/bi\_v75" />
    <property name="wps.username" value="admin" />
    <!-- Server password must be plain text. To avoid storing the server -->
    <!-- password in a script, it can be stored in -->
    <!-- the soap.client.props file instead. Refer to the password option -->
    <!-- in the wsadmin command reference: -->
    <!-- http://publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=/com.ibm.websphere.nd.multiplatform.doc/info/ae/ae/rxml\_commandline.html -->
    <property name="wps.password" value="admin" />
    <property name="wps.node" value="qnode" />
    <property name="wps.server" value="server1" />

    <!-- Source code repository properties -->
    <!-- This sample uses CVS. -->
    <property name="cvs.username" value="cvsuser" />
    <property name="cvs.password" value="cvspassword" />
    <property name="cvs.root" value=":pserver:${cvs.username}:${cvs.password}@cvs:/cvs/repository" />
    <property name="cvs.packageroot" value="testProjects" />
    <property name="cvs.stream" value="HEAD" />

    <!-- Build and test properties -->
    <property name="test.servlet.url" value="http://localhost:9080/HelloWorldTestWeb/TestServlet?username=${wps.username}&password=${wps.password.encoded}" />
    <property name="test.output.file" value="${build.output.dir}/TestOutput.xml" />
    <property name="build.output.dir" value="C:/BuildOutputDir" />
    <property name="build.working.dir" value="C:/BuildWorkingDir" />
    <!-- The Workspace location can already exist or it can be the -->
    <!-- destination of a source code repository extract -->
    <property name="workspace.dir" value="D:\Workspaces\20100625cvs2/" />
    <!-- Server password for the test servlet url. It can be plain text or -->
    <!-- encoded. For password encoding, refer to -->
    <!-- http://publib.boulder.ibm.com/infocenter/wasinfo/v7r0/index.jsp?topic=/com.ibm.websphere.nd.doc/info/ae/ae/rsec\_propfilepwdencoder.html -->
    <property name="wps.password.encoded" value="{xor}PjsyNjE=" />

    <!-- Ant task definitions -->
    <taskdef name="wsStartApplication"
             classname="com.ibm.websphere.ant.tasks.StartApplication" />
    <taskdef name="wsStartServer"
             classname="com.ibm.websphere.ant.tasks.StartServer" />
    <taskdef name="wsStopServer"
             classname="com.ibm.websphere.ant.tasks.StopServer" />
    <taskdef name="wsInstallApp"
             classname="com.ibm.websphere.ant.tasks.InstallApplication" />
    <taskdef name="servicedeploy"
             classname="com.ibm.websphere.ant.tasks.ServiceDeployTask" />
    <taskdef name="wsUninstallApp"
             classname="com.ibm.websphere.ant.tasks.UninstallApplication" />

 3  <target name="checkout">
        <cvs command="export -r ${cvs.stream} -d ${module1}"
             package="${cvs.packageroot}/${module1}"
             dest="${workspace.dir}"
             cvsroot="${cvs.root}"
             cvsrsh="ssh"
             output="${build.output.dir}/${module1}.extract.log"
             quiet="true" />
        <cvs command="export -r ${cvs.stream} -d ${module2}"
             package="${cvs.packageroot}/${module2}"
             dest="${workspace.dir}"
             cvsroot="${cvs.root}"
             cvsrsh="ssh"
             output="${build.output.dir}/${module2}.extract.log"
             quiet="true" />
        <cvs command="export -r ${cvs.stream} -d ${library1}"
             package="${cvs.packageroot}/${library1}"
             dest="${workspace.dir}"
             cvsroot="${cvs.root}"
             cvsrsh="ssh"
             output="${build.output.dir}/${library1}.extract.log"
             quiet="true" />
        <cvs command="export -r ${cvs.stream} -d ${testproject1}"
             package="${cvs.packageroot}/${testproject1}"
             dest="${workspace.dir}"
             cvsroot="${cvs.root}"
             cvsrsh="ssh"
             output="${build.output.dir}/${testproject1}.extract.log"
             quiet="true" />
    </target>

 4  <target name="createPI">
        <!-- This sample target is applicable when using CVS as the source -->
        <!-- code repository. Excluding **/CVS/** means CVS metadata is not -->
        <!-- included in the PI. If using another source code repository, -->
        <!-- change or remove the exclude attribute. -->
        <zip basedir="${workspace.dir}"
             destfile="${build.output.dir}/${module1}.zip"
             includes="${module1}/**/**/*, ${library1}/**/**/*"
             excludes="**/CVS/**" />
        <zip basedir="${workspace.dir}"
             destfile="${build.output.dir}/${module2}.zip"
             includes="${module2}/**/**/*, ${library1}/**/**/*"
             excludes="**/CVS/**" />
        <zip basedir="${workspace.dir}"
             destfile="${build.output.dir}/${testproject1}.zip"
             includes="${testproject1}/**/**/*"
             excludes="**/CVS/**" />
    </target>

 5  <target name="generateEAR" depends="createPI">
        <!-- The following link below provides a detailed description of the -->
        <!-- serviceDeploy task: -->
        <!-- http://publib.boulder.ibm.com/infocenter/dmndhelp/v7r0mx/index.jsp?topic=/com.ibm.websphere.wps.doc/doc/tdep\_usingant.html -->
        <servicedeploy scaModule="${build.output.dir}/${module1}.zip"
                       workingDirectory="${build.working.dir}"
                       outputApplication="${build.output.dir}/${module1}.ear"
                       wasHome="${wps.home}"
                       cleanStagingModules="true"
                       keep="true" />
        <servicedeploy scaModule="${build.output.dir}/${module2}.zip"
                       workingDirectory="${build.working.dir}"
                       outputApplication="${build.output.dir}/${module2}.ear"
                       wasHome="${wps.home}"
                       cleanStagingModules="true"
                       keep="true" />
        <servicedeploy scaModule="${build.output.dir}/${testproject1}.zip"
                       workingDirectory="${build.working.dir}"
                       outputApplication="${build.output.dir}/${testproject1}.ear"
                       wasHome="${wps.home}"
                       cleanStagingModules="true"
                       keep="true"
                       ignoreErrors="true" />
    </target>

 6  <!-- The following sections start and stop the server -->

    <target name="startServer">
        <wsStartServer server="${wps.server}"
                       logFile="${build.output.dir}/start.log"
                       trace="false"
                       failonerror="false" />
    </target>

    <target name="stopServer">
        <wsStopServer server="${wps.server}"
                      logFile="${build.output.dir}/stop.log"
                      trace="false"
                      username="${wps.username}"
                      password="${wps.password}"
                      failonerror="false" />
    </target>

 7  <target name="deploy" depends="generateEAR">
        <!-- Install the apps on the server -->
        <wsInstallApp ear="${build.output.dir}/${module1}.ear"
                      user="${wps.username}"
                      password="${wps.password}"
                      failonerror="false" />
        <wsInstallApp ear="${build.output.dir}/${module2}.ear"
                      user="${wps.username}"
                      password="${wps.password}"
                      failonerror="false" />
        <wsInstallApp ear="${build.output.dir}/${testproject1}.ear"
                      user="${wps.username}"
                      password="${wps.password}"
                      failonerror="false" />
        <!-- After installing the apps they must be explicitly started -->
        <wsStartApplication application="${module1}App"
                            server="server1"
                            node="${wps.node}"
                            user="${wps.username}"
                            password="${wps.password}" />
        <wsStartApplication application="${module2}App"
                            server="server1"
                            node="${wps.node}"
                            user="${wps.username}"
                            password="${wps.password}" />
        <wsStartApplication application="${testproject1}App"
                            server="server1"
                            node="${wps.node}"
                            user="${wps.username}"
                            password="${wps.password}" />
    </target>

 8  <target name="undeploy">
        <wsUninstallApp application="${module1}App"
                        user="${wps.username}"
                        password="${wps.password}"
                        failonerror="false" />
        <wsUninstallApp application="${module2}App"
                        user="${wps.username}"
                        password="${wps.password}"
                        failonerror="false" />
        <wsUninstallApp application="${testproject1}App"
                        user="${wps.username}"
                        password="${wps.password}"
                        failonerror="false" />
    </target>

 9  <target name="runTest">
        <!-- Run the test using the test project servlet -->
        <get src="${test.servlet.url}" dest="${test.output.file}" />
    </target>

    <target name="run"
            depends="checkout, startServer, deploy, runTest, undeploy, stopServer">
        <!-- Display the results of the run -->
        <loadfile srcFile="${test.output.file}"
                  property="testoutput" />
        <echo message="${testoutput}" />
    </target>

</project>
```

| Section of Ant script                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  Define the projects                    | The following projects from the Hello World Part 1 sample are referenced in the Ant script:  HelloWorldMediation module HelloService module HelloWorldLibrary library HelloWorldTest component test project                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2  Set the properties                     | In this section of the code, several properties are defined. When the Ant script is run, the variable names for modules and projects appear as projects in the workspace. The property test.output.file has a value of OrderTest.xml. This is the name of the XML output file that will contain the results of the test. Note the test.servlet.url property. The URL is for a servlet that is generated into the web project of the component test project. The servlet interface enables you to query test suites and test cases and run whole tests, partial tests, and specific test cases. The servlet is generated into the web project of the component test project. The servlet APIs can be incorporated in the script or used on a stand-alone basis. If used on a stand-alone basis, the application must be already deployed and the server running. If you are testing applications in a CVS system, you need to pass values in the properties fields, such as the following values: CVS user ID and password Location of your CVS root directory Location of a directory on your local computer where the extracted CVS files will be placed Name of the CVS stream containing your applications, such as the head stream or a branch from the head stream Name of the log file containing information on the interaction with the CVS system |
| 3  Check out the projects                 | Component test projects are checked out of CVS. Your script checks out the projects you identified using the CVS variables specified at the top of the script. There are also CVS commands that you should know if your script will be extracting files from a CVS repository.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 4  Create the project interchange file    | In this section of code, component test projects are zipped into a project interchange file. See the topic "Populating CVS with the required artifacts" to learn about what needs to be included in the PI file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 5  Generate the EAR file                  | In this section of code, component test projects are built into an application using the serviceDeploy facility. The script builds the projects using the names in the project interchange file. Note the dependency on the previous section. This dependency specifies that the project interchange file must have been created first.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 6  Start the server or stop the server    | In this section of code, the server is started or stopped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 7  Deploy the application to the server   | In this section of the code, the application is deployed to the server and the application is started. using the wsadmin facility. There is a dependency that the application has first been built.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 8  Remove the application from the server | In this section of the code, the application is removed from the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 9  Run the test                           | In this section of code, a Get operation is used in conjunction with a URL to call a servlet task to run the tests. The following URL uses the product's built-in test features: http://localhost:9080/${test}Web/TestServlet If you are interested in learning about other servlet tasks that you can invoke using a URL, see the topic "Additional servlet tasks."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## What to do next