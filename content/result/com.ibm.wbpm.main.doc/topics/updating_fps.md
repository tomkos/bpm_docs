# Installing fix packs and interim fixes on IBM Process Federation
Server

## About this task

1. Read the fix pack and interim fix documentation thoroughly. The
documentation lists dependencies that you must install before you
apply the fix pack or interim fix.
2. To ensure that your implementation is performing the same way
that it did before you applied the fix pack or interim fix, prepare
a regression test plan.
3. Back up the Workflow Server or Process Server
(BPMDB) and Shared (CMNDB) databases on the federated systems that include the change log tables for
the Process Federation Server index.
4. Optional: Back up the usr directory on your
current installation of Process Federation Server by
using the following command: server package --archive=package\_file\_name.zip --include=usr
5. Before you deploy the fix pack or interim fix to a production
environment, install the fix pack or interim fix in a development
or quality-assurance environment.
6. You must perform the installation with the same user account that
you used to install the product packages.

## Procedure

1 Download the refresh pack repositories to a local directory.If you are installing the refresh pack interactively by using IBMInstallation Manager to connect to the live repository, skip thisstep.
    1. Download the appropriate fix repositories to a temporary
disk location.
    2. Unpack the repository files to any directory that you
choose. The files must be unpacked to the same location. Note the
location where you have unpacked the files.
    3. Extract each set of fixpack or interim fix repository
files to its own local directory, although a common staging directory
can be used.  For example, staging\_directory\fixpack,
staging\_directory\refreshpack, or
staging\_directory\IFix1.Important: If a fix pack or refresh pack
repository consists of multiple .zip files, ensure that they are all extracted
to the same root directory.
2 Install the service updates.

1. Start Installation Manager.
2 Add the repositories to the Installation Manager preferences.Click File > Preferences . Under Repositories , selectone of the following options:
    - If you have Internet access, ensure that the Search
service repositories during installation and updates option
is selected.
    - If you do not have Internet access, add the location or locationsof the local repositories that you downloaded in the previous step.
        1. Click Add Repository.
        2. Type or browse to the repository.config file
for the repository that you extracted and click OK.
        3. Repeat this process for all new repositories.
        4. Click OK to save the new repository settings.
3. Click Update.  Installation
Manager searches its repositories for the updates that apply to your
installation.
4. Select the version of IBM®
WebSphere® Application Server Liberty
profile that is installed and click Next.
5. Enter your IBM user ID and password. Installation
Manager searches its repositories for the updates that apply to your
installation.
6. Select the applicable fix packs or interim fixes, click Next twice
and then Update to apply the service updates.
7. After the update completes, click Finish,
and close Installation Manager.

## What to do next

1. Stop the server on the system.
2. Copy the usr directory and all its subdirectories from the original
installation to the new installation. You can use the server package
--archive=package\_file\_name.zip --include=usr command to create a
compressed file of the directory. You can then extract the files on the new installation.
3. Restart the server on the new installation and verify that the installation is working
correctly.
4. Remove or archive the original installation.