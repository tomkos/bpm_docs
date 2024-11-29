# Promoting case solutions to the Workflow Center

## About this task

After you upgrade your IBM Case
Manager system to
IBM Business Automation
Workflow, you can promote
your case solutions to workflow projects to be able to take advantage of new capabilities that are
offered in IBM Business Automation
Workflow, or
you can continue managing your case solutions in the Case Builder landing page as usual. The
promoted projects can continue to be edited and deployed as before.

- When you're ready to take advantage of the capability offered by the Workflow Center to manage and deploy
unified projects, you can promote your case solutions from the 5.3.x version to workflow projects.
The new workflow projects are automatically migrated to the Workflow Center, where they are once
again labeled as "case solutions" for familiarity.
- Case solutions that are not promoted still open in the classic Case Builder view. Once promoted, the
case solutions are no longer visible in the Case Builder landing page.
- Continue using existing case solutions that are not promoted in the same way as you did in
IBM Case
Manager. The
tools and the client-side runtime environment that you are familiar with are still available in
IBM Business Automation
Workflow.

## Procedure

To promote a case solution:

1. Open the Case Builder landing page by loading its URL in a web browser. For example,
https://servername:9080/CaseBuilder.
2. If your case solution is flagged with the Solution must be upgraded
icon, open the solution to update it to the current version.
3. To manage a case solution in the Workflow Center, promote it to a workflow project. 
The case solution appears in the Workflow Center and is removed from the
Case Builder landing page. See the topic Promoting case solutions to workflow projects.
4. Open the promoted solution from the Workflow Center and click
Redeploy All to deploy the solution.

## What to do next

- Edit and develop the case solution as usual in the Designer. See Adding and deploying a case management solution.Note: Commit, deploy, test and deliver actions have moved to the
Designer.
- Define activities to work with new or existing processes that reside in the same case solution
or in a different case solution, process app or toolkit. See Adding an activity with a new process.
- In processes that implement case activities, use new operations that interact with case
JavaScript operations. You can also use services that are available in the Content Management
Toolkit to work with case properties. See Interacting with a parent case from a process.
- Create snapshots to manage case solution versions. See Managing snapshots.
- Export the snapshot and install it to the Workflow Server. See Installing snapshots
or Installing a case solution by using REST APIs.