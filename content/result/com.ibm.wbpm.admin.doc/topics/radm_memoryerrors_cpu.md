# Best practices for high JVM CPU utilization issues

Although reasons for high CPU differ, high memory utilization is a common cause. Improper memory
configuration or incorrect memory usage results in frequent Garbage Collection cycles. Each cycle is
prevents the JVM from performing application processing. Since Garbage Collection is a CPU intense
operation, if the duration between Garbage Cycles is short, the system's CPU can be pegged by
Garbage Collection activity. Therefore, prior to performing in depth CPU reviews, ensure the JVM's
verbose Garbage Collection data indicates the heap is properly sized. Conversely, if CPU reviews
show high CPU consumed by Garbage Collection, this indicates the heap is improperly size.

- Identify the ID of the process that is consuming CPU excessively
- Reviewing CPU utilization with JVM utilities - thread dumps
    - Using a dedicated tool - TDMA
    - Using RAW data
- Using additional tools or scripts

## Identify the ID of the process that is consuming CPU excessively

Because each JVM on a system runs as its own process. , reviewing the operating system's overall
CPU utilization is insufficient. Therefore, in a clustered environment several JVM instances could
be causing high utilization even though each individual process is consuming a reasonable amount of
CPU.

After you have identified a specific process ID, further diagnostic information for this instance
is required.

## Reviewing CPU utilization with JVM utilities - thread dumps

Newer JVM versions print absolute CPU consumption of each thread within a thread dump (Javacore).
To understand whether threads consume more, constant, or less CPU over time, it is recommended to
compare several Javacores.

## Using a dedicated tool - TDMA

Using a dedicated tool like IBM Thread and Monitor Dump Analyzer (TMDA) simplifies these
CPU reviews by generating diagrams along with relative CPU usage. For more information, see Java Core
Debugging using IBM Thread and Monitor Dump Analyzer for Java.

## Using RAW data

```
3XMTHREADINFO            "WebContainer : 8" J9VMThread:0x000000000C707800, j9thread\_t:0x000000001EE3B770, java/lang/Thread:0x00000001AA9B5520, state:R, prio=5
3XMJAVALTHREAD           (java/lang/Thread getId:0x4D59, isDaemon:true)
3XMTHREADINFO1           (native thread ID:0x24AC, native priority:0x5, native policy:UNKNOWN, vmstate:CW, vm thread flags:0x00000001)
3XMCPUTIME               CPU usage total: 90.667781200 secs, user: 73.726072600 secs, system: 16.941708600 secs, current category="Application"
3XMHEAPALLOC             Heap bytes allocated since last GC cycle=286624 (0x45FA0)
3XMTHREADINFO3           Java callstack:
```

- "WebContainer : 8" represents the JVM internal name of a thread and
java/lang/Thread getId:0x4D59 represents the JVM internal ID.Tip: You
can search for this thread in the IBM® Business Automation
Workflow
logs. To find the equivalent thread ID, remove the leading 0x then prepend the
getId value with 0s until there is an 8 digit number. For the
previous example, getID:0x4D59 becomes 00004D59 which can be
searched for in the log files. However not all threads log content and are shown in the log
files.
- native thread ID:0x24AC represents the thread ID provided to the operating
system. Depending on the operating system details a conversion from hexadecimal to decimal is
required.
- CPU usage total: 90.667781200 secs, user: 73.726072600 secs, system: 16.941708600 secs, current category="Application"
is the CPU usage of the thread.
- Everything following the entry Java callstack: refers to the processing chain
on that specific JVM thread. The first Java method listed on the stack is the current method called.
Moving down the stack shows the chain of Java calls, thereby identifying components used by the
thread.

```
1TIDATETIME    Date: 2018/12/15 at 13:43:50:398             // generation time of the Javacore
...
3XHNUMCPUS       How Many       : 8                         // number of CPUs multiplied with elapsed time equals entire available CPU time
...
1CISTARTTIME   JVM start time: 2018/12/14 at 13:15:13:765   // start up time of the JVM minus generation time of the Javacore equals elapsed time
```

A Javacore is a current snapshot of the threads in the JVM. Historical data is not retained in
the Javacore. So a thread in one Javacore might not exist in a different Javacore. Additionally,
pooled threads (for example WebContainer) might be reused for different processing. Always check in
the call stack to see if the same processing is executed before you compare the CPU usage and draw
conclusions on the usage.

```
CPU\_Usage\_ThreadA\_between\_Javacores = (CPU\_Usage\_ThreadA\_JavaCore2 - CPU\_Usage\_ThreadA\_JavaCore1) * 100 / ((Generation\_Time\_Javacore2 - Generation\_Time\_Javacore1) * Number\_CPUs)
```

## Using additional tools or scripts

- On Unix based environments, using top and top -h <pid> can
be useful to determine the overall usage by all processes and break it down to certain threads
within a process.
- On Windows environments, additional scripts or tools are required to collect CPU information.

For IBM Business Automation
Workflow environments the general
must-gather details for WebSphere® Application
Server are applicable.
These collect operating system details along with Javacore files and enable a proper in-depth
analysis.