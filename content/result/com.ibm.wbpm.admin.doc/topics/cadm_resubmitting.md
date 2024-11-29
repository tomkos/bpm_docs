<!-- image -->

# Resubmitting failed events in IBM Business Automation Workflow

When a failed event is resubmitted, the processing resumes only for the failed branch and not for
the entire event. You can use the unique ID of the event to track its success or failure. If a
resubmitted event fails again, it is returned to the failed event manager with its original event ID
and an updated failure time.

If you have modified the trace control value, you can also trace resubmitted SCA
events to monitor the event processing.

- The application is stopped on the server
- The input and output parameters are modified
- The schema for the input and output parameters is modified