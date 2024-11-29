# Rolling upgrade for case projects and legacy case solutions in the production
environment

As of 24.0.0.0, it is not required that you upgrade the development environment and the project versions before
you deploy a project.

1. Case projectsYour project can now be installed even if the project
version is earlier than the staging or production environment version. Previously, the development
environment upgrade and project version upgrade had to be done first to deploy the case project to
the Workflow Server.
2. Legacy case solutionsDeployments are allowed if your case solution
version is 22.0.1 or later. If the case solution version is earlier than
22.0.1, upgrade the solution in the Staging or Production environment by using the
Upgrade Swagger API, and then deploy the upgraded case solution.
3 Upgrade solutions directly within the production environment
    - Previously, to upgrade the workflow projects you had to upgrade them using the development
environment and then the upgraded workflow projects had to be installed in production. The solution
version upgrade and the environment upgrade had to be done separately. Now, the workflow project is
upgraded along with the solution installation in the production environment. The workflow project
upgrade happens during the installation of the workflow project in the production environment.
Rolling upgrades are supported only for new workflow projects that have not yet been deployed in
production.
    - To upgrade the legacy case solutions in production, use the Swagger API.
    - During installation of the work flow project in production environment for the rolling solution
upgrade, configure the 100 custom.xml. The following configuration needs to be
added
<server merge="mergeChildren"><run-automatic-case-project-upgrade merge="replace">true</run-automatic-case-project-upgrade></server>
For configuring the 100Custom.xml file, see:The 100Custom.xml file and configuration