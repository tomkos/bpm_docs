# Examine the Advanced HR Open New Position process

You should see the Advanced HR Open New Position process open in the process diagram, as shown in
the following figure:

You will note the following details in the process:

- In the diagram, the process begins with the Start event and terminates at
the End event.
- The first task named Submit job requisition has several user interfaces
that prompt the hiring manager for specific information about the job requisition.
- If general manager (GM) approval is required, the next task in the process is Approve
/ reject requisition.
- If the general manager approves the job requisition, or if the job requisition does not require
the general manager's approval, the next step is FindCandidatesList.
This step is automatic and it calls an Advanced Integration Service that attempts to find suitable
job candidates from a number of (simulated) HR back-end systems or from a (simulated) external
agency.
- If no candidates are found, or if the general manager rejects the job requisition, the next step
is Notify hiring manager, which informs the job requester that no candidate
was found or the general manager does not accept the job requisition.
- If at least one candidate is found, the candidate (or a list of candidates) is presented to thehiring manager in the task Select candidate for interview . The hiring managercan now take one of the following actions:
    - Invite one of the candidates to an interview.
    - Ask for a new list of candidates in the Requesting new list task (in
which case the task FindCandidatesList is run again).
    - End the process because there is no suitable candidate available at this time.

## Related concepts

- Overview of the Advanced Hiring tutorial

## Related tasks

- Managing access to the Hiring Sample Advanced process application
- Verifying access to the Hiring Sample Advanced process application
- Activating the Hiring Sample Advanced process application
- Opening the Hiring Sample Advanced process application
- Running the process in the Process Designer Inspector view