# Delegating authentication to an OIDC Identity Provider

## Before you begin

- authorizationEndpointUrl
- tokenEndpointUrl
- issuerIdentifier
- jwkEndpointUrl
- signatureAlgorithm

## Procedure

To configure UMS to delegate authentication to an OIDC IdP, perform the following steps:

1. Register UMS as OIDC client of the OIDC IdP by following the instructions of your identity
provider to register UMS as an OIDC client.
2. Obtain the signer certificate of your OIDC IdP.
3 Create an OIDC IdP secret.
    1. Create a configuration file for the secret, for example, named
idp-secret.yaml, and add the signer certificate that you obtained in the
previous step as the value of the property tls.crt:
apiVersion: v1
kind: Secret
metadata:
  name: idp-tls
type: Opaque
stringData:
  tls.crt: |+
    -----BEGIN CERTIFICATE-----
    <include the IdP certificate>
    -----END CERTIFICATE-----Where
idp-tls is the name of the secret.
4. Create the secret.
In the namespace where UMS will be deployed, run the
command:oc apply -f idp-secret.yaml
5 To configure UMS to delegate authentication to the IdP, make the following edits to the CustomResource (CR):

1. Add the name of the IdP certificate secret to the
shared\_configuration.trusted\_certificate\_list section of the CR.
For example:    trusted\_certificate\_list:
      - idp-tls
During
deployment, the operator adds the IdP signer certificate to the truststore of UMS.
2 In the ums\_configuration section, specify the OpenID Client configuration inthe custom\_xml parameter, including the information about the IdP and specify theauthFilter value to redirect only URLs that point to/oidc/endpoint/ums/authorize . Forexample: custom\_xml: | <server> <openidConnectClient id="client\_id " clientId="client\_id " clientSecret="client\_secret " authorizationEndpointUrl="authorizationEndpointUrl " tokenEndpointUrl="tokenEndpointUrl " issuerIdentifier="issuerIdentifier " jwkEndpointUrl="jwkEndpointUrl " signatureAlgorithm="signatureAlgorithm "> <authFilter> <requestUrl matchType="contains" urlPattern="/oidc/endpoint/ums/authorize"></requestUrl> <requestHeader id="allowBasicAuth" matchType="notcontain" name="Authorization" value="Basic" /> </authFilter> </openidConnectClient> </server> Tip: For more information about the parameters in the OIDC client configuration see Configuring an OpenID Connect Client inLiberty . During deployment, the operator adds the OIDC client configuration to theserver configuration of UMS.
    - If you use dedicated pods for UMS capabilities, add the following configuration information to
the custom\_xml parameter in the configuration of the sso pod in
the ums\_configuration section.
    - If you deploy all UMS capabilities in one pod, add the following configuration information to
the custom\_xml parameter in the ums\_configuration section.

```
custom\_xml: |
      <server>
        <openidConnectClient id="client\_id" 
          clientId="client\_id" 
          clientSecret="client\_secret" 
          authorizationEndpointUrl="authorizationEndpointUrl"
          tokenEndpointUrl="tokenEndpointUrl"
          issuerIdentifier="issuerIdentifier" 
          jwkEndpointUrl="jwkEndpointUrl"
          signatureAlgorithm="signatureAlgorithm">
          <authFilter>
            <requestUrl matchType="contains" urlPattern="/oidc/endpoint/ums/authorize"></requestUrl>
            <requestHeader id="allowBasicAuth" matchType="notcontain" name="Authorization" value="Basic" />
          </authFilter>
        </openidConnectClient>
      </server>
```

During deployment, the operator adds the OIDC client configuration to the
server configuration of UMS.

3. If you use dedicated pods for UMS capabilities. also include the following
featureManager section in custom\_xml to add the required
openidConnectClient-1.0 feature. 
          <featureManager>
            <feature>openidConnectClient-1.0</feature>
          </featureManager>For
example:    # Configuration for sso pods
    sso:
      ...
      custom\_xml: |
        <server>
          <featureManager>
            <feature>openidConnectClient-1.0</feature>
          </featureManager>
          <openidConnectClient id="client\_id"
            clientId="client\_id"
            clientSecret="client\_secret"
            authorizationEndpointUrl="authorizationEndpointUrl"
            tokenEndpointUrl="tokenEndpointUrl"
            issuerIdentifier="issuerIdentifier"
            jwkEndpointUrl="jwkEndpointUrl"
            signatureAlgorithm="signatureAlgorithm">
            <authFilter>
              <requestUrl matchType="contains" urlPattern="/oidc/endpoint/ums/authorize"></requestUrl>
              <requestHeader id="allowBasicAuth" matchType="notcontain" name="Authorization" value="Basic" />
            </authFilter>
          </openidConnectClient>
        </server>