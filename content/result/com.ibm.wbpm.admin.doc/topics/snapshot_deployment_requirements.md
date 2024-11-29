# Snapshot deployment requirements

Before you install a snapshot, make sure that you have the proper
requirements.

## Authorization

- The user needs the following access to the process application that depends on the type oftarget environment: Note: To create a generic deployment package, you need read access only. For moredetails on environment type, see Workflow Server configurationparameters and Modifying the IBM Workflow Server environment type .
    - Administrative access to deploy to production environments.
    - Write access to deploy to any nonproduction environments, such as staging and testing.
    - Read access to install to development environments.

For more
details on environment type, see Workflow Server configuration
parameters and Modifying the IBM Workflow Server environment type.

- If the processCenterInstall group is enabled, the user must be a member of the
processCenterInstall group. For more details on
processCenterInstall and offlineInstall groups, see Restricting installation access to runtime servers.

- The user must be a member of tw\_admins or the BPMAuthor user and a member of
tw\_authors.Important: If these internal groups, which are created when
the deployment environment is created, are deleted, you can't deploy snapshots.
Note: For traditional Business Automation Workflow, online deployment uses
the BPMAuthor user. If you override this user with a trust association interceptor (TAI), the new
user must pass these checks.
- If the offlineInstall group is enabled, the user must be a member of the
offlineInstall group to run offline deployment commands.
- Traditional:  if the
snapshot contains advanced content like SCA or BPEL, the user that performs the deployment on the
runtime environment must be assigned the Deployer administrative security role. For more
information, see the deployer role in Administrative
roles.
- Traditional:  if the
snapshot contains any projects with case features enabled, the EmbeddedECMTechnicalUser needs to be
a member of the Solution administrator group or have the same permissions. For more information
about these permissions, see table 3 in Planning for security in the development environment .

## Naming

The acronyms that are used during snapshot deployment must be unique in the runtime environment.
If multiple projects or snapshots are using the same acronyms, a conflict occurs that prevents
deployment. When using multiple authoring environments, it is recommended to deploy only through a
single authoring environment so that naming conflicts can be found before deployment.

## Capabilities

The target runtime server must support the capabilities that are used within the snapshot. The
snapshot might contain various types of content that restricts the types of environments where the
snapshot can be deployed like advanced, case, IBM® Cloud Pak for Business
Automation or container content
types. These added restrictions might be the result of the authoring environment type, project type
or settings, or artifacts contained in the project. When you deploy snapshots to a server without
the required capabilities, you get a message or exception that indicates that the server does not
contain sufficient capabilities to run the snapshot.

Snapshots cannot be deployed if they were created in a newer authoring environment than the
runtime environment. Also, if the snapshot contains case-enabled projects, the runtime environment
version must match the authoring environment where the snapshot was created.

- Snapshots containing advanced content can be deployed only to a traditional Business Automation Workflow deployment environment of
Advanced type.
- Snapshots with case-enabled projects can only be deployment to Business Automation Workflow environments with case
enabled.
- Snapshots that are created in a Cloud Pak for Business Automation authoring environment
can only be deployed to Cloud Pak for Business Automation workflow
environments.
- Snapshots must only contain projects that are restricted for container content when deployed to
container runtime targets.