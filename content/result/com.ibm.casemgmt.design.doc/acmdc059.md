# Solution migration and deployment

When you migrate a solution, you move the solution definition data and its related
assets to a different environment. When you deploy a solution, you make the solution
operational in the target environment.

Several types of assets must be exported from the development environment and imported into the
target environment. Some assets, such as class definitions and property templates, are usable
immediately after migration. Other assets, like workflow definitions, must be deployed to become
usable. After migration, the various assets are combined to re-create the solution in the target
environment.

## Migration and deployment task flow

1. Before you migrate a solution, you must test the solution and ensure that the solution works
correctly in the development environment.
    - Legacy case solution package: A solution package consists of assets that are stored in the
solution folder in a case management design object store. You use the Case administration client to export the solution
package from the development environment.
    - Workflow Center case solution project: A case solution project snapshot consists of assets that are stored in the solution
folder in a case management design object store. You use Workflow Center to
export a snapshot of the solution
package from the development environment.
- If the solution includes solution application assets that were created with other FileNet P8 tools, use FileNet Deployment
Manager and Process Configuration
Console to export the assets from the development environment.
- If the solution includes assets that are managed by other IBM products or tools or external products or tools, use tools and processes that are native
to those products and tools to migrate the assets from the development environment.

- Legacy case solution package: Use the Case administration client to import the previously
exported solution package to the staging object store of the test or production environment. (If you
migrate a solution from one development environment to another, import the solution package to the
design object store of the target development environment.)
- Workflow Center case solution project:
Use the BPMInstallPackage command to install the previously exported solution
package snapshot .zip to the test or production environment. See BPMInstallPackage command. (If you migrate a solution from one development environment to
another, import the solution package .twx to the target development environment.)
- If you exported solution application assets that are managed by other FileNet P8 tools, use FileNet Deployment
Manager and Process Configuration
Console to import the assets to the test or production environment. Importing these assets also
deploys the assets in the target environment.
- Legacy case solution: Use the Case administration client to deploy the migrated
solution in the test or production environment.
- If you exported assets that are managed by other IBM
products or tools or external products or tools, use tools and processes that are native to those
products and tools to make the assets operational in the test or production environment.
- Depending on the solution application, you might need to configure the environment after you
deploy the solution. For example, you might need to import security settings and audit settings. If
the solution is translated, you must migrate the translated user interface elements.
- Test the solution to ensure that it works correctly before you release the solution to your case
workers.