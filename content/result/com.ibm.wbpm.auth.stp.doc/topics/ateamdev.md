<!-- image -->

# Team development in Business Automation Workflow

## Working with the Workflow Center

The Workflow Center includes
a repository for all processes, services, and other assets created
in Business Automation Workflow authoring
environments. You can use the Workflow Center repository
to share artifacts with other users who are developing process applications
and toolkits.

Workflow Center
provides a convenient location in which to create and maintain high-level
library items such as process applications and toolkits. Administrators
who do not actively work in the Designer view can use Workflow Center
to provide a framework in which BPM analysts and developers can build
their processes and underlying implementations. Another primary task
for administrators is managing access to the Workflow Center repository
by setting up the appropriate authorization for users and groups.
You can use the console in a web browser as well as in Process Designer
and IBM Integration Designer

## Reusing artifacts

Process developers use Business Automation Workflow to reuse
existing items, both within and across process applications. For example,
if you know several services already exist that include artifacts
that you and other developers need, you can access and reuse those
items by including them in a toolkit. Then, from your process application,
you can add a dependency to the toolkit that contains the items. You
can then pick one of the existing services when you choose the implementation
for an activity. The items in the toolkit can also be used by other
developers working in different process applications.

If you are working
with BPEL processes or services in the Business Integration perspective
of Integration Designer,
you can share artifacts from one module by placing them in a library.
You or others can then reuse those artifacts in other modules. To
use artifacts from a library, set up a dependency from that module
to the library using the Integration Designer dependency
editor. You can set up dependencies on a library from any number of
modules.

## Creating and managing groups

If you have
configured Business Automation Workflow to
work with your external security provider, you can view the groups
from that external provider in the Process Center console, but you
cannot edit the external groups. You can, however, add users and groups
from your external provider to any Business Automation Workflow security
groups that you create. When you create a group in Business Automation Workflow, you
can add users and groups from your external security provider to the Business Automation Workflow group.
You can also add Business Automation Workflow users
and groups, so that you can combine accounts from different providers
into one group.

In addition to managing group membership, you
can designate a Team Manager Group for each group. When you have a
Team Manager Group, you can establish a hierarchy for the Team Performance
dashboard available in Heritage Process Portal.

## Team Performance dashboard

You can use standard
dashboards in Heritage Process Portal (deprecated) to
manage your business processes and the work done on these processes.
The Team Performance dashboard shows the current status of the Business Automation Workflow tasks
for the groups for which you are designated as a team manager.

## Tracks

## Software configuration management systems

You
can use Integration Designer with
software configuration management (SCM) systems. You can view or change
the preferences for available version control systems under Window > Preferences > Team.

## Related concepts

- Service-oriented architecture
- Service Component Architecture (SCA)
- Deployment options for IBM Integration Designer
- The runtime environments for IBM Integration Designer
- Task flows

## Related reference

- Keyboard shortcuts for the workbench, Java development tools, and the Debug perspective