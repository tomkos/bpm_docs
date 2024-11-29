# Deploying a solution with Business Automation Workflow

You use different ways to deploy a solution depending on the type of
server to which you are deploying the solution.

- If you are using a Workflow Center
development profile environment, deploy promoted case solution projects by using Workflow Center.
You can deploy legacy case solutions by using legacy Case Builder or Case administration client.
- If you are using a Workflow Server production profile
environment, you can install a solution by using Workflow Center or the command line for offline installation. You can deploy legacy case
solutions by using Case administration client.

- Deploying a solution by using Workflow Center or legacy Case Builder
- Installing a solution using Workflow Center or the command line
- Deploying a legacy case solution using Case administration client

## Deploying a solution by using Workflow Center or
legacy Case Builder

### Procedure

To deploy a case solution by using Workflow Center or
legacy Case Builder:

1. Start Workflow Center or Case Builder.
2. Enter the following URL in a browser: 
http://server:port/WorkflowCenteror
http://server:port/CaseBuilder where
server is the Business Automation Workflow IP address or the fully
qualified server name, and port is the Business Automation Workflow port
number.
3. Open a solution by clicking a solution card.
4. To deploy the solution, click the deploy button from the solution
details.

## Installing a solution using Workflow Center or
the command line

## Deploying a legacy case solution using Case administration client

### Procedure

To deploy a legacy case solution by using Case administration client:

1. Start the Case administration client.
2. Enter the following URL in a
browser: http://server:port/navigator/?desktop=bawadmin
where server is the IBM® Content
Navigator IP address or
the fully qualified server name, and port is the IBM Content
Navigator port
number.
3. In the navigation tree, select a design object store and click
Solutions.
4. In the Solutions page, select the solution that you want to
deploy.
5 ClickActions > Deploy and completethe wizard steps. You can deploy a solution from either a design object store indevelopment environment or a staging object store in production environment.
    - If you deploy from a design object store in development environment, the target environment name
field is automatically populated by the wizard.
    - If you deploy from a staging object store in production environment, you must select the target
environment name from the Target Environments list. This list contains the
target environments in the object store in production environment staging that have the same
integration type as the solution.