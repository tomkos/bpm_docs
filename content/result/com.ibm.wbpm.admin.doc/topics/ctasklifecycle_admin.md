<!-- image -->

# State transition diagrams for administration tasks

If an administration task template is not available, a default
administration task is created at run time whenever one is needed
by the BPEL process.

<!-- image -->

Business Flow Manager creates and starts an administration
task implicitly in a single transaction. The inactive state is therefore
not visible externally, and the task directly reaches the ready state.

The
finished state is an end state. It does not, however, prohibit further
administrative actions.

Administration tasks are always inline
tasks and thus their lifecycle is controlled by the BPEL process.
They are always deleted with the BPEL process.