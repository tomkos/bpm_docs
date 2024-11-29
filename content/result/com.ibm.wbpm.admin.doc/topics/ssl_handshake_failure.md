# SSL handshake failure when connecting with an external HTTP
server

## Problem

```
CWPKI0022E: SSL HANDSHAKE FAILURE:  A signer with SubjectDN "xx=xxxxx" was sent from target host:port "de1:xxx".
The signer may need to be addedto local trust store "/home/bpmsvt/ibm/BPM/v8.5/profiles/Node1Profile/config/cells/PCCell1/trust.p12" 
located in SSL configuration alias "NodeDefaultSSLSettings" loaded from SSL configuration file "security.xml". The extended error message 
from the SSL handshake exception is: "PKIX path building failed: java.security.cert.CertPathBuilderException: unable to find valid 
certification path to requested target".
```

## Solution

1. Log into the administrative console.
2. Click Security  > SSL
certificate and key management.
3. Under Configuration settings, click Manage endpoint
security configurations.
4. Select the outbound configuration. For example, PCCell1(CellDefaultSSLSettings).
5. Under Related Items, click Key
stores and certificates and click CellDefaultTrustStore.
6. Under Additional properties, click Signer
certificates.
7. Click Retrieve from port. The Configuration
panel is displayed.
8 Complete the following general properties fields:
    1. In the Host field, enter the IHS virtual
host. For example, de1.
    2. In the Port field, enter the virtual host
port. For example, 443.
    3. In the Alias field, enter the certificate
alias. For example, de1\_cert.
    4. Click OK and save your changes to the master
configuration.
9. Click Retrieve signer information.
10. Verify that the certificate information is for a trusted certificate.
11. Click Apply and Save.