# WSRR administration commands

## Introduction

IBM® Business Automation Workflow supports
the use of the WSRR product, which allows the storage and retrieval
of services endpoints and mediation policies.

WSRR is installed
as an enterprise application and provides a web service interface
that allows you to connect Endpoint Lookup mediation primitives and
Policy Resolution mediation primitives to a registry instance (as
part of a mediation flow). You can use the Endpoint Lookup mediation
primitive to look up services, and the Policy Resolution mediation
primitive to find mediation policies.

- Locate the command that starts the wsadmin scripting client: this
is found in the install\_root\bin directory.
- Run the wsadmin command.
    - If the server is not running, use the -conntype none option.
    - If you are not connecting to the default profile, use the -profileName profile\_name option.

```
$AdminTask help SIBXWSRRAdminCommands
```

```
$AdminTask help command\_name
```

If these commands throws exceptions, they are of the
type: public class WSRRDefinitionException