<!-- image -->

# Deployment of BPEL processes and human tasks

When you deploy an enterprise application that contains BPEL processes
or human tasks, then these are stored as BPEL process templates or
human task templates, as appropriate, in the Business Process Choreographer
database. Newly deployed templates are, by default, in the started
state. However, the newly deployed enterprise application is in the
stopped state. Each deployed enterprise application can be started
and stopped individually.

- If the name of the template and the target namespace do not already exist, a new template is
deployed
- If the template name and target namespace are the same as those of an existing template, but the
valid-from date is different, a new version of an existing template is deployed

- The template name is derived from the name of the component and not from the BPEL process or
human task.
- If your EAR file was created for a WebSphere® Process
Server version earlier than 7.0, you must pre-process it by using the serviceDeploy
command. This action is particularly important if you migrate process applications you haven't
accessed for years. For more information about this command, see serviceDeploy command-line utility.

- If you use Integration Designer, the valid-from date is the date on which the human task
or the BPEL process was modeled.
- If you use service deployment, the valid-from date is the date
on which the serviceDeploy command was run. Only
collaboration tasks get the date on which the application was deployed
 as the valid-from date.