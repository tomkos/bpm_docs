# Working with projects

- Versioning projects

Versioning provides the ability for the runtime environment to identify snapshots in the lifecycle of a project, and to be able to concurrently run multiple snapshots on a workflow server.
- Managing snapshots

Snapshots record the state of items within a workflow project at a specific point in time. You can create snapshots in Workflow Center or in IBM® Process Designer. Snapshot management, such as installing, exporting, and archiving, is performed in Workflow Center.
- Managing branches

You can enable and manage branches for the process applications and toolkits that you create or have administrative access to. Branches are called tracks in IBM Process Center. You cannot enable branches, as branches are not supported, for case solutions.
- Cleaning up branches and snapshots

To clean up, or delete, a branch, you can delete the entire project, which deletes all the branches and snapshots.
- Configuring projects for a CI/CD integration

Github offers the facility to configure a webhook that you can use to trigger an automated and secure continuous integration and continuous delivery (CI/CD) pipeline hosted in your preferred CI/CD tool. When a new snapshot of your workflow project is created, you can trigger the Github webhook by pushing a file descriptor of the project (in JSON format) to a configured Git repository, which in turn triggers the CI/CD pipeline.