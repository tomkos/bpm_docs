# Securing communications between Process Portal or Workplace and Process Federation Server

## Before you begin

## About this task

- If the browser connects directly to the federated environment, a signer certificate for each of
the process federation servers and federated systems that it communicates with.
- If the browser connects to the federated environment through IBM HTTP Server, a signer
certificate for each of the IBM HTTP Servers.

If CA-signed certificates are not used, for example, in a
development or test environment, users must import signer certificates into their browsers before
they use Process Portal or
Workplace in the
federated environment. The signer certificate can be manually imported into the browser.
Alternatively, the user can go to the URL for each component in the federated environment that
Process Portal or Workplace communicates with, and
accept the certificate when prompted.

## Procedure

If CA-signed certificates are not used and the certificates from the federated
environment are not available in users' browsers, users can go to the URL for each of the components
in the federated system and accept the associated signer certificate when prompted by the
browser.Tip: If IBM HTTP Server is used, the URL is the IBM HTTP Server URL instead of
the Process Federation Server URL or the URL for the
federated system.

- From the Process Portal or Workplace browser, go to a URL on
each federated system, for example, the Process Portal URL:
https://bpm\_host.mycompany.com:9443/ProcessPortal.
Import the signer certificate if prompted to do so by the browser.
- From the browser, go to a Process Federation Server URL, for
example, the systems REST service:
https://pfs\_host.mycompany.com:9443/rest/bpm/federated/v1/systems.
Import the signer certificate if prompted to do so by the browser.

## Results