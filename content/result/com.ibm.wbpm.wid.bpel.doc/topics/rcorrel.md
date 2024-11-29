<!-- image -->

# Correlation tab: BPEL process editor

Use the settings on this page to associate one of the
process artifacts listed below with a specific correlation set.

- Receive activity
- Reply activity
- Invoke activity
- Receive case element
- OnEvent element within an EventHandler
- Receive case element within a receive choice activity

- Send
- Choose this if this set is to be used for outgoing messages.

- Receive
- Select this if this set is to be used for incoming messages.

- Both
- Choose this when the correlation set can be used for either incoming
or outgoing messages.

- No
- Select No if the correlation set will be always initialized
by another activity (which must have been run previously).

- Yes
- Select Yes if this is the first time this correlation
set has been run, and this is when the messages that will link this
user to this workflow are to be stored.

- Join
- Select Join if multiple activities can initialize the
correlation set. This is especially useful if you are designing a
process with multiple parallel receives, and you are not sure which
one will run first. If you specify Join for both of them, then the
first one to run will initiate the correlation set, and the second
will use the existing value.

## Related concepts

- Correlating BPEL processes

## Related reference

- Defaults tab: BPEL process editor
- Description tab: business state machine editor