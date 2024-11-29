<!-- image -->

# Lifecycle of escalations

<!-- image -->

- When a task is created, any predefined escalations are created
and are put into the inactive state.
- When the task reaches the activation state for the escalation,
the escalation is put into the waiting state and the timer is started.
- A waiting escalation becomes escalated, the escalation actionis performed, and the associated task is put into the escalated substateif one of the following situations occurs:
    - The task has not yet reached the expected state and an authorized
user triggers the escalation manually.
    - The task has not yet reached the expected state and the timeout
is triggered.
- A waiting escalation becomes superfluous, and is deleted if oneof the following situations occurs:

- The task has reached the expected state and an authorized user
triggers the escalation manually.
- The task has reached the expected state and the timeout is triggered.
- The task has reached an end state and the escalation is canceled.
- You can change the escalation duration and repetition duration.

- Viewing task escalations

An escalation notifies the escalation receiver that a user might have problems completing their assigned task on time.

<!-- image -->