# Manage Team

This view helps to control the security of a particular case. You can set the team members as
owners who can access and control a case.

1. Click Manage Team.
2. Select a role from the Roles list.
3. Select a user from the Available list. The available users are the people
who are assigned to the selected role in the solution.
4. Click the Add button.Note: Click the Make Owner
button to make the selected user a team owner.

- If you are creating the team for a case, then you are automatically added as an owner of that
case team.
- As an owner, you cannot remove yourself from the owners' list; Only another case owner can
remove you from the list.
- If you are only member of the team and not an owner, you have a read access and cannot modify
the case membership.

## Configuration properties

| Property                    | Description                                                                                                                                                         | Data type   |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Target Object Store Name    | The repository name that the view needs to connect.                                                                                                                 | String      |
| Case Identifier             | The Case Identifier of the case instance needed by the view.                                                                                                        | String      |
| Get Repository Name Service | Service to retrieve the repository name that is associated with the case activity.                                                                                  | String      |
| Initial size                | The initial number of rows that are displayed against each of the columns in the Manage team dialog box. Default: When no value is specified, 5 rows are displayed. | Number      |
| Appearance                  | Appearance                                                                                                                                                          | Appearance  |
| Hide Manage team Button     | To hide the default Manage team button from the Case Details page.                                                                                                  | Boolean     |
| Color style                 | To change the button color style.                                                                                                                                   |             |
| Shape style                 | To change the button shape style.                                                                                                                                   |             |
| Size                        | To change the button size style.                                                                                                                                    |             |
| Outline only                | To use an outline only appearance for the button.                                                                                                                   | Boolean     |
| Icon                        | To change the button appearance to an icon.                                                                                                                         | String      |
| Width                       | To change the width of the button.                                                                                                                                  | String      |
| Icon location               | The location of the inout icon.                                                                                                                                     |             |
| Ghost style                 | To change the button appearance with no solid fill (the body of the button adopts the look of the background).                                                      | Boolean     |