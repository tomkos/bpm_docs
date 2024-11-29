<!-- image -->

# Managing Business Flow Manager hold queue messages

In a long-running process, the Business Flow Manager can send itself request messages that
trigger follow-on navigation. These messages trigger either a process-related action (for example,
starting a fault handler) or an activity-related action (for example, continuing process navigation
at the activity). A navigation message always contains its associated process instance ID (piid). If
the message triggers an activity-related action, it also contains the activity template ID (arid)
and the activity instance ID (arid).

You can use the failed event manager to manage Business Flow Manager hold queue messages, or you
can use a custom program.

You cannot delete Business Flow Manager hold queue messages in the failed event manager. If the
related process instance does not exist, replay the hold queue message to delete the message.