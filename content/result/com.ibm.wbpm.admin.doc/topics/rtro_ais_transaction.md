# AIS does not participate in the same transaction as business
process

## Overview

BPD process navigation is not part
of the same transaction as an invoked AIS. If a BPD process navigation
invokes an AIS and then experiences a runtime failure (not an error
in the business process logic),  the process navigation becomes unavailable
while the AIS is running. When the AIS commits its transaction, it
cannot indicate to the process navigation that the AIS has concluded.
When the process navigation later resumes, the AIS is invoked again
because the process navigation is unaware of the previously successful
invocation.

## Resolving the problem

To resolve this problem,
place checks within the AIS application logic to ensure that a second
invocation does not corrupted the state of an application.