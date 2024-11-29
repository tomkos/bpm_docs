# Configuring UMS routes for load balancing

## Procedure

1 If the ums\_configuration.hostname parameter is defined, define a load balancerroute for each of the following endpoints: Where hostname is the value of theums\_configuration.hostname parameter, and port is the portnumber (typically 443).
    - ums-sso-hostname:port
    - ums-teams-hostname:port
    - ums-scim-hostname:port
    - ums-hostname:port
2 If the ums\_configuration.hostname parameter is not defined, define a loadbalancer route for the deprecated catch all endpoint: Where hostname is the value of theshared\_configuration.sc\_deployment\_hostname\_suffix parameter, andport is the port number (typically 443).

- ums.hostname:port