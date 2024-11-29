# Setting permissions to import applications to the Workflow Center repository

## About this task

This task is required when you are running Workflow Center as
a service.

## Procedure

Complete the following steps that are appropriate for
your operating system:

- Windows
    1. From the Start menu, click Control
Panel > Administrative Tools > Services.
    2. Select the properties for the Workflow Center service.
    3. On the Log On tab, browse for
a local user who has permission to write to the temp directory.
    4. Enter the appropriate password.
    5. Apply your changes and then restart the service.
- AIX or Linux Important: If your company has a security policythat requires you to change the password on your machine periodically,you must remember to also change your password in the Workflow Center serviceproperties.

1 Issue either of the following commands:
    - chmod 777 /tmp
    - chmod a+rwx /tmp