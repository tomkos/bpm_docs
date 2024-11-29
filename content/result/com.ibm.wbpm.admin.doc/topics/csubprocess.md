<!-- image -->

# Lifecycle management of BPEL subprocesses

For modularity and reuse, it often makes sense to implement one
or more steps of the business logic as a separate process and to invoke
this process from the main process. A subprocess can also start another
process. This can lead to a hierarchy of process instances. When these
processes are deployed, all of the process templates in the process-to-process
relationship must be deployed to the same Business Process Choreographer
database.

A subprocess can have a peer-to-peer relationship or a parent-child
relationship with the calling process. This relationship determines
the behavior of a subprocess when an action that manages the process
lifecycle is invoked for the calling process. The lifecycle operations
comprise suspend, resume, terminate, delete, and compensation. In
a parent-child relationship, operations that manage the process lifecycle
 can be taken only on top-level process instances.

A long-running process
that is created and started using a one-way interface is considered
to be a peer process. Its autonomy attribute is ignored at run time.

If the parent is terminated, it must wait until all
of the child processes have been terminated. If the invoke activity
that called the child process expires, is skipped, force retried or
force completed, the child process is terminated first. While the
child process is terminating, the invoke activity stays in the running
state until the child process reaches the terminated state.

A
microflow always runs as a child process, that is, its autonomy attribute
is ignored.

A parent-child relationship can be established
only between processes that interact directly within a module, or
across module boundaries using SCA Import or Export. If another SCA
component intercepts this interaction, it might prevent a parent-child
relationship from being established, for example, an interface map
component that is wired between the two process components.

<!-- image -->