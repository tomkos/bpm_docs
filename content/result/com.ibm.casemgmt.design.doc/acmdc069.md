# Preparing the system configuration for migration

## About this task

During redeployment of a solution, some system configuration information might be overwritten and
might need to be specified again. However, most configuration steps do not need to be repeated.

- Creating the FileNet Deployment Manager deployment tree
- Creating the FileNet Deployment Manager environment

## Creating the FileNet Deployment
Manager
deployment tree

If your solution package includes assets that are managed by FileNet P8, create a deployment tree for
the files to be migrated with FileNet Deployment
Manager.

### About this task

A deployment tree contains the files that FileNet Deployment
Manager creates. A deployment can be
between connected or disconnected environments.

After you export the solution assets from the
source environment by using FileNet Deployment
Manager, you must move the deploy
package to the destination environment. The package contains the information about the source
environment that is needed to import the package into the destination environment. If the systems
are disconnected, the source environment is typically extracted from the deploy package into the
deployment tree for the FileNet Deployment
Manager instance that is used to import the solution into the destination environment.

If the deployment is connected, only one deployment tree is needed. However, if a deployment is
disconnected or different computers are used to import and deploy the solution assets, a deployment
tree must be created on each computer.

### Procedure

To create a FileNet Deployment
Manager deployment tree:

- Start FileNet Deployment
Manager.
- In the Select Deployment Tree Location window, browse to the folder in
which to create the deployment tree.
- ClickWindow > Preferences Generaloptions and set the following options.
    - Clear the Enable FIPS 140-ready mode option to allow FileNet Deployment
Manager to store passwords as
encrypted data. Otherwise, you must enter a password each time you runFileNet Deployment
Manager. In addition, clearing this
option allows FileNet Deployment
Manager to
convert embedded passwords for certain service data in a deploy dataset if you enter new passwords
for the target service data as a part of the data mapping task. For more information, see About passwords.
    - Verify that the Export metadata assets created by an AddOn option is set
to Never.

## Creating the FileNet Deployment
Manager
environment

You must create a FileNet Deployment
Manager environment definition for
each of the development, test, and production environments that are involved in the solution
application migration. Environment definitions enable FileNet Deployment
Manager to connect to Content Platform Engine.

### About this task

Each FileNet Deployment
Manager environment
can serve as the source environment in one operation and the destination environment in another
operation. The inclusion of an environment in a source-destination pair determines whether the
environment is being used as a source environment or a destination environment.

### Procedure

To create a FileNet Deployment
Manager environment

1. Start the FileNet Deployment
Manager and
ensure that the correct deployment tree is selected.
2. Create the environment definition by clicking
File > New
Environment.
3 Define the connection parameters for the environment.
    1. In the deployment tree, double-click the node for the new environment.
    2. On the Content Platform Engine
Connection tab at the bottom of the window, enter the connection information for
Content Platform Engine.

Tip: Select the Save the password check box to store the
encrypted password.
    3. Click Test Connection.
If FileNet Deployment
Manager cannot
connect to Content Platform Engine, verify that the specified connection information is correct.
    4. In the PE Connection Point list, select the connection point that
corresponds to the project area or target environment with which this environment is to be
used.
    5. Click File > Save to save
the connection settings.