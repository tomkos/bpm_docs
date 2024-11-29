<!-- image -->

# Example of an Ant script

The following code fragment shows the contents
of an example Ant script:

```
<!-- Sample component test script for use with IBM Business Process Manager -->

<project name="Automated Test Case Run" basedir="." default="run">

    <!-- Modules, libraries, and test projects being tested -->
    <property name="module1" value="HelloWorldMediation" />
    <property name="module2" value="HelloService" />
    <property name="library1" value="HelloWorldLibrary" />
    <property name="testproject1" value="HelloWorldTest" />

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

    <target name="checkout">
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

    <target name="createPI">
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

    <target name="generateEAR" depends="createPI">
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

    <target name="deploy" depends="generateEAR">
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

    <target name="undeploy">
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

    <target name="runTest">
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