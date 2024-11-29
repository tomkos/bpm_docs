# Event is not valid (message CEIEM0027E)

## Cause

- The global instance identifier must be at least 32 characters
but no more than 64 characters in length.
- The severity must be within the range of 0 - 70.

## Remedy

To correct this problem:

1. Check the detailed exception message in the log file to determine
which event property is not valid. For example, this messages indicates
that the length of the global instance identifier (ABC)
is not valid:Exception: org.eclipse.hyades.logging.events.cbe.ValidationException
  : IWAT0206E The length of the identifier in the specified Common 
     Base Event property is outside the valid range of 32 to 64 
     characters.
  Property: CommonBaseEvent.globalInstanceId 
  Value: ABC
2. Correct the event content at the source so it conforms to the
Common Base Event specification.
3. Resubmit the event.