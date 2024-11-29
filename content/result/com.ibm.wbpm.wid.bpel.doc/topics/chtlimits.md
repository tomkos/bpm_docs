<!-- image -->

# Limitations for human tasks

- Due to a limitation in the Business Process Choreographer tag
library in IBM® Integration
Designer,
JSPs generated as human task clients will not be able to accomodate
xsd:any, choice and substitution group constructs out of the box.
You will need to use your own custom code using the Service Data Object
(SDO) API in order to work with these constructs. For more information,
see http://www.ibm.com/support/docview.wss?rs=2308&uid=swg21306783.
- It is not possible to map an application containing SCA modules
to a deployment target that has no SCA configured in IBM Workflow
Server.
This causes problems in a golden topology where:
Heritage Process Portal (or
other clients), and SCA modules, are configured on different clusters;
and the web module that contains the generated forms is in the
same application as the BPEL process or human task.

 You need to have the generated forms
in a separate application and not in the same application as the SCA
modules.