<!-- image -->

# Stopping and starting process templates using the administrative
console

## Before you begin

- If WebSphere® administrative security is enabled,
verify that your user ID has operator authority.
- The application server, on which the process templates are to
be stopped or started, must be running. That is, the -conntype none
option of wsadmin cannot be used, because a server connection is required.

## About this task

## Procedure

1. Select the module that you want to manage. In
the navigation pane of the administrative console, click Applications > SCA modules > module\_name .
2 In the Configuration page for the SCA module under AdditionalProperties , click Business processes ,and then a process template.
    - To stop the process template, click Stop.Existing
instances of the process templates continue to run until they end
normally, but you cannot create new instances from the stopped template.
If the process is a subprocess, the creation of new instances depends
on whether the subprocess is a peer or a child of the calling process.
If the process template is part of a process application, the business
process definition (BPD) cannot start new instances of the BPEL process,
and therefore it cannot run to completion.
    - To start the process template, click Start.

<!-- image -->