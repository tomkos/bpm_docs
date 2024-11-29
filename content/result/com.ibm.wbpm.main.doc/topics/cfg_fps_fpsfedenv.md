# Configuring Process Federation Server and the
federated environment

## About this task

- Roadmap for configuring Process Federation Server and federated environments

Federated environments accommodate various configuration scenarios. This roadmap guides you through the most common paths for configuring Process Federation Server and federated environments and helps you ensure that the federated environment is secure.
- The Process Federation Server server.xml configuration file

You can edit and update the template server.xml file to meet the requirements of your environment. In this file, you can configure your federated systems, configure a common user registry, single sign-on, the federated data repository service, the Liberty HTTP server, secure communications, or enable specific features.
- Configuring the Process Federation Server database

The Process Federation Server database stores saved search definitions that Process Portal uses.
- Configuring a common user registry for federated process server environments

A common user registry is required across Workplace, Process Portal, custom client applications, Process Federation Server, and the federated systems, so that authenticated users can access the entire environment through single sign-on (SSO). Supported user registries include LDAP and custom user registry. In development and test environments, you can also use a file-based basic registry.
- Configuring single sign-on for federated process environments

Federated environments include different types of server: the server that hosts Workplace and Process Portal, Process Federation Server, and the federated systems. When single sign-on (SSO) is enabled, users log in to any of these servers, and then they can access all the other servers in the federated environment for which they are authorized without getting prompted again.
- Configuring load balancing and failover for federated environments

You can configure IBM HTTP Server or another reverse proxy server for load balancing and failover handling in federated environments. Instead of incoming HTTP requests going directly to Process Federation Server, they go to the IBM HTTP Server or reverse proxy server, which then distributes the requests across multiple Process Federation Servers that perform the work.
- Configuring the federated data repository service

You can configure some aspects of the federated data repository service behavior.
- Configuring Process Portal for a federated environment

You can run Process Portal in both single business process management  systems or in federated environments based on Process Federation Server. For federated environments, you need to configure certain aspects of the environment for Process Portal to work correctly. No additional configuration is required for a single system.
- Configuring Workplace on-premises for a federated environment

You can run Workplace on-premises in either single business process management systems or federated environments based on Process Federation Server. For Workplace to work correctly in a federated environment, you need to configure certain aspects of the environment.
- Securing communications in federated environments

Communication in federated environments is secured with Secure Sockets Layer (SSL) protocol. The SSL protocol provides transport layer security that includes authenticity, data signing, and data encryption to ensure that the connection between the client and the server is secure.
- Validating the Process Federation Server and federated environment configuration

Multiple connection and security aspects are involved in configuring a federated environment. To help ensure that your environment is configured correctly, use the validation tool that is provided with Process Federation Server to check your settings.