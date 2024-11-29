# Adding an activity with a new process

You can add a case activity and implement it with a new process that is created locally
in the same case solution as the activity. You can manage and deploy your process and case solution
together.

The new process has full access to the case and
activity properties.

## Before you begin

- A legacy solution created in Case Builder, which you have promoted to a
workflow project.
- A new case solution that you created in Workflow Center.
- A case type is added to the case solution.

## Procedure

To add an activity with a new process:

1. In Case Builder, open the solution that contains
the case type to which you want to add the activity.
2. Click the Case Types tab.
3. Open the case type and then click Activities.
4. On the Activities page, click Add Activity > Activity with New Process.

Tip: If you want to add the process as a subactivity inside a container activity, open
the container activity first. Then, click Add Subactvity > Subactivity with New Process.
5 On the General page, specify the name, unique identifier, and description,define how the activity starts, assign the activity to a set, and select a Process Task DetailsAdapter. To define how the activity starts, choose one of the following options: If you select the Discretionally option, the activity must be added to acase programmatically or by the caseworker in Case Client . To select a Process Task Details Adapter, expand Process Task DetailsAdapter and choose an item from the drop-down list. By default, the Process Task DetailsAdapter page is already selected when a BPM process task is opened for a parent case activity. Youcan create your own Task Details pages from the default Process Task Details Adapter page and addmore case widgets to the page (such as the Case Information widget).Note: When a page is created fora BPM process activity, it must contain both the Task toolbar widget and the website Viewerwidget.

To define how the activity starts, choose one of the following options:

    - Automatically
    - Manually
    - Discretionally

If you select the Discretionally option, the activity must be added to a
case programmatically or by the caseworker in Case Client.

6. On the Preconditions page, define any preconditions that are required
before the activity can start.
An example of a precondition is when a document is filed in the case and the document is then
passed to the process as an initiating attachment.
7. On the Activity Properties page, define the activity properties.

These properties are accessed from the new process. The properties are persisted on the content
object, which is created along with the activity and is useful for when the activity can be started
multiple times and the solution needs to capture some data that is specific to each process
instance.
8. Click OK and then click Save to finish creating
the new activity.

## Results

In addition to the new activity, Case Builder also creates the new process to implement the
activity.

A content object is also created to contain the case
and activity properties.

The process runs when the activity starts, which is based on the specified precondition for the
activity. If you delete the case activity, the associated process is also deleted.

## What to do next

1. In Case Builder, hover the
cursor over the activity with the process, and then click Open Workflow
Designer.
2. Define the process in the designer. See the topic Creating a process.

When you have finished defining your process, you can commit, deploy, and test the solution.

You can also test the enhanced capability of the Case Client, which uses role-to-team
mapping to detect and display both case activities and process
tasks.

- Creating flexible case activities

In previous releases, when users initiated case instance activities much later after the case instance creation, the activities began from the default and active (tip) snapshot at the time of initiation.