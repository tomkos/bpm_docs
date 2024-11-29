<!-- image -->

# Outbound calling using WOLA

A REGISTER API call registers the external address space with the WebSphere Application Server for z/OS.
During this call, the external application that runs in CICS or IMS,
or as a batch server indicates the cell, node, and server that the
external application communicates with. The external application also
provides a register name and information about the maximum number
of established connections.

For outbound requests, the external address space applications
must first use one of the native WOLA APIs Host Service or Receive
Request and be identified as target services. On the connection
factory, specify the register name and on the interaction specification,
specify the service name. WebSphere Application Server for z/OS uses
these specifications to call the target service.

Using WOLA, business processes and services on WebSphere Application Server for z/OS can
call CICS or IMS transactions, or batch programs on z/OS.