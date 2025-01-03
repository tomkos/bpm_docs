# Deploying migrated solutions

## About this task

When you design and create a solution, you must decide what the solution locale
is. The solution locale refers to the locale of display names, such as case properties, case types,
activities, and other solution artifacts that you create with Case Builder. When you deploy the solution to a target environment
for the first time, you must deploy the solution under the same locale to ensure that the display
names are preserved.

- Backing up the target environment before deploying solutions

Create a backup of the target environment before you deploy any solutions that you migrated.
- Deploying prerequisite assets

If you extend your solution with non-case management assets, you must migrate the assets to the target domain by using the appropriate migration tool for that asset, such as FileNet Deployment Manager for assets managed by the Content Platform Engine or the Process Configuration console for Content Platform Engine Process Services objects. Some assets must be deployed before you use the  Case administration client to deploy the solution package.
- Deploying a solution with Business Automation Workflow

You use different ways to deploy a solution depending on the type of server to which you are deploying the solution.
- Installing a case solution by using REST APIs

Installing a case solution on a production server or Workflow Server makes it a runnable application.
- Deploying postrequisite assets

Some assets must be deployed after you use the Case administration client to deploy the solution package.