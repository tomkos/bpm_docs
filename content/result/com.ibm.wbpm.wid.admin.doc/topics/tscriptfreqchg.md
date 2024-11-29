<!-- image -->

# Creating a script for test cases that change frequently

## About this task

If the modules and test projects are expected to change
frequently then running the script shown in Creating a script for test cases that rarely change is limited.

For
test cases that change frequently, use an import task to bring in
the module or modules that have changed. This module would be contained
in a project interchange (PI) file. The import task imports project
interchange files into the workspace.

Typically, when you
are using these tasks you are working in a headless mode. A headless
mode means that the display, keyboard and mouse are not used.

## Procedure

1. Change your script to import the project interchange (PI)
files that have changed. <project name="Automated Test Case Run" basedir="." default="run">
   <property name="module" value="OrderEntry"/>
   <property name="testp" value="OrderTest"/>
   <property name="testfile" value="OrderTest.xml"/>
   <property name="url" value="http://localhost:9080/OrderTestWeb/TestServlet"/>
   
   <target name="importFromPI">
      <importPI pif="D:\wbit\workspaces\widspaces/ant2.zip" projects="${testp}"/>
   </target>
   
   <target name="build" depends="importFromPI">
      <projectBuild projectName="${module}"/>
      <projectBuild projectName="${testp}"/>
   </target>
   
   <target name="run">
      <get dest="${testfile}" src="${url}"/>
   </target>
</project>
2. Examine the pass/fail results in the returned XML file.
This file will be placed in the same directory as defined in your
script. See Example of an XML output file,
which shows an example of the type of output you should expect.
You can optionally use an existing workspace, in which case
you can reuse existing projects and can remove the import and potentially
the deploy/undeploy task.
To run the script in headless mode,
call the batch file or shell script (runAntWid.bat) and pass the script
as a parameter. For example, runAntWid -buildfile e:\testscript\doAll.xml.
Since build.xml is the default, you would not need the -buildfile
attribute if you script was named build.xml.