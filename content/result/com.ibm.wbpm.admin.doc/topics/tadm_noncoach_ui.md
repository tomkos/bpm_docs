# Integrating custom web-based user interfaces in Process Portal

## Before you begin

## About this task

## Procedure

- For activities in business processes (BPDs).
    1. Create an external implementation for each custom task
completion UIs that you want to use in Process Portal.
For more information, see Creating an external implementation. Ensure that you specify
the URL for the task completion UI in the URL section.
    2. Implement the activity by using the external implementation.
See Creating an external implementation to implement an activity.
- For human tasks in BPEL processes:

1. Define the user interface for the task.  For
more information, see Defining user interfaces for a human task. Select External
Implementation for use in Process Portal  as
the client type and specify a URL template.

## Results

The custom task completion UI is launched from Process Portal when
a user opens the task from a task list or saved search. The UI always
opens in a new browser window regardless of the setting of the com.ibm.bpm.portal.openTaskInNewWindow mashups
property. For more information about the mashups property, see Configuring custom properties. For the UI to work
correctly, users must allow pop-up windows in their browsers.