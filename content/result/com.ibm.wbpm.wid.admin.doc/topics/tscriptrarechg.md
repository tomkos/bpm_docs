<!-- image -->

# Creating a script for test cases that rarely change

## About this task

The following example demonstrates a situation that rarely
changes. It is assumed that the server has been started.

## Procedure

1. One Ant get task is used to run the test case. Variables
are used to provide the input data. When completed, the results will
be written to the OrderTest.xml file. <project name="Automated Test Case Run" basedir="." default="run">
   <property name="testfile" value="OrderTest.xml"/>
   <property name="url" value="http://localhost:9080/OrderTestWeb/TestServlet"/>
   <target name="run">
      <get dest="${testfile}" src="${url}"/>
   </target>
</project>
2. By default, Ant expects the script to be named build.xml
file.  Assuming that is the name of the script, at the command prompt,
you would type ant.  The script runs to completion.
If the script is not in a build.xml file then at
the command prompt type ant -buildfile <directory><build
file>  .
3. Examine the pass/fail results in the returned XML file.
This file will be placed in the same directory as defined in your
script. See Example of an XML output file,
which shows an example of the type of output you should expect.