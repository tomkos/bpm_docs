# Distributing solutions as templates

## Before you begin

Be sure to have your completed configuration checklist available.

## About this task

To distribute a solution template, use the Case administration client to export the solution
template as a package file that can be imported into another environment. The package that you
export includes all assets that were created for the solution in Case Builder.

## Procedure

To distribute a solution template:

1 Export the template from your source development environment.
    1. Start the  Case administration client .
 Enter the following URL in a
browser:
http://server:port/navigator/?desktop=bawadmin
server
is the IBM® Content
Navigator server name or IP
address.
port is the IBM Content
Navigator port number.
    2. In the navigation tree in the left pane, select the design object store that contains the
template that you want to distribute and click Solution Templates.
    3. On the Solution Templates page in the right pane, select the
template.
    4. Click Actions > Export and complete the wizard steps.
2 Import the template into the target development environment.

1. Start the  Case administration client for the target
development environment.
2. In the navigation tree in the left pane, select the design object store into which you want to
import the template and click Solution Templates.
3. On the Solution Templates page in the right pane, click
Import and complete the wizard steps.

## What to do next

If you also want to distribute assets that were created in non-workflow tools, package these
assets by using their native tools so that you can import the assets for any solution that is
created from the solution template.

In addition, distribute a comprehensive set of migration and deployment instructions that are
customized for solution applications that are created from the solution template.

The process of preparing solution application assets is similar to the process used when a
solution application is migrated to another environment. For more information, see Preparing for solution migration.