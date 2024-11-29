# Administering processes with Process Inspector

## Procedure

1 Open the Process Inspector from the Process Admin Consolein one of the following ways:
    1. Click the Process Inspector toolbar
link.
    2. Click an item in the Process Status Summary on
the Server Admin home page.
2. In the search panel, define the search criteria for the
Process Inspector. Each section in the search panel has
an AND relationship with the other sections.
For example, to search for an active process instance of
the MyProcessApp (MPA) that is overdue, you select the Active status
check box, the Overdue severity type check box, and the MyProcessApp
(MPA) check box. You might select fewer criteria but the list of instances
in the results might be longer. Tip: Selecting no check
boxes in a section is the same as selecting all of the check boxes.
That is, if you want to see all process instances regardless of their
status, you can select all of status check boxes or clear all of them.

Within a section, each element has an OR relationship except
for the last modified date section. Each field in that section has
an AND relationship.For example, if you know that
a process instance completed three days ago, set the From date in
the last modified section to three days ago. You might narrow the
results by setting the To date to two days ago so that the results
show only the process instances that changed three days ago.
3. Click Search. The
results panel lists the process instances that fulfill all of the
criteria. The list of process instances is a snapshot. It is not automatically
updated to include any process instances that are created after you
do the search.
4. If you get too many results, update the search panel with
additional information and click Refresh.
5 In the results panel, select the process instance or processinstances that you are interested in viewing. You can selectinstances in two ways: The details panel updates to display informationabout the selected instance or instances. If you selected morethan one instance, the details panel lists their status along withany actions that are common to all of the selected instances. Ifyou selected one instance, the details panel displays informationabout the process instance. This information includes the activitiesand tasks that are associated with the instance, the data of the instanceand other details.

- If you click the instance text, you clear any existing selected
instances and select the clicked instance.
- If you hover on the instance text, a check mark becomes visible.
If you then click the check mark, the clicked instance is added to
any existing selected instances.

If you selected more
than one instance, the details panel lists their status along with
any actions that are common to all of the selected instances.

If
you selected one instance, the details panel displays information
about the process instance. This information includes the activities
and tasks that are associated with the instance, the data of the instance
and other details.

6. Use the information in the details panel to resolve issues
with the process instance. For example, you can override
timers to move an instance onto its next step, edit the instance data
to correct a problem, or open a task to examine and fix task data.

- Process Inspector

The Process Inspector is an administrative tool that you can use to investigate and resolve runtime problems with process instances.
- Runtime states for activities in process applications

At run time, different events cause activities to transition between various states. And the state that an activity is in determines which actions can be performed.
- Troubleshooting errors and failures in a failed process instance

Using the Process Inspector, you can take corrective actions on process instance that have failed or are in an error state one at a time or in bulk across multiple locations. The best corrective action for you to take depends on the nature of the failure.
- Actions in the Process Inspector

You can use actions in the Process Inspector to administer process instances and their components.