# Profile commands in a multi-profile environment

The first profile that you create within one installation of IBM Business Automation Workflow becomes
the default profile. (You can optionally change the default profile
when you create another profile later.) The default profile is the
default target for commands issued from the bin directory
in the directory where IBM Business Automation Workflow is
installed. You can set any new profile to be the new default profile.
If only one profile exists on a system, every command operates on
that profile.

- If you want to issue the command from any directory, follow the
command with the -profileName parameter and the
name of the profile to address. For example: <install\_root>/bin/startServer server1 -profileName <profilename>
- To overcome having to specify the -profileName parameterfor a command, use the version of the command that exists in the bin directoryof the profile to address. The directory is one of the following basedon platform: Where profile\_root defaultsto <install\_root> /profiles/<profileName>
    - profile\_root/bin
    - profile\_root\bin