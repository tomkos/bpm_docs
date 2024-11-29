# updateBPMConfig command

The updateBPMConfig command is run
using the AdminTask object of the wsadmin scripting client. If you
have multiple versions of the 100Custom.xml file,
such as 101Custom.xml and 102Custom.xml,
only the 100Custom.xml file is updated by the
command. Information about the location of the 100Custom.xml files
and associated configuration files is found in the topic Location of 100Custom configuration files.

## Prerequisites

The following conditions
must be met:

- In a network deployment environment, run the
command on the deployment manager node. In a single-server environment,
run the command on the stand-alone server.
- If the deployment manager or stand-alone server is stopped, use
the wsadmin -conntype none option to run the command
in disconnected mode (which is the recommended mode for this command).
- If the deployment manager or stand-alone server is running, you
must connect with a user ID that has WebSphere Application Server
configurator privileges. Do not use the wsadmin -conntype
none option.

## Location

Start the wsadmin scripting client
from the profile\_root/bin directory.
The updateBPMConfig command does not write to a
log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## Syntax

```
updateBPMConfig
[-de deployment\_environment\_name]
-environmentName environment\_name
-environmentType environment\_type
-create XPath
-update XPath
-delete XPath
-append XPath
-xNodeValue xNode\_value
-xmlPath XML\_file
[-xServerType (PS | PDW)]
```

## Parameters

For examples of how to run
the updateBPMConfig command and its parameters,
see the "Examples" and "Performance tuning examples" sections.

## Examples

Most of the
following examples are related. For instance, the updateBPMConfig -create example
shows how to add an element and the updateBPMConfig -delete example
shows how to remove the same element.

- The following Jython example uses the updateBPMConfig command
and the -environmentName parameter to set the
environment name value for the Workflow Server environment:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-environmentName', 'myEnvironment'])
wsadmin> AdminConfig.save()
- The following Jython example uses the updateBPMConfig command
and the -environmentType parameter to set the
environment type value for the Workflow Server environment:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-environmentType', 'Staging'])
wsadmin> AdminConfig.save()
- The following Jython example uses the updateBPMConfig and
the -create parameter to create an empty element
in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-create', '/common/webservices','-xServerType', 'PDW'])
wsadmin> AdminConfig.save()The empty element that was
created using the above command is shown in bold text in the following
code fragment:<properties>
   <common merge="mergeChildren">
      <webservices></webservices>
   </common>
</properties>
- The following Jython example uses the updateBPMConfig and
the -create parameter to create an element with
content in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-create', '/common/webservices/default-client-timezone', '-xNodeValue', 'GMT-08:00', '-xServerType', 'PDW'])
wsadmin> AdminConfig.save()The element and content that
were created using the above command are shown in bold text in the
following code fragment:<properties>
   <common merge="mergeChildren">
      <webservices>
         <default-client-timezone>GMT-08:00</default-client-timezone>
      </webservices>
   </common>
</properties>
- The following Jython example uses the updateBPMConfig and
the -create parameter to create an attribute
in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-create', '/common/webservices/default-client-timezone/@merge', '-xNodeValue', 'replace', '-xServerType', 'PDW'])
wsadmin> AdminConfig.save()The attribute that was created
using the above command is shown in bold text in the following code
fragment:<properties>
   <common merge="mergeChildren">
      <webservices>
         <default-client-timezone merge="replace">GMT-08:00</default-client-timezone>
      </webservices>
   </common>
</properties>
- The following Jython example uses the updateBPMConfig and
the -update parameter to update the content of
an element in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-update', '/common/webservices/default-client-timezone', '-xNodeValue', 'GMT-05:00', '-xServerType', 'PDW']) 
wsadmin> AdminConfig.save()The element content that was
updated using the above command is shown in bold text in the following
example:<properties>
   <common merge="mergeChildren">
      <webservices>
         <default-client-timezone>GMT-05:00</default-client-timezone>
      </webservices>
   </common>
</properties>
- The following Jython example uses the updateBPMConfig and
the -update parameter to update the content of
an attribute in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-update', '/common/webservices/default-client-timezone/@merge', '-xNodeValue', 'append', '-xServerType', 'PDW'])  
wsadmin> AdminConfig.save()The attribute content that
was updated using the above command is shown in bold text in the following
code fragment:<properties>
   <common merge="mergeChildren">
      <webservices>
         <default-client-timezone merge="append">GMT-08:00</default-client-timezone>
      </webservices>
   </common>
<properties>
- The following Jython example uses the updateBPMConfig and
the -delete parameter to delete an element in
the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-delete', '/common/webservices/default-client-timezone','-xServerType', 'PDW'])
wsadmin> AdminConfig.save()The parent element that contained
the element that was deleted using the above command is shown in bold
text in the following code fragment:<properties>
   <common merge="mergeChildren">
      <webservices></webservices>
   </common>
</properties>
- The following Jython example uses the updateBPMConfig and
the -delete parameter to delete an attribute
in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-delete', '/common/webservices/default-client-timezone/@merge', '-xServerType', 'PDW'])
wsadmin> AdminConfig.save()The element that contained
the attribute that was deleted using the above command is shown in
bold text in the following code fragment:<properties>
   <common merge="mergeChildren">
      <webservices>
         <default-client-timezone>GMT-08:00</default-client-timezone>
      </webservices>
   </common>
<properties>
- The following Jython example uses the updateBPMConfig and
the -append parameter to append the contents
of an XML file to the end of a parent node in the 100Custom.xml file:wsadmin -conntype none -lang jython
wsadmin> AdminTask.updateBPMConfig(['-de', 'De1', '-append', '/common/webservices', '-xmlPath', 'c:\JR50215.xml', '-xServerType', 'PDW'])
wsadmin> AdminConfig.save()The contents of the XML file
that were appended to the end of the parent node using the above command
are shown in bold text in the following code fragment:<properties>
   <common merge="mergeChildren">
      <webservices>
         <callservice-valid-services>
            <valid-service-entry>integration Service</valid-service-entry>
         </callservice-valid-services>
      </webservices> 
   </common>
</properties>

## Performance tuning examples

- The following Jython example shows how to specify the number of
simultaneous tasks that can execute on the BPD queue. The value should
be 10 multiplied by the number of virtual CPUs (10 * #VCPUs), capped
at 80. The initial factory default value is 40.
Additional information is found in the topic Event Manager configuration settings. For the commands in this
example, it is assumed that the <event-manager> element
and its nested <scheduler> elements do not
yet exist in the 100Custom.xml file.wsadmin> AdminTask.updateBPMConfig( [ '-create', '/event-manager' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/event-manager/scheduler' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/event-manager/scheduler/bpd-queue-capacity', '-xNodeValue', '80' ] )
wsadmin> AdminConfig.save()
- The following Jython example shows how to specify the maximum
number of threads for the engine thread pool. The value should be
10 multiplied by the number of virtual CPUs plus 30 (10 * #VCPUs +
30), capped at 80 + 30. The initial factory default value is 70.
Additional information is found in the topic Event Manager configuration settings. For the commands in this
example, it is assumed that the <event-manager> element
and its nested <scheduler> elements already
exist in the 100Custom.xml file.wsadmin> AdminTask.updateBPMConfig( [ '-create', '/event-manager/scheduler/max-thread-pool-size', '-xNodeValue', '110' ] )
wsadmin> AdminConfig.save()