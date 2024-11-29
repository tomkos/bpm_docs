# Completing post-deployment tasks for User Management Service

## Procedure

1. Optional: 
If you want to configure Business Automation Workflow or IBM Process Federation
Server to use UMS
single sign-on, perform the following task: Adding IBM Business Automation Workflow and IBM Federated Process Portal to use the User Management
Service.
2. Optional: 
Delegating authentication to a Security Assertion Markup Language (SAML) identity provider.
3. Optional: 
Delegating authentication to an OIDC Identity Provider.

- Delegating authentication to a Security Assertion Markup Language (SAML) identity provider

User Management Services (UMS) can delegate authentication to SAML identity provider (IdP).
- Delegating authentication to an OIDC Identity Provider

User Management Services (UMS) can delegate authentication to an OIDC Identity Provider (IdP).
- Configuring UMS routes for load balancing

 Containers: 
If you are not using Red Hat OpenShift Kubernetes Service (ROKS) or OpenShift Container Platform (OCP) and you have a load balancer in front of your User Management Service services, you must define serviceType: NodePort endpoints.