# Naming conventions for Workflow Center server
deployments

On the IBM® Workflow
Center server, you
can deploy a snapshot of a process application as well as a snapshot of a toolkit. In addition, you
can deploy the tip of a process application or the tip of a toolkit. (A tip is the
current working version of your process application or toolkit.) The version context varies,
depending on the type of deployment.

- You might be unable to expose the business process definitions as web services without some form
of mediation.
- You might be unable to invoke a business process definition created in IBM Process
Designer from a BPEL process created in IBM Integration
Designer.

For process applications, the process application tip or the specific
process application snapshot is used to uniquely identify the version.

Toolkits can be deployed with one or more process applications,
but the lifecycle of each toolkit is bound to the lifecycle of the
process application. Each process application has its own copy of
the dependent toolkit or toolkits deployed to the server. A deployed
toolkit is not shared between process applications.

If the track associated with the process application is named something
other than the default of Main, the track acronym
is also part of the version context.

For more information, see the Examples section,
later in this topic.

## Process application snapshots

- Process application name acronym
- Process application track acronym (if a track other than Main is
used)
- Process application snapshot acronym

## Stand-alone toolkits

- Toolkit name acronym
- Toolkit track acronym (if a track other than Main is
used)
- Toolkit snapshot acronym

## Tips

Process application tips are used during
iterative testing in Process Designer. They
can be deployed to Workflow Center servers
only.

- Process application name acronym
- Process application track acronym (if a track other than Main is
used)
- "Tip"

Toolkit tips are also used during iterative testing in Process Designer. They
are not deployed to a production server.

For toolkit tip deployments,
the version context is a combination of the following items:

- Toolkit name acronym
- Toolkit track acronym (if a track other than Main is
used)
- "Tip"

## Examples

- The following table shows an example of names that are uniquely
identified. In this example, a process application tip uses the default
track name (Main):
Table 1. Process application
tip with default track name

Type of name
Example

Process application name
Process Application 1

Process application name acronym
PA1

Process application track 
Main

Process application track acronym
 "" (when the track is Main)

Process application snapshot
 

Process application snapshot acronym
Tip

Any SCA modules associated with this process application
tip include the version context, as shown in the following table:
Table 2. SCA modules and version-aware EAR files

SCA module name
Version-aware name
Version-aware EAR/application name

M1
PA1-Tip-M1 
PA1-Tip-M1.ear

M2
PA1-Tip-M2 
PA1-Tip-M2.ear
- The following table shows an example of a process application
tip that uses a non-default track name: 
Table 3. Process application
tip with non-default track name

Type of name
Example

Process application name
Process Application 1

Process application name acronym
PA1

Process application track 
Track1

Process application track acronym
 T1

Process application snapshot
 

Process application snapshot acronym
Tip

Any SCA modules associated with this process application
tip include the version context, as shown in the following table:
Table 4. SCA modules and version-aware EAR files

SCA module name
Version-aware name
Version-aware EAR/application name

M1
PA1-T1-Tip-M1
PA1-T1-Tip-M1.ear

M2
PA1-T1-Tip-M2
PA1-T1-Tip-M2.ear

- The following table shows an example of names that are uniquely
identified. In this example, a process application snapshot uses the
default track name (Main):
Table 5. Process application
snapshot with default track name

Type of name
Example

Process application name
Process Application 1

Process application name acronym
PA1

Process application track 
Main

Process application track acronym
 "" (when the track is Main)

Process application snapshot
Process Shapshot V1

Process application snapshot acronym
PSV1

Any SCA modules associated with this process application
snapshot include the version context, as shown in the following table:
Table 6. SCA modules and version-aware EAR files

SCA module name
Version-aware name
Version-aware EAR/application name

M1
PA1-PSV1-M1 
PA1-PSV1-M1.ear

M2
PA1-PSV1-M2 
PA1-PSV1-M2.ear
- The following table shows an example of a process application
snapshot that uses a non-default track name: 
Table 7. Process
application snapshot with non-default track name

Type of name
Example

Process application name
Process Application 1

Process application name acronym
PA1

Process application track 
Track1

Process application track acronym
 T1

Process application snapshot
Process Snapshot V1

Process application snapshot acronym
PSV1

Any SCA modules associated with this process application
snapshot include the version context, as shown in the following table:
Table 8. SCA modules and version-aware EAR files

SCA module name
Version-aware name
Version-aware EAR/application name

M1
PA1-T1-PSV1-M1
PA1-T1-PSV1-M1.ear

M2
PA1-T1-PSV1-M2
PA1-T1-PSV1-M2.ear