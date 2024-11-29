# Key performance indicators (KPIs) and service level agreements
(SLAs)

## KPIs

Key performance indicators (KPIs) are
measurements that Business Automation Workflow tracks
at process run time, storing results that you can use to analyze process
and task performance in the Optimizer. Business Automation Workflow includes
the following types of KPIs:

| KPIs          | Description                                                                                                                                                                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Standard KPIs | Located in the System Data Toolkit. By default, most of the standard KPIs are associated with each activity that you add to a BPD diagram. Click the KPIs option in the properties for an activity to see the associated KPIs. Each of these KPIs has default settings that you can change. |
| Custom KPIs   | You can define custom KPIs and associate them with one or more activities in your BPDs.                                                                                                                                                                                                     |

When you run instances of a business process definition
(BPD), Business Automation Workflow tracks
and stores data for configured KPIs in the Business Performance Data
Warehouse. Business Automation Workflow uses
stored KPI data when you run certain types
of historical analyses in the Optimizer. Not all historical analyses
available in the Optimizer rely on data that is generated and stored
because of KPIs.

## SLAs

You can create
service level agreements (SLAs) that
are based on standard and custom KPIs. With SLAs, you establish a
condition for one or more activities that triggers a consequence.
For example, you can create an SLA that causes Business Automation Workflow to send
an email notification when a particular activity takes longer than
expected to run.

When you run instances of your processes, SLA
consequences do not trigger until the associated activity starts or
completes. For example, if you configure an SLA to send an email notification
when a particular activity takes longer than two days to run, Business Automation Workflow does
not send the notification when the violation occurs. Instead, Business Automation Workflow sends
the notification when the activity is complete. Therefore, if the
activity takes three days to complete, Business Automation Workflow sends
the notification then, informing users of the violation. With SLAs
you can report violations and, over time, understand the trend in
violations.

To enable Process Portal users
to immediately react to time-based conditions for one activity, use
a timer event to capture the violation.
If an SLA is not based on time, consider using exposed process values
(EPVs) to model the SLA. To
provide immediate notification of violations, develop the appropriate
implementation for your needs (such as a timer event for an escalation),
and then create an SLA so that you can track and report historical
trends.

SLAs enable in-depth performance analysis over time,
as described in the following table:

| Analysis                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| My SLA Overview dashboard                 | View this report in Process Portal to see the name, description, and status of each configured SLA, and a trend chart of violations for all SLAs or a specified SLA. The My SLA Overview dashboard is not exposed by default for Process Portal users. If you want process participants to see the My SLA Overview dashboard in their tabs list, you must expose it manually, as described in step 10 of Creating SLAs in Process Designer. |
| Custom SLA reports (deprecated)           | Use SLA data that is stored in the Business Performance Data Warehouse to create custom reports using Business Automation Workflow or a third-party tool. You can use the SLASTATUS and the SLATHRESHOLDTRAVERSALS database views to query the data..                                                                                                                                                                                       |
| Historical analysis in the Optimizer view | When you are running scenarios, choose the SLA visualization mode to display results that are based on SLA violations.                                                                                                                                                                                                                                                                                                                      |