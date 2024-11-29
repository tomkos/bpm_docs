# Starting Workplace

## Deployment options

- When Workplace is
available as a toolkit and wrapped with a process application, it is implemented as a set of Workplace toolkit and UI toolkit views that are combined in a
client-side human service, and can be accessed from any build:
https://{baw-server-host}/Workplace
- When Workplace is
provided as a process application that runs in the Application Engine, it runs as a desktop in the
Business Automation Navigator, which is the
single public entry point in IBM® Cloud Pak for Business
Automation:https://{navigator\_hostname}/icn/navigator/?desktop=workplace

## Search capabilities

Depending on the environment, Workplace includes the following
search capabilities.

## Getting started

```
https://{navigator\_hostname}/icn/navigator/?desktop=workplace
```

- https://workflow\_hostname where
workflow\_hostname corresponds to the
baw\_configuration.hostname property in your custom resource file.
- https://pfs\_hostname/rest/bpm/federated/v1/systems where
pfs\_hostname corresponds to the
pfs\_configuration.hostname property in your custom resource file. Remember to log
in with your LDAP user name and password.
- https://ae\_hostname/ where
ae\_hostname either corresponds to the
application\_engine\_configuration.hostname property or the
shared\_configuration.sc\_deployment\_hostname\_suffix property in your custom resource
file.

```
https://route\_host/baw-instance-name/Workplace
```

To get
you started using Workplace, watch this video:

Get started with Workplace
Note
that even though the video shows a slightly earlier version of the user interface, the functionality
is still valid.