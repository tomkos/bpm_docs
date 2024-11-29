<!-- image -->

# Swinging profiles between product installations

## About this task

A profile defines the runtime environment. When you change the service level of the installation,
the service level of the profile also changes. You can configure your environment to use a common
set of profiles. Because the profiles are decoupled from any specific installation, you can
associate the profiles with different application server installations, or swing the
profiles.

- This process applies to Linux only.
- This process applies to updating binary code and configuration properties but not database
metadata, which limits some of the benefits for rolling back Business Automation Workflow. Any service that is
applied to Business Automation Workflow also
requires manual steps to be performed for each profile.

Business Automation Workflow follows a
V.R.M.F naming scheme, where the letters stand for version, release, modification, and fix pack. You
can swing profiles only within a release, such as between product installations at different fix
packs or interim fix levels. You cannot swing profiles between different product versions. For
example, you can swing profiles between 23.0.1.1 and later fix packs, such as 23.0.1.3, but you
cannot swing profiles between 23.0.1.1 and 23.0.2.

An environment that is configured for swinging profiles relies on one or more master
installations, which are the installations to which you apply service from fix packs or interim
fixes. The master installation is used to create application server copies for production use, and
application server profiles are created in a way that enables their service levels to be changed
with a symbolic link.

<!-- image -->

<!-- image -->

- Installing and configuring a swinging profiles environment

To be able to swing profiles, you must install and configure a master installation and a set of common profiles.
- Applying an interim fix or cumulative fix by swinging profiles

If you configured your IBM Business Automation Workflow environment for swinging profiles, you can apply an Business Automation Workflow interim fix  or cumulative fix and swing the profiles.

## Related tasks

- WebSphere Application Server: Swinging profiles between product installations