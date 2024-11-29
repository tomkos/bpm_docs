# Configuring or disabling the Activity Sweep Custom policy

Every three hundred seconds (five minutes), the SweepHandler, initiated by the Activity
Sweep Custom policy, checks the status of currently working processes and case
activities.

The SweepHandler identifies any failed case activities that are connection failure exceptions and
updates the case activity state from Failed to Working. Then Business Automation Workflow retries to launch the
process again for these case activities.

If any case activity that is associated with a workflow project is in the In Progress state, but
its underlying workflow is in the Completed, Terminated, or Failed state, a SweepHandler updates the
corresponding case activity with the same state in IBM® Business Automation
Workflow.

A case activity and its associated process status might become out of sync because the Content Platform Engine stopped and was restarted or network issues
occurred between two systems while Business Automation Workflow was
making updates.

## About this task

To avoid performance issues, you can configure the policy to run less
frequently or disable the policy.

- To configure the policy to run less frequently, select Policy-Controlled Sweeps > Task and, under Properties, change the value of the
Inter-Sweep Delay property.Note: Ensure the value is greater than
300.
- To disable the policy, select Sweep Policies > Custom Policies > Activity Sweep Custom Policy and clear Enable sweep policy.