# Triggers for recovery

## Situations from which solution recovery is necessary

Solution
recovery is the process of returning the system to a state from which
operation can be resumed. It encompasses a set of activities that
address system failure or system instability that can be triggered
by unforeseen circumstances.

You may need to perform solution
recovery activities for the following circumstances:

- Hardware failure Abnormal termination or system down
can be caused by a power outage or catastrophic hardware failure.
This can cause the system (all if not most JVMs) to stop.
In
the case of a catastrophic hardware failure, the deployed solution
may enter an inconsistent state on restart.
Hardware failures
and environmental problems also account for unplanned downtime, although
by far not as much as the other factors.
You can reduce the
likelihood of hardware failures and environmental problems by using
functions such as state-of-the-art LPAR capabilities with self-optimizing
resource adjustments, Capacity on Demand (to avoid overloading of
systems), and redundant hardware in the systems (to avoid single points
of failure).
- System is not responsiveNew requests continue to flow
into the system but on the surface it appears that all processing
has stopped.
- System is unable to initiate a new BPEL process instanceThe
system is responsive and the database seems to work correctly. Unfortunately,
the new BPEL process instance creation is failing.
- Database, Network or Infrastructure Failure In the case
of fundamental infrastructure failure, the solution may require administration
to restart/resubmit business transactions after the infrastructure
failure is resolved.
- Poor tuning or a lack of capacity planning System is
functional but is severely overloaded. Transaction time-outs are reported
and there is evidence of an overflow of the planned capacity.
Incomplete
capacity planning or performance tuning can cause this type of solution
instability.
- Defects in application module development The modulesthat are part of a custom developed solution can have bugs. Thesebugs can result in solution instability and failed services. Bugsin a custom developed solution can result from a variety of situations,including (but not limited to) the following:

The modules
that are part of a custom developed solution can have bugs.  These
bugs can result in solution instability and failed services.

Bugs
in a custom developed solution can result from a variety of situations,
including (but not limited to) the following:

    - Business data that was not planned for or unforeseen by the application
design.
    - An incomplete error handling strategy for the application design.A
detailed error handling design can reduce solution instability.
- WebSphere® software
defect A defect in the WebSphere product
causes a backlog of events to process or clear.