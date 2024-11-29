# Optional: Customizing the container runtime environment Workflow Server to connect to Workflow Center

## About this task

To establish a connection between workflow server in IBM Business Automation
Workflow on containers and Workflow Center, configure the
workflow\_center section of the custom resource (CR) YAML file.

## Procedure

When Workflow Server connects to Workflow Center, authentication is
required. Create a TLS secret in the operator by using the root CA certificate of Workflow Center so that it can be
recognized as a trusted server:

1 Extract the Workflow Center root SSLcertificate.
    1. In the WebSphere administrative console, click Security > SSL certificate and key management > Key stores and certificates > CellDefaultTrustStore > Signer certificates.
    2. Select the root certificate and click Extract.
    3. Name the file. For example, name the file WorkflowCenter.cert.
    4. For the data type, select Base64-encoded ASCII data.
    5. Click Apply. From the message, note where the certificate is stored on
the file system.
2 Copy the file and create the secret:

1. Copy the certificate from step 1 to Workflow Server.
2. On the IBM Business Automation
Workflow runtime environment, run the
following oc command to create a secret:
> oc create secret generic baw-tls-secret --from-file=tls.crt=/root/WorkflowCenter.cert
3. Add this secret to the trust list section of the IBM Business Automation
Workflow CR file, for example
baw\_configuration:
- name: instance1
  tls:
   tls\_trust\_list: [baw-tls-secret]
3 Create a secret that holds the username and password of the Workflow Center administrator.

1. On the IBM Business Automation
Workflow
runtime environment, create a new secret called, for example,
adminSecrets4operator-ctnrs.yaml. This secret contains the credentials of an
administrator for Workflow Center, for
exampleapiVersion: v1
kind: Secret
metadata:
 name: ibm-baw-wc-secret
type: Opaque
stringData:
 username: deadmin
 password: deadmin
2. Apply this new secret to the runtime environment:
> oc apply -f ./adminSecrets4operator-ctnrs.yaml
4. Update the following parameters in the workflow\_center section of the IBM Business Automation
Workflow CR YAML file to apply
changes to your deployment environment, for example:
url: "https://example.fyre.ibm.com:9443/ProcessCenter"
secret\_name: "ibm-baw-wc-secret"
heartbeat\_interval: 30After these steps, IBM Business Automation
Workflow on container shows up on
the Servers page of Workflow Center.
5 So that the Workflow Center recognizes Workflow Server as a trusted server, complete thesesteps:

1. In the Workflow Center WebSphere administrative
console, click Security > SSL certificate and key management > Key stores and certificates > CellDefaultTrustStore > Signer certificates > Retrieve from port > .
2. Enter the hostname, secure port of Workflow Server, and alias, and click
Retrieve signer information.
3. Click Apply to save your changes.