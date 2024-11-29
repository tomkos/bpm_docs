# Warnings about GTK or ulimit on Linux or UNIX when installing
or migrating

## GTK warning

```
Your operating system failed the launchpad prerequisites check. The following 32-bit GTK Library for running IBM Installation Manager is not available in underlying OS: list\_of\_missing\_files. Please install the 32-bit GTK Library and restart your installation.
```

If you see this message, your server does not have
the 32-bit version of the GTK library installed, or the library is
an incorrect version. You must update your server with the correct
version of the 32-bit GTK library before you continue the installation.
You can get the library from the DVD or official website of your operating
system.

## ulimit warning

```
Current system has detected a lower level of ulimit than the recommended value of recommended\_value. Please increase the ulimit number to minimum value of recommended\_value and re-start the installation.
```

```
Shutdown your installer. If you are a root user open a command prompt and issue ulimit -n recommended\_value and then restart the installer. If you are a non-root user, work with your system administrator to increase your ulimit -n recommended\_value and then restart the installer.
```

1 Set the maximum number of open files using the following steps:

<!-- image -->

    1. Open /etc/security/limits.
    2. Edit or add the default section and include
this line:nofiles = recommended\_value
    3. Save and close the file.
    4. Log off and log in again.

<!-- image -->

    1. Open /etc/security/limits.conf.
    2. Locate the nofile parameter and increase the
value. If a line containing the nofile parameter
does not exist, add the following lines to the file:* hard
nofile  recommended\_value
*
soft nofile  recommended\_value
    3. Save and close the file.
    4. Log off and log in again.

<!-- image -->

    1. Open /etc/system and add the following line
to the end of the file:set rlim\_fd\_max=8800
    2. Save and close the file.
    3. Log off and log in again.
2. Restart the computer.
3. Restart the installer.