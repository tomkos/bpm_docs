# Configuring endpoint URLs for Process Portal

## Before you begin

## About this task

For more information about the 99Local.xml and
100Custom.xml files, see The 100Custom.xml file and configuration.

## Procedure

1. Open the 100Custom.xml files in a text
editor.
2. Copy the following code snippet to the 100Custom.xml file
and update the URLs for your environment: <server merge="mergeChildren">
  <portal merge="mergeChildren"> 
    <bpm-data-endpoint>https://pfs.mycompany.com:port/rest/bpm/federated</bpm-data-endpoint>
   <trusted-sources>https://bpm1.mycompany.com:port,https://bpm2.mycompany.com:port</trusted-sources>
  </portal>
</server>
3. Save your changes.
4. To avoid any Content Security Policy issue when Process Portal sends requests to
Process Federation Server and
federated systems URLs declared in <bpm-data-endpoint> and
<trusted-sources>, ensure that the
Security.ContentSecurityPolicyHeaderValue property is correctly configured and
allows calls to these URLs. For more information about the
Security.ContentSecurityPolicyHeaderValue property configuration, see  Security.ContentSecurityPolicyHeaderValue.