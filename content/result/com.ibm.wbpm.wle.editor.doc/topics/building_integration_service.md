# Building an Integration service in the desktop Process Designer
(deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

To create
services, you must have access to a process application or toolkit
in the Workflow Center repository.
Access to process applications and toolkits is controlled by users
who have administrative rights to the repository. For more information,
see Managing access to the Workflow Center repository.

## About this task

For example, you may want users to choose from a list
of products available from a common site on the internet. In that
case, you can build an Integration service that calls a web service
to display the list of options. Integration services are the only
services that can include Web Service Integration and Java Integration
components as well as content integration. For more information about
inbound and outbound integrations, see Integrating with web services, Java and databases.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Specify a name for the service and click Finish.
IBM Process
Designer displays the
diagram of the service with the default Start Event and End Event components.
4. Select the Variables tab, and add
the variables that your integration service will use as input or output
and also add private variables that the service will use. See Declaring variables for a process or service for information.
5 Select the Diagram tab, and addthe appropriate components to the service and then connect the componentsto create the flow. For information about the componentsthat you can add to the diagram, see Service components in Process Designer .In particular, add one or more of the following components: Tip: You can also use the Invoke UCA component forintegration. See Undercover agents .
    - Web Service Integration component. For information about integrating
web services, see Creating outbound integrations to web services.
    - Java Integration component.
    - Nested service component by dragging an integration service or
other service onto the diagram. This action attaches the service to
the component.
    - Content Integration component. For information about this component
and how to configure it, see Building a service that integrates with an ECM system or a BPM store.
6 Configure the components in the flow. For the integrationcomponents listed in the previous step, configure them so that theyinteract with the external system. In particular, for the Web ServiceIntegration, Java Integration, Content Integration, and nested servicecomponents, map the data used in the task flow to the input and outputfor the component:

1. Click the Data Mapping option
in the properties. Because you already created the input
and output variables for the nested service, the Data Mapping tab
includes these variables.
2 From the Input Mapping section, you can map each variableusing one of the following ways:
    - Use  to suggest mappings. If the automatic mapper
does not find a variable, you can create a private variable for the
mapping.
    - Use  and then
select the appropriate variable.
3. In the Output Mapping section,
do similar mappings for the output variables.
7 If you want the results of the service to be cached forunique combinations of input parameter values, enable and configurethe service result cache.

1. Select the Overview tab, then
in the Service Result Cache section, select Enable
caching of service results. The cache configuration fields
are displayed. Restriction: The
service result cache setting works only for top-level services that
are called directly. If a service is called within another service,
the cache setting does not apply.
2. By default, when caching is enabled, the results for
each combination of input parameter values are kept in the cache for
12 hours. To change the caching period, in the Cache results
for section, use the Days, Hours, Minutes,
and Seconds fields to select the duration that
you want. Important: You might be able to improve
the performance of some services by using the cache, however you must
take care when you decide how long to cache results for, and might
need to tune the size of the cache to avoid memory problems. By default,
the cache stores up to 4096 results. You can change the size of the
cache by setting a different value for <service-result-cache-size> in
the 100Custom.xml file, inside the <server
merge="mergeChildren"> section.
8. If you do not want to automatically synchronize shared business objects that are inputs to this
service when the business object is changed in other instances, switch to
Overview and clear Automatically sync shared business
objects.

Important: Nested services inherit the synchronization behavior of the starting service.
In addition, if you have a service that runs custom logic and then explicitly saves your shared
business objects, always clear the automatic synchronization option. Otherwise, the shared business
object is automatically saved and the code in your service will not run.

## Example