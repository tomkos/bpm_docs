<!-- image -->

# Deploying BPEL process and human task applications interactively

## About this task

Perform the following steps to deploy BPEL process applications
interactively.

## Procedure

1. Start the wsadmin tool. In the profile\_root/bin directory, enter wsadmin.
2. Deploy the application. At the wsadmin command-line
prompt, enter the following command:$AdminApp installInteractive application.earwhere application.ear is the qualified name of the enterprise archive file that contains
your process application. 
You are prompted
through a series of tasks where you can change values for the application.
3. Save the configuration changes. At the wsadmin
command-line prompt, enter the following command:$AdminConfig save
You must save your changes to transfer the updates to the
master configuration repository. If a scripting process ends and you
have not saved your changes, the changes are discarded.

- Configuring process application data source and set reference settings

You might need to configure process applications that run SQL statements for the specific database infrastructure. These SQL statements can come from information service activities or they can be statements that you run during process deployment or instance startup.