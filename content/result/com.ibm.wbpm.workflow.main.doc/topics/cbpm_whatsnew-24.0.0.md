# What's new in IBM Business Automation
Workflow 24.0.0.0

- What changed in interim fix 1 - July 2024
- Work efficiently with tasks, workflows, and cases
- Build process applications and case solutions
- Business Automation Workflow Advanced
- Process Admin Console
- Advanced searches in federated and nonfederated environments
- Federated data repository BPD indexing
- Intelligent Task Prioritization
- Validation for the 100custom.xml file
- Install and upgrade Business Automation Workflow on containers
- Security and compliance for Business Automation Workflow on containers

For information about features that are deprecated or
removed in 24.0.0.0, see Deprecated and removed features of IBM Business Automation Workflow.

Update to 
Business Automation Workflow 24.0.0 to
experience all the highlights, such as these added abilities and improvements.

## What changed in interim fix 1 - July 2024

- From 24.0.0.0-IF001, you can upgrade Business Automation Workflow on containers directly
from 22.0.2-iF006 to 24.0.0-IF001. 
Learn more...
- From 24.0.0.0-IF001, you can upgrade Process Federation Server on containers
directly from 22.0.2-iF006 to 24.0.0-IF001. 
Learn more...
- For information, see Business Automation Workflow
on containers 24.0.0 interim fixes.

## Work efficiently with tasks, workflows, and cases

The following list contains the new features for using Workplace and Case Client in Business Automation Workflow:

- Easily modify multiple process tasks at once in the case task list and
in-basket in Case Client.

Learn more...
- Automatically log out inactive users from Workplace to improve performance.

Learn more...

Back to top

## Build process applications and case solutions

The new features for modelling your process applications in Process Designer and case solutions
in Case Builder include:

- In Process Designer, there are new
server side validation messages when an asynchronous service flow is used by a coach model.
- The number of decimal places in a business object is set by default in the
Decimal UI view configuration when you create a simple type variable.
- Easily create case pages based on new human service-based solution layouts,
or manage classic pages based on widgets. 
Learn more...
- Easily find and reuse case and activity properties by displaying their
unique identifier and choice list designation in Case Builder.
- New configuration option on the Case Stages view to display stages in a
vertical orientation, allowing more flexible layout designs.  
Learn more...
- For process work items in all assigned in-baskets, non-admin users who are managers of roles can
view other user claimed tasks. 
Learn more...

Back to top

## Business Automation Workflow
Advanced

You can now use the following new features in Business Automation Workflow Advanced:

- Now API keys can be used as an authentication option to call REST services in
addition to the basic authentication support. 
Learn more...
- Create a migration path to easily move, containerize, and modernize
mediation flows to service flows. 
Learn more...

Back to top

## Process Admin Console

The following list contains some of the new features for Process Admin Console:

- Track changes that administrators make across the product with a new
auditing log file.
Learn more...
- You are now prompted to confirm that you want to delete a user or group in
the Process Admin Console.
- In the Installed Apps page, you can now search snapshots by their name or
the application name and easily refresh the results.
- Check whether the user synchronization results are up to date with the new Check
Synchronization Result feature.

Back to top

## Advanced searches in federated and nonfederated environments

New advanced searches are now available in federated and nonfederated Business Automation Workflow environments:

- You can now create advanced searches and build complex queries with keywords
such as AND, NOT, and OR in Workplace in addition to using basic
searches. For reuse, the advanced search queries can be saved and shared with teams.  
Learn more...
- A new REST API for advanced search across tasks, process and case instances
is available in Process Federation Server (federated
environment) and Business Automation Workflow
server (nonfederated environment). 
Learn more...
- A nonfederated Business Automation Workflow server can be configured
to index tasks, processes, and cases to an Elasticsearch or OpenSearch environment.
Learn more...
- The new search query condition syntax supports: Learn more...
    - Existing saved search conditions, query filter, and search filter syntax.
    - A new flexible JSON syntax that supports complex combinations of AND, OR, and
NOT keywords.

<!-- image -->

- Existing saved search definitions can be migrated to advanced search queries automatically to
ease transition to the new REST APIs.

Back to top

## Federated data repository BPD indexing

- The indexing of BPD data can be done without having Process Federation Server installed, and
enables the advanced searches. 
Learn more...
- In federated topologies, federating a Business Automation Workflow BPD system by configuring
the Process Federation Server
indexer is now deprecated, being required only for the federation of Business Automation Workflow 23.0.2 and earlier
systems. As of 24.0.0.0, you can configure the federated Business Automation Workflow systems to index directly
into the federated data repository. 
Learn more....
- Compared to the Process Federation Server BPD indexer andthe Process Portal search indexer, the federated data repository indexer is more performant and easier toadminister. Learn more...

<!-- image -->

    - For the Process Federation Server BPD indexer
Learn more...
    - For the Process Portal search indexer Learn more...

Back to top

## Intelligent Task Prioritization

The following list contains the new features for Intelligent Task Prioritization:

- The training data for Intelligent Task Prioritization in Business Automation Insights is now hosted in
OpenSearch.
- Use an enhanced Intelligent Task Prioritization feature with new
RETRAIN\_MODEL\_SCHEDULE environment variable and Transport Layer Security (TLS)
communication improvements. 
Learn more...

Back to top

## Validation for the 100custom.xml file

If there is a mistake in the 100custom.xml file, the customization is not
applied and it is difficult to find where the issue is. The BPMConfig -validate
command has been enhanced to generate two files,
TeamworksConfiguration.running.xml and
TeamWorksConfiguration.system.xml for each server, and also at the cluster
level. The TeamWorksConfiguration.system.xml file contains only the default
configuration, so you can compare the two files and see what customizations have been made. 
Learn more...

Back to top

## Install and upgrade Business Automation Workflow on containers

The following list describes the enhancements for installing and upgrading your Business Automation Workflow on containers deployments.

- Business Automation Workflow Runtime
server component is now managed by a separate operator. The new operator comes with new custom
resource definitions (CRD), service accounts, roles, role bindings, cluster roles, and cluster role
bindings.
The installation experience of Business Automation Workflow on containers remains the
same, using the Cloud Pak for Business Automation custom resource. 
Learn more...
- If you deploy Business Automation Workflow on containers and Business Automation Insights in the samenamespace, you can automatically retrieve the required server connection properties by setting thenew dynamic\_generate\_connection\_info parameters.
    - For Kafka 
Learn more...
    - For search 
Learn more...
- Because it is a production runtime deployment, the Hiring Sample is no longer included with
Business Automation Workflow on containers.
- Business Automation Workflow 24.0.0.0
supports a direct upgrade from 21.0.3 as well as from the previous version 23.0.2. 
Learn more...
If you have 22.0.1 or 22.0.2 deployments, you must first upgrade them to 23.0.2 and then upgrade
to 24.0.0.0. If you have 23.0.1 deployments, you must first upgrade them to 23.0.2 and then upgrade
to 24.0.0.0.

To find out more about the supported environments for Business Automation Workflow, see the detailed system requirements.

Back to top

## Security and compliance for Business Automation Workflow on containers

When Business Automation Workflow
capabilities interact with each other, network traffic is encrypted by default. In earlier versions,
encryption used TLS 1.2. In 24.0.0.0, most internal communication now defaults to the more modern
and secure TLS 1.3 version. The same is true for outbound communication, for example to custom
databases or APIs that are used by customized applications.

Back to top