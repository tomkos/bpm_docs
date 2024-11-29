<!-- image -->

# Stopping and starting process and task templates using administrative
scripts

## Before you begin

- Include the wsadmin -user and -password options
to specify a user ID that has operator or administrator authority.
- Run the script in connected mode,
that is, do not use the wsadmin -conntype none option.
- If you are not working with the default
profile, use the wsadmin -profileName profile option
to specify the profile.

## About this task

## Procedure

1. Change to the Business Process Choreographer admin directory.
cd install\_root\ProcessChoreographer\admin
cd install\_root/ProcessChoreographer/admin
2. To stop the process and task templates that are in the
application that is named application\_name, enter
the following command: wsadmin -f manageTemplates.py -stop application\_name
wsadmin.sh -f manageTemplates.py -stop application\_name
Existing instances of the process templates continue
to run until they end normally, but you cannot create new instances
from the stopped template. If the process is a subprocess, the creation
of new instances depends on whether the subprocess is a peer or a
child of the calling process. If the process template is part of a
process application, the business process definition (BPD) cannot
start new instances of the BPEL process, and therefore it cannot run
to completion.
3. To start the process and task templates that are in the
application that is named application\_name, enter
the following command: wsadmin -f manageTemplates.py -start application\_name
wsadmin.sh -f manageTemplates.py -start application\_name
The templates that belong to the application start. For
BPEL processes, you can use Business Process Choreographer Explorer
to start process instances from the process templates, and work with
task instances associated with the task template.

<!-- image -->