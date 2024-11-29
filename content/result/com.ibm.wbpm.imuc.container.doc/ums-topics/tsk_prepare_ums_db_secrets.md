# Securing communications with the UMS database

## Procedure

Perform the step for the database type that you use for UMS:

1 If you are using Db2®, create a secret to ensure that allcommunications between UMS and Db2 are encrypted:
    1. Import the database CA Certificate to UMS and create a secret to store the certificate:
oc create secret generic ibm-baw-ums-db2-cacert --from-file=cacert.crt=path\_to\_certificate\_PEM\_fileWhere
path\_to\_certificate\_PEM\_file is the path to the PEM format certificate file. Do
not change the part --from-file=cacert.crt=.
    2. Make a note of the datasource SSL information that you will need later to add to the
datasource\_configuration section of the custom resource file:

datasource\_configuration:
  dc\_ums\_datasource: 
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-db2-cacert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-db2-cacert
    dc\_ums\_teamserver\_ssl: true
2 If you are using Oracle, ensure that all communications between UMS and Oracle areencrypted:

1. Import the database CA Certificate to UMS and create a secret to store the certificate by
running the following command:
oc create secret generic ibm-baw-ums-oracle-cacert --from-file=cacert.crt=path-to-oracle-certificate-fileWhere
path-to-oracle-certificate-file is the path to the local copy of the Oracle
certificate file, which must be in PEM format. Do not change the part
--from-file=cacert.crt=
2. Make a note of the name of the secret, for example ibm-baw-ums-oracle-cacert
that you will need later to add to the dc\_ums\_datasource section of the custom
resource file:

datasource\_configuration:
  dc\_ums\_datasource: 
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-oracle-cacert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-oracle-cacert
    dc\_ums\_teamserver\_ssl: true
3 If you are using MS SQL, ensure that all communications between UMS and MS SQL areencrypted:

1. Obtain the base-64 encoded X.509 signer certificate of your MS SQL server.
2. Create a configuration file for the secret, for example, named mssql.yaml
and add the signer certificate of the MS SQL server as the value of the property
tls.crt for the secret named ibm-baw-ums-mssql-cert, based on the
following example:

apiVersion: v1
kind: Secret
metadata:
  name: ibm-baw-ums-mssql-cert
type: Opaque
stringData:
  tls.crt: |+
    -----BEGIN CERTIFICATE-----
    <Include the MS SQL certificate here>
    -----END CERTIFICATE-----
3. Create a secret that contains the MS SQL certificate by using the following command:

oc create -f mssql.yaml
4. Add the name of the MS SQL certificate to the list of trusted certificates in the custom
resource:
shared\_configuration:
  trusted\_certificate\_list:
    - ibm-baw-ums-mssql-certDuring
the UMS deployment, the operator adds the MS SQL signer certificate to the truststore of UMS.
5. In the datasource configuration enable SSL and specify the hostname that is used in
certificate.
4 If you are using PostgreSQL, ensure that all communications between UMS and PostgreSQL areencrypted:

1. Import the database CA Certificate to UMS and create a secret to store the certificate by
running the following command:
oc create secret generic ibm-baw-ums-postgresql-cacert --from-file=cacert.crt=path-to-postgresql-certificate-fileWhere
path-to-postgresql-certificate-file is the path to the local
copy of the PostgreSQL certificate file, which must be in PEM format. Do not change the part
--from-file=cacert.crt=.
2. Make a note of the name of the secret, for example
ibm-baw-ums-postgresql-cacert that you will need later to add to the
dc\_ums\_datasource section of the custom resource file:

datasource\_configuration:
  dc\_ums\_datasource:
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-postgresql-cacert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-postgresql-cacert
    dc\_ums\_teamserver\_ssl: true