# Troubleshooting server tools after a typical installation on Windows

If you ran the typical installation as an administrator, the deployment environment created
during the typical installation process must be administered by a user ID with likewise elevated
permissions. If you are now administering the deployment environment with a nonadministrative user
ID, you must elevate your permissions to Administrator to do operations such as starting and
stopping servers, deployment managers, and nodes, or running the Quick Start console or the Profile
Management Tool. Running these operations with a non-elevated ID will result in error messages.

- BPMQuickStart command and the Quick Start console
- firststeps command and the First steps console
- manageprofiles command and the Profile Management Tool
- startServer command
- stopServer command
- startManager command
- stopManager command
- startNode command
- stopNode command

If you cannot elevate your user ID authority to Administrator, install IBM® Business Automation Workflow using a custom installation path and
configure the deployment environment with a nonadministrative user ID.