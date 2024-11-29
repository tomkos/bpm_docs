# Regenerating certificates for IBM® Business Automation
Machine Learning Server

## Procedure

1. Stop Machine Learning Server by
using the following command: ./bin/ba-ml-server-stop
2. Remove the certificate directory (ba-ml-server\_install\_dir/certs)
for each component you want to regenerate certificates for.
3. Restart Machine Learning Server by
using the following command and enter all the prompted variables:
./bin/ba-ml-server-start --init --acceptLicense