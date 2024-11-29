# Configuring EDS for Case Client

## Procedure

To configure EDS:

1. Import the EDS Solution. Say, “EDS\_001”.
2. From  Business Automation Studio, select the
solution and click Advanced context menu.
3. Select the solution and click Actions→ Register External Data
Service.
4. Register External Data Service with the URL:
https://edshost.com:9443/ExternalDataService/ICMEDREST.
5. Click Next.
6. Review the External Data Services to register and click
Finish.
7. After the EDS is successfully registered, import the EDS Server certificate.
 Run the steps in Importing the certificate of an external
service.
8. Run the EDS Solution, you are able to see the external data successfully.
9 Optional: If the EDS application is configured with asecured login, then do the following configuration:
    1. From the WebSphere, select the EDS application
→ Security role to user/group mapping and map the All
Authenticated role to the special subject All Authenticated in Application's
Realm.
    2. Restart the EDS application.