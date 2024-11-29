# Solution import problems

## Symptoms

1. When you import the solution, the Case configuration tool displays the following
message: A uniqueness requirement has been violated.
The value for property ContainmentName of class
DynamicReferentialContainmentRelationship is not unique.
2. Case Builder displays
the imported solution as being out of sync or as already deployed
even though you did not yet deploy the newly imported solution.
3. When you deploy the imported solution, you receive the following
error message: FNRPA0037E The page that is associated with the step
 processor cannot be found because no page ID exists for the
 page name page.
 You receive this error
for every page that is missing from the solution package.

## Causes

1. The solution that you are importing has the same name as an existing
solution and the objects in the solutions have the same name but different
GUIDs. For example, if you import a solution into the production environment
and then delete pages from the solution with the same name in the
development environment and export the pages again, importing the
solution fails because now the pages have the same name but different
GUIDs.
2. A newly imported solution displays as deployed because a previous
version of the solution might have been deployed, and Case Builder is displaying the status
of the previously deployed solution for the newly imported solution.
3. The solution package is missing one or more pages.

## Diagnosing the problem

1. See the Case configuration tool debug trace logs and the
FileNet® P8 error logs, which will
list the GUIDs of the problem objects in the full stack trace. The Case configuration tool log file is located in
the /logs directory in the location where you installed IBM Business Automation
Workflow. If you use WebSphere® Application
Server, the FileNet P8 server log files are located in
<WAS\_install\_location>/WebSphere/AppServer/profiles/<AppServer01>/FileNet/server1.
2. If you removed a solution from the design object store and then re-imported that solution into
the same environment or you copied a solution that you previously removed back into the same
environment, Case Builder might
display the newly imported solution as deployed, even though it is not deployed. Case Builder might also show the copied
solution to be out of sync.
3. Compare the pages of the imported solution with the source solution
on the original development environment to determine what pages need
to be regenerated.

## Resolving the problem

1. If you are importing a solution that already exists in the system,
ensure that the common objects between the solution that you are importing
and the solution in the system have matching GUIDs.
2. Reinitialize the target object store to remove the previously
deployed solution and deploy your solution again.
3. If the solution package is missing pages, compare the pages of
the imported solution to the source solution on the original development
environment then redeploy the solution to the original development
environment to ensure that the solution successfully deploys. Also,
ensure that all of the pages are generated. Export the solution package
again and import and deploy the solution to the target environment
again.