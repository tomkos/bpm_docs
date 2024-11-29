# Installing Process Federation Server on
containers

Process Federation Server helps you
create a federated process environment. It provides business users with a single point of access to
their task list and launch list. This accessibility is available regardless of the type of process
that they are working on and the backend system where the process artifacts are stored. Process Federation Server containers
include indexers, retrievers, REST services, and integrate with a federated data repository
(Elasticsearch or OpenSearch) cluster where it stores both federated data and saved
searches.

In 23.0.2, Elasticsearch was replaced with OpenSearch. For more information about Process Federation Server containers, see
Administering and operating IBM
Process Federation Server Containers.

You can install Process Federation Server on Red Hat
OpenShift® Container
Platform (OCP). The
OpenShift Container
Platform OperatorHub
provides a user interface for you to install a deployment with operator lifecycle manager (OLM).

- Preparing for a Process Federation Server deployment
- Deploying required components
- Deploying Process Federation Server
- Completing post-deployment tasks for Process Federation Server
- Verifying your Process Federation Server deployment
- Configuring your workflow for federation
- Enable common UI
- Troubleshooting your Process Federation Server deployment
- Uninstalling your Process Federation Server deployment

## Preparing for a Process Federation Server
deployment

1. Make sure that you have the resources for your deployment. See Planning for a CP4BA Process Federation Server production deployment.
2. Plan and prepare your deployment on your cluster by completing the steps in Option 1: Preparing your cluster for an online deployment.

Prepare storage, including the persistent volumes (PVs) and persistent volume claim (PVCs) for
the Process Federation Server,
see Prepare for Process Federation Server.

## Deploying required components

To install Process Federation Server, you must use
the Cloud Pak for Business Automation operator to
configure the root certificate authority (CA) and User Management Services.

If you already installed a Business Automation Workflow with the required
components, you can proceed directly to Step 3. For
instructions on how to install Business Automation Workflow, see Creating a production deployment.

1 If a Business Automation Workflow deployment pattern is not yet installed, configure the ICP4ACluster custom resource(CR) to deploy the components required by Process Federation Server .
    1 Create the following cp4ba.yaml file, and replace the values of<Required> . If you want to use a federated data repository cluster, which isprovided separately, rather than an embedded OpenSearch instance, you do not need the sectionelasticsearch\_configuration . For more information about configuring parameters, seethe following topics. apiVersion: icp4a.ibm.com/v1kind: ICP4AClustermetadata: name: icp4deploy labels: app.kubernetes.io/instance: ibm-dba app.kubernetes.io/managed-by: ibm-dba app.kubernetes.io/name: ibm-dba release: 23.2.0spec: appVersion: 23.2.0 ibm\_license: accept shared\_configuration: sc\_deployment\_context: BAW sc\_deploy\_zen\_with\_iaf: false sc\_deployment\_license: production sc\_deployment\_platform: OCP sc\_deployment\_type: custom sc\_image\_tag: <required> sc\_image\_repository: <required> image\_pull\_secrets: <required> root\_ca\_secret: icp4a-root-ca sc\_deployment\_hostname\_suffix: <required> storage\_configuration: sc\_block\_storage\_classname: "<Required>" sc\_fast\_file\_storage\_classname: "<Required>" sc\_medium\_file\_storage\_classname: "<Required>" sc\_slow\_file\_storage\_classname: "<Required>" ## The beginning section of LDAP configuration for CP4A ldap\_configuration: ## The possible values are: "IBM Security Directory Server" or "Microsoft Active Directory" or "Custom" lc\_selected\_ldap\_type: "<Required>" ## The name of the LDAP server to connect lc\_ldap\_server: "<Required>" ## The port of the LDAP server to connect. Some possible values are: 389, 636, etc. lc\_ldap\_port: "<Required>" ## The LDAP bind secret for LDAP authentication. The secret is expected to have ldapUsername and ldapPassword keys. Refer to Knowledge Center for more info. lc\_bind\_secret: ldap-bind-secret ## The LDAP base DN. For example, "dc=example,dc=com", "dc=abc,dc=com", etc lc\_ldap\_base\_dn: "<Required>" ## Enable SSL/TLS for LDAP communication. Refer to Knowledge Center for more info. lc\_ldap\_ssl\_enabled: true ## The name of the secret that contains the LDAP SSL/TLS certificate. lc\_ldap\_ssl\_secret\_name: "<Required>" ## The LDAP user name attribute. Semicolon-separated list that must include the first RDN user distinguished names. One possible value is "*:uid" for TDS and "user:sAMAccountName" for AD. Refer to Knowledge Center for more info. lc\_ldap\_user\_name\_attribute: "<Required>" ## The LDAP user display name attribute. One possible value is "cn" for TDS and "sAMAccountName" for AD. Refer to Knowledge Center for more info. lc\_ldap\_user\_display\_name\_attr: "<Required>" ## The LDAP group base DN. For example, "dc=example,dc=com", "dc=abc,dc=com", etc lc\_ldap\_group\_base\_dn: "<Required>" ## The LDAP group name attribute. One possible value is "*:cn" for TDS and "*:cn" for AD. Refer to Knowledge Center for more info. lc\_ldap\_group\_name\_attribute: "*:cn" ## The LDAP group display name attribute. One possible value for both TDS and AD is "cn". Refer to Knowledge Center for more info. lc\_ldap\_group\_display\_name\_attr: "cn" ## The LDAP group membership search filter string. One possible value is "(|(&(objectclass=groupofnames)(member={0}))(&(objectclass=groupofuniquenames)(uniquemember={0})))" for TDS ## and "(&(cn=%v)(objectcategory=group))" for AD. lc\_ldap\_group\_membership\_search\_filter: "<Required>" ## The LDAP group membership ID map. One possible value is "groupofnames:member" for TDS and "memberOf:member" for AD. lc\_ldap\_group\_member\_id\_map: "<Required>" ## Set to true if you want to enable LDAP nested search in IAM, by default it is false lc\_ldap\_recursive\_search: false ## Set to true if you want to enable LDAP pagination in IAM, by default it is false lc\_enable\_pagination: false ## If lc\_enable\_pagination is set to true, then specify the pagination size. If not specified, the following default values will be used: ## IBM Tivoli Directory Server: 20000; Microsoft Active Directory:1000, and Custom: 4500 lc\_pagination\_size: 1000 ## add custom group search bases to IAM lc\_group\_searchbase\_list: [] ## add custom user search bases to IAM lc\_user\_searchbase\_list: [] ## The lc\_ldap\_precheck parameter is used to enable or disable LDAP connection check. ## If set to "true", then LDAP connection check will be enabled. ## if set to "false", then LDAP connection check will not be enabled. # lc\_ldap\_precheck: true ## The User script will uncomment the section needed based on user's input from User script. If you are deploying without the User script, ## uncomment the necessary section (depending if you are using Active Directory (ad) or Tivoli Directory Service (tds)) accordingly. # ad: # lc\_ad\_gc\_host: "<Required>" # lc\_ad\_gc\_port: "<Required>" # lc\_user\_filter: "(&(sAMAccountName=%v)(objectcategory=user))" # lc\_group\_filter: "(&(cn=%v)(objectcategory=group))" # tds: # lc\_user\_filter: "(&(cn=%v)(objectclass=person))" # lc\_group\_filter: "(&(cn=%v)(|(objectclass=groupofnames)(objectclass=groupofuniquenames)(objectclass=groupofurls)))" # custom: # lc\_user\_filter: "(&(objectClass=person)(cn=%v))" # lc\_group\_filter: "(&(objectClass=group)(cn=%v))" ## This is to add customized IAM SCIM LDAP attributes for this LDAP configuration, If you only add 'scim\_configuration\_iam', we will create SCIM LDAP attributes mapping using default values and the default value meant for IBM Security Directory Server only. Comment the whole section if you don't want this to be configured. # scim\_configuration\_iam: # user\_unique\_id\_attribute : dn # user\_external\_id\_attribute: dn # user\_emails\_attribute: mail # user\_name\_attribute: uid # user\_display\_name\_attribute: cn # user\_groups\_attribute: memberOf # user\_object\_class\_attribute: person # user\_principal\_name\_attribute: uid # user\_given\_name\_attribute: cn # user\_family\_name\_attribute: sn # user\_full\_name\_attribute: cn # ## Optional: Uncomment 'user\_custom\_mapping' and add any custom mapping below # # user\_custom\_mapping: # # <scim\_attr\_name> : <ldap attr name> # # like below # # ibmentryuuid : ibm-entryuuid # group\_unique\_id\_attribute: dn # group\_external\_id\_attribute: dn # group\_display\_name\_attribute : cn # group\_members\_attribute: member # group\_object\_class\_attribute: groupOfNames # group\_name\_attribute: cn # group\_principal\_name\_attribute: cn # ## Optional: Uncomment 'group\_custom\_mapping' and add any custom mapping below # # group\_custom\_mapping: # # <scim\_attr\_name> : <ldap attr name> # # like below # # ibmentryuuid : ibm-entryuuid ## This section allows to enhance the ldap configuration for the UMS SCIM capability. If lc\_user\_filter or lc\_group\_filter cannot handle a custom LDAP filter for user or group searches this section should be enabled. ## optional: enables the liberty ldapEntityType configuration and disables the usage of lc\_user\_filter, lc\_group\_filter, lc\_ldap\_group\_member\_id\_map, lc\_ldap\_user\_name\_attribute and lc\_ldap\_group\_name\_attribute in the UMS capabilities. ## for detailed information about the ldapEntityType, loginProperty and groupProperties parameters please see the liberty documentation: https://www.ibm.com/docs/en/was-liberty/nd?topic=configuration-ldapregistry ## default is false lc\_use\_ldap\_entity\_type: ## optional: only used if lc\_use\_ldap\_entity\_type is true ## default is uid lc\_ldap\_login\_property: ## optional: only used if lc\_use\_ldap\_entity\_type is true ## the defaults depends on the lc\_selected\_ldap\_type lc\_ldap\_entity\_type\_user: object\_class: search\_base: search\_filter: ## optional: only used if lc\_use\_ldap\_entity\_type is true ## the defaults depends on the lc\_selected\_ldap\_type lc\_ldap\_entity\_type\_group: object\_class: search\_base: search\_filter: ## optional: only used if lc\_use\_ldap\_entity\_type is true ## the defaults depends on the lc\_selected\_ldap\_type lc\_ldap\_group\_properties: # member\_attribute: # The name of the member. Required if member\_attribute is set # name: # The name of the object class. Required member\_attribute is set # object\_class: ## the scope options are: all, direct, nested # scope: #membership\_attribute: # The name of the membership. Required if membership\_attribute is set # name: ## the scope options are: all, direct, nested # scope: datasource\_configuration: ## The database configuration for UMS (User Management Service) dc\_ums\_datasource: ## Provide the datasource configuration for oauth ## Possible dc\_ums\_oauth\_type values are "derby" for test only and "db2", "oracle", "sqlserver" and "postgresql" for production. ## This configuration should be the same as the other datasource configuration in the dc\_ums\_datasource section. ## db2 with HADR is automatically activated if dc\_ums\_oauth\_alternate\_hosts and dc\_ums\_oauth\_alternate\_ports are set. ## For Oracle RAC, specify the host name of the SCAN listener as the value of the dc\_ums\_oauth\_host parameter dc\_ums\_oauth\_type: "<Required>" ## Provide the database server name or IP address of the database server. dc\_ums\_oauth\_host: "<Required>" ## Provide the database server port. For Db2, the default is "50000". For Oracle, the default is "1521". For MSSQL, the default is "1433"- For PostgreSQL, the default is "5432". dc\_ums\_oauth\_port: "<Required>" ## Provide the name of the database for UMS. For example: "UMSDB". ## Required for all databases, except when database type "oracle" is used with service name. ## For "oracle", specify the SID here. If service name should be used instead of SID, leave it empty. dc\_ums\_oauth\_name: "<Required>" ## For "oracle", you can specify the service name here if you want to connect by service name instead of SID dc\_ums\_oauth\_oracle\_service\_name: dc\_ums\_oauth\_schema: OAuthDBSchema dc\_ums\_oauth\_ssl: true dc\_ums\_oauth\_ssl\_secret\_name: "<Required>" ## For "oracle", "sqlserver" and "postgresql" provide the names of the driver files dc\_ums\_oauth\_driverfiles: ######################################################################## ## For db2 with HADR, complete the rest of the parameters below. ## db2 with HADR is automatically activated if dc\_ums\_oauth\_alternate\_hosts and dc\_ums\_oauth\_alternate\_ports are set. ######################################################################## dc\_ums\_oauth\_alternate\_hosts: dc\_ums\_oauth\_alternate\_ports: dc\_ums\_oauth\_retry\_interval\_for\_client\_reroute: 2 dc\_ums\_oauth\_max\_retries\_for\_client\_reroute: 5 ## Provide the datasource configuration for the teamserver ## Possible dc\_ums\_teamserver\_type values are "derby" for test only and "db2", "oracle", "sqlserver" and "postgresql" for production. ## This configuration should be the same as the other datasource configuration in the dc\_ums\_datasource section. ## db2 with HADR is automatically activated if dc\_ums\_teamserver\_alternate\_hosts and dc\_ums\_teamserver\_alternate\_ports are set. ## For Oracle RAC, specify the host name of the SCAN listener as the value of the dc\_ums\_teamserver\_host parameter dc\_ums\_teamserver\_type: "<Required>" dc\_ums\_teamserver\_host: "<Required>" ## Provide the database server port. For Db2, the default is "50000". For Oracle, the default is "1521". For MS SQL, the default is "1433"- For PostgreSQL, the default is "5432". dc\_ums\_teamserver\_port: "<Required>" ## Provide the name of the database for UMS teamserver. For example: "UMSDB". ## Required for all databases, except when database type "oracle" is used with service name. ## For "oracle", specify the SID here. If service name should be used instead of SID, leave it empty. dc\_ums\_teamserver\_name: "<Required>" ## For "oracle", you can specify the service name here if you want to connect by service name instead of SID dc\_ums\_teamserver\_oracle\_service\_name: dc\_ums\_teamserver\_ssl: true dc\_ums\_teamserver\_ssl\_secret\_name: "<Required>" ## For "oracle", "sqlserver" and "postgresql" provide the names of the driver files dc\_ums\_teamserver\_driverfiles: ######################################################################## ## For db2 with HADR, complete the rest of the parameters below. ## db2 with HADR is automatically activated if dc\_ums\_teamserver\_alternate\_hosts and dc\_ums\_teamserver\_alternate\_ports are set. ######################################################################## dc\_ums\_teamserver\_alternate\_hosts: dc\_ums\_teamserver\_alternate\_ports: dc\_ums\_teamserver\_retry\_interval\_for\_client\_reroute: 2 dc\_ums\_teamserver\_max\_retries\_for\_client\_reroute: 5 ums\_configuration: admin\_secret\_name: ibm-dba-ums-secret
        - For general Cloud Pak for Business Automation
parameters, see Shared configuration.
        - For LDAP parameters, see LDAP configuration.
        - For User Management Service parameter,see User Management Services (UMS)configuration parameters .
            - To create a database for User Management Service, see Preparing the UMS database.
            - To create the secret for User Management Services, see Creating the UMS database admin secret.

```
apiVersion: icp4a.ibm.com/v1
kind: ICP4ACluster
metadata:
  name: icp4deploy
  labels:
    app.kubernetes.io/instance: ibm-dba
    app.kubernetes.io/managed-by: ibm-dba
    app.kubernetes.io/name: ibm-dba
    release: 23.2.0
spec:
  appVersion: 23.2.0
  ibm\_license: accept
  shared\_configuration:
    sc\_deployment\_context: BAW
    sc\_deploy\_zen\_with\_iaf: false
    sc\_deployment\_license: production
    sc\_deployment\_platform: OCP
    sc\_deployment\_type: custom
    sc\_image\_tag: <required>
    sc\_image\_repository: <required>
    image\_pull\_secrets: <required>
    root\_ca\_secret: icp4a-root-ca
    sc\_deployment\_hostname\_suffix: <required>
    storage\_configuration:
      sc\_block\_storage\_classname: "<Required>"
      sc\_fast\_file\_storage\_classname: "<Required>"
      sc\_medium\_file\_storage\_classname: "<Required>"
      sc\_slow\_file\_storage\_classname: "<Required>"

    ## The beginning section of LDAP configuration for CP4A
  ldap\_configuration:
    ## The possible values are: "IBM Security Directory Server" or "Microsoft Active Directory" or "Custom"
    lc\_selected\_ldap\_type: "<Required>"

    ## The name of the LDAP server to connect
    lc\_ldap\_server: "<Required>"

    ## The port of the LDAP server to connect.  Some possible values are: 389, 636, etc.
    lc\_ldap\_port: "<Required>"

    ## The LDAP bind secret for LDAP authentication.  The secret is expected to have ldapUsername and ldapPassword keys.  Refer to Knowledge Center for more info.
    lc\_bind\_secret: ldap-bind-secret

    ## The LDAP base DN.  For example, "dc=example,dc=com", "dc=abc,dc=com", etc
    lc\_ldap\_base\_dn: "<Required>"

    ## Enable SSL/TLS for LDAP communication. Refer to Knowledge Center for more info.
    lc\_ldap\_ssl\_enabled: true

    ## The name of the secret that contains the LDAP SSL/TLS certificate.
    lc\_ldap\_ssl\_secret\_name: "<Required>"

    ## The LDAP user name attribute. Semicolon-separated list that must include the first RDN user distinguished names. One possible value is "*:uid" for TDS and "user:sAMAccountName" for AD. Refer to Knowledge Center for more info.
    lc\_ldap\_user\_name\_attribute: "<Required>"

    ## The LDAP user display name attribute. One possible value is "cn" for TDS and "sAMAccountName" for AD. Refer to Knowledge Center for more info.
    lc\_ldap\_user\_display\_name\_attr: "<Required>"

    ## The LDAP group base DN.  For example, "dc=example,dc=com", "dc=abc,dc=com", etc
    lc\_ldap\_group\_base\_dn: "<Required>"

    ## The LDAP group name attribute.  One possible value is "*:cn" for TDS and "*:cn" for AD. Refer to Knowledge Center for more info.
    lc\_ldap\_group\_name\_attribute: "*:cn"

    ## The LDAP group display name attribute.  One possible value for both TDS and AD is "cn". Refer to Knowledge Center for more info.
    lc\_ldap\_group\_display\_name\_attr: "cn"

    ## The LDAP group membership search filter string.  One possible value is "(|(&(objectclass=groupofnames)(member={0}))(&(objectclass=groupofuniquenames)(uniquemember={0})))" for TDS
    ## and "(&(cn=%v)(objectcategory=group))" for AD.
    lc\_ldap\_group\_membership\_search\_filter: "<Required>"

    ## The LDAP group membership ID map.  One possible value is "groupofnames:member" for TDS and "memberOf:member" for AD.
    lc\_ldap\_group\_member\_id\_map: "<Required>"

    ## Set to true if you want to enable LDAP nested search in IAM, by default it is false
    lc\_ldap\_recursive\_search: false

    ## Set to true if you want to enable LDAP pagination in IAM, by default it is false
    lc\_enable\_pagination: false

    ## If lc\_enable\_pagination is set to true, then specify the pagination size.  If not specified, the following default values will be used:
    ##  IBM Tivoli Directory Server: 20000; Microsoft Active Directory:1000, and Custom: 4500
    lc\_pagination\_size: 1000 

    ## add custom group search bases to IAM
    lc\_group\_searchbase\_list: []

    ## add custom user search bases to IAM
    lc\_user\_searchbase\_list: []
    
    ## The lc\_ldap\_precheck parameter is used to enable or disable LDAP connection check.
    ## If set to "true", then LDAP connection check will be enabled.
    ## if set to "false", then LDAP connection check will not be enabled.
    # lc\_ldap\_precheck: true

    ## The User script will uncomment the section needed based on user's input from User script.  If you are deploying without the User script,
    ## uncomment the necessary section (depending if you are using Active Directory (ad) or Tivoli Directory Service (tds)) accordingly.
    # ad:
    #   lc\_ad\_gc\_host: "<Required>"
    #   lc\_ad\_gc\_port: "<Required>"
    #   lc\_user\_filter: "(&(sAMAccountName=%v)(objectcategory=user))"
    #   lc\_group\_filter: "(&(cn=%v)(objectcategory=group))"
    # tds:
    #   lc\_user\_filter: "(&(cn=%v)(objectclass=person))"
    #   lc\_group\_filter: "(&(cn=%v)(|(objectclass=groupofnames)(objectclass=groupofuniquenames)(objectclass=groupofurls)))"
    # custom:
    #   lc\_user\_filter: "(&(objectClass=person)(cn=%v))"
    #   lc\_group\_filter:  "(&(objectClass=group)(cn=%v))"

    ## This is to add customized IAM SCIM LDAP attributes for this LDAP configuration, If you only add 'scim\_configuration\_iam', we will create SCIM LDAP attributes mapping using default values and the default value meant for IBM Security Directory Server only. Comment the whole section if you don't want this to be configured.
    # scim\_configuration\_iam:
    #   user\_unique\_id\_attribute : dn
    #   user\_external\_id\_attribute: dn
    #   user\_emails\_attribute: mail
    #   user\_name\_attribute: uid
    #   user\_display\_name\_attribute: cn
    #   user\_groups\_attribute: memberOf
    #   user\_object\_class\_attribute: person
    #   user\_principal\_name\_attribute: uid
    #   user\_given\_name\_attribute: cn
    #   user\_family\_name\_attribute: sn
    #   user\_full\_name\_attribute: cn
    #   ## Optional:  Uncomment 'user\_custom\_mapping' and add any custom mapping below
    #   # user\_custom\_mapping:
    #     # <scim\_attr\_name> : <ldap attr name>
    #     # like below
    #     # ibmentryuuid : ibm-entryuuid
    #   group\_unique\_id\_attribute: dn
    #   group\_external\_id\_attribute: dn
    #   group\_display\_name\_attribute : cn
    #   group\_members\_attribute: member
    #   group\_object\_class\_attribute: groupOfNames
    #   group\_name\_attribute: cn
    #   group\_principal\_name\_attribute: cn
    #   ## Optional:  Uncomment 'group\_custom\_mapping' and add any custom mapping below
    #   # group\_custom\_mapping:
    #     # <scim\_attr\_name> : <ldap attr name>
    #     # like below
    #     # ibmentryuuid : ibm-entryuuid

    ## This section allows to enhance the ldap configuration for the UMS SCIM capability. If lc\_user\_filter or lc\_group\_filter cannot handle a custom LDAP filter for user or group searches this section should be enabled.
    ## optional: enables the liberty ldapEntityType configuration and disables the usage of lc\_user\_filter, lc\_group\_filter, lc\_ldap\_group\_member\_id\_map, lc\_ldap\_user\_name\_attribute and lc\_ldap\_group\_name\_attribute in the UMS capabilities.
    ## for detailed information about the ldapEntityType, loginProperty and groupProperties  parameters please see the liberty documentation: https://www.ibm.com/docs/en/was-liberty/nd?topic=configuration-ldapregistry
    ## default is false
    lc\_use\_ldap\_entity\_type:
    ## optional: only used if lc\_use\_ldap\_entity\_type is true
    ## default is uid
    lc\_ldap\_login\_property:
    ## optional: only used if lc\_use\_ldap\_entity\_type is true
    ## the defaults depends on the lc\_selected\_ldap\_type
    lc\_ldap\_entity\_type\_user:
      object\_class:
      search\_base:
      search\_filter:
    ## optional: only used if lc\_use\_ldap\_entity\_type is true
    ## the defaults depends on the lc\_selected\_ldap\_type
    lc\_ldap\_entity\_type\_group:
      object\_class:
      search\_base:
      search\_filter:
    ## optional: only used if lc\_use\_ldap\_entity\_type is true
    ## the defaults depends on the lc\_selected\_ldap\_type
    lc\_ldap\_group\_properties:
      # member\_attribute:
        # The name of the member. Required if member\_attribute is set
        # name:
        # The name of the object class. Required member\_attribute is set
        # object\_class:
        ## the scope options are: all, direct, nested
        # scope:
      #membership\_attribute:
        # The name of the membership. Required if membership\_attribute is set
        # name:
        ## the scope options are: all, direct, nested
        # scope:
  datasource\_configuration:
    ## The database configuration for UMS (User Management Service)
    dc\_ums\_datasource:
      ## Provide the datasource configuration for oauth
      ## Possible dc\_ums\_oauth\_type values are "derby" for test only and "db2", "oracle", "sqlserver" and "postgresql" for production.
      ## This configuration should be the same as the other datasource configuration in the dc\_ums\_datasource section.
      ## db2 with HADR is automatically activated if dc\_ums\_oauth\_alternate\_hosts and dc\_ums\_oauth\_alternate\_ports are set.
      ## For Oracle RAC, specify the host name of the SCAN listener as the value of the dc\_ums\_oauth\_host parameter
      dc\_ums\_oauth\_type: "<Required>"
      ## Provide the database server name or IP address of the database server.
      dc\_ums\_oauth\_host: "<Required>"
      ## Provide the database server port.  For Db2, the default is "50000".  For Oracle, the default is "1521". For MSSQL, the default is "1433"- For PostgreSQL, the default is "5432".
      dc\_ums\_oauth\_port: "<Required>"
      ## Provide the name of the database for UMS.  For example: "UMSDB".
      ## Required for all databases, except when database type "oracle" is used with service name.
      ## For "oracle", specify the SID here. If service name should be used instead of SID, leave it empty.
      dc\_ums\_oauth\_name: "<Required>"
      ## For "oracle", you can specify the service name here if you want to connect by service name instead of SID
      dc\_ums\_oauth\_oracle\_service\_name:
      dc\_ums\_oauth\_schema: OAuthDBSchema
      dc\_ums\_oauth\_ssl: true
      dc\_ums\_oauth\_ssl\_secret\_name: "<Required>"
      ## For "oracle", "sqlserver" and "postgresql" provide the names of the driver files
      dc\_ums\_oauth\_driverfiles:
      ########################################################################
      ## For db2 with HADR, complete the rest of the parameters below.
      ## db2 with HADR is automatically activated if dc\_ums\_oauth\_alternate\_hosts and dc\_ums\_oauth\_alternate\_ports are set.
      ########################################################################
      dc\_ums\_oauth\_alternate\_hosts:
      dc\_ums\_oauth\_alternate\_ports:
      dc\_ums\_oauth\_retry\_interval\_for\_client\_reroute: 2
      dc\_ums\_oauth\_max\_retries\_for\_client\_reroute: 5

      ## Provide the datasource configuration for the teamserver
      ## Possible dc\_ums\_teamserver\_type values are "derby" for test only and "db2", "oracle", "sqlserver" and "postgresql" for production.
      ## This configuration should be the same as the other datasource configuration in the dc\_ums\_datasource section.
      ## db2 with HADR is automatically activated if dc\_ums\_teamserver\_alternate\_hosts and dc\_ums\_teamserver\_alternate\_ports are set.
      ## For Oracle RAC, specify the host name of the SCAN listener as the value of the dc\_ums\_teamserver\_host parameter
      dc\_ums\_teamserver\_type: "<Required>"
      dc\_ums\_teamserver\_host: "<Required>"
      ## Provide the database server port.  For Db2, the default is "50000".  For Oracle, the default is "1521". For MS SQL, the default is "1433"- For PostgreSQL, the default is "5432".
      dc\_ums\_teamserver\_port: "<Required>"
      ## Provide the name of the database for UMS teamserver.  For example: "UMSDB".
      ## Required for all databases, except when database type "oracle" is used with service name.
      ## For "oracle", specify the SID here. If service name should be used instead of SID, leave it empty.
      dc\_ums\_teamserver\_name: "<Required>"
      ## For "oracle", you can specify the service name here if you want to connect by service name instead of SID
      dc\_ums\_teamserver\_oracle\_service\_name:
      dc\_ums\_teamserver\_ssl: true
      dc\_ums\_teamserver\_ssl\_secret\_name: "<Required>"
      ## For "oracle", "sqlserver" and "postgresql" provide the names of the driver files
      dc\_ums\_teamserver\_driverfiles:
      ########################################################################
      ## For db2 with HADR, complete the rest of the parameters below.
      ## db2 with HADR is automatically activated if dc\_ums\_teamserver\_alternate\_hosts and dc\_ums\_teamserver\_alternate\_ports are set.
      ########################################################################
      dc\_ums\_teamserver\_alternate\_hosts:
      dc\_ums\_teamserver\_alternate\_ports:
      dc\_ums\_teamserver\_retry\_interval\_for\_client\_reroute: 2
      dc\_ums\_teamserver\_max\_retries\_for\_client\_reroute: 5
  ums\_configuration:
    admin\_secret\_name: ibm-dba-ums-secret
```

2. Deploy the CR by running the following
command.oc apply -f cp4ba.yaml
2. Wait a few minutes for your resources to initiate. Run the command oc get icp4acluster
-o yaml to make sure that User Management Services and root certificate
authority are ready. Make sure that .status.components.prereq.rootCAStatus is
Ready and .status.components.prereq.rootCASecretName is filled
with the correct secret name. For any issues with the resources, check the pod logs by following
the instructions in Troubleshooting your Process Federation Server deployment.
3. Make sure that .status.endpoints[“UMS*“] appears in the endpoints
list. For example: status:
    components:
      ...
      prereq:
        conditions: []
        encryptionKeySecret: ibm-iaws-shared-key-secret
        iafStatus: Ready
        iamIntegrationStatus: Ready
        rootCASecretName: icp4a-root-ca
        rootCAStatus: Ready
      ums:
        adminSecret: ibm-dba-ums-admin-secret-internal
        service: Installed
    endpoints:
    - name: UMS
      scope: External
      uri: 'https://ums-hostname'
    - name: UMS SSO
      scope: External
      uri: 'https://ums-sso-hostname'
    - name: UMS SSO
      scope: Internal
      uri: 'https://icp4adeploy-ums-sso-service:9443'
    - name: UMS Teams
      scope: External
      uri: 'https://ums-teams-hostname'
    - name: UMS SCIM
      scope: External
      uri: 'https://ums-scim-hostname'
    - name: UMS Profile
      scope: External
      uri: 'https://ums-profiles-hostname'
4 Make sure that the expected pods are listed in the kubectl get pods commandresult.Operator pods with names similar to the following: For example, the results of oc get pods might look similar to thefollowing:[root@xxxxxx]# oc get podsNAME READY STATUS RESTARTS AGENAME READY STATUS RESTARTS AGEibm-ads-operator-676d4df84-sct5j 0/1 Running 0 17hibm-common-service-operator-77ddf8574c-5h5pj 1/1 Running 0 17hibm-content-operator-67558cf5b7-m6n9w 1/1 Running 0 17hibm-cp4a-operator-bawstd-5787f7f577-r8wh2 1/1 Running 0 17hibm-cp4a-wfps-operator-7b47b9fdc5-lsfj7 1/1 Running 0 17hibm-dpe-operator-7d7d4cb8c8-jxbpr 1/1 Running 0 17hibm-insights-engine-operator-585bd964f8-z8756 1/1 Running 0 17hibm-odm-operator-6cb5d4c786-8cpmc 1/1 Running 0 17hicp4a-foundation-operator-68979f47c5-s8ml9 1/1 Running 0 17hoperand-deployment-lifecycle-manager-5df67fd7dd-hcbjf 1/1 Running 0 17hicp4adeploy-ums-scim-deployment-5bbdb4cf47-2wvtj 1/1 Running 0 17hicp4adeploy-ums-scim-deployment-5bbdb4cf47-8vwg8 1/1 Running 0 17hicp4adeploy-ums-sso-deployment-6bdcd78689-qfqxk 1/1 Running 0 17hicp4adeploy-ums-sso-deployment-6bdcd78689-sm5x2 1/1 Running 0 17hicp4adeploy-ums-teams-deployment-58d648876f-8pbxw 1/1 Running 0 17hicp4adeploy-ums-teams-deployment-58d648876f-k75sx 1/1 Running 0 17h

- ibm-ads-operator-676d4df84-sct5j
- ibm-common-service-operator-77ddf8574c-5h5pj
- ibm-content-operator-67558cf5b7-m6n9w
- ibm-cp4a-operator-bawstd-5787f7f577-r8wh2
- ibm-cp4a-wfps-operator-7b47b9fdc5-lsfj7
- ibm-dpe-operator-7d7d4cb8c8-jxbpr
- ibm-insights-engine-operator-585bd964f8-z8756
- ibm-odm-operator-6cb5d4c786-8cpmc
- icp4a-foundation-operator-68979f47c5-s8ml9
- operand-deployment-lifecycle-manager-5df67fd7dd-hcbjf

```
[root@xxxxxx]# oc get pods
NAME                                                             READY   STATUS      RESTARTS        AGE
NAME                                                    READY   STATUS             RESTARTS         AGE
ibm-ads-operator-676d4df84-sct5j                        0/1     Running            0                17h
ibm-common-service-operator-77ddf8574c-5h5pj            1/1     Running            0                17h
ibm-content-operator-67558cf5b7-m6n9w                   1/1     Running            0                17h
ibm-cp4a-operator-bawstd-5787f7f577-r8wh2               1/1     Running            0                17h
ibm-cp4a-wfps-operator-7b47b9fdc5-lsfj7                 1/1     Running            0                17h
ibm-dpe-operator-7d7d4cb8c8-jxbpr                       1/1     Running            0                17h
ibm-insights-engine-operator-585bd964f8-z8756           1/1     Running            0                17h
ibm-odm-operator-6cb5d4c786-8cpmc                       1/1     Running            0                17h
icp4a-foundation-operator-68979f47c5-s8ml9              1/1     Running            0                17h
operand-deployment-lifecycle-manager-5df67fd7dd-hcbjf   1/1     Running            0                17h
icp4adeploy-ums-scim-deployment-5bbdb4cf47-2wvtj        1/1     Running            0                17h
icp4adeploy-ums-scim-deployment-5bbdb4cf47-8vwg8        1/1     Running            0                17h
icp4adeploy-ums-sso-deployment-6bdcd78689-qfqxk         1/1     Running            0                17h
icp4adeploy-ums-sso-deployment-6bdcd78689-sm5x2         1/1     Running            0                17h
icp4adeploy-ums-teams-deployment-58d648876f-8pbxw       1/1     Running            0                17h
icp4adeploy-ums-teams-deployment-58d648876f-k75sx       1/1     Running            0                17h
```

## Deploying Process Federation Server

1. Configure your ProcessFederationServer custom resource. Your starting custom
resource might look similar to:apiVersion: icp4a.ibm.com/v1
kind: ProcessFederationServer
metadata:
  name: pfsdeploy
spec:
  appVersion: 23.2.0 
  license:
    accept: true
  shared\_configuration: 
    sc\_deployment\_license: production
    sc\_delivery\_type: baw
    sc\_deployment\_context: BAW
    sc\_deployment\_hostname\_suffix: <Required>
    storage\_configuration:
      sc\_fast\_file\_storage\_classname: <Required>
      sc\_medium\_file\_storage\_classname: <Required>
      sc\_slow\_file\_storage\_classname: <Required>
  pfs\_configuration:
    replicas: 1
  elasticsearch\_configuration:
    privileged: false
    ## If elasticsearch\_configuration.privileged is set to true, you must create a service account that has the privileged SecurityContextConstraint to allow running privileged containers. See "Preparing SecurityContextConstraints (SCC) requirements" for instructions.
    ## If elasticsearch\_configuration.service\_account not set, default service account "{{ meta.name }}-elasticsearch-service-account" will be used.
    ## If elasticsearch\_configuration.privileged is set to false, see "Preparing SecurityContextConstraints (SCC) requirements" for instructions.
    service\_account: "<Required>"In a production deployment cluster, for the
pfs\_configuration.replicas parameter, it is recommended that you set a value of
2 or higher.
For more information, see the Process Federation Server configuration
section in IBM Business Automation Workflow Runtime and Workstream Services parameters.
2. Apply your custom resource by running the following
command.oc apply -f your\_custom\_resource\_name

## Completing post-deployment tasks for Process Federation Server

To add custom configuration for Process Federation Server, see Customizing Process Federation Server.

## Verifying your Process Federation Server
deployment

1. Get your Process Federation Server REST base URL
by running the command:
oc get pfs cr\_name -o=jsonpath='{.status.endpoints[1].uri}'
2. To access Process Federation Server REST, see The Process Federation Server REST APIs.

## Configuring your workflow for federation

- To federate traditional (on-premises) Business Automation Workflow servers, see Federating IBM Business Automation Workflow running on-premise.
- To federate Business Automation Workflow on container servers, see Federating IBM Business Automation Workflow in CP4BA.

A dedicated custom resource (CR) called the FederatedSystem CR is provided. Each server to be
federated into the Process Federation Server container
applies the dedicated FederatedSystem CR. The full parameter list for the CR is found in Federated system parameters.

## Enable common UI

Workplace is a user
interface application, which runs on the Application Engine Server. It also has a desktop
that is configured in Business Automation Navigator. You can also enable
Common UI, see Enabling Common UI.

## Troubleshooting your Process Federation Server
deployment

1. Get the Process Federation Server operator pod
name by running the following command.oc get pods|grep pfs-operator
2. Using the pod name, get the Process Federation Server operator log by
running the following
command.oc logs pfs\_operator\_pod\_name

## Uninstalling your Process Federation Server
deployment

1. Delete your Process Federation Server instance by
running the following
command.oc delete processfederationserver pfs\_cr\_name
2. Uninstall your Business Automation Workflow environment by
following the steps in Uninstalling capabilities.

- Federating IBM Business Automation Workflow in CP4BA -
After you configure the Process Federation Server, you can deploy
and federate Business Automation Workflow on containers servers when Process Federation Server is in the same
namespace.
- Federated system parameters - Each server to be federated into
the Process Federation Server
container applies the FederatedSystem CR. Provide the details that are relevant to your environment.
To enable the notification server, add the notifications section and set the Java Message Service
(JMS) access information. To enable database indexing, add the section for your database and set the
database connection information.