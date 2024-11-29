<!-- image -->

# Configuring the cleanup service and cleanup jobs

## Before you begin

## About this task

You want completed instances to be deleted automatically
after keeping them for a while. There is a separate cleanup service
for the Business Flow Manager and for the Human Task Manager. For
each of them, you must first enable the service and define the service
parameters, such as the schedule, maximum duration of the cleanup,
and the database transaction size. Then you can define cleanup jobs
for sets of templates and define the end states and the duration that
an instance must be in to qualify for deletion.

The Human Task
Manager cleanup service only deletes stand-alone human tasks, but
when the Business Flow Manager cleanup service deletes a BPEL process,
it also deletes all of the child processes and inline human tasks
that are contained in the process. The cleanup user ID specified for
the Business Process Choreographer configuration must be in the business
administrator role.

## Procedure

1 Configure the cleanup service for the Business FlowManager .
    1. To configure the cleanup service,
in the administrative console, click Servers > Clusters > WebSphere
application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer,
and click Business Flow Manager.
    2 Chooseone of the following options:
        - To change settings without having to restart the cluster, select
the Runtime tab.
        - To make changes that will only have an effect after the cluster
is restarted, select the Configuration tab.
3. In the Additional properties section,
click Cleanup Service Settings.
4. If the cleanup service is not enabled, select Enable
cleanup service. For a cluster configuration,
the cleanup service will be scheduled to run on one of the cluster
members of the cluster it is configured on.
5. For Frequency,
specify the time and frequency when the Business Flow Manager cleanup
service will run. Enter a WebSphere crontab format
string, which defines the start of a low load time slot. For
example, to run the cleanup service every night at eleven o'clock,
use the default value of 0 0 23 * * ?  .
6. For Maximum duration,
enter the maximum time that the cleanup is allowed to run. The
default is 120 minutes. Make sure that the maximum duration is shorter
than the time interval specified by the frequency.
7. For Transaction slice, enter
the number of BPEL process instances that will be deleted in each
database transaction. The
default value is 10. Because the value affects the performance of
the cleanup service, it is worth trying different values. Depending
on the size of the human tasks being deleted, you might be able to
increase the slice size to increase the performance. However, if you
get transaction timeouts, you should reduce the value.
8. Save your changes.
2 Add a new cleanup job for the Business Flow Manager .

1. In the administrative console, on the Business
Flow Manager page, click Cleanup Service Jobs.
2. To create a new cleanup job, click Add.
3. If this is not the only cleanup job, for Order
Number, you can select a sequence number that determines
the order that the jobs will be run, starting with number zero.
4. For Cleanup Job, enter a name
for the job.
5. For Templates, either enter the
name of one or more BPEL process templates (one per line) whose instances
(including any inline human tasks) will be deleted, or enter an asterisk
('*') to specify all BPEL process templates.
6 For Restrict cleanup to instances in thefollowing states , select one or more of the followingstates:
    - FINISHED
    - TERMINATED
    - FAILED
7. For Duration until deletion,
specify how long an instance must be in one of the specified states
before it becomes eligible for deletion by the cleanup job. Enter
integers in the following fields: Minutes, Hours, Days, Months,
and Years. The default is two hours.
8. Click Apply or OK.
9. Save your changes.
10. If necessary, repeat this step to define more cleanup
jobs for BPEL process instances.
3 Configure the cleanup service for the Human Task Manager .

1. To configure the cleanup service,
in the administrative console, click Servers > Clusters > WebSphere
application server clusters > cluster\_name,
then on the Configuration tab, in the Business Process Manager section, expand Business Process Choreographer,
and click Human Task Manager.
2. If the cleanup service is not enabled, select Enable
cleanup service. For a cluster configuration,
the cleanup service will be scheduled to run on one of the cluster
members of the cluster it is configured on.
3. For Frequency, specify the time
and frequency when the Human Task Manager cleanup service will run.
Enter a WebSphere crontab format string, which
defines a low load time slot. Tip: If the cleanup
service for the Business Flow Manager is also enabled, specify a schedule
that does not overlap with the time window defined by the values specified
in steps 1.e and 1.f.
For example, if the Business Flow Manager cleanup service starts every
night at one o'clock, and can run for up to two hours, you can specify
that the cleanup service for the Human Task Manager runs every night
at three o'clock by entering the value 0 0 3 * * ?.
4. For Maximum duration, enter the
maximum time that the cleanup is allowed to run. The default
is 120 minutes. Make sure that the maximum duration is shorter than
the time interval specified by the frequency.
5. For Transaction slice, enter
the number of human task instances that will be deleted in each database
transaction. The
default value is 10. Because the value affects the performance of
the cleanup service, it is worth trying different values. Depending
on the size of the human tasks being deleted, you might be able to
increase the slice size to increase the performance. However, if you
get transaction timeouts, you should reduce the value.
6. Save your changes.
4 Add a new cleanup job for the Human Task Manager .

1. In the administrative console, on the Human
Task Manager page, click Cleanup jobs.
2. To create a new cleanup job, click Add.
3. If this is not the only cleanup job, for Order
Number, you can select a sequence number that determines
the order that the jobs will be run, starting with number zero.
4. For Cleanup Job, enter a name
for the job.
5. For Templates, either enter the
name of one or more stand-alone human task templates (one per line)
whose instances will be deleted, or enter an asterisk (*)
to specify all stand-alone human task templates.  To specify
a namespace for a task template, append it in brackets, for example, myTaskTemplate
(http://bpc/samples/task/).Note: The Human Task Manager
cleanup service can also delete inline invocation tasks that are started
using the Human Task Manager API.
6 For Restrict cleanup to instances in thefollowing states , select one or more of the followingstates:
    - FINISHED
    - TERMINATED
    - FAILED
    - INACTIVE
    - EXPIRED
7. For Duration until deletion,
specify how long an instance must be in one of the specified states
before it becomes eligible for deletion by the cleanup job. Enter
integers in the following fields: Minutes, Hours, Days, Months,
and Years. The default is two hours.
8. Click Apply or OK.
9. Save your changes.
10. If necessary, repeat this step to define more cleanup
jobs for stand-alone human task instances.
5. If you made the changes on the Configuration tab,
restart the cluster to activate the changes.

## Results

<!-- image -->