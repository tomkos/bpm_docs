# Using custom certificates for IBM® Business Automation
Machine Learning Server

## Procedure

1. Stop Machine Learning Server by
using the following command: ./bin/ba-ml-server-stop
2 Replace the certificates, keystore, and truststores withyour own. The certificates are in the ba-ml-server\_install\_dir /certs directory.Use them to secure communication with the server.
    - ca.crt: The root certification authority (CA) certificate, in
privacy-enhanced mail (PEM) format
    - ca.key: The root CA key, in PEM format
    - local-server.crt: The server certificate signed by the root CA
certificate, in PEM format
    - local-server.key: The server private key, in PEM format
3. Restart Machine Learning Server by
using the following command and enter all the prompted variables:
./bin/ba-ml-server-start --init --acceptLicense