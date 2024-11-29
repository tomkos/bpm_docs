# Configuring the roster to enable launching activity workflows

## Procedure

To configure the roster:

1. In Administration Console for Content Platform
Engine,
select the object store to which the solution was deployed, and click Administrative > Workflow System.
2. On the Workflow System tab, click Actions > Configure Workflow Settings.
3. Navigate to the rosters in the left pane, and highlight
the roster that you want to configure.
4. Right click the roster and click Properties.
5. Click the Security tab, and select Groups.
Select the group for which you want to assign permissions, and move
the group to the Selected Users window.
6. Set the Default rights, and click OK.

## Example

| Group               | Permissions                                                                                                                                                                                                                                                                                                     |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Case viewers        | None.                                                                                                                                                                                                                                                                                                           |
| Case initiators     | Create. When the case is created, workflows associated with activities are launched on behalf of the user who created the case.                                                                                                                                                                                 |
| Case workers        | Create. If case workers must create new activities or start activities, they must have Create rights on the roster in order to launch the workflow. Because there is only one roster for the entire solution, you should specify all groups that are associated with roles to have Create rights on the roster. |
| Case administrators | Query and Create A case administrator needs Query rights for troubleshooting. If administrators must start activities, grant administrators Create rights as well.                                                                                                                                              |

- Roster permissions

A workflow roster is a database structure that stores information about all workflows in an isolated region. Workflow rosters provide Content Platform Engine workflow administrators an efficient way to locate specific active workflows.