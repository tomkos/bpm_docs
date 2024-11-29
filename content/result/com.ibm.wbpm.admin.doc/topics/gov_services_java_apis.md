# Traditional: Governance service flows (deprecated)

## Introduction

During IBM Business Automation
Workflow installation,
the System Governance toolkit (TWSYSG) is imported into the Process Center repository.
Each governance process that you create must include a dependency
on the System Governance toolkit. The toolkit provides the machinery
required to build a governance process. The toolkit has service flows
for installing process application snapshots and setting snapshot
status.

You cannot edit or change the artifacts in the System
Governance toolkit, but you can open the toolkit and view the artifacts
within it.

## Templates

The System Governance toolkit
provides two templates, the Installation Requested template and the
Snapshot Status Change template. Each of these templates is a governance
process that you can adapt to the needs of your particular organization.
Each of these templates is associated with a corresponding governance
event. Your governance processes in Process Center must
be built from one of these templates to take advantage of the governance
service flows.

## Installation service flows

If an installation attempt fails, call the Cancel
Snapshot Installation service flow to clear the status in Process Center. The
only other way to clear the failure is to reset the governance process
for the process application to the system default process. The governance
process that called the Install Snapshot service flow should have
all the data that is available from the failure already and can send
that information in an email or log it. For failures that occurred
because of an error in the process application, you might want to
leave that status as a failure so no one tries to install that version
again.

## Install Snapshot

- Input: processAppInstallation
- Input: processAppInstallationRequest is used in the Default Installation
Requested governance process.
- Output: installResponse, which is used to determine if the installation
succeeded and if a failure is recoverable.
- Implementation: Calls Java API for installation.

This service flow can fail to install a snapshot for a number
of reasons. The installation request produces a return value that
indicates if an error occurred and if the error is recoverable.

## Cancel Snapshot Installation

- Input: installRequest (processAppInstallation)
- Implementation: Calls Java API for installation.

This service flow can fail under the following circumstances:

- The Cancel Snapshot Installation service flow takes the processAppInstallation
object as an input and uses various IDs set on processAppInstallation
during processing. Those IDs must not be null or zero length and must
be the same IDs that were received by the processAppInstallation object
when the snapshot installation request was made.
- If cancel is called after installation has started, the cancel
request is ignored.
- If cancel is called multiple times for the same installation request,
all calls after the first call are ignored, because the installation
request is already canceled.
- If cancel is called against a process application for which governance
is not enabled, the cancel request is ignored.
- If there is not an active installation request for the snapshot
and workflow server combination, the cancel request cannot succeed.
- If the snapshot or workflow server is not properly identified,
it cannot be found in Process Center.

## Get All Process Servers

- Output: processServers (processServers) provides a list of available
workflow servers.
- Implementation: Calls Java API for the list.

## Set Installation Status

Use this service
flow to update the installation status while an installation request
is waiting for approval. When this service flow is called, the status
updates immediately, without waiting for the current status or the
installation to complete.

This service flow takes the following
inputs:

- processServerID (String)
- snapshotID (String)
- status (String) must be between 1 and 64 characters.
- description (String) is optional; the length must be between 0
and 250 characters.

Implementation: Calls Java API to set the installation status.

This
service flow can fail under the following circumstances:

- If governance is not enabled, you cannot use this service flow.
- If no installation request for that snapshot and workflow server
combination exists, no status can be provided. That is, an installation
request must be open and active.
- The Set Installation Status service flow cannot be called after
the Install Snapshot service flow has completed. The Install Snapshot
request changes the status, and when the installation is complete,
all status values disappear.
- If the installation fails before this service flow is called,
no status is provided.
- If the snapshot or workflow server is not properly identified,
it cannot be found in Process Center.

## Get Installation Status

- Input: processServerID (String)
- Input: snapshotID (String)
- Output: status (String) provides predefined status messages if
custom messages are not provided through Set Installation Status.
- Implementation: Calls Java API to set the installation status.

## Snapshot status service flows

## Get Snapshot Status

- Input: snapshotID (String)
- Output: status (String)
- Implementation: Calls Java API for the status.

## Get Snapshot Statuses

- Output: statuses (String) (List)
- Implementation: Calls Java API for the list of statuses.

## Set Snapshot Status

- Input: status (String) Extension of string. Length must be between
1 and 50 characters.
- Input: snapshotID (String)
- Implementation: Calls Java API for setting the status.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)