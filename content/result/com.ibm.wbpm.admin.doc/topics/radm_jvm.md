# General JVM configuration settings for IBM Business Automation
Workflow environments

This topic consists of the following
sections:

- Garbage collection mode
- Fixed or flexible heap size
- Nursery size
- Explicit garbage collection
- Optimization

## Garbage collection mode

Field
experience in tuning IBM Business Automation
Workflow environments
has confirmed best performance using the garbage collection mode gencon.
This is the default garbage collection mode that IBM Business Automation
Workflow is tested
and shipped with. Accordingly, changes to the garbage collection settings
require thorough evaluation based on extensive performance tests for
each environment individually.

## Fixed or flexible heap size

IBM Business Automation
Workflow environments
perform best with properly tuned flexible heap sizes. IBM Business Automation
Workflow relies
on dynamic class loading and unloading. The JVM unloads classes only
during global garbage collection events. For gencon mode,
this means that only a compaction cycle triggers unloading.

The
exact values are environmental specific, so determining the settings
for a flexible heap size requires iterative testing.

In a fixed
heap scenario, class unloading takes place when the maximum is reached.
As a result, many classes might have accumulated and require significantly
more time to unload. This could negate the positive impacts of using
a fixed heap size. Using fixed initial and maximum heap sizes (-Xms
= -Xmx) is preferable for running rather static content like
serving Servlets or reading files. Using a fixed heap size prevents
large compaction cycles during garbage collection, which impacts JVM
performance. Having a larger initial heap size increases the initial
start up time of a JVM, because the entire heap is reserved at the
beginning. Although this cost is marginal, environments with frequent
restarts might benefit from using a lower initial heap size. Furthermore,
the entire heap is reserved against the operating system for the entire
life cycle of the JVM. This might be inappropriate for environments
that share limited system resources.

## Nursery size

The nursery
is a dedicated Java heap space that is used in the gencon garbage
collection mode. It contains the most recently generated objects.
If these objects survive a certain number of garbage collection cycles,
they are moved to the remaining space, that is known as the tenured
space. The following equation applies to these areas:

```
current heap size - current nursery size = tenured size
```

Using
a very large nursery size can have a major impact on the memory behavior.
If the tenured space cannot fulfill a memory request an OutOfMemory
error occurs. It is therefore possible to get OutOfMemory errors even
though memory is free in the nursery.

IBM Business Automation
Workflow does not
specify any default nursery size. The JVM automatically optimizes
the nursery size. As long as a nursery setting is not specified, the
minimum (-Xmns) and maximum (-Xmnx)
are adjusted to 25% of the Java heap size (-Xms and -Xmx).

## Explicit garbage collection

Recent
JVM versions have improved the usage of the Direct Data Buffer (DDB)
residing on the native memory. This improved the stability while using -Xdisableexplicitgc.
The Lucene Index (that is used by Workflow Center and Process Portal index) also
relies on the DDB. This means that large indexes can result in large
native memory usage. In most scenarios, the setting has no negative
impact on  IBM Business Automation
Workflow.

```
HKLM\System\CurrentControlSet\Control\Session Manager\Memory Management\AllocationPreference = 0x100000 (REG\_DWORD)
```

## Optimization

In order to optimize
allocation requests IBM Business Automation
Workflow uses compressed
references (-Xcompressedrefs), which effectively
reduces the address space from 64-bit to 32-bit only. As a result,
objects might be allocated below the 4 gigabyte mark (232).

Ideally,
the native heap is located in the same area in the operating system's
memory. It contains the objects that are required for the JVM to work
with the underlying operating system, for example, allocating resources
for JVM threads. It is used for JVM internal processing whereas the
Java heap is only used for running application code. This memory layout
might result in insufficient space on the lower 4 gigabyte address
space and cause native OutOfMemory errors. For more details, see Java heap OutOfMemory error versus native OutOfMemory
error.

In order to prevent the usage of the lower 4
gigabyte address space, by default, IBM Business Automation
Workflow uses the
property -Xgc:preferredHeapBase=0x100000000. It effectively
shifts the Java heap above the 4 gigabyte mark and helps to ensure
that there are enough resources for other processes.

For
Java 6 R1 SR6 initial version, Java 7 R1 SR5 initial version and later,
increasing the Java heap to 4 gigabyte or more, will automatically
cause the address space to be moved above the 4 gigabyte mark. Because IBM Business Automation
Workflow environments
consist of different JVMs with different heap sizes, this approach
might be useful, depending on the specific Java heap that you are
tuning.

For more information, see Using -Xgc:preferredHeapBase with -Xcompressedrefs.