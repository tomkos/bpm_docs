<!-- image -->

# Handling Business Process Choreographer EJB API exceptions

## About this task

However, it is common practice to handle only a subset of the
exceptions specifically and to provide general guidance for the other potential
exceptions. All specific exceptions inherit from a generic ProcessException
or TaskException. Catch generic exceptions with a final catch(ProcessException) or catch(TaskException) statement.
This statement helps to ensure the upward compatibility of your application
program because it takes account of all of the other exceptions that can occur.