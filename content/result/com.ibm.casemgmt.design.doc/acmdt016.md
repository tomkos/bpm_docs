# Managing project areas

## About this task

If you have many solution projects in different phases of development, you can define a project
area for each solution so that when a solution is ready to test, you can do so without affecting the
other solutions that share design object store. You can use the Case administration client to define project areas,
remove project areas, move solutions to different project areas, and add or remove users from
project areas.

## Procedure

To manage your project areas:

1. Start the bawadmin desktop. Enter the following URL in a browser:

https://server:port/navigator?desktop=bawadmin
where
server is the Navigator IP address or fully qualified
server name, and port is the Navigator port number. For
the embedded Navigator, the server and port are the same as
the Business Automation Workflow.
2. In the navigation tree in the left pane, select a design
object store and click Project Areas.
3 On the Project Areas page in the rightpane, select a project area and click Actions toedit, register, or delete the project area. Restriction:
    - You cannot delete the default project area; you can delete regular
project areas only.
    - For the default project area, you can add and remove users and
groups. For regular project areas, you can add and remove individual
users only.
    - If you add a solution to a project area and that solution does
not match the integration type of the project area, the solution is
filtered out.
    - If you remove a solution from a project area other than the default
project area, that solution is assigned automatically to the default
project area. However, if the default project area is of a different
integration type than the solution, then the system prevents you from
removing that solution from the non-default project area.