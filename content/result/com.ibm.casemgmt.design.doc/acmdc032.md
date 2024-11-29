# Migrating and deploying case management solutions

Add the Enterprise Content Management (ECM) technical user
(EmbeddedECMTechnicalUser) as a member of the Solution administrators user
group. The project and solution migration process configures this user as the owner of solution
artifacts. Solution administrators must be a member of the tw\_admins group and have
access to the Workflow Server or
Workflow server repository.

For more information about EmbeddedECMTechnicalUser user, see Business Automation Workflow security roles.

For more information about the Solution administrators group, see Planning for security in the development environment .

- Solution migration and deployment

You can migrate a solution from one development environment to another development environment, a test environment, or a production environment. After you develop and test a case management solution, you must deploy the solution in the production environment to make the solution available for your case workers.
- Preparing for solution migration

To help you prepare for migration, identify and collect information about the solution assets that you want to migrate. In addition, prepare a comprehensive set of migration and deployment instructions that are tailored for your environment and solution applications. If your solution package includes assets that are managed by FileNet® P8, you must create the FileNet Deployment Manager deployment tree and environment definition.
- Migrating solutions

To migrate a solution, you export the solution assets that were defined in Case Builder and optionally other solution application artifacts from the development environment.
- Deploying migrated solutions

Deploying a solution makes it available as an application in the target environment.
- Configuring the target environment after solution deployment

After you migrate a solution and deploy the solution package and its related assets, you must configure some system settings to make the solution operational.
- Modifying solutions after deployment

If you update the solution design, you can redeploy the solution to a production object store that already contains cases for the solution. Modifying a case and redeploying it affects existing case data and new case data. Before you modify a solution that was deployed into production, you must plan for how the changes affect both your new cases and existing cases.
- Verifying solution deployment

Verify your solution completely in your test and pre-production environments before you deploy the solution into production. After you deploy the solution, test the solution to verify that all of the components are working correctly.