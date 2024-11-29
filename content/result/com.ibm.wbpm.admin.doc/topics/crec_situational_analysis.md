# Situational analysis

- Abnormal termination or system downA power outage or catastrophic
hardware failure has caused the system (all if not most JVMs) to stop.
- System is not responsiveNew requests continue to flow into
the system but on the surface it appears that all processing has stopped.
- System is functional but is severely overloadedTransaction
time-outs are reported and there is evidence of an overflow of the
planned capacity.
- System is unable to initiate new process instanceThe system
is responsive and the database seems to work correctly.  Unfortunately,
new process instance creation is failing.