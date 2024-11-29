# Preparing to upgrade  IBM Case
Manager to IBM Business Automation
Workflow.

- Review the requirements and considerations
- Choose your upgrade path
- Update your custom widgets, plug-ins, and extension packages

## Review the requirements and considerations

- Before you upgrade IBM Case
Manager, you must install
IBM Business Automation
Workflow. It is
recommended that you upgrade to IBM Business Automation
Workflow
24.x. If you are
running IBM Business Process Manager
 or
an earlier version of IBM Business Automation
Workflow, you can upgrade by
following the instructions for your specific configuration. See Upgrading to IBM Business Automation Workflow.
- It is recommended that you upgrade from IBM Case
Manager V5.3.3. If you
want to upgrade from a different version with a supported upgrade path, such as V5.3.2 or V5.2.1.7,
see Troubleshooting IBM Case Manager system upgrades.
- Upgrades from IBM Case
Manager V5.2.1.7 to
IBM Business Automation
Workflow 22.0.2 or later
requires a two-step upgrade. Upgrade to IBM Case
Manager V5.3.3 or
IBM Business Automation
Workflow 21.0.3 first,
then you can upgrade to IBM Business Automation
Workflow 22.0.2 and later.
- Before you upgrade, review the Software Product Compatibility Reports (SPCR) to ensure that
compatible component products are at their proper supported versions for IBM Case
Manager and IBM Business Automation
Workflow.

- The upgrade of IBM Case
Manager to IBM Business Automation
Workflow requires a new
installation of Business Automation Workflow on a new WebSphere Application
Server installation. See Upgrading your IBM Case Manager system using an external IBM Content Navigator.
- Business Automation Workflow is
based on WebSphere Application
Server V8.5.5.
This means that the Business Automation Workflow components must stay
on WebSphere Application
Server V8.5.5.
However, an external Content Platform Engine or IBM Content
Navigator can remain
on WebSphere Application
Server V9.0.
- You can have different WebSphere Application
Server versions like V8.5 and
V9.0 in the same Business Automation Workflow environment.
Therefore, you can also install Business Automation Workflow on WebSphere Application
Server Network Deployment V8.5 and the external
Content Platform Engine on WebSphere Application
Server Base Edition V9.0 in the
same environment. The requirement is that the JVM versions are the same.

- To continue seeing the case solutions that were created in IBM Case
Manager in Business Automation Workflow after the upgrade,
configure Business Automation Workflow to use
the same Content Platform Engine
environment that IBM Case
Manager uses for the
design object store (DOS) and target object store (TOS). See step 4  in the upgrade procedure.
- To use the same configurations and customizations in IBM Content
Navigator after the
upgrade, configure Business Automation Workflow to use the same IBM Content
Navigator environment
that is used with IBM Case
Manager. See step 6 in the upgrade procedure.

- Ensure that the properties for the Lightweight Directory Access Protocol (LDAP) configuration
that is used by both Business Automation Workflow and FileNet® Content
Manager are matching.
See step 5.
- IBM
FileNet P8
Content Platform Engine and IBM Content
Navigator are on their
respective supported versions.
- Eliminate deprecated systems or reach out to your IBM representative to discuss other options,
such as eForms or
IBM Forms. Important: (Deprecated) eForms and IBM Forms are supported only with an
embedded IBM Content
Navigator
configuration. Using an external IBM Content
Navigator
configuration is the only upgrade path for a production Business Automation Workflow environment.
- Ensure that all participant computers have a hostname with a domain name suffix, for example,
my\_computer.my\_domain\_name .com.
- Use a Trusted CA SSL certificate. Otherwise, a message is displayed stating that resources for
straight-through processing are not reachable. See How do I avoid
"The resources that are required for straight-through processing are not reachable" error being
displayed when trying to access Case client from an external IBM Content Navigator
configuration.

## Choose your upgrade path

Based on whether you need a production or a non-production environment, choose the appropriate
upgrade path. You can upgrade your IBM Case
Manager system to
Business Automation Workflow by using
either an external IBM Content
Navigator or the
embedded IBM Content
Navigator.

See Upgrading IBM Case Manager to IBM Business Automation Workflow.

## Update your custom widgets, plug-ins, and extension packages

Update your custom widgets, plug-ins, and extension packages, to make them work with the new
Business Automation Workflow
configuration. See steps 7.a and 7.b in the upgrade
procedure.