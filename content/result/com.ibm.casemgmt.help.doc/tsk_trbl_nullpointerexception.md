# Deploying case solution fails with NullPointerException

## Symptoms

When you deploy the case solution snapshot using REST API, the following error occurs:
FNRPA0949E An attempt to reindex case instances to Elasticsearch after a deployment has
failed.

## Resolving the problem

1. Using ACCE, go to Search > New object store search
2. Search by using the assignment base class. The list of users that match your search criteria
appears.
3. Verify the user deleted from LDAP.
4. Select the user and delete by using bulk actions.