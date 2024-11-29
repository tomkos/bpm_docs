# Creating SLAs in Process Designer

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

When
you run instances of your processes, SLA consequences do not trigger
until the associated activity starts or completes. With SLAs you can
report violations and, over time, understand the trend in violations.
Use other methods, such as timer events, to enable Process Portal users
to immediately react to time-based conditions.

The My SLA Overview
dashboard is not exposed by default for Process Portal users.
If you want process participants to see the My SLA Overview dashboard
in their tabs list, you must expose it manually, as described in step 11 of the following procedure. In
that step, you work in Heritage Process Portal and
the result affects both Heritage Process Portal and Process Portal.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open an appropriate process application or toolkit in the Designer view.
3. Click the plus sign next to Decisions and
select Service Level Agreement from the list.
4. In the New Service Level Agreement window,
type a descriptive name for the new SLA and click Finish.
5. Describe the SLA in the Documentation field.
6 In the Trigger section of the window,the default trigger statement is displayed: Whenever thecondition is violated. Complete the following steps:
    1. Click Whenever (displayed in
blue font and underlined) to change the trigger for the SLA.
For example, if you select Violated % of the time
over period, the trigger statement changes to When
the condition was violated 10% of the time over
the last day.
    2. Click 10% of the time and set
the percentage.
    3. Click last day and set the time
frame.
7 In the Condition section of the window,the default condition statement is displayed: The TotalTime (Clock) KPI for <select activities> is greaterthan 1 day . Complete the following steps:

1. Click Single value and choose Single
value, Sum of values over time,
or Average value over time.
2. Click Total Time (Clock) and
choose the key performance indicator (KPI) that you want to use.
3. Click <select activities> and
choose the activities that you want to apply this SLA to.
All activities are displayed under the BPD that they are in.
4. Click Greater than and choose greater
than, less than, or equal
to.
5. Click 1 day and choose Threshold, %
above threshold, % below threshold, Value
above threshold, Value below threshold,
or Value. Then, set more parameters as necessary.
8 In the Consequence section of thewindow, select the check box next to the action that you want to takewhen the specified condition is violated.

1. To choose the Send email option,
click <enter email address> and provide
the address or addresses of the recipients of the notification. Separate
addresses with a comma.
2. To choose the Initiate process option,
click <select process> and select a BPD. IBM Business Automation Workflow displays
the BPDs in the current process application and any BPDs that are
referred to in toolkits. The process that you run as a consequence
of the violation must have the following input variables: 

Input variable
Type
Description

violationRecord 
SLAViolationRecord
Indicates which SLA was violated, to what degree,
and when

 parameters 
XMLElement
Reserved for future use
9. Click Select next to the Expose
to view label and select the team whose members can view
data for this SLA in the My SLA Overview dashboard in Process Portal.
10. Click the Save icon in the toolbar.
11 Expose the My SLA Overview dashboard so thatit is available in Process Portal :

1. In Process Designer,
open the Heritage Process Portal application.
2. Click Performance and then open PM
SLA Overview.
3. In the Exposing section, click Select next
to the Exposed to field
to choose the team whose members can view and use the My SLA Overview
dashboard.  To create a team, click New.
To remove an assigned team, click the X icon
next to the Exposed to field.
4. Save your changes.
12 Test the SLA in the My SLA Overview dashboard in Process Portal . If the dashboard does not display any data, complete one ofthe following steps:

- In the Process Portal application,
select Implementation > Periodic
SLA Update, and click Run now.
- Include the Update All SLA Statuses service from the system
toolkit in a process application, and run the process application
in Process Portal before
you test your SLA.