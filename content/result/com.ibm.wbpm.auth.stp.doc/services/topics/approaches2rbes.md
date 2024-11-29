<!-- image -->

# Approaches to rules-based endpoint selection

## Dynamic Endpoint Selection using Business Process
Manager Rules

This option provides you with the capability
to use simple decision tables within IBM Integration Designer for
evaluating endpoint rules using the native rules interface editor
within IBM Integration Designer. The rules are then deployed to Process
Server during runtime for invocation by the BPEL micro-flow.

Prerequisites

- Library projects for service implementation (Endpoints)
- Implementation of rules based on WebSphere® Process
Server, exposed through service component
architecture (SCA)

## Dynamic Endpoint Selection using IBM Operational Decision
Manager

This option allows you to employ the simple decision tables within IBM® ODM Studio for evaluating endpoint rules.
IBM ODM provides SupportPAC LA71 which
incorporates decision services into business processes running on IBM Business Process Management
solutions such as WebSphere Process Server and IBM Business Process Manager. The rules are then
deployed to Process Server on runtime for invocation by the BPEL micro-flow.

Prerequisites

- Library projects for service implementation
- Decision Service exposed through SCA using LA 71 Support Pack