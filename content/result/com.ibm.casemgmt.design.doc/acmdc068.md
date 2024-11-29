# Preparing customized migration and deployment instructions

## About this task

Ensure that the instructions include the required activities,
their order of execution, configuration details and options, and the
roles that are involved in the processes, including information about
required system privileges. The following types of information are
examples of solution migration and deployment process information
to include.

- To ensure that assets are imported in the correct order during
deployment, you must understand the dependencies between assets. Consult
with your development team and system administrators to develop a
detailed plan for all types of assets that must be exported and imported.
- Although this documentation can be created when the deployment
process begins, it is more efficient and produces a more complete
description if the developers and designers complete the documentation
as part of the development process.

- Name and location of any existing deployment trees and FileNet Deployment
Manager environments with required
export manifests. If deployment trees were not already created, information
about the environment and the FileNet P8 assets
to export is needed to facilitate creation of the FileNet Deployment
Manager environments and export
manifests.
- Name of the project area from which to export the assets that
are managed by FileNet P8.
- If the Include all document versions include
option will not be used, note which assets must be deleted or added
to the manifest each time to ensure that the correct version of the
asset is included in the export. For a description of the export include
options that are typically used for IBM® Business Automation
Workflow solution application
export, see Include options for assets in FileNet Deployment Manager
- Which assets must be deployed before or after the solution is
deployed, and which assets must be deployed before or after other
assets.

- By its type as extracted from the metadata and content in the
deploy dataset. For example, all services of type PESystemAdministration\_F\_WebServer
in the source map are mapped to services of type PESystemAdministration\_F\_WebServer
in the destination map.
- Labeled source services are matched with destination services
that have the same labels and are of the same type. If no destination
services have matching labels, the mapping is done by name.
- Any source services that cannot be mapped to a destination service
are added to the data map as unmapped services.

- System configuration steps to complete before the solution is
deployed, such as establishing a web service.
- Postrequisite steps to complete after the solution is deployed,
such as setting up the printers that are expected to be available
as a part of the operating environment of the case worker.
- Security configuration details
- Audit definition configuration details

- Assets that are not directly managed by IBM Business Automation
Workflow or FileNet P8 tools, such as rules or
custom services.
- Special backup considerations, such as for assets that are managed
in an organization-wide technology such as IBM Operational Decision
Manager.