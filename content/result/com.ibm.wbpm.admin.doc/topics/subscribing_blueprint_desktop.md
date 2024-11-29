# Subscribing to Blueworks Live processes
in the desktop Process Designer (deprecated)

## Before you begin

- To subscribe to Blueworks Live processes,
you must have or create a Blueworks Live account.
See http://www.blueworkslive.com.
- The Blueworks Live API
must be enabled in the account.
- If you are not using the default Blueworks Live server,
ensure that the administrator has imported the Blueworks Live signer
certificates into the IBM Business Automation Workflow server
truststore before you create subscriptions to Blueworks Live processes.
See Adding a signer certificate to the default signers
keystore and IBM Business Automation Workflow (BPM)
cannot connect to Blueworks Live due to
a missing or expired certificate. This step is not required
if you use the default Blueworks Live server.

## About this task

- You cannot subscribe to Blueworks Live processes
from a toolkit in Process Designer. Blueworks Live subscriptions
are available only from process applications.
- You cannot subscribe to processes in Process Designer if you are using a Blueworks Live user account that has single sign-on enabled or
IBMid enabled.

## Procedure

1. In desktop IBM Business Automation Workflow, open
the Designer view.
2. If you have not already done so, set the Blueworks Live preferences
for IBM Business Automation Workflow by
going to File > Preferences > Business Automation Workflow > Blueworks Live and entering the Blueworks Live server
URL https://www.blueworkslive.com and the email address
that you use as your user ID to log into Blueworks Live.
3. In the library in the Designer view, click the plus sign
next to Blueworks Live Processes.
4. Enter the password that you use to log in to Blueworks Live and click Next.
5 Select the check boxes next to the processes that you wantto subscribe to. If the list of processes displayed istoo long, you can filter the list of processes by typing part or allof the space name containing the processes you are looking for. Topreview a Blueworks Live processin a web browser, click the preview icon next to the process name.Restrictions:
    - You can subscribe only to Blueworks Live processes
that have at least one snapshot. If you select a process that does
not have a snapshot, you are notified and the subscription is not
created.
    - You can subscribe only to Blueworks Live processes
that have a process diagram. Processes without diagrams are not displayed
in the list.
6. On the Summary page, verify the list
of Blueworks Live processes
shown. If you want the subscription names that are displayed in Process Designer to
be different from the Blueworks Live process
names, type the new names in the BPD name fields
for the relevant processes.

## Results

Blueworks Live processes
that you subscribe to are displayed in the Blueworks Live Processes
category in the library. The Blueworks Live process
names that are longer than 64 characters are truncated in the list.
If you go to the All category and click to see all library items in
the current process application, Blueworks Live items
are marked with a Blueworks Live tag.

| Blueworks Live element                         | New element created in Business Automation Workflow                                                                                                                                             |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process                                        | BPD                                                                                                                                                                                             |
| Milestone                                      | Timing interval created for each interval. Tracking group created to contain all timing intervals in process.                                                                                   |
| Normal activity                                | User task implemented by a new heritage human service, if assigned to a swimlane participant. System task implemented by the default system service, if not assigned to a swimlane participant. |
| User task                                      | User task implemented by a new heritage human service                                                                                                                                           |
| Decision task                                  | Decision task implemented by a new decision service                                                                                                                                             |
| Service task                                   | System task implemented by a new general system service                                                                                                                                         |
| Subprocess                                     | Subprocess                                                                                                                                                                                      |
| Linked subprocess                              | New BPD created for linked-to process, with its own subscription                                                                                                                                |
| Parallel gateway                               | Parallel gateway                                                                                                                                                                                |
| Exclusive gateway                              | Exclusive gateway                                                                                                                                                                               |
| Inclusive gateway                              | Inclusive gateway                                                                                                                                                                               |
| Swimlane participant                           | Team                                                                                                                                                                                            |
| Process inputs                                 | Included in process documentation                                                                                                                                                               |
| Activity inputs                                | Included in activity documentation                                                                                                                                                              |
| Process outputs                                | Included in process documentation                                                                                                                                                               |
| Activity outputs                               | Included in activity documentation                                                                                                                                                              |
| Start event                                    | None start event                                                                                                                                                                                |
| Timer start event                              | If the timer start event is the only start event in the diagram, a none start event is created.                                                                                                 |
| Message start event                            | Message start event                                                                                                                                                                             |
| Message event                                  | Message receiving event                                                                                                                                                                         |
| Timer event                                    | Timer event                                                                                                                                                                                     |
| End event (default)                            | End event                                                                                                                                                                                       |
| Error end event                                | Error end event                                                                                                                                                                                 |
| Message end event                              | Message end event                                                                                                                                                                               |
| Message boundary event                         | Message boundary event                                                                                                                                                                          |
| Timer boundary event                           | Timer boundary event                                                                                                                                                                            |
| Error boundary event                           | Error boundary event                                                                                                                                                                            |
| Escalation boundary event                      | No corresponding element created                                                                                                                                                                |
| Loop marker: Simple loop                       | Simple loop                                                                                                                                                                                     |
| Loop marker: Multi-Loop                        | Multi-instance loop                                                                                                                                                                             |
| Documentation (activity)                       | Documentation for activity                                                                                                                                                                      |
| Documentation (process)                        | Documentation for process                                                                                                                                                                       |
| Activity details (cost, business owners, etc.) | Included in activity documentation                                                                                                                                                              |
| Process details (cost, business owners, etc.)  | Included in process documentation                                                                                                                                                               |
| Tags                                           | No corresponding element created                                                                                                                                                                |
| Policies                                       | No corresponding element created                                                                                                                                                                |
| Attachments                                    | No corresponding element created                                                                                                                                                                |

## What to do next

If you subscribe to Blueworks Live processes
and need to change those processes later, you can open the processes
in Blueworks Live directly
from Process Designer.
Right-click the subscription and select Open in Blueworks
Live. You can make the required changes in both Blueworks Live and Process Designer, and
then reset the subscription date so that you know your process application
is in sync with Blueworks Live.
Make sure to subscribe to only those Blueworks Live processes
that you want included in the process application.

To find
out if other people have updated the Blueworks Live process,
see Managing changes for Blueworks Live processes.