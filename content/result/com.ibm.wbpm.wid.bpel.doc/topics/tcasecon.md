<!-- image -->

# Adding a collaboration scope

## About this task

Enhanced dynamic workflows are BPEL processes in
which the business logic can be adapted at run time. For example,
the assigned worker may decided to repeat an activity, to launch a
subtask, or to skip some steps in the BPEL process.

If
you decide to model all or part of your business process as a case,
add a collaboration scope to your BPEL process.

## Procedure

1. Select Collaboration Scope in the Human
Workflow palette.
2. Click in the canvas to create a collaboration scope.

Situation
Action

If this is the first time you have added a collaboration
scope to a BPEL process in this project.
The first time you add a collaboration scope to a project,
you'll be prompted to import the data types and interfaces needed
for case handling. Click OK to import them
into your project. The Select a Folder Variable window
opens. Create a new folder or select an existing folder.Note: The
folder variable is of a predefined type (tCaseFolder) that has been
imported into your workspace
The specified folder is used in
Business Space as a container for all information and activities relating
to this case

If you have previously added a collaboration scope to this
project.
The Select a Folder Variable window opens.
Select an existing folder or create a new one. The data types and
interfaces needed for case handling have already been imported into
this project and so this step is not repeated.
3. Set the administrators for the collaboration scope. Administrators
are the people that are allowed to perform the skip and jump actions
at run time.  Click the Administration tab
in the Properties view. An administration task
was automatically created for your collaboration scope. The default
setting is that Everybody is given administrative
control over the case. In realistic situations only certain task owners
should be able to modify the business logic at run time. To change
this setting click the link to the human task on the Administration tab.
In the Human Task editor, click Administrators in
the People Assignment section. In the Properties view
on the Assign People tab select the users or
groups who should have dynamic control over the case model.
4. You can create business logic within your collaboration
scope by dropping activities from the Basic Actions category
in to the collaboration scope. You cannot include the Receive Choice
activity, nor any of the activities from the Structures category
in a collaboration scope. The fork gateway is also not supported by
collaboration scopes.
5 Optional: Define exit criteria for the activitieswithin your collaboration scope. You can build more flexibilityinto the business logic of your case by setting exit conditions forthe activities and tasks in the container. An exit condition is amechanism for automatically skipping or repeating activities, withoutadministrator intervention, if certain conditions are met. Use exitconditions to automatically: It is assumed that you have wired the activities within the container. Note: Exit conditions cannot be overruled by an administrator.For example, if an activity has an exit condition on exit which evaluatesto false, then the activity will repeat, and the administrator cannotinitiate a jump to the next activity. However, if the activity isfailing to complete because an earlier activity requires repetition,then the administrator can request the earlier activity to repeat. An example of when an exit condition canbe used is in review of cases. A medical procedure needs review bya surgeon before a certain step is considered complete. You can usean exit condition on exit at that step to say that the case must bein the reviewed by surgeon state before theprocess can move on to the next step.
    - skip steps if the specified conditions are met, or
    - repeat steps until the specified conditions are met.
    1. Select the activity within the collaboration scope which
will carry the exit condition.
    2. In the Properties view navigate
to the ExitCondition tab.
    3 Define when the evaluation of the exit condition shouldbe performed. In the Evaluate condition fieldselect one of the following options: Note: The exit condition is evaluated on entry only if both offollowing are true: If the activity is reached by a jump, then exit condition evaluationson entry are skipped and the activity commences.
        - on entry - the criteria is evaluated immediately
after the activity is initiated. If the ExitCondition evaluates true,
the activity is skipped, otherwise the activity continues normally.
        - on exit - the criteria is evaluated before
the activity is exited. If the ExitCondition evaluates false, the
activity is repeated, otherwise the activity is completed and outgoing
connectors are evaluated.
        - on both entry and exit - the criteria is
evaluated immediately after the activity is initiated. If the ExitCondition
evaluates true, the activity is skipped. If the ExitCondition evaluates
false at entry, then the activity is run normally. When the activity
is complete the ExitCondition is evaluated again. The activity is
repeated if the condition evaluates as false, otherwise the activity
is finished and outgoing connectors are evaluated.
        1. Either on entry or on both entry
and exit is selected as the Evaluate condition,
and
        2. the activity is reached by a modeled link.
4. Define the condition that must be met. Define
the condition by setting the Expression language and
then stipulating the criteria. If you choose No Expression as
the Expression language, you can click Create
a New Condition in the Condition field
to launch the expression builder and compose a condition yourself.
The other choices in the Expression Language list
are very similar to the options described in the Expiration tab:
BPEL process editor topic.

- BPEL processes and IBM Business Automation Workflow cases

Case handling is an alternative way to handle knowledge-intensive business flows. It seeks to combine operational flexibility with well-defined procedures.