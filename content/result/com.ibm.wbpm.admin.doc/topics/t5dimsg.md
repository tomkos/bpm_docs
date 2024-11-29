<!-- image -->

# Working with process-related or task-related messages

## About this task

When processes and tasks run, messages are either
displayed in Business Process Choreographer Explorer, or they are
added to the SystemOut.log file and traces. If
the message text provided in these files is not enough to help you
solve your problem, you can use the WebSphere® Application
Server symptom database to find more information. To view Business
Process Choreographer messages, check the activity.log file
by using the WebSphere log analyzer.

## Procedure

1 Start the WebSphere log analyzer. Run one of the following scripts:
    - install\_root/bin/waslogbr.bat
    - install\_root/bin/waslogbr.sh
2. Optional: Click File  >  Update database  > WebSphere Application
Server Symptom Database to check for the
newest version of the symptom database.
3 Optional: Load the activity log.

1 Select the activity log file
    - profile\_root\profiles\profile\_name\logs\activity.log
    - profile\_root/profiles/profile\_name/logs/activity.log
    - profile\_root/profiles/profile\_name/logs/activity.log
2. Click Open.