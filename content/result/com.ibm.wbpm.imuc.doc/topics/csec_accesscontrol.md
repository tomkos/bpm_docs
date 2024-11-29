# Access control

Access control can be arranged for components that you develop
to make them secure. You provide access control for components by
using service component architecture qualifiers at development time.

Some IBM Business Automation Workflow components,
packaged as enterprise archive (EAR) files, secure their operation
using Java EE role-based security. In contrast to code-based security,
which secures the operation of components, role-based access control
secures resources. For example, in the Business Calendars
widget, you can specify the type of access that users have to
individual timetables.

## Security Roles widget

Use the Security
Roles widget in Business Space to specify, for each timetable,
the owner of the timetable as well as those who have writer and reader
access to the timetable.

| Roles          | Default permission          |
|----------------|-----------------------------|
| BPMAdmin       | Primary administrative user |
| BPMRoleManager | All authenticated users     |

## EAR files and associated roles

The Business Process Choreographer and the Common
Event Infrastructure are  installed
as part of IBM Business Automation Workflow.

| Name of .ear file                                                            | Role                 | Default           |
|------------------------------------------------------------------------------|----------------------|-------------------|
| BPEContainer\_nodeName\_serverName.ear OR BPEContainer\_clusterName             | APIUser              | All Authenticated |
| BPEContainer\_nodeName\_serverName.ear OR BPEContainer\_clusterName             | SystemAdministrator  | None              |
| BPEContainer\_nodeName\_serverName.ear OR BPEContainer\_clusterName             | SystemMonitor        | None              |
| BPEContainer\_nodeName\_serverName.ear OR BPEContainer\_clusterName             | JMSAPIUser           | All Authenticated |
| BPEContainer\_nodeName\_serverName.ear OR BPEContainer\_clusterName             | AdminJobUser         | All Authenticated |
| BPEContainer\_nodeName\_serverName.ear OR BPEContainer\_clusterName             | JAXWSAPIUser         | Everyone          |
| BPCExplorer\_nodeName\_serverName.ear OR BPCExplorer\_clusterName               | WebClientUser        | All Authenticated |
| BPCArchiveExplorer\_nodeName\_serverName.ear OR BPCArchiveExplorer\_clusterName | WebClientUser        | All Authenticated |
| BSpaceEAR\_nodeName\_server.ear                                                | businessspaceusers   | All Authenticated |
| BSpaceForms\_nodeName\_server.ear                                              | WebFormUsers         | All Authenticated |
| BusinessRulesManager.ear                                                     | BusinessRuleUsers    | All Authenticated |
| BusinessRulesManager.ear                                                     | NoOne                | None              |
| BusinessRulesManager.ear                                                     | AnyOne               | Everyone          |
| BusinessRules\_nodeName\_server.ear                                            | Administrator        | All Authenticated |
| EventService.ear                                                             | eventAdministrator   | All Authenticated |
| EventService.ear                                                             | eventConsumer        | All Authenticated |
| EventService.ear                                                             | eventUpdater         | All Authenticated |
| EventService.ear                                                             | eventCreator         | All Authenticated |
| EventService.ear                                                             | catalogAdministrator | All Authenticated |
| EventService.ear                                                             | catalogReader        | All Authenticated |
| mm.was\_nodeName\_server.ear                                                   | All Authenticated    | All Authenticated |
| mm.was\_nodeName\_server.ear                                                   | everyone             | Everyone          |
| REST Services Gateway.ear                                                    | RestServicesUser     | All Authenticated |
| REST Services Gateway Dmgr .ear                                              | RestServicesUser     | All Authenticated |
| TaskContainer\_nodeNameserverName.ear OR TaskContainer\_clusterName            | APIUser              | All Authenticated |
| TaskContainer\_nodeNameserverName.ear OR TaskContainer\_clusterName            | SystemAdministrator  | None              |
| TaskContainer\_nodeNameserverName.ear OR TaskContainer\_clusterName            | SystemMonitor        | None              |
| TaskContainer\_nodeNameserverName.ear OR TaskContainer\_clusterName            | EscalationUser       | All Authenticated |
| TaskContainer\_nodeNameserverName.ear OR TaskContainer\_clusterName            | AdminJobUser         | All Authenticated |
| TaskContainer\_nodeNameserverName.ear OR TaskContainer\_clusterName            | JAXWSAPIUser         | Everyone          |
| wpsFEMgr\_7.0.0 Security                                                      | WBIOperator          | Everyone          |

- Access control in business process and human task applications

Business Process Choreographer, which is installed as part of the IBM Business Automation Workflow installation, uses roles to determine the capabilities of the user on a production system.