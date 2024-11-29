# Configuring User Management Services

## About this task

## Procedure

1. Edit the ums\_configuration section of the custom resource file.
2. Specify the name of the UMS database admin secret that you created for the
ums\_configuration.admin\_secret\_name during, for example
ibm-baw-ums-secret.
3 Specify the UMS datasource settings for your database in thedatasource\_configuration section of the custom resource. For example: Important: If you do not have a separate teams database, UMSTSDB, specify identicalvalues for the dc\_ums\_teamserver\_ parameters as for thedc\_ums\_oauth\_ ones. Trouble: If you plan to use UMS integration with other capabilities, you might encounterregistration failure errors during deployment. This can happen if the UMS deployment is not ready bythe time the other containers come up. The situation resolves in the next operator loop, so theerrors can be ignored.
    - For Db2®:datasource\_configuration:
  dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
    # oauth database config
    dc\_ums\_oauth\_type: db2
    dc\_ums\_oauth\_host: host\_name
    dc\_ums\_oauth\_port: 50000
    dc\_ums\_oauth\_name: UMSDB
    dc\_ums\_oauth\_schema: OAuth\_DB\_Schema
    dc\_ums\_oauth\_driverfiles: db2jcc4.jar, db2jcc\_license\_cu.jar
    dc\_ums\_oauth\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com"
    dc\_ums\_oauth\_alternate\_ports: "50443, 51443"
    dc\_ums\_oauth\_ssl: true
    # teamserver database config
    dc\_ums\_teamserver\_type: db2
    dc\_ums\_teamserver\_host: host\_name
    dc\_ums\_teamserver\_port: 50000
    dc\_ums\_teamserver\_name: UMSTSDB
    dc\_ums\_teamserver\_driverfiles: db2jcc4.jar, db2jcc\_license\_cu.jar
    dc\_ums\_teamserver\_alternate\_hosts: "server1.db2.example.com, server2.db2.example.com"
    dc\_ums\_teamserver\_alternate\_ports: "50443, 51443"
    dc\_ums\_teamserver\_ssl: trueIf you created a
secret for the Db2 certificate to secure communications
between UMS and Db2, specify the name of the secret, and
enable SSL, for example: datasource\_configuration:
  dc\_ums\_datasource: 
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-db2-cacert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-db2-cacert
    dc\_ums\_teamserver\_ssl: true
    - For Oracle:   datasource\_configuration:
    dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
    # oauth database config
      dc\_ums\_oauth\_type: oracle
      dc\_ums\_oauth\_host: host\_name
      dc\_ums\_oauth\_port: 1521
      dc\_ums\_oauth\_name: SID
      dc\_ums\_oauth\_schema: DB\_user\_ID
      dc\_ums\_oauth\_oracle\_service\_name: DB\_service\_name
      dc\_ums\_oauth\_ssl: false
      dc\_ums\_oauth\_driverfiles: ojdbc8.jar, orai18n.jar
    # teamserver database config
      dc\_ums\_teamserver\_type: oracle
      dc\_ums\_teamserver\_host: host\_name
      dc\_ums\_teamserver\_port: 1521
      dc\_ums\_teamserver\_name: SID
      dc\_ums\_teamserver\_oracle\_service\_name: DB\_service\_name
      dc\_ums\_teamserver\_ssl: false
      dc\_ums\_teamserver\_driverfiles: ojdbc8.jar, orai18n.jarWhere
host\_name is the name of your database host,
SID is the SID of your database, for example UMSDB, DB\_user\_ID is your database user ID, for example
C##UMS.Important: For Oracle RAC, specify the host name of the SCAN
listener as the value of the dc\_ums\_oauth\_host and
dc\_ums\_teamserver\_host parameters.
If you created a secret for the Oracle
certificate to secure communications between UMS and Oracle, specify the name of the secret, and
enable SSL, for example:datasource\_configuration:
  dc\_ums\_datasource: 
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-oracle-cacert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-oracle-cacert
    dc\_ums\_teamserver\_ssl: true
    - For MS SQL: datasource\_configuration:
    dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
    # oauth database config
      dc\_ums\_oauth\_type: sqlserver
      dc\_ums\_oauth\_host: host\_name
      dc\_ums\_oauth\_port: 1433
      dc\_ums\_oauth\_name: UMSDB
      dc\_ums\_oauth\_driverfiles: mssql-jdbc-8.2.2.jre8.jar
      dc\_ums\_oauth\_ssl: true
    # teamserver database config
      dc\_ums\_teamserver\_type: sqlserver
      dc\_ums\_teamserver\_host: host\_name
      dc\_ums\_teamserver\_port: 1433
      dc\_ums\_teamserver\_name: UMSDB
      dc\_ums\_teamserver\_driverfiles: mssql-jdbc-8.2.2.jre8.jar
      dc\_ums\_teamserver\_ssl: true
Where
host\_name is the name of your database host,
1433 is the port number, UMSDB is the name of your
database.If you created a secret for the MS SQL certificate to secure communications between UMS
and MS SQL, specify the name of the secret, and enable SSL, for example,
ibm-baw-ums-mssql-cert:datasource\_configuration:
  dc\_ums\_datasource: 
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-mssql-cert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-mssql-cert
    dc\_ums\_teamserver\_ssl: true
    - For PostgreSQL:
  datasource\_configuration:
    dc\_ums\_datasource: # credentials are read from ums\_configuration.admin\_secret\_name
      # oauth database config
      dc\_ums\_oauth\_type: postgresql
      dc\_ums\_oauth\_host: host\_name
      dc\_ums\_oauth\_port: 5432
      dc\_ums\_oauth\_name: umsdb
      dc\_ums\_oauth\_driverfiles: postgresql-42.2.14.jar
      # teamserver database config
      dc\_ums\_teamserver\_type: postgresql
      dc\_ums\_teamserver\_host: host\_name
      dc\_ums\_teamserver\_port: 5432
      dc\_ums\_teamserver\_name: umsdb
      dc\_ums\_teamserver\_driverfiles: postgresql-42.2.14.jar
Where host\_name is the name of your database host and umsdb is
the name of your database.If you created a secret for the PostgreSQL certificate to secure
communications between UMS and PostgreSQL, specify the name of the secret, and enable SSL, for
example, ibm-baw-ums-postgresql-cacert:datasource\_configuration:
  dc\_ums\_datasource: 
    ...
    dc\_ums\_oauth\_ssl\_secret\_name: ibm-baw-ums-postgresql-cacert
    dc\_ums\_oauth\_ssl: true
    ...
    dc\_ums\_teamserver\_ssl\_secret\_name: ibm-baw-ums-postgresql-cacert
    dc\_ums\_teamserver\_ssl: true
Important: If you configured PostgreSQL for high availability following the Patroni
architecture with an HAproxy for load balancing, make sure that you specify the host name and port
number of the HAproxy as the values for dc\_ums\_oauth\_host and
dc\_ums\_teamserver\_host and dc\_ums\_oauth\_port and
dc\_ums\_teamserver\_port.
4 Specify the certificates and routing for secure communications with UMS. ums\_configuration: hostname: <ums-host> admin\_secret\_name: ibm-baw-ums-secret # optional: create routes for backwards compatibility backwards\_compatibility\_routes: false # optional for secure communication with UMS external\_tls\_secret\_name: ibm-baw-ums-external-tls-secret # optional for secure communication with UMS external\_tls\_ca\_secret\_name: ibm-baw-ums-external-tls-ca-secret # optional for secure communication with UMS external\_tls\_teams\_secret\_name: ibm-baw-ums-external-tls-teams-secret # optional for secure communication with UMS external\_tls\_scim\_secret\_name: ibm-baw-ums-external-tls-scim-secret # optional for secure communication with UMS external\_tls\_sso\_secret\_name: ibm-baw-ums-external-tls-sso-secret

1 If you are creating a test environment and you do not want to deal with certificates, you do notneed the following secrets, and should remove them from the custom resource: This causes the root\_ca\_secret to be used to generate an internal TLS secretfor all services and an external TLS secret for each of the routes ums-route ,ums-sso-route , ums-scim-route , andums-teams-route . If you do not specify a root signing CA in theshared\_configuration section of the custom resource,root\_ca\_secret is generated by the operator with a self-signed root CA.
    - external\_tls\_secret\_name
    - external\_tls\_ca\_secret\_name
    - external\_tls\_teams\_secret
    - external\_tls\_sso\_secret
    - external\_tls\_scim\_secret

If you do not specify a root signing CA in the
shared\_configuration section of the custom resource,
root\_ca\_secret is generated by the operator with a self-signed root CA.

2 If you are creating a production environment, you can perform one of the following options:

- Specify the secrets that contain a TLS certificate that represents the host names of the routes
that your clients connect to.
- Use the shared secret shared\_configuration.external\_tls\_certificate\_secret that
contains a single HTTPS wildcard certificate that can be used to secure all routes.
3. If you upgraded from a version earlier than 21.0.2 and you have existing secrets that contain
host names, they will not conform to the new host name convention, if you do not want to regenerate
the secrets, you can set backwards\_compatibility\_routes to true to
use the old host naming pattern.

```
ums\_configuration:
  hostname: <ums-host>
  admin\_secret\_name: ibm-baw-ums-secret
  # optional: create routes for backwards compatibility
  backwards\_compatibility\_routes: false
  # optional for secure communication with UMS
  external\_tls\_secret\_name: ibm-baw-ums-external-tls-secret
  # optional for secure communication with UMS 
  external\_tls\_ca\_secret\_name: ibm-baw-ums-external-tls-ca-secret
  # optional for secure communication with UMS 
  external\_tls\_teams\_secret\_name: ibm-baw-ums-external-tls-teams-secret
  # optional for secure communication with UMS 
  external\_tls\_scim\_secret\_name: ibm-baw-ums-external-tls-scim-secret
  # optional for secure communication with UMS 
  external\_tls\_sso\_secret\_name: ibm-baw-ums-external-tls-sso-secret
```

5 Decide whether you want each UMS service (UMS SSO, UMS Teams, UMS SCIM-based Users and Groups)to run in its own dedicated pod so that they can scale individually, which is the default. Orwhether you want all UMS services to run in a single pod. Perform one of the following:

1 For dedicated pods:
    1. In the section ums\_configuration set
  dedicated\_pods: true
    2. For the UMS SSO service, default values are specified for the replica\_count,
resource, autoscaling and logs parameters. If the
default values do not meet your requirements, you can change the values
.    # Configuration for sso pods
    sso:
      replica\_count: 2
      resources:
        limits:
          cpu: 500m
          memory: 512Mi
        requests:
          cpu: 200m
          memory: 256Mi
        autoscaling:
          enabled: true
          minReplicas: 2
          maxReplicas: 5
          targetAverageUtilization: 98
      custom\_xml:
      logs:
        traceSpecification: "*=info"
    3. For the UMS SCIM-based Users and Groups service, default values are specified for the
replica\_count, resource, autoscaling and
logs parameters. You can change the values if the default values do not meet your
requirements.    # configuration for scim pods
    scim:
      replica\_count: 2
      resources:
      limits:
        cpu: 500m
        memory: 512Mi
      requests:
        cpu: 200m
        memory: 256Mi
      autoscaling:
        enabled: true
        minReplicas: 2
        maxReplicas: 5
        targetAverageUtilization: 98
      custom\_xml:
      logs:
        traceSpecification: "*=info"
    4. For the UMS Teams service, default values are specified for the replica\_count,
resource, autoscaling and logs parameters. You
can change the values if the default values do not meet your
requirements.    # configuration for teamserver pods
    teamserver:
      replica\_count: 2
      resources:
      limits:
        cpu: 500m
        memory: 512Mi
      requests:
        cpu: 200m
        memory: 256Mi
      autoscaling:
        enabled: true
        minReplicas: 2
        maxReplicas: 5
        targetAverageUtilization: 98
      custom\_xml:
      logs:
        traceSpecification: "*=info"
2. To have all UMS services run in the same pod, set the value dedicated\_pods:
false.
Default values are specified for the replica\_count,
resource, autoscaling and logs parameters. You
can change the values if the default values do not meet your
requirements.    #### If dedicated\_pods is set to false, the UMS capabilities sso, scim, teamserver
    #### run in the same pods with this configuration.
    replica\_count: 2
    resources:
      limits:
        cpu: 500m
        memory: 512Mi
      requests:
        cpu: 200m
        memory: 256Mi
    autoscaling:
      enabled: true
      min\_replicas: 2
      max\_replicas: 5
      target\_average\_utilization: 98
    custom\_xml:
    logs:
      traceSpecification: "*=info"
6. If you want to change the database connection pool sizes, health parameters, or certificate
checking options, you can modify the settings that are described in UMS advanced parameters by using the
custom\_xml section.
7 From 23.0.1, JDBC drivers are provided for all databases.

1. For 21.0.3 and previous versions:If you are using an Oracle, MS SQL, or PostgreSQL database,
specify as shown in the
ums\_configuration:
use\_custom\_jdbc\_drivers: true
existing\_claim\_name: operator-shared-pvc Where operator-shared-pvc is
the persistent volume claim that you prepared for the operator.
2. For 23.0.1 and later versions:If you want to use custom JDBC drivers, instead of the provided
default JDBC drivers, specify as shown in the
ums\_configuration
use\_custom\_jdbc\_drivers: true
existing\_claim\_name: operator-shared-pvcWhere operator-shared-pvc is
the persistent volume claim that you prepared for the operator.
8. Customize any other UMS configuration settings as necessary to suit your requirements. For
example, in the sections oauth, resources,
autoscaling, or logs:

  oauth:
    # optional: full DN of an LDAP group that is authorized to manage OIDC clients, in addition to primary admin from admin secret
    client\_manager\_group:
    # optional: full DN of an LDAP group that is authorized to manage app\_tokens, in addition to primary admin from admin secret
    token\_manager\_group:
    # optional: lifetime of OAuth access\_tokens. default is 7200s
    access\_token\_lifetime:
    # optional: lifetime of app-tokens. default is 366d
    app\_token\_lifetime:
    # optional: lifetime of app-passwords. default is 366d
    app\_password\_lifetime:
    # optional: maximimum number of app-tokens or app-passwords per client. default is 100
    app\_token\_or\_password\_limit:
    # optional: encoding / encryption when sotring client secrets in OAuth database. Default is xor for compatibility. Recommended value is PBKDF2WithHmacSHA512
    client\_secret\_encoding:
    use\_custom\_binaries: false  
    service\_type: Route
    routes\_ingress\_annotations:
	
  resources:
    limits:
      cpu: 500m
      memory: 512Mi
    requests:
      cpu: 200m
      memory: 256Mi
  ## Horizontal Pod Autoscaler
  autoscaling:
    enabled: true
    min\_replicas: 2
    max\_replicas: 5
    target\_average\_utilization: 98
  use\_custom\_jdbc\_drivers: false
  use\_custom\_binaries: false
  custom\_secret\_name:
  custom\_xml:
  logs:
    console\_format: json
    console\_log\_level: INFO
    console\_source: message,trace,accessLog,ffdc,audit
    trace\_format: ENHANCED
    trace\_specification: "*=info"
9. Specify
the following:

shared\_configuration
  sc\_deploy\_zen\_with\_iaf: false
10. Specify an LDAP group that is authorized to administer UMS Teams by adapting the following
snippet, where UMSTeamsAdmins is the name of the UMS Teams administration
group:

ums\_configuration:
  teamserver:
    admingroup: 'cn=UMSTeamsAdmins,dc=example,dc=org'

Remember: After deployment, you can administer teams for your business needs by logging
on to  the UMS Teams Management UI at
https://ums\_host/teamserver/ui using a user ID that is in the
UMS Teams administration group.