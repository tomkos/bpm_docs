# Promoting case solutions to workflow projects

## About this task

## Procedure

To promote a solution to a workflow project:

1. Launch the Case Builder.
2. On the solution that you want to promote, click the Commit all of the components of
the solution icon.
3. From the menu of the solution, select Promote to Workflow Project.

When the solution has been successfully promoted, an Promotion successful
icon appears on the solution and a Solution Promotion Status dialog box opens.
4. In the Solution Promotion Status dialog box, open the Workflow Center and
work with the new workflow project.

When you next log into Case Builder, the solution will no longer
be displayed.
5. Open the promoted solution from the Workflow Center and
click Redeploy All to deploy the solution.
6. If you want to view the promotion logs, select Show promotion logs from
the solution menu.
It is particularly important to view the promotion logs if the promotion was not successful,
as indicated by an Promotion failed icon on the solution.Note: A process team
is not synchronized correctly with a case solution role if the CB\_PrimaryQueue attribute is missing
from the case solution role definition. See Troubleshooting IBM Case Manager system upgrades.
If a role does not have CB\_PrimaryQueue attribute, and when the solution is
promoted or when the security manifest configuration is applied or manage roles in Case Client is
performed, the workflow process team synchronization is skipped for the role.