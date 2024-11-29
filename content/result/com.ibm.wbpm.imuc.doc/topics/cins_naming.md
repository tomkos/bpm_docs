# Naming considerations for profiles, nodes, servers, hosts,
and cells

## Profile naming considerations

- Spaces
- Special characters that are not allowed within the name of a directory
on your operating system, such as *, &, or ?.
- Slashes (/) or back slashes (\)

Directory
path considerations: The installation directory path must be less
than or equal to 60 characters. The number of characters in the profiles\_directory\_path\profile\_name directory
must be less than or equal to 80 characters.

## Node, server, host, and cell naming
considerations

- cells
- nodes
- servers
- clusters
- applications
- deployments

- Stand-alone server profiles
- Deployment manager profiles
- Managed-node profiles

| Field name                               | Default value                                                                                                              | Constraints                                                                       | Description                                                                                                                                                     |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Node name                                | shortHostNameNodeNodeNumber where: shortHostName is the short host name. NodeNumber is a sequential number starting at 01. | Avoid using the reserved names.                                                   | Select any name you want. To help organize your installation, use a unique name if you plan to create more than one server on the system.                       |
| Server name                              | server1                                                                                                                    | Use a unique name for the server.                                                 | The logical name for the server.                                                                                                                                |
| Host name                                | The long form of the domain name server (DNS) name.                                                                        | Use a fully qualified host name that is addressable through your network.         | Use the actual DNS name or IP address of your workstation to enable communication with it. See additional information about the host name following this table. |
| SSL certificate subject common name (CN) | Generated certificates use the host name as the subject common name (CN).                                                  | The common name on the certificate must match the host name for SSL verification. |                                                                                                                                                                 |

| Field name                               | Default value                                                                                                                      | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                   |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Node name                                | shortHostNameCellManager NodeNumber where: shortHostName is the short host name. NodeNumber is a sequential number starting at 01. | Use a unique name for the deployment manager. Avoid using the reserved names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The name is used for administration within the deployment manager cell.                                                                                                                                                                                                                       |
| Host name                                | The long form of the domain name server (DNS) name.                                                                                | Use a fully qualified host name that is addressable through your network. Avoid using the reserved names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Use the actual DNS name or IP address of your workstation to enable communication with it. See additional information about the host name following this table.                                                                                                                               |
| Cell name                                | shortHostNameCellCellNumber where: shortHostName is the short host name. CellNumber is a sequential number starting at 01.         | Use a unique name for the deployment manager cell. A cell name must be unique in any circumstance in which the product is running on the same physical workstation or cluster of workstations, such as a Sysplex. Additionally, a cell name must be unique in any circumstance in which network connectivity between entities is required either between the cells or from a client that must communicate with each of the cells. Cell names also must be unique if their name spaces are going to be federated. Otherwise, you might encounter symptoms such as a javax.naming.Name NotFoundException exception, in which case, you need to create uniquely named cells. | All federated nodes become members of the deployment manager cell, which you specify in one of the following ways: The Node, Host, and Cell Names page of the Profile Management Tool The manageprofiles -cellName parameter The bpm.cell.name property of the BPMConfig command-line utility |
| SSL certificate subject common name (CN) | Generated certificates use the host name as the subject common name (CN).                                                          | The common name on the certificate must match the host name for SSL verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                               |

| Field name                               | Default value                                                                                                              | Constraints                                                                          | Description                                                                                                                                                              |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Node name                                | shortHostNameNodeNodeNumber where: shortHostName is the short host name. NodeNumber is a sequential number starting at 01. | Avoid using the reserved names.Use a unique name within the deployment manager cell. | The name is used for administration within the deployment manager cell to which the managed-node profile is added. Use a unique name within the deployment manager cell. |
| Host name                                | The long form of the domain name server (DNS) name.                                                                        | Use a fully qualified host name that is addressable through your network.            | Use the actual DNS name or IP address of your workstation to enable communication with it. See additional information about the host name following this table.          |
| SSL certificate subject common name (CN) | Generated certificates use the host name as the subject common name (CN).                                                  | The common name on the certificate must match the host name for SSL verification.    |                                                                                                                                                                          |

Host name considerations:The host name is the network name for the physical
workstation on which the node is installed. The host name must resolve to a physical network node on
the server. When multiple network cards exist in the server, the host name or IP address must
resolve to one of the network cards. Remote nodes use the host name to connect to and to communicate
with this node.

IBM® Business Automation Workflow is compliant to both Internet
Protocol version 4 (IPv4) and version 6 (IPv6). Wherever you can enter IP addresses in the
administrative console, or elsewhere, you can do so in either format. Note that if IPv6 is
implemented on your system you must enter the IP address in IPv6 format, and conversely, if IPv6 is
not yet available to you, enter IP addresses in IPv4 format. For more information on IPv6 refer to
the following description: IPv6.

- Select a host name that other workstations can reach within your network.
- Do not use the generic identifier, localhost, for environments that are spread across multiple
computers.
- Do not attempt to install IBM Business Automation Workflow
products on a server with a host name that uses characters from the double-byte character set
(DBCS). DBCS characters are not supported when used in the host name.
- Avoid using the underscore ( \_ ) character in server names. Internet standards dictate that
domain names conform to the host name requirements described in Internet Official Protocol Standards
RFC 952 and RFC 1123. Domain names must contain only letters (uppercase or lowercase) and digits.
Domain names can also contain dash characters ( - ) as long as the dashes are not on the ends of the
name. Underscore characters ( \_ ) are not supported in the host name. If you have installed IBM Business Automation Workflow on a server with an underscore character in
the server name, access the server with its IP address until you rename it.
- If you are using Secure Sockets Layer (SSL) the host name that
the server connects to must match the common name (CN) in the SSL certificate.
- If you have configured Secure Sockets Layer (SSL)
communication and the name of a server certificate does not match the host name of a server, an SSL
connection failure may occur with the IOException message HTTPS hostname
wrong. To help resolve this problem, you can add a Subject Alternative Name (SAN) set
to the server certificate. Information about SAN sets is found in the SSL fails when host name
configuration fails topic.

If you define coexisting nodes on the same computer with unique IP addresses, define
each IP address in a domain name server (DNS) look-up table. Configuration files for servers do not
provide domain name resolution for multiple IP addresses on a workstation with a single network
address.

- Fully qualified domain name servers (DNS) host name string, such as
xmachine.manhattan.ibm.com
- The default short DNS host name string, such as xmachine
- Numeric IP address, such as 127.1.255.3

The fully qualified DNS host name has the advantages of being totally unambiguous and
flexible. You have the flexibility of changing the actual IP address for the host system without
having to change the server configuration. This value for host name is particularly useful if you
plan to change the IP address frequently when using Dynamic Host Configuration Protocol (DHCP) to
assign IP addresses. A disadvantage of this format is being dependent on DNS. If DNS is not
available, then connectivity is compromised.

The short host name is also dynamically resolvable. A short name format has the added
ability of being redefined in the local hosts file so that the system can run the server even when
disconnected from the network. Define the short name to 127.0.0.1 (local loopback) in the hosts file
to run disconnected. A disadvantage of the short name format is being dependent on DNS for remote
access. If DNS is not available, then connectivity is compromised.

A numeric IP address has the advantage of not requiring name resolution through DNS.
A remote node can connect to the node you name with a numeric IP address without DNS being
available. A disadvantage of this format is that the numeric IP address is fixed. You must change
the setting of the hostName property in configuration documents whenever you change the workstation
IP address. Therefore, do not use a numeric IP address if you use DHCP, or if you change IP
addresses regularly. Another disadvantage of this format is that you cannot use the node if the host
is disconnected from the network.

## Related concepts

- Process and process application considerations
- Resource considerations
- Development and deployment version levels

## Related tasks

- Preparing necessary security authorizations

## Related reference

- Installation directories for the product and profiles
- Unique cell names are required in an IBM Business Process Manager (BPM) topology

## Related information

- SSL fails when host name configuration fails