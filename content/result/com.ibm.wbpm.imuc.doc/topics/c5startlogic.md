<!-- image -->

# Understanding the startup behavior of Business Process Choreographer

When the Business Process Choreographer is started or restarted, no messages
in the internal queues are processed until all enterprise applications have
started. It is not possible to change this behavior. The time that the Business
Flow Manager and Human Task Manager are unavailable during a restart depends
on how long it takes until all enterprise applications are started. This behavior
is necessary to avoid navigating any processes with associated enterprise
applications that are not running.

Starting to process messages in the internal queue before all applications
are started would result in ClassNotFound exceptions.