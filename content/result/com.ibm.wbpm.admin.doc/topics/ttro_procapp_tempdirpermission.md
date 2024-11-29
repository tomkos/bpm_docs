# Granting permission to write to the temp directory

## Procedure

Complete the following steps that are appropriate for
your operating system:

- Windows
    1. From the Start menu, click Control
Panel > Administrative Tools > Services.
    2. Select the properties for the workflow center service.
    3. On the Log On tab, browse for
a local user who has permission to write to the temp directory.
    4. Enter the appropriate password.
    5. Apply your changes and then restart the service.
- Linux or UNIX Important: If your company has a security policy that requires you to change thepassword on your machine periodically, you must remember to also change your password in theworkflow center service properties.

1 Issue either of the following commands:
    - chmod 777 /tmp
    - chmod a+rwx /tmp