# Automatically starting the user's next task

## About this task

For example, a customer service
agent might be assigned a task for opening a new customer account
that is followed immediately by a task for taking the new customer's
order. Instead of having the user return to his or her task list to
retrieve the second task after the first one completes, you can designate
that the coach for the second task opens immediately upon completion
of the first task.

## Procedure

1. Open the process that you want to work with.
2. To configure an activity to automatically start the following task, go to the
Implementation tab of the first task in the sequence and select
Automatically flow to next task.  In Process Portal, if the
owner of the first task is the same as the owner of the second task, the second task starts
automatically when the first task is complete.
3 In the following task, set the assignment to be the last user: selectLane from the Assign To list and select Last User fromthe User Distribution list in the Assignments section of the properties for the activity. Activities are still considered to be sequential even if they are separated by synchronousactions such as exclusive gateways or tracking points. However, there are a number of scenarioswhere the second activity in a sequence cannot be automatically started even if the check box isselected on the first task:

Activities are still considered to be sequential even if they are separated by synchronous
actions such as exclusive gateways or tracking points. However, there are a number of scenarios
where the second activity in a sequence cannot be automatically started even if the check box is
selected on the first task:

    - When the second task in the sequence is a system task and the Optimize execution for
latency check box is not selected in the process. Enable Optimize execution
for latency in the BPD model for autoflow to work.
    - When an intermediate timer event or an intermediate message event follows the first activity in
the sequence.
    - When the first activity flows to multiple tasks assigned to the same user, for example in a
multi-instance loop or a parallel (split) gateway.
    - If the task is being tested in the Inspector.
    - If the elapsed time between the end of the first task and the arrival of the token at the next
task is greater than the autoflow-timeout setting. The value for
thread-reuse-duration should be less of equal to the value of
autoflow-timeout. By default, the
autoflow-timeout is set to 3 seconds. To change the default 3-second value of the
autoflow-timeout setting, you can add the following code to the
100Custom.xml file (where new\_value is the new value in
seconds):<properties>
     <server>
          <bpd-engine>
               <autoflow-timeout merge="replace">new\_value</autoflow-timeout>
          </bpd-engine>
     </server>
</properties>Information about modifying the
100Custom.xml file is found in the topic Creating a 100Custom.xml configuration file.