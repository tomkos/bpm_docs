# Validating the Process Federation Server and
federated environment configuration

## About this task

To troubleshoot configuration problems in your federated environment, run the validation
tool manually from a web browser.

- Process Federation Server can connect to all the
specified LDAP servers.Restriction: The validation tool does not check the
baseDN, bindDn, or bindPassword
settings.
- Process Federation Server can connect to all the
specified data sources.
- Process Federation Server Secure Sockets Layer
(SSL) key stores are valid.
- Process Federation Server can connect to all thespecified federated systems by using the internalRestUrlPrefix property that isdefined for the retrieval service. The following connection aspects are tested:
    - If an HTTPS connection is configured, the signer certificates are tested.
    - Authorization across Process Federation Server and
federated systems.
    - Single-sign on (SSO) between Process Federation Server and federated systems, including
propagation of LTPA cookies, for example, to validate that common domain names are configured.
- The federated data repository service and indexing are working correctly.
- Each federated system has a retriever defined.
- Each federated system has an indexer defined.
- The Process Federation Server REST service is
working correctly.

## Procedure

1. Change the security for the web access of the validation
tool. In the server.xml file, under the
authorization-roles element, add or change the users in the security role that
can run the tool. Attention: To validate connections to the federated systems, the user
must be a common user across Process Federation Server
and each of the federated
systems.
<authorization-roles id="com.ibm.bpm.federated.security.config.authorization">
   <security-role name="bpmadmin">
     <user name="uid=admin,o=defaultWIMFileBasedRealm"/>
   </security-role>
</authorization-roles>
2. Start the validation tool from a browser window.
Go to
https://host\_name:port\_number/pfs-validate/Where: 
host\_name
The Process Federation Server host name.
port\_number
The Process Federation Server port number. The
default port number is 9443.
3. Validate each of the components in the federated environment by clicking the corresponding
links in the tool.
In the result page, green items passed validation successfully while red items indicate
errors. For each red items, read the detailed error description, adjust the settings in the
server.xml file accordingly, and run the validation tool on the component
again.