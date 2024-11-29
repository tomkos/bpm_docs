# Securing communications in federated environments

- Securing outbound communications between Process Federation Server and federated systems

Process Federation Server communicates with each federated system by using REST services. Configure the Process Federation Server for secure communications between Process Federation Server and each of the federated REST endpoints.
- Securing inbound communications to Process Federation Server

Configure Process Federation Server for secure inbound communications between a client and a server.
- Securing communications between Process Portal or Workplace and Process Federation Server

Communication between Process Portal or Workplace and servers in the federated environment is secured with the Secure Sockets Layer (SSL) protocol. To secure communication, ensure that Process Portal or Workplace browsers are configured with the signer certificates for Process Federation Server and each of the federated systems.
- Securing communication between Process Federation Server and the federated data repository

In a production environment, you must secure communications between Process Federation Server and the federated data repository (Elasticsearch or OpenSearch cluster) by using SSL.
- Securing communications between Process Federation Server and LDAP

Enable communication with an SSL-enabled Lightweight Directory Access Protocol (LDAP) server.
- Configuring secure database access in federated environments

The indexing service on Process Federation Server requires access to task and process-related data that is in databases on the federated systems. To ensure secure communication between Process Federation Server and the database system, configure the Secure Sockets Layer (SSL) protocol for database access.