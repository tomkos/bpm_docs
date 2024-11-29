# Synchronization mode not supported (message CEIEM0015E)

## Cause

- The event source is specifying a synchronization mode that is
not valid. This is indicated by an IllegalArgumentException with the
message "Synchronization mode mode is not valid."
- The event source is specifying a synchronization mode that the
emitter is not configured to support. This is indicated by a SynchronizationModeNotSupportedException
with the message "The emitter does not support the specified synchronization
mode: mode."

## Remedy

- SynchronizationMode.ASYNCHRONOUS
- SynchronizationMode.SYNCHRONOUS
- SynchronizationMode.DEFAULT

If the exception message indicates that the specified
synchronization mode is not supported by the emitter (SynchronizationModeNotSupportedException),
check the emitter factory configuration:

1. In the administrative console, click Service Integration > Common
Event Infrastructure > Event Emitter Factories > emitter\_factory.
Make sure you are viewing the emitter factory used by the event source
application.
2 Check the emitter factory settings to see which synchronizationmodes are supported: Querying transaction modes: Anevent source can programmatically query the supported transactionmodes for a particular emitter by using the isSynchronizationModeSupported()method. Refer to the Javadoc API documentation for more information.
    - If the Support Event Service transmission property is selected,
synchronous mode is supported.
    - If the Support JMS transmission property is selected, asynchronous
mode is supported.
3. If the emitter does not support the synchronization mode you are
trying to use, you must either change the emitter factory configuration
or modify your event source to use a supported synchronization mode.