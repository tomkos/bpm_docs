<!-- image -->

# ClassCastException when stopping an application containing a microflow

## Reason

When an application is stopped, the classes
contained in the EAR file are removed from the class path. However,
microflow instances that need these classes may still be executing.

## Resolution

1. Stop the microflow process template first. From now on, it is not possible
to start new microflow instances from that template.
2. Wait for at least the maximum duration of the microflow execution so that
any running instances can complete.
3. Stop the application.