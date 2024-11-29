# Converting a solution into a template

You can convert a solution into a template. You use templates to quickly create new
solutions that are based on the same design. The template contains all the solution design
information and assets, but you cannot edit the template directly or create running cases from it.

- You create a template from a snapshot of a base case solution.
- You create a new case solution from a snapshot of a template. See Adding a solution.

## Converting a case solution into a template

You create a template from a snapshot of a base case solution. The template inherits the
assets of the solution snapshot it is based on.

### Procedure

To convert a case solution into a template in Workflow Center:

1. Start  IBM® Workflow
Center. Enter the following
URL in a
browser: http://server:port/WorkflowCenterwhere
server is the Workflow Center IP address or fully
qualified server name, and port is the Workflow Center port number.
2. Create a snapshot of the base case solution: in the Case solutions
page, click Details on the case solution tile, go to the
Snapshots tab, select Create a snapshot from the
overflow menu of the solution row, and then name and create the snapshot. The snapshot is
added to the list of solution snapshots.
3. Create a solution template from the snapshot: from the overflow menu of the snapshot row,
click New template. In the Create a template modal,
enter a name and an optional description for the template, and click
Create. The template opens in Case Builder in read-only
mode.
4. To use your template as a base for a new case solution, create a snapshot of the
template: in the navigation tree, select Templates, click
Details on the template tile, go to the Snapshots tab,
select Create a snapshot from the overflow menu of the template row, and then
name and create the snapshot. The snapshot is added to the list of template
snapshots.

## Converting a legacy case solution into a template

You convert a legacy solution into a template in a development environment.

### Procedure

To convert a legacy case solution into a template:

1. Start the Case administration client. Enter the following URL in a
browser: http://server:port/navigator/?desktop=bawadminwhere
server is IBM Content Navigator IP address or fully qualified server name, and
port is the IBM Content Navigator port number.
2. In the navigation tree, select an object store and click
Solutions.
3. On the Solutions page, select the solution that you want to convert into a
template.
4. Click Actions > Convert to Solution
Template and complete the wizard steps.