<!-- image -->

# Setting up security for system REST services

## Before you begin

- Enable application security and administrative security. See Setting up security for the Business Space component and Process Portal.
- Check that your user ID is registered in the user registry for
your product.

## About this task

How you map users to a REST service provider application
affects all the services for the provider.

To see the affected
services, select Services > REST
services > REST service providers, and select the matching provider application in the
list of providers.

## Procedure

1 On the administrative console, select one of the followingoptions:
    - For a server environment, select Applications > Application types > WebSphere enterprise
applications > REST Services Gateway
    - In addition, for a network deployment environment, select Applications > Application types > WebSphere enterprise applications > REST
Services Gateway Dmgr
2. Under Detail Properties, select  Security role to user/group
mapping.
3. To control access to the data in all the REST services
widgets, add users and groups to the RestServicesUser role.