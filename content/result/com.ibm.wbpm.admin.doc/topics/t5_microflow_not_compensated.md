<!-- image -->

# A microflow is not compensated

## Resolution

1. Log in to the Business Process Choreographer Explorer and click Failed Compensations to check whether the compensation
service has failed and needs to be repaired.
2. The compensation of a microflow is triggered only when the transaction
for the microflow is rolled back. Check whether this is the case.
3. The compensationSphere attribute of the microflow must be set
to required.
4. A compensation service is run only if the corresponding forward
service has not participated in the microflow's transaction. Ensure
that the forward service does not participate in the navigation transaction,
for example, on the reference of the process component, set the Service
Component Architecture (SCA) qualifier suspendTransaction to True.