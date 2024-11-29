# Importing a project into a branch

## Before you begin

## Procedure

When two people work in isolation on separate features that are related to the same
project, you can import the projectin the core development environment and copy the changes over.

1. In the classic Workflow Center, under
Process Applications tab or Toolkits tab, click
Import Process App or Import Toolkit.

Remember: When dependent toolkits that are part of a process application are imported in
a destination Workflow Center, they are imported to
the branch they belonged to before the export from the source. You cannot select the target branch
for such dependent toolkits. If you want the toolkits to be imported after selecting the destination
branch, export the dependent toolkit from the source Workflow Center, and then import it into the destination
Workflow Center. Using this method, you can select
the branch where you want to import the dependent toolkit to. Now, when you import the process
application with the dependent toolkit, the toolkit is not imported as a dependency. For any
dependent toolkit that the you want to import separately, you must import it before importing the
process application with the dependent toolkit.
2. Click Browse, select the file that
you want to import, and click OK.
3 Select one of the following options:
    - To import the project to the main branch, select Existing Branch (Main)
and click OK.
    - To import the project to a new branch, select New Branch, name and
describe the branch, and then click OK.

## Results