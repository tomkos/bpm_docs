# Controlling the number of items displayed in the Event Manager
monitor

## About this task

When there are many event jobs in the database, the
query for the event jobs might 				take a long time to run and require
a lot of server resources. Thus, controlling the 				number of items
displayed in the Event Manager monitor can reduce server and 				database
load. Setting the event-job-threshold option
has the 				following effects:

- If no threshold or no valid threshold is defined, a threshold
of 100 is 					used.
- If a threshold larger than 0 is configured and the number of existing
event jobs exceeds this 					threshold, the resulting list is limited
and a Show All button is displayed at 					the end of the list. Clicking
the button retrieves all event jobs.
- If 0 is configured as threshold, no query runs. Therefore, use
the 						event-job-threshold=0 option if you
don't need to list 					event job details and just want to administer
the displayed schedulers by using 					the button toolbar.
- If a threshold less than 0 is configured, the query is not limited,
and all event jobs are 					listed.

## Procedure

To change the threshold, complete the following steps:

1. In the appropriate 100Custom.xml files
in Workflow Server and Workflow Center (see
the topic Location of 100Custom configuration files for
their location), specify the threshold by using the following format:
 <server>    	    	
	<process-admin-console merge="mergeChildren"> 
		<event-job-threshold>100</event-job-threshold>
	</process-admin-console>
</server>
2. Restart the server.