# Creating the UMS database admin secret

## Procedure

For your database (Db2, Oracle, PostgreSQL or MSSQL), generate the UMS database admin
secret ibm-baw-ums-secret.

1. Copy the following as ums-dba-secret.yaml, then edit it to specify the
required user identifiers and passwords.
apiVersion: v1
kind: Secret
metadata:
  name: ibm-baw-ums-secret
type: Opaque
stringData:
  adminUser: "umsadmin"
  adminPassword: "password"
  oauthDBUser: "oauthDBUser"
  oauthDBPassword: "oauthDBPassword"
  tsDBUser: "tsDBUser"
  tsDBPassword: "tsDBPassword"Where 
adminUser / adminPassword
Specify the user and password values for an internal UMS admin user that will be created in a
local user registry. This user must be unique and not exist in the LDAP user registry. If these
parameters are left out, the values will be generated.
oauthDBUser / oauthDBPassword
Specify the user and password for the OAuth (SSO) database.
tsDBUser / tsDBPassword
Specify the user and password for the UMS Teams database. If you do not have a separate UMS
Teams database, specify the same database user ID and password that you specify for
oauthDBUser and oauthDBPassword.
2. Create the secret by running the following command:

oc create -f ums-dba-secret.yaml
3. Make a note of the secret name ibm-baw-ums-secret, that you will need later to
specify for the ums\_configuration.admin\_secret\_name in the custom resource.