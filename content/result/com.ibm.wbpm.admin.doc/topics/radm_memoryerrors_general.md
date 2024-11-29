# Best practices for JVM memory issues

- Keep verboseGC (historical memory data) enabled
- Javacore and Heapdump generation
- Ensure proper Coredump settings
- Custom Xdump agents
- Allocation filter in IBM Business Automation Workflow
- Java heap OutOfMemory error versus native OutOfMemory error
- Java Heap OutOfMemory reviews using dedicated tools
- False positive leak suspects for Java Heap OutOfMemory conditions
- Impacts of cache tuning for memory / performance

## Keep verboseGC (historical memory data) enabled

When verboseGC is enabled, each JVM garbage collection cycle, allocation, and duration request
are logged, which allows historical data to be reviewed. This is mandatory data for reviewing memory
processing on a JVM. IBM® Business Automation
Workflow has verboseGC
enabled by default. Because the performance impact is marginal, it is suggested to keep verboseGC
enabled on all development, test and production systems.

Historical data is important for proper reviews. It is a best practice to archive this data
frequently, for example, during maintenance windows. Having smaller files enables quick reviews and
focusing on the recent time period. Also, disk space requirements are kept low.

## Javacore and Heapdump generation

By default, for the first four OutOfMemory conditions during a JVM lifetime, a Javacore and Heapdump is generated. The default settings generate
these files in the <profile>/logs directory.

The Javacore contains general details about the JVM configuration, such
as generic JVM arguments. It also outlines runtime information like a current Java heap usage and
Java threads processing, for example CPU usage and current execution status.

The Heapdump contains the objects allocated in the Java heap and the
reference pattern between objects, but omits object values (such as the value of a String).

Both types represent snapshot data at the time of the triggered event. Memory patterns that show
that a single instance or object type is consuming large amounts of high memory may warrant further
investigation. However, further investigation requires experience and knowledge of the product and
custom code to determine if the Heapdump indicates a tuning issue or a
possible memory leak. For example, it is expected for classes that are associated with caches to
consume a significant amount of heap. For more information, see False positive leak suspects for Java Heap OutOfMemory conditions.

## Ensure proper Coredump settings

Although most memory reviews due to OutOfMemory conditions can be solved with the generated
Javacore and heapdump only, certain situations require an in-depth review. By default, only the
first OufOfMemory condition during a JVM lifetime will generate a Coredump. However operating system
settings often prevent a full Coredump from being generated, so proper Coredump settings are
required.

A Coredump (also called a Systemdump) is a one-to-one snapshot of the JVM. In addition to the
information that is contained in a heap dump, a Coredump also contains thread processing details
like in a Javacore. Also, each specific runtime value is accessible enabling in depth reviews even
on business data processing. Furthermore, a Coredump contains native memory processing. This might
be relevant for native OutOfMemory conditions that are caused by the Classloader or Thread
Leaks.

Although Coredumps contain valuable information, the time required to generate the dump depends
on the JVM heap size. During that period, a JVM is inaccessible for additional requests. As a
result, WebSphere Application
Server
functionality might quit the processing by sending another termination signal. This can result in an
unexpected combination of dump events. Details on this scenario are available here: DUMP EVENT: "user" (00004000) received permanently

## Custom Xdump agents

Xdump agents are used to generate diagnostic information by listening for defined signals and
trigger actions. The default Xdump agents generate Javacores, Heapdumps, Coredumps and other
files on certain JVM events. You can customize Xdump agents to generate or even prevent dumps,
depending on the configuration, for example, to prevent large Coredumps being generated.

## Allocation filter in IBM Business Automation
Workflow

IBM Business Automation
Workflow defines
a custom Xdump agent for better monitoring of memory usage:

```
-Xdump:stack:events=allocation,filter=#300m
```

This prints the Java Callstack for each thread that allocates more than 300 MB in a single
request. Depending on business data processing such requests might be expected. However, requests of
this size warrant additional investigation due to the memory footprint of these objects which can
lead to an OutOfMemory condition. It is a best practice to make business data as small as possible
to improve performance. Using a lower filter value has been successfully tested with IBM Business Automation
Workflow, the pre-defined
size ensures accommodation with different business data processing needs in IBM Business Automation
Workflow environments.

## Java heap OutOfMemory error versus native OutOfMemory error

- The Java process memory is divided into the Java native heap and the Java heap. The Java heap is
defined by -Xms and -Xmx.
- The Java heap is divided into the nursery space and the tenured space. The nursery space is
defined by -Xmns and -Xmnx or -Xmn.

If the JVM native heap fails to fulfill an allocation requests, a native OutOfMemory error
occurs. This might indicate issues like thread leaks or incorrect settings at the JVM and operating
system level. Those incidents are often referred to as nOOM condition. If an allocation requests on
the Java heap (more specifically the tenured space) fails, a Java Heap OufOfMemory error is thrown.
This is often referred to as OOM.

- Details for a native OutOfMemory
(nOOM):"systhrow" (00040000) Detail "java/lang/OutOfMemoryError" "Failed to create a thread: retVal -1073741830, errno 11" received
- Details for an OutOfMemory
(OOM):"systhrow" (00040000) Detail "java/lang/OutOfMemoryError" "Java heap space" received

## Java Heap OutOfMemory reviews using dedicated tools

- To visualize the verboseGC data and get a better overview of garbage collection performance, use
IBM
Pattern Modeling and Analysis Tool for Java Garbage Collector (PMAT).
- To help identify leak suspects, search IBM
Community for suggestions.
- To monitor runtime data and analyze generated diagnostic data after incidents, use the Monitoring and Post
Mortem tools.

## False positive leak suspects for Java Heap OutOfMemory conditions

To improve performance, IBM Business Automation
Workflow relies on various
caches. As a result, cache related classes may retain a disproportionate amount of the heap and be
identified by tooling as a leak suspect. However, this is not a memory leak because the cache size
is limited by the cache settings. If cache related object structures are listed as a leak suspect,
you should consider reviewing the JVM's heap size, cache settings, and housekeeping. The following
caches have been observed to be marked as leak suspects:

Review the section Impacts of cache tuning for memory / performance for
more details on that topic.

IBM Business Automation
Workflow provides
components for developing custom applications. Accordingly, usage and memory utilization is directly
impacted by the actual application design, workload, and the business data. As a result, the
following leak suspects probably indicate issues related to custom code rather than product defects
in the specific component:

Memory usage depends on the number of coaches used. High utilization might indicate issues in
coach handling, for example, not completing a coach at all.

These objects might be stored in different lists. They are usually related to custom SQL queries
and the associated returned data. Large amounts of memory retained by
teamworks.sql.IndexMapImp objects might indicate problems with looping
requests.

These objects contain business data. Review your application design and code to determine whether
the size of business data is as expected. Often object structures for XML processing are observed in
this context, too.

## Impacts of cache tuning for memory / performance

A cache is meant to store data in memory for better performance, however, if memory is limited,
caches can block resources for other components. Hence, improperly tuned caches can result in high
memory usage and excessive garbage collection, which can cause CPU usage issues. If caches are sized
correctly and are consuming a significant portion of the heap, increasing the heap sizes can improve
the performance.

For more information about how to review cache and tuning in IBM Business Automation
Workflow, see Using process instrumentation data for cache tuning.