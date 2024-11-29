<!-- image -->

# Fixing the CWSCA9523E error so you can use HTTPS to call a REST endpoint

## Procedure

To fix this error and call a REST endpoint by using HTTPS, complete the following
steps:

1. Open the Properties view for the import.
2. Select Binding > Advanced
Configuration.
3. On the Security tab, enter any value for SSL configuration
name.
4. Select File > Save
All. The error no longer appears in the
Problems view.
5. Generate the .ear file and install it on IBM® Business Automation
Workflow or use the unit test
environment (UTE) in IBM Integration
Designer.
6. Open the IBM console. For the UTE, go to https://localhost:9043/ibm/console and use
celladmin for the user name and the password.
7. Go to Security > SSL certificate and key
management > Key stores and
certificates > NodeDefaultTrustStore > Signer
certificates.
8 Click Retreive from port and enter the followinginformation: and then click Retrieve signer information and clickOK .
    - Host - for example, virtserver.swaggerhub.com
    - Port - 443
    - SSL configuration for outbound connection - NodeDefaultSSLSettings
    - Alias - for example, virtserver.swaggerhub.com
9. Go to Applications > SCA
modules > your module's
name. The Module components
view opens.
10. In the Module components view, go to
Imports > import
name > Binding > HTTP.
11. For SSL Configuration, select
NodeDefaultSSLSettings and click OK to save the
configuration.

## What to do next