<!-- image -->

# Compensation handling in BPEL processes

You can define compensation for long-running processes
and for microflows in your process model.

- Compensation handling in BPEL microflows

Compensation for microflows is also known as technical compensation. This type of compensation is triggered when the transaction, or the activity session, that contains the microflow is rolled back.
- Compensation handling in long-running BPEL processes

Compensation for long-running processes is also known as business-level compensation. The compensation logic can be defined on the scope level, for invoke activities, or for human task activities. This means that either a single invoke activity or human task activity, or a set of activities in a scope can be compensated.