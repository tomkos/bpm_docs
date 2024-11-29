# Integration considerations for ECM products

CMIS-based interactions for workflows are supported with any ECM product implementing the CMIS 1.0 web service interface. A specific ECM
product may not support all optional CMIS capabilities (see the CMIS 1.0 standard for details). As a result, some workflow content
integration steps might not be available for use with a specific product.

Integration considerations, supported CMIS capabilities, and known limitations for selected ECM
products are described in the following topics.

- References to external ECM systems from a BPM folder

When you work with folders in the BPM managed store and add document and folder references to it, communication with the Enterprise Content Management (ECM) system that contains the documents and folders uses the Content Management Interoperability Services (CMIS) standard. The ECM system must support certain operations and capabilities to use all the workflow functions.
- Integration considerations for IBM FileNet Content Manager

When you define the ECM server properties for FileNet® Content Manager, the default CMIS web service context path is "/fncmis".
- Integration considerations for IBM Content Manager

When you define the ECM server properties for IBM® Content Manager, the default CMIS web service context path is "/cmcmis".
- Integration considerations for Alfresco Community

When you define the ECM server properties for an Alfresco Community server, the default CMIS web service context path is "/alfresco/cmisws".
- Integration considerations for Microsoft SharePoint

When you define the ECM server properties for a Microsoft SharePoint server, the default CMIS web service context path is "/\_vti\_bin/cmis/soap".