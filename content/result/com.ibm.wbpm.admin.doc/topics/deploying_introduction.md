# Snapshot installation

- Make sure the version of the Workflow Center server is equal to or
earlier than the version of the connected or offline workflow server before you install to the
workflow server.
- To
import a snapshot that was created in IBM® BPM V8.5.5 or V8.5.6, which
contains Basic Case Management features, into a new installation of Business Automation Workflow
24.0.0.0 that no longer
has Basic Case Management features, you must first import the .twx file that
contains Basic Case Management content into a 24.0.0.0
Workflow Center to update the
case types to the 24.0.0.0 model and remove the document types.If your installation of IBM BPM V8.5.5 or V8.5.6 had Basic
Case Management features and was upgraded to 24.0.0.0, your deployment
environment still has Basic Case Management features and you can import snapshots that contain Basic
Case Management features.
- Before installing the case project snapshot into another workflow environment, follow the steps
in Updating the data maps of a case project before importing to a workflow environment to ensure that the data maps,
and the Design and the target object stores mapping are correct.
- To ensure consistency and update all group and team assignments after deploying each case
solution snapshot (having BPM activities), it is essential to apply the security manifest.

If you plan to install a snapshot that contains Integration Designer artifacts, the user or
group to which you belong must be assigned to the Configurator, Operator, and  Deployer
administrative security role. If you are not currently assigned to all of these roles, click
Users and Groups in the WebSphere administrative console to modify the user
or group roles. For more information, see Administrative security roles. In addition, if the snapshot contains BPEL process and human task applications,
you can use the serviceDeploy command or the wsadmin tool to deploy the EAR file
that contains the applications. For more information, see Deploying BPEL process and human task applications.

## Connected workflow servers

You can install snapshots to connected workflow servers in your environment by using either
Workflow Center or the
BPMInstall command. Ordinarily, you have connections to one or more servers in
your environment, as shown in the following figure.

## Offline workflow servers

You can also install snapshots to an offline server that is running but is not connected to
Workflow Center (for example,
if the workflow server is behind a firewall). In this situation, use the wsadmin commands to create
an installation package for a particular snapshot on the Workflow Center server, transfer the
package to the offline workflow server, and then run the wsadmin command to install the package.
Always install snapshots to an offline workflow server from the same Workflow Center.

## Custom and generic installation packages

| Generic installation packages   | Custom installation packages   |
|---------------------------------|--------------------------------|
|                                 |                                |

With custom installation packages, you can continue to use scripts and installation services that
are created  for IBM BPM
version 8.5.5.0 or earlier.

## Requirements for Case solution projects snapshots installation

To install the Case solution project snapshots from a Workflow Center to a Workflow Server,
the snapshot needs to be installed or exported from a Workflow Center version that matches
the Workflow Server. Installing a snapshot from a different version of Workflow Center to a Workflow Server
is not supported. For example,

Not supported: Installing a snapshot from Workflow Center v19.0.0.3 to Workflow
Server v20.0.0.2.

Supported: Installing a snapshot from Workflow Center v20.0.0.2 to Workflow
Server v20.0.0.2.

You can migrate the solutions from a Workflow Center to another Workflow Center by using the snapshot
.twx files that allow for migrating a case project solution from a lower or
older version of Business Automation Workflow to a higher or newer version of Business Automation
Workflow. See Importing and exporting projects.