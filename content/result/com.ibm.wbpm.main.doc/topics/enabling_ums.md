# Installing and configuring the User Management Service

## Overview

IBM Business Automation Workflow combines
several server technologies, including WebSphere® Application
Server Network Deployment and IBM
WebSphere Application Server Liberty.
You can deploy these runtime servers in your (on-premises) data center,
in virtual cloud-based environments, in managed cloud environments,
or in hybrid setups that combine a mix of different deployment environment
types.

- Do all runtime technologies support the same set of LDAP servers?
- Do all runtime technologies support your single sign-on solution?
- How to establish single sign-on for components in distributed
network environments that cannot share cookies or encryption keys?

The User Management Service component helps you manage
this complexity by consolidating aspects of user management in a single
component. In this initial stage, it provides a configuration for
a single sign-on experience within your solution.

For maximum
compatibility, the User Management Service builds upon Liberty,
which brings the following advantages:

- Allows you to reuse existing customizations of Trust Association
Interceptors for single sign-on.
- Provides a state-of-the-art authentication scheme that is based
on the OpenID Connect standard.
- Familiarity for many administrators from a configuration and operations
perspective.

## Authentication concepts

The User Management
Service provides a single sign-on experience that is based on the
open standards OpenID
Connect 1.0 and OAuth
2.0.

Because it implements the OpenID Connect Authorization
Code Flow protocol, the User Management Service acts as an OpenID
Connect Offering Party (OP), and the IBM Business Automation Workflow server
acts as an OpenID Connect Relying Party (RP).

If an unauthenticated
end user requests access to a protected resource that is owned by IBM Business Automation Workflow, then
the user is redirected to the User Management Service to sign on.
After the authentication has completed successfully, the user is redirected
back to the IBM Business Automation Workflow,
which then checks the user’s authorization and, if successful
also, returns the protected resource.

The OpenID Connect protocol
requires that the Offering Party and Relying Party components are
made known to each other as part of their configurations.

The
following sections describe how to install and configure the User
Management Service, and the how to configure the service consumers.

- Planning your User Management Service environment

You must decide whether you want to setup the User Management Service (UMS) in a production configuration that includes load-balancing and fail-over facilities.
- Understanding User Management Service login and logout behavior

This topic describes the current behavior of login and logout for Digital Business Automation (DBA) components that delegate authentication to User Management Service (UMS).
- Installing the User Management Service

 Traditional: 
 Install the optional User Management Service product extension on IBM WebSphere Application Server Liberty
- Configuring the User Management Service

You must configure various components to provide a single sign-on experience.