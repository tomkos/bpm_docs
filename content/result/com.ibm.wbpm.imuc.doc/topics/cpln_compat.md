# Development and deployment version levels

When you try to determine the version levels of IBM Business Automation Workflow or IBM Business Automation
Workflow that you need in your environment, your decision
depends on the version levels that were used when your applications were developed.

Various actions are supported when version mismatches exist between the development tools
(IBM Process
Designer and IBM Integration
Designer) and the runtime servers.

- The term earlier supported versions refers to applications and artifacts that were
generated in an earlier product that has runtime migration or upgrade support to this product
version.
- For snapshots from earlier supported versions, it is recommended that you update the system
toolkits to the latest levels. To use new features or apply defect fixes, you must update the
toolkits.
- For EAR applications from earlier supported versions, it is recommended that you migrate your
project interchange files (PIs) to the latest version of Integration Designer and regenerate your EAR files. For more
information, see Migrating IBM Integration Designer artifacts.

## Snapshot content and Process Designer

- Each IBM Workflow
Center
version level (including cumulative fix levels) has a specific Process Designer version level that it
supports. This required version can be downloaded from the version of Workflow Center that supports it.
Version mismatches between Workflow Center and Process Designer are not
supported.Note: See the supported software section of  Detailed system requirements for a specific product to determine the
specific Process Designer
version associated with a particular Business Automation Workflow or IBM Business Automation
Workflow version.
- Version 8.5.0 and later versions of IBM Process Center as well as Workflow Center can connect to an online IBM Workflow
Server at the current version level.
- Workflow Center at the current version level
cannot connect to a Workflow Server at an earlier
version level (including cumulative fix levels).
- You can import and deploy snapshots from earlier supported product versions to IBM Business Automation
Workflow servers at the current product version
level.
- You can't import or deploy snapshots from Workflow Center at the current version level to IBM Business Automation
Workflow servers from earlier product version levels
(including cumulative fix levels).

## Advanced content and Integration Designer

- To connect to Workflow Center, Integration Designer must meet the Detailed system requirements for a specific product.
- EAR applications originally created on earlier supported versions can continue running on or be
deployed to the current version. Note: You must use version 7.0 or later of WebSphere
Adapters.
- EAR applications that are generated in the current versions of Integration Designer or IBM Business Automation
Workflow are not supported for deployment to earlier
server levels that do not support the same Integration Designer level.
- PI files from earlier supported versions can be imported into the current version of Integration Designer.
- PI files that are created in the currently supported Integration Designer version cannot be imported into earlier Integration Designer versions.

## Related concepts

- Process and process application considerations
- Resource considerations
- Naming considerations for profiles, nodes, servers, hosts, and cells

## Related tasks

- Preparing necessary security authorizations

## Related reference

- Installation directories for the product and profiles