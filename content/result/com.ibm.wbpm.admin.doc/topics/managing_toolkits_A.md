# System toolkits

- Don't modify anything in a system toolkit, such as the library items in that toolkit.
- Don't edit the project or snapshot properties, like changing the names or acronyms for a system
application or toolkit, because doing so will cause issues for upgrade commands.
- Don't deactivate, archive, or delete system snapshots or you might experience issues while
upgrading or using Business Automation Workflow features.

In most cases, if you delete a system toolkit you
just need to run the bootstrapProcessServerData command to reinstall the system
toolkit. For more information, see Loading the database with system information in a network deployment environment on Windows.

## System Data toolkit (TWSYS)

- Many predefined business objects. You can open a business object in IBM Process
Designer and review the
Documentation field to learn when and how to use each business object.
- Traditional:  Assets
needed for SQL integration so that you can easily integrate with external databases.
- Traditional:  Assets
that provide XML transformation and XML validation.

## System Governance toolkit (TWSYSG)

- The toolkit has integration services for installation and snapshot status, templates that
provide business process definitions for installation and snapshot status change, and governance
business objects.
- Custom governance processes must be developed from one of the templates in the toolkit. The
System Governance toolkit provides two templates, the Installation Requested template and the
Snapshot Status Change template. Create custom governance business process definitions to meet your
business needs by using these governance templates as a base.

## Content Management toolkit (SYSCM)

There are two versions of the Content Management toolkit: one for the
Traditional environment (8.6.0.0) and one for the
Traditional or Container environment (8.6.0.0\_TC).
 Traditional:  Predefined assets that use and
support deprecated capabilities are only in the 8.6.0.0 Content Management toolkit, not in the
8.6.0.0\_TC Content Management toolkit.

Add the Content Management toolkit to your dependencies to gain access to Enterprise Content
Management types and services. You need these resources to allow a business process developed in
Process Designer to work with an Enterprise Content
Management system. The toolkit also contains data types that enable integration with Enterprise
Content Management systems, such as the ECMContentEvent business object. For more information, see
Content Management toolkit.

## Dashboards toolkit (SYSD)

Add a dependency on the Dashboards toolkit so that you can create custom, localized dashboards
with the reusable interface elements, implementation services, and data objects. For more
information, see Controls in the Dashboards toolkit.

## Responsive Portal Components toolkit (SYSRPC)

The Responsive Portal Components toolkit contains a set of coach views that you can use to design
a custom portal that can run on mobile and desktop devices. For more information, see Controls in the Responsive Portal Components toolkit.

## UI toolkit (SYSBPMUI)

The UI toolkit, which is the default toolkit for coaches, gives you access to an extensive set of
views for designing applications that can run on multiple device types. All the views in the UI
toolkit are suitable for use on both desktop and mobile devices. Use the rich set of out-of-the-box
views in the UI toolkit to create widget-style or composite-style views from scratch or by combining
other views. For more information, see UI toolkit.

## Workplace toolkit
(SYSWPT)

The Workplace toolkit
consists of a set of views that you can use to design your own client-side human service-based
business applications and dashboards that are customized for work management in Workplace. The Workplace toolkit views are
available in the Designer palette for dashboard and application design. For more information, see
Workplace toolkit.

## Coaches toolkit (deprecated) (SYSC)

Add a dependency on the Coaches toolkit so that you can add stock coach views to your coach.
Process applications created in version 8.5.6 or earlier have a default dependency on this toolkit.
For more information, see Coaches toolkit.

## Responsive Coaches toolkit (deprecated) (SYSRC)

Add a dependency on the Responsive Coaches toolkit so that you can add responsive coach views to
your coach. For more information, see Responsive Coaches toolkit.

## SAP Guided Workflow toolkit (deprecated) (SGW)

Because SAP runtime systems are not process driven and little or no visibility of throughput and
backlog is available, process issues can be difficult to detect and correct. Therefore, users must
be trained to understand and comply with the SAP process documentation to complete their business
activities. However, using the SAP Guided Workflow toolkit, which uses the SAP WebGUI technology,
you can enable an information flow between the SAP transactions and Business Automation Workflow, prioritize process tasks dynamically, sequence
tasks in the correct order, and customize and refine business processes.

You can generate SAP guided workflows either automatically for SAP business projects that are
imported from SAP Solution Manager, manually for business process definitions (BPD) that are defined
in Business Automation Workflow, or interactively by using SAP
Transaction coach views that you can build by dragging SAP components from specified SAP
transactions. After you generate the SAP guided workflow, you can use it to enable the information
flow between the SAP transactions and Business Automation Workflow,
or you can customize it to update the implementation of various steps in your business flow in
Heritage Process Portal.