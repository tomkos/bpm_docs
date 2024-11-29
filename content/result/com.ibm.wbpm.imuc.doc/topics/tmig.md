# Upgrading and migrating

Traditional: 
Upgrading refers to the process of installing a new release of the product on top of
the previous release and updating the existing installation, configuration, and database in place.
Migrating refers to the process of moving applications and configuration information
from an earlier version of a product to a later version of the product, or from one product to a
different product.

If you want to augment IBM® Case
Manager with
Business Automation Workflow, see Upgrading IBM Case Manager to IBM Business Automation Workflow. If
you have both IBM Case
Manager and IBM Business Process Manager
, first upgrade IBM Business Process Manager
 to the latest version of Business Automation Workflow and then follow the instructions in Upgrading IBM Case Manager to IBM Business Automation Workflow.

## About this task

- Update your product installation from an earlier version of IBM Business Automation Workflow
Enterprise to IBM Business Automation Workflow
Enterprise 24.x.
- Update your product installation from an earlier version of IBM Business Automation Workflow
Express to IBM Business Automation Workflow
Express 24.x.
- Upgrade your product installation from IBM Business Automation Workflow
Express to the same version of  IBM Business Automation Workflow
Enterprise. See Upgrading a product installation.
- Change your deployment environment from Standard to Advanced. See Upgrading a deployment environment from Standard to Advanced.

- Move to the same version (IBM Business Automation
Workflow 24.x) on new
hardware.
- Move to IBM Business Automation Workflow
Enterprise
24.x from IBM Business Process Manager
Advanced
or IBM Business Process Manager
Standard. You
must use artifact migration.
- Move to IBM Business Automation Workflow
Enterprise
24.x from IBM Business Process Manager
Advanced
or IBM Business Process Manager
Standard earlier
than V8.5.0. You must use artifact migration.
- Move to IBM Business Automation Workflow
Express
24.x from any version of IBM Business Process Manager
Express. You cannot upgrade
from IBM Business Process Manager
Express to
IBM Business Automation Workflow
Express. You must use
migration.
- Move to IBM Business Automation Workflow
Enterprise
Service Bus 24.x from IBM Business Process Manager
 Enterprise Service
Bus 8.6. You must use artifact migration.

- Upgrading from IBM Business Automation Workflow
Enterprise or IBM Business Automation Workflow
Express 18.0.x, 19.0.0.1, or
19.0.0.2 to 24.x is
not supported. Upgrade to 23.0.1, then upgrade to 24.x.
- You cannot upgrade from IBM Business Process Manager
Express to IBM Business Automation Workflow
Express. Use migration
instead.
- Upgrading from IBM Business Process Manager
 V8.5 or V8.6 is not
supported. Install a fix pack earlier than 22.0.2, then upgrade to 23.0.1.
- Migrating from IBM Business Process Manager
 V7.5.x to IBM Business Automation Workflow 24.x is not supported.
Migrate to IBM Business Automation Workflow
V19.0.0.3, then install the latest cumulative fix. See Migrating and upgrading in the V19.x information.
- Migrating from WebSphere® Process
Server V7.0.x to IBM Business Automation Workflow is not supported.
Migrate to IBM Business Process Manager

V8.6 cumulative fix 2018.03, then install the fix pack earlier than 23.0.1, then upgrade to latest
cumulative fix. See Migrating and upgrading in the V8.6.x information.
- Migrating from IBM Business Process Manager
 V8.0.x to IBM Business Automation Workflow 24.x is not supported.
You can use artifact migration, or you can migrate to IBM Business Automation Workflow V20.0.0.1, then
install the latest cumulative fix.
- Migrating from IBM Business Process Manager
 Advanced or IBM Business Process Manager
 Standard V8.5.x or
V8.6 to IBM Business Automation Workflow 24.x
is not supported. You can use artifact migration, or you can migrate to IBM Business Automation Workflow V22.0.1, then install
the latest cumulative fix.
- If you are migrating from IBM Business Process Manager
Express to IBM Business Automation Workflow
Express, you can use artifact
migration (see Migrating artifacts to IBM Business Automation Workflow) or you can migrate business data and
applications (see Migrating business data and applications from any version of IBM BPM Express to IBM Business Automation Workflow).

1. Define the servers again in the new version of the Heritage Process Portal application.
2. Create a snapshot.
3. Activate the snapshot on Workflow Center.
4. Install the snapshot on Workflow Server.

- Upgrading IBM Business Automation Workflow

You can install upgrades to IBM Business Automation Workflow when they are available. You can also upgrade your configuration, perform a rolling upgrade, or make other changes.
- Upgrading IBM Case Manager to IBM Business Automation Workflow

 Traditional: 
Install Business Automation Workflow and upgrade your environment. You can benefit from the full spectrum of Business Automation Workflow capabilities to manage and deploy unified process and case solutions by using the new common Workflow Center.
- Planning a migration

Before you migrate any production environment, make sure that you have migrated your staging or test environment and have tested your applications in the new environment.
- Migrating artifacts

Artifact migration uses a parallel target production environment that is configured differently from the source production environment. You import the applications from the source production environment into development tools and migrate the applications using the migration procedures of the development tools.
- Migrating business data and applications from any version of IBM BPM Express to IBM Business Automation Workflow

 You can migrate business data and applications, as well as artifacts, from any previous version of IBM BPM Express to IBM Business Automation Workflow.
- Migrating Business Automation Workflow to the same version on new hardware

You can migrate your IBM Business Automation Workflow environment, including applications and running instances, to the same version running on new hardware. The source and target systems can be running different operating systems. For example, you can migrate from a Windows system to a Linux system or from a Linux system to a Windows system.

## Related reference

- IBM Support

## Related information

- Installing fix packs and interim fixes interactively
- Deprecated and removed features of IBM Business Automation Workflow