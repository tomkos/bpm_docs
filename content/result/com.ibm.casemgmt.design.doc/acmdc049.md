# Exporting solution assets from a design object store

You can use Workflow Center or
Case administration client to export
solution assets from the design object store. This export process creates a solution package that
contains all the assets that were created for the solution in Case Builder.

You can use the Case administration client to export legacy Business Automation Workflow solution assets from
the design object store if they have not yet been promoted into Workflow Center.
This export process creates a solution package that contains all the assets that were created for
the solution in Case Builder. The
information on this page pertains to the export of legacy workflow solution assets.

For case solutions that have been promoted into Workflow Center to become case solution projects, you need to export a snapshot. A snapshot contains
all the assets that were created for the solution in Case Builder. For
more information on how to export a snapshot, see Importing and exporting projects.

## Before you begin

The  Case administration client can only
export a solution package if the solution was committed from Case Builder.

If the solution includes assets or components that are not managed by Business Automation Workflow or by FileNet® P8 tools, migrate these external
assets to the target environment by using native tools and processes as required by the particular
solution application asset.

## Procedure

To export a legacy case solution package from Case administration client:

1. Start the IBM® Business Automation
Workflow
Case administration client .
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
server
is the IBM Content
Navigator
server name or IP address.
port is the
IBM Content
Navigator port
number.
2. In the navigation tree in the left window, select a design
object store and click Solutions.
3. On the Solutions page in the right
window, select the solution that you want to export.
4. Click Actions > Export > Solution and complete the wizard steps. After you complete the wizard steps,
the solution package ZIP file is created in the folder that you specified.

## What to do next

- If your solution contains assets that were created in FileNet P8, use FileNet Deployment
Manager to create a deploy package
that contains the assets.
- If your solution is associated with a process application, you must export a snapshot of the process
application. Before you import the solution
package to the target environment, you must import the process
application.
- If your solution includes pages that contain custom widgets, which might not exist in the target
environment, you must migrate the widgets before you import the solution package. The pages are
included in the Pages folder of the exported solution.
- If your solution uses properties that are associated with marking sets and you move the solution
to a different environment, you must re-create the marking sets and any property templates that use
the marking sets in the target environment. To re-create the marking sets, use the appropriate
FileNet P8 tools. When you
re-create the properties, you must use the same symbolic name that is used in the source
environment.To migrate the marking sets, use FileNet Deployment
Manager to export and import the
marking sets but not any property templates, which are created when the solution is deployed by
Business Automation Workflow.