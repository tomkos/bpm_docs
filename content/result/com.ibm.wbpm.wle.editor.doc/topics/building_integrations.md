# Integrating with web services, Java, and databases

IBM® Business Automation Workflow supports
both outbound and inbound integration as described in the following
table:

| Integration type   | Description                                                                                            | Required Business Automation Workflow components                                               |
|--------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Outbound           | Business Automation Workflow communicates with an external system to retrieve, update, or insert data. | Integration service, IBM Business Automation Workflow Integration Service, or Undercover Agent |
| Inbound            | An external system calls into Business Automation Workflow to initiate a service.                      | Undercover Agent and Web Service                                                               |

- Creating outbound integrations

Outbound integrations enable business process authored in Process Designer to interact with other systems, such as a web service, a content management system, or an external database. Depending on the system that you are integrating with, you can implement the integration service using an Integration Service implementation or an IBM Business Automation Workflow Integration Service implementation.
- Creating inbound integrations

For inbound integrations that involve an external system or application calling into IBM Business Automation Workflow to kick off a service, you need to build several Business Automation Workflow components and corresponding services.
- Web services compatibility

Web services conform to a flexible architecture that allows variation in web services implementations. This variation unfortunately can lead to compatibility problems.