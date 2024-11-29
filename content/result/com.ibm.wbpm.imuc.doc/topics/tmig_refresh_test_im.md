# Testing the upgrade by using installation data from an existing
installation

## Procedure

1 Set up a test server that has the same operating systemas the production system. Ensure that the test serverhas the following characteristics:
    - The same user or group that was used for the IBM® Installation
Manager installation
of the production system.
    - Similar operating system settings, especially those, such as the ulimit setting,
that can affect the installation.
2 Copy the following directories:

- The Business Automation Workflow installation
and profile directories.
- The Installation Manager installation
directory, agent data directory, registry, and shared resource directory.
See Backing up IBM Installation Manager agent data and
shared files for recovery with IBM Business Process Manager (BPM).
3. Copy the directories to the test server. Ensure
that you are using the same paths and permissions as the production
system for an accurate test.  Tip: Make sure
that the production database cannot be accessed from the test system.
4. Download the repositories and apply the upgrade. From the
upgrade instructions, run only the steps that are related to installing
the update with Installation Manager. If the installation fails, use
the test environment to further debug problems that might exist in
your production system.  Important: Do not
start the Business Automation Workflow servers
or use the environment except to test Installation Manager and profile
upgrade commands. If you run the DBUpgrade command
as described in the upgrade instructions, or if you start the servers
in the test environment, this will affect your production database
that the test system points to.
5. Optional: To make sure that there are no problems
in the WebSphere configuration that would cause profile upgrade to
fail, go to the install\_root/bin directory
and run the following command: BPMConfig -upgrade -profile profileNamewhere profileName is
the name of the deployment manager profile.
6. Repeat these steps for each Business Automation Workflow installation
in your environment.

## Results