# Modifying solutions after deployment

- Redeployment restrictions for modifying a solution

You can redeploy a solution to an object store. For example, you can update the solution design and then deploy the solution to a production object store that already contains cases for the solution. Modifying a case and redeploying it affects existing case data and new case data. Before you modify an existing solution, make sure that your changes will not cause problems when you redeploy the solution to an object store that already was associated with that solution.
- Synchronizing cases with solution data

If you modify a solution after it is deployed, run the case synchronizer utility to update existing instances to match the changes that you made. You can run the utility by using commands or the Case Manager REST protocol.