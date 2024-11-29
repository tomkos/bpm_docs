# Subscribing to Blueworks Live processes in the Process Designer

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

## Procedure

1. In the designer, go to the library and click the plus sign next to
Processes, and click Blueworks Live
Subscription.
2. If you are not using the default Blueworks Live server, specify the URL.
Enter the client ID and client secret created by the Blueworks Live admin and click
Next. For more information, see Blueworks Live API.
3 Click the Blueworks Live space that you want and select the processes to subscribe to. The processes are listed alphabetically. You can search for specific spaces by name, and youcan search for specific processes by name or by selecting their space. To select multiple spaces,use CTRL + click . To open a Blueworks Live process in Blueworks Live , click the preview iconnext to the process name.Restrictions:
    - You can subscribe only to Blueworks Live processes that have at
least one snapshot. If you select a process that does not have a snapshot, you are notified and the
subscription is not created.
    - You can subscribe only to Blueworks Live processes that have a
process diagram. Processes without diagrams are not displayed in the list.
4. On the Summary page, verify the list of Blueworks Live processes shown. If you
want the process names that are displayed in Process Designer to be different from the Blueworks Live process names, type the
new names.

## Results

Blueworks Live processes that
you subscribe to are displayed when you expand the Processes category in the library. If you go to
the All category and click to see all library items in the current process application, Blueworks Live items are marked with a
Blueworks Live tag.

| Blueworks Live element                         | New element created in Business Automation Workflow                                                                 |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Process                                        | Process                                                                                                             |
| Milestone                                      | Timing interval created for each interval. Tracking group created to contain all timing intervals in process.       |
| Normal activity                                | System task implemented by the default system service                                                               |
| User task                                      | Inline user task. System task implemented by the default system service, if not assigned to a swimlane participant. |
| Decision task                                  | Decision task implemented by a new service flow                                                                     |
| Service task                                   | System task implemented by a new service flow                                                                       |
| Subprocess                                     | Subprocess                                                                                                          |
| Linked subprocess                              | New process created for linked-to process, with its own subscription                                                |
| Parallel gateway                               | Parallel gateway                                                                                                    |
| Exclusive gateway                              | Exclusive gateway                                                                                                   |
| Inclusive gateway                              | Inclusive gateway                                                                                                   |
| Swimlane participant                           | Team                                                                                                                |
| Process inputs                                 | Included in process documentation                                                                                   |
| Activity inputs                                | Included in activity documentation                                                                                  |
| Process outputs                                | Included in process documentation                                                                                   |
| Activity outputs                               | Included in activity documentation                                                                                  |
| Start event                                    | None start event                                                                                                    |
| Timer start event                              | If the timer start event is the only start event in the diagram, a none start event is created.                     |
| Message start event                            | Message start event                                                                                                 |
| Message event                                  | Message receiving event                                                                                             |
| Timer event                                    | Timer event                                                                                                         |
| End event (default)                            | End event                                                                                                           |
| Error end event                                | Error end event                                                                                                     |
| Message end event                              | Message end event                                                                                                   |
| Message boundary event                         | Message boundary event                                                                                              |
| Timer boundary event                           | Timer boundary event                                                                                                |
| Error boundary event                           | Error boundary event                                                                                                |
| Escalation boundary event                      | No corresponding element created                                                                                    |
| Loop marker: Simple loop                       | Simple loop                                                                                                         |
| Loop marker: Multi-Loop                        | Multi-instance loop                                                                                                 |
| Documentation (activity)                       | Documentation for activity                                                                                          |
| Documentation (process)                        | Documentation for process                                                                                           |
| Activity details (cost, business owners, etc.) | Included in activity documentation                                                                                  |
| Process details (cost, business owners, etc.)  | Included in process documentation                                                                                   |
| Tags                                           | No corresponding element created                                                                                    |
| Policies                                       | No corresponding element created                                                                                    |
| Attachments                                    | No corresponding element created                                                                                    |

## What to do next

If you subscribe to Blueworks Live processes and need to
change those processes later, you can open the processes in Blueworks Live directly from Process Designer. Open the subscription and click Open
Process in Blueworks Live. You can make the required changes in both Blueworks Live and Process Designer, and then reset the subscription date so that
you know your process application is in sync with Blueworks Live. Make sure to subscribe to
only those Blueworks Live
processes that you want included in the process application.

To find out if other people have updated the Blueworks Live process, see Managing changes for Blueworks Live processes.