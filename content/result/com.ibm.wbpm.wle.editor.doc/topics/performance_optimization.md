# Optimizing process execution for latency

## About this task

By default, new processes are not optimized for latency, which means that, between activities,
instances return their execution threads to the shared thread pool. You can change the optimizing
setting for a process in the designer.

- The default processing behavior is not optimized for latency, which means that the thread is
released after each unit of work. This behavior ensures that all process instances that use the
default setting have an equal chance to continue navigation of the process.
- System tasks and decision tasks that are optimized for latency are executed on the same thread
that the process uses for navigation. If multiple system tasks or decision tasks exist in parallel
paths of the process, only one path is executed by the same thread, the other paths are scheduled to
use the default behavior by the Event Manager. Process instances with this execution optimization
use the Event Manager threads for longer and so they provide a more predictable latency. If a system
task calls an asynchronous implementation such as an asynchronous Advanced Integration service, the
default processing behavior is used.

You must take care to avoid causing a negative performance impact on other
instances, services, undercover agents, and other functions that use the shared pool of threads.

## Procedure

To enable the optimization for latency, complete the following actions.

1. Open the process.
2. On the Overview tab, open the Advanced section.
3. Select
Optimize Execution for
Latency to reduce thread context-switching for the process. Clearing the
option turns off the optimization for the process.