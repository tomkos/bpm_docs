# Securing communications routes with User Management Services (UMS)

## Before you begin

## Procedure

1. If you are creating a test environment and do not want to deal with certificates, you do not
need to generate any ums\_configuration.external\_tls\_* secrets. Later, by removing
them from the custom resource file, the root\_ca\_secret will be used to generate an
internal TLS secret for all UMS services and an external TLS secret for each of the routes: 
ums-route, ums-sso-route, ums-scim-route,
and ums-teams-route.
2. If you are creating a production environment, and you want to use the shared secret
shared\_configuration.external\_tls\_certificate\_secret that contains a single HTTPS
wildcard certificate that can secure all routes, you should not define any of the UMS secrets with
names starting with the string ibm-baw-ums-external-tls. When they are not defined,
the shared secret is used, if it is defined.
3 If you are creating a production environment and you do not want to use a shared secret, youmust create one or more secrets that contain TLS certificates that represent the host names or acommon hostname suffix of the routes that your clients connect to.
    1 Obtain or generate a TLS certificate that represents the host names or a common hostname suffixof the routes that your clients will use to connect to UMS: Perform one of the following:
        - ums-route
        - ums-teams-route
        - ums-scim-route
        - ums-sso-route
        - Obtain a certificate that is signed by an external certificate authority (CA) that is trusted by
your clients.
        - Generate a certificate by using OpenSSL:
            1. Create a TLS certificate signing request by executing OpenSSL. Note that the final certificate
should have a Subject Alternative Names (SAN) value that matches the hostname. Many
certificate authorities allow you to specify SANs during the ordering process, otherwise you must
provide the SAN directly in the certificate signing request
(CSR).openssl req -new -newkey rsa:2048 -subj "/CN=UMS" -extensions SAN  -days 365 -nodes -out ums.csr -config <(cat /etc/ssl/openssl.cnf <(printf "[SAN]\nsubjectAltName=DNS:ums.mycluster.com"))
            2. Two files are generated: a private key (privkey.pem) and a certificate signing
request that can be sent to your certificate authority for signing.
2 Use the private key and your certificate authority's response to generate the following secrets If the response from your certificate authority does not include all certificates from itssigning chain, you can provide them in ibm-baw-ums-external-tls-ca-secret .Create each TLS secret by running the followingcommand:oc create secret tls ibm-baw-ums-external-tls-secret --cert tls.crt --key tls.key Theresult in a YAML structure like thefollowing:apiVersion: v1kind: Secretmetadata: ...type: kubernetes.io/tlsdata: tls.crt: [very long base64 string of certificate] tls.key: [very long base64 string of private key] Foreach secret, run your YAML file, forexample:oc create -f ums-external-tls-secret.yaml

- ibm-baw-ums-external-tls-secret for the ums-route route
- ibm-baw-ums-external-tls-teams-secret for the ums-teams-route
route
- ibm-baw-ums-external-tls-scim-secret for the ums-scim-route
route
- ibm-baw-ums-external-tls-sso-secret for the ums-sso-route
route

```
oc create secret tls ibm-baw-ums-external-tls-secret --cert tls.crt --key tls.key
```

```
apiVersion: v1
kind: Secret
metadata:
  ...
type: kubernetes.io/tls
data:
  tls.crt: [very long base64 string of certificate]
  tls.key: [very long base64 string of private key]
```

```
oc create -f ums-external-tls-secret.yaml
```

3. Make a note of the secret names that you will need later to specify in the custom resource for
the ums\_configuration.external\_tls\_*
parameters:ums\_configuration:
    hostname:
    ## optional: create routes for backwards compatibility
    backwards\_compatibility\_routes:
    ## optional for secure communication with UMS
    external\_tls\_secret\_name:
    ## optional for secure communication with UMS
    external\_tls\_ca\_secret\_name:
    ## optional for secure communication with UMS
    external\_tls\_teams\_secret\_name:
    ## optional for secure communication with UMS
    external\_tls\_scim\_secret\_name:
    ## optional for secure communication with UMS
    external\_tls\_sso\_secret\_name: