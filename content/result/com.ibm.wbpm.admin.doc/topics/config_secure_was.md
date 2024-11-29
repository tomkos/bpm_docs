# Configuring access to a secure application server

- Extracting a signer certificate

WebSphere® Application Server uses the certificates that reside in keystores to establish trust for a Secure Sockets Layer (SSL) connection. The first step in enabling IBM Process Designer users to access is to extract the appropriate signer certificate from the remote WebSphere Application Server instance. The extracted certificate is saved as Distinguished Encoding Rules (DER) file that you can then install in your local trust store.
- Installing a signer certificate in IBM Workflow Server trust store

Signer certificates establish the trust relationship in SSL communication. After you extract the signer certificate from WebSphere Application Server, you must add it to the IBM Workflow Server trust store.