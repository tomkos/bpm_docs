# Planning for an external IBM Content
Navigator

You can configure IBM® Business Automation
Workflow with an
external IBM Content
Navigator.

IBM Content
Navigator is a web client for
content management. It features a web console for working with content that is stored on IBM
Enterprise Content Management repositories, such as IBM Content
Manager, IBM Content
Manager OnDemand, or IBM
FileNet® Content Manager.

IBM Content
Navigator
includes several components that you can use to integrate client applications with your
repositories, such as an API toolkit that you can use to extend the web client and build custom
applications.

You should consider using an external IBM Content
Navigator under the
following conditions:

- You have an existing IBM Content
Navigator that you
want to use with a new installation or an existing upgrade of IBM Business Automation
Workflow.
- You have a legacy IBM Case
Manager installation that
you want to upgrade to IBM Business Automation
Workflow.
- You want to build integrated solutions and use IBM Content
Navigator as a unified
user interface for other Enterprise Content Management components in the IBM Digital Business
Automation portfolio.

To use an external IBM Content
Navigator
installation, you must have a common user repository and it must contain the users that work with
your applications. This repository is an enterprise-wide Lightweight Directory Access Protocol
(LDAP) repository that contains all the users and groups. You must also ensure that IBM Content
Navigator is set up on
WebSphere® Application
Server.

The following graphic shows the typical architecture of the Case Client and Case administration client in the context of the
IBM Content
Navigator UI
framework on a single server:

<!-- image -->

The following graphic shows the typical architecture of the Case Client and Case administration client in the context of the
IBM Content
Navigator UI
framework in a distributed development environment. It also shows the features with which the case
tools can integrate:

<!-- image -->

For more information about IBM Content
Navigator, see the
following topics in the IBM Content
Navigator
documentation:

- IBM Content Navigator overview
- IBM Content Navigator architecture overview

If you want to upgrade IBM Case
Manager to IBM Business Automation
Workflow for a production
environment, you must use an external IBM Content
Navigator. This is
also the recommended approach for upgrading in a development environment. Information about how to
upgrade IBM Case
Manager
to IBM Business Automation
Workflow is found in
topic "Upgrading your system with an external IBM Content
Navigator".

For information about how to configure IBM Business Automation
Workflow for use with IBM Content
Navigator, see the
topic "Configuring IBM Business Automation
Workflow with an external IBM Content
Navigator".

## Related information

- Upgrading your IBM Case Manager system using an external IBM Content Navigator
- Configuring IBM Business Automation Workflow with an external IBM Content Navigator