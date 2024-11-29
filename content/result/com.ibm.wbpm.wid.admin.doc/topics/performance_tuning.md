<!-- image -->

# Performance tuning for IBM Integration
Designer

IBM® Integration
Designer can be
used in a number of configurations. The information in this topic focuses on the use of Integration Designer with the test environment
and with Workflow Server.
Although the context is the tools environment, the tuning solutions also involve adjustments to the
test environment and Workflow Server using its
administrative console. The issues described here could also occur if you are using Integration Designer with IBM Workflow
Center.

- An out of memory exception occurs, and the server process stops.
- Performance degrades significantly because either physical memory
is overcommitted and swapping occurs, or an excessive amount of time
is being spent in garbage collection.

## Identifying problems with heap size

When IBM Integration
Designer is
responding slowly to mouse clicks or keyboard strokes, you can use
the Heap Status widget or generate the verbosegc.log file
to see JVM heap usage.

A check for Java heap size issues would
be to turn on the Heap Status widget in Integration Designer by selecting Window > Preferences > General > Show heap status. This widget allows you to see how much of the heap
is being used and to trigger a garbage collection.

1. Using a text editor, from the Integration Designer installation
directory, open the eclipse.ini file.
2. Add the following line: -verbosegc -Xverbosegclog:location for the generated gclog file If
you do not specify an exact location, the file will be created in
the installation directory.
3. To analyze the verbosegc.log file, download the  IBM Monitoring and Diagnostic Tools - Garbage Collection and Memory
Visualizer (GCMV).
4. To run PMAT, type the following command in a command prompt: java -Xmx500m -jar ga39.jar .

## Analyzing system memory use

When heap size
is increased, the memory available for the rest of the process is
decreased. The remaining system memory is used by native code, the
JVM loading classes, the JVM itself, and so on. To analyze system
memory utilization, use the appropriate system memory tool (for example,
vmstat for Linux or Unix systems, and Performance Monitor or Task
Manager for Windows).

## Addressing problems from swapping

- Ensure that there is enough physical memory to support Business Automation Workflow and all
other running processes. Use the system memory tools to do this. Note
that some 32 bit operating systems can only use a certain amount of
physical memory (for example, 3 GB for Windows).
- Stop all processes that are not required (for example, browsers,
tools, office applications).
- Use a remote DB2 system, and stop the DB2 processes on the local
system.
- For authoring, use a remote test environment or Process Center.

## Addressing problems related to garbage collection

- An out of memory exception occurred with frequent garbage collection
activity immediately before the out of memory exception, which results
in very little free space in the Java heap.
- Performance is severely degraded without swapping occurring, but
the system is spending an excessive amount of time doing garbage collection.

You can address these symptoms by increasing the Java
heap size (-Xmx) or tuning the JVM heap. The Java heap must be large
enough to contain all required Java objects. However, on 32 bit systems
ensure that it is not so large that the amount of native memory becomes
a bottleneck. You need to experiment to determine these limits.

1. Generate the verbosegc.log file.
2. Tune the Java heap size parameters.
3. Experiment with different garbage collection policies. These policies are set by using the
-Xgcpolicy JVM option. There are two choices: optthruput and gencon. The gcpolicy
choice can influence the amount of memory used, depending on the particular scenario. If you use the
gencon gc policy, tune the nursery size parameters (-Xmnsize,
-Xmnsinitial size, and -Xmnxmaximum size. These parameters are
found in the eclipse.ini file in the IID\_HOME directory.

## Changing heap size settings

1. In the left panel of the administrative console, select Servers > Server Types > WebSphere application servers.
2. Select the server that requires more memory.
3. Under Java and Process Management, select Process Definition.
4. In the Additional Properties section, select Java Virtual
Machine.
5. There are two fields that are related to heap size, initial heap
size and maximum heap size. By default, if the initial heap size is
not specified, it is 256 KB. For a 32-bit system, the Java Virtual
Machine (JVM) heap size is limited to 1.5 GB on Microsoft Windows
and 2.5 GB on AIX.

There are no definite rules for the optimal heap size,
because the required size depends on the number and size of the modules
deployed on the server and on whether the server is used as development
server or production server. However, here is a technique that has
worked for some administrators. Increase the maximum value to a level
that is large enough for the server not to run out of memory and collect
verbosegc data. The verbosegc data shows the typical or maximum amount
of live data in the heap. Set the maximum heap size so that the server
remains approximately 50% empty during a steady state. For example,
if the verbosegc data reveals that there is typically about 500MB
of data, set the maximum heap size to 1024MB.

You might not
be able to use the maximum setting, because that setting might cause
you to run out of memory on your system before the JVM limit is reached.
That is the case if the symptom is an out of memory exception, and
there is not a garbage collection taking place immediately before
the out of memory exception. In this case, the issue is that the native
memory for a resource (such as threads, sockets, file handles,  JIT
compiled code) has been exhausted. In this case, decrease the maximum
Java heap size (-Xmx) to allow more room for native memory in the
JVM address space. This issue typically occurs only on 32 bit operating
systems.

## Processing Java files in Integration Designer

1. Importing the Java files into the workspace.
2. Compiling the Java files.
3. JDT indexing to gather basic information from the Java files for
validation and search purposes.
4. Integration Designer indexing
and validation to identify Java sources that use the business object
API for better validation and refactoring.

Here is one step you can take to improve performance in this
situation. Bundle Java classes into Java Archive (JAR) files and reference
the JAR files instead of individual Java files. By compiling all the
Java source files into a JAR file, you save Java compilation time
(which is actually quite significant) and you save time on the Java
indexing and validation as well. To support source-level debugging,
bundle the Java source files together with the Java classes in the
same JAR.

This technique should only be used if the Java code
is not likely to be changed, or will be changed infrequently. To create
the JAR file, import the classes and then use the JAR export wizard.

See
"Using binary JAR files with Integration Developer and Process Server"
in the related links for more information about this subject.