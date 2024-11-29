# Troubleshooting interactions with Enterprise Content Management
systems

Some known issues are:

- A connection cannot be established to an ECM system
- Operation parameters that are considered optional in designer might be mandatory in some ECM
systems

## A connection cannot be established to an ECM system

A
connection must be established through the Content Management Interoperability
Services (CMIS) by using the web services protocol rather than the
Atom protocol. When you add an ECM server, ensure that the context
path specifies the path to the CMIS web services application on the
server.

## Operation parameters that are considered optional in designer might be mandatory in some ECM
systems

In designe, the Content Management Interoperability Services (CMIS) specification is used to
determine which operation parameters are marked as optional. However, parameters that are marked as
optional might be mandatory for some ECM systems. You can consult your ECM system documentation to
determine whether a parameter is optional or mandatory for your ECM system.