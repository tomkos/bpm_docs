# Containers: Installing, configuring, and upgrading IBM Business Automation
Workflow on containers

Containers: 
 Follow the
instructions provided to install, configure, and upgrade stand-alone IBM Business Automation
Workflow on containers.

For details about the Business Automation Workflow on containers
environment, see Container runtime.

## Overview

- To get started with OpenShift Container Platform (OCP), see Getting started with Red Hat OpenShift
- To understand the roles you'll need, see Cloud Pak
roles and personas
- To understand important terms, such as operator, custom resource, and pattern, see Understanding Custom resources and patterns

- Workflow Server (JMS
included)
- OpenSearch (except for Linux on IBM Z and on IBM Power (ppc64le), where OpenSearch is not
included because they support only external Elasticsearch or OpenSearch)
- From the Foundation pattern:
    - User Management Service (UMS): For
information about installing UMS, see Installing and configuring User
Management Services on containers.
    - Business Automation Navigator (BAN)
- From the Content pattern:

- Content Platform Engine (Content
Platform Engine)
- Content Management Interoperability Services (CMIS)
- Content Services GraphQL

- Installation options

 Containers: 
You can install stand-alone IBM Business Automation Workflow on containers for various purposes and in multiple hybrid environments to automate parts of your business.
- Red Hat OpenShift security and compliance

 Containers: 
As a cloud administrator on the Red Hat OpenShift Container Platform, you must ensure that your cluster allows authorized users access to the data and applications that they need. At the same time, you must protect the cluster from accidental or malicious access by granting only the minimal privileges to users and processes to restrict system calls and file system access.
- Planning for IBM Business Automation Workflow on containers

 Containers: 
 Before you install stand-alone Business Automation Workflow on containers, it is important to understand what you need, what options you have, the entitlement of your license, and how you can measure the usage of your deployments.
- Installing a production deployment

 Containers: 
 Installation of stand-alone IBM Business Automation Workflow on containers uses an operator, which is a Kubernetes feature that makes it simpler to install and update without having to worry about the underlying cloud provider. However, it is important for cluster administrators and non-administrators who want to install containers to understand the main concepts and how you interact with the operator.
- Customizing Business Automation Workflow on containers

You can customize Business Automation Workflow in many different ways. All customizations are optional.
- Installing Process Federation Server on containers

Process Federation Server helps you create a federated process environment. It provides business users with a single point of access to their task list and launch list. This accessibility is available regardless of the type of process that they are working on and the backend system where the process artifacts are stored. Process Federation Server containers include indexers, retrievers, REST services, and integrate with a federated data repository (Elasticsearch or OpenSearch) cluster where it stores both federated data and saved searches.
- Installing and configuring User Management Services on Containers

This document provides information for configuring and using User Management Services (UMS) in Business Automation Workflow on containers.
- Updating deployments

 Containers: 
You can reconfigure and update the software that is already installed. For information about how to update deployments, see Updating deployments.
- Uninstalling IBM Business Automation Workflow on containers

 Containers: 
You can uninstall resources and components from your platform deployment.
- Upgrading IBM Business Automation Workflow on containers

 Containers: 
If IBM Business Automation Workflow on containers was installed as a production deployment in 21.0.3, 22.0.2 or 23.0.2 and you want to continue to use your applications in 24.0.0.0, upgrade your applications.
- Upgrading Process Federation Server

If you installed Process Federation Server 23.0.2 or 22.0.2, you can upgrade to the latest Process Federation Server. There was no Process Federation Server on containers in 21.0.3, so to upgrade from 21.0.3, you must install a new Process Federation Server.
- IBM Business Automation Workflow on containers parameters

 Containers: 
Each container image needs a set of values for its configuration parameters to create a Kubernetes deployment.
- Troubleshooting IBM Business Automation Workflow on containers

 Containers: 
You can use the operator and Ansible containers to retrieve log files of the installed operator to assist with troubleshooting IBM Business Automation Workflow on containers.