<!-- image -->

# Additional Ant tasks

Although your script will be composed of mostly standard
Ant tasks, you will find these additional Ant tasks helpful for testing applications created in IBM® Integration
Designer.

- importPI
- importProject
- wid.deploy
- wid.undeploy

## importPI

This task imports a project
interchange file into the workspace.

| Attribute   | Description                                             | Required?                           |
|-------------|---------------------------------------------------------|-------------------------------------|
| pif         | The absolute path to the project interchange (PI) file. | Yes                                 |
| overwrite   | Overwrite the current project in the workspace.         | No.                                 |
| projects    | Comma-delimited list of projects to import.             | No. Default is import all projects. |

## importProject

This task imports
a project into the workspace.

| Attribute   | Description                          | Required?   |
|-------------|--------------------------------------|-------------|
| projectName | The name of the module or test case. | Yes         |

## wid.deploy

This task deploys a project to a server. The default server is IBM Business Automation
Workflow.

| Attribute      | Description                                                                          | Required?   |
|----------------|--------------------------------------------------------------------------------------|-------------|
| projectName    | A project name, which must be either a module, a mediation module or a test project. | Yes         |
| connectionType | Type of connection.                                                                  | No          |
| password       | Password for server.                                                                 | No          |
| port           | Port number.                                                                         | No          |
| profile        | Server profile.                                                                      | No          |
| userid         | Userid for server.                                                                   | No          |

## wid.undeploy

This task undeploys a project from a server. The default server is IBM Business Automation
Workflow.

| Attribute   | Description                                                                          | Required?   |
|-------------|--------------------------------------------------------------------------------------|-------------|
| projectName | A project name, which must be either a module, a mediation module or a test project. | Yes         |