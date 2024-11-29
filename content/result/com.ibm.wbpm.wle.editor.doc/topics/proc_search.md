# Searching for process instances in the Inspector

You can search for and view your previously run and currently running process instances
in the Inspector. You can manage running instances and interact with them.

Developers who have read access to the project can use the Inspector to work with instances and
tasks for debugging purposes.

## About this task

## Procedure

1. Open a process.
2. Click Search
, which opens the Inspector mode.
3. In the search panel, define the search criteria for the
 Inspector. Each section in the search panel has an AND relationship
with the other sections.For example, to search for
an active process instance of  that is overdue, you select the Active
status check box and the Overdue severity type check box. Tip: Selecting no check boxes in a section is the same as selecting
all of the check boxes. That is, if you want to see all process instances
regardless of their status, you can select all of status check boxes
or clear all of them.
Within a section, each
element has an OR relationship except for the last modified date section.
Each field in that section has an AND relationship.For
example, if you know that a process instance completed three days
ago, set the From date in the last modified section to three days
ago. You might narrow the results by setting the To date to two days
ago so that the results show only the process instances that changed
three days ago.
4. Click Search. The
results panel lists the process instances that fulfill all of the
criteria. The list of process instances is a snapshot. It is not automatically
updated to include any process instances that are created after you
do the search.
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

6. You can click an instance to select it, and run or debug
the instance in the panel on the right.

## What to do next