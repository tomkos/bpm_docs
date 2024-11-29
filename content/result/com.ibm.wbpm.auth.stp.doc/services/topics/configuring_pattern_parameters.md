<!-- image -->

# Configuring and mapping pattern parameters

## About this task

You will learn the names and meanings of the pattern parameters,
and how to configure them.

1. Service Interface: This is the interface of the service
that will be exposed to the service consumer.
2. Endpoint Decision Service Interface:  This is the export interface for the endpoint
decision service. Tip:  The decision service implementation will be in a separate module
and can be implemented in IBM® Operational Decision
Manager.
3. Assignments: The Assignments widget helps you map the input
parameters from the service interface to the decision service, and
map the output parameters from decision service to endpoint reference.
The Assignments widget employs a table to map the input parameters
of the service interface to the decision service input parameters.
It allows you to use the request message element from the service
interface to assign one or more attributes to the decision service
input message.

## Procedure

1. Click the Pattern Configuration tab for the pattern
instance that you just created. The Configure
Pattern Parameters page opens.
2 Service Interface : Select the interface of the servicethat will be exposed to the service consumer.
    1 Specify the name and the service interface definitionrequired for pattern implementation. The following artifactswill be generated based on the service name. The Assembly DiagramNames are as follows:
        - <SERVICE\_NAME>\_SelectionExport
        - <SERVICE\_NAME>\_SelectionProcess
        - <SERVICE\_NAME>\_Partner (Target endpoint export )
        - <SERVICE\_NAME>\_EndpointDecisionService
2. Click Browse  to select the interface of the
service that will be exposed to the service consumer. The interface
selection window displays a list of interfaces. Important: The service Interface must exist in a library in
order to be available in the list.
3. Select your Service Interface and click OK.
The selected service interface NameSpace URL displays.
3. Endpoint Decision Service Interface:  Click Browse  to
select the decision service interface export to be invoked. Ensure
that the endpoint decision service is exposed via SCA binding. The
implementation and the dependent library have to be in the active
workspace where the pattern is instantiated.The
SCA Export Selection window displays. Important: The SCA
Export for the decision service must exist in a library in order to
be available in the list.
4. Select your SCA export interface and click OK.
An import for the Decision Service configured with the
Decision Service Transport protocol binding is generated in the Assembly
Editor.Tip: You must ensure that an output parameter has
an attribute of type String to return the endpoint address.
5 Assignments: You can use the Map Input Parameterstable to map the input parameters of the service interface to thedecision service input parameters. Select the appropriate XPaths formapping the Payload data to input request of Endpoint Decision Service.

- Map input parameters table - Left column The first (left)
column allows you to traverse the XPath for input parameter from the
Service interface.
- Map input parameters table - Right column The second (right)
column allows to traverse the XPath for input parameter from the Endpoint
Decision Service.
6. Click the Add button. The Add
Map Input Parameters box displays.
7. Click the Edit button against Service Interface
parameters field. The XPath Expression Builder box
displays
8. In the XPath Expression Builder box type an XPath expression
or click Insert Simple XPath.
9. Select the required attribute and click OK.
10. Repeat the steps for Decision Service Interface Parameters field.
11. Click the Generate button.  A summary of generated artifacts for the Dynamic Endpoint Selection pattern in both
assembly diagram and BPEL formats are displayed for your review.Note: This implementation is
expected to be in a separate module and can be based either on IBM Operational Decision
Manager rules or on WebSphere® Process
Server rules.