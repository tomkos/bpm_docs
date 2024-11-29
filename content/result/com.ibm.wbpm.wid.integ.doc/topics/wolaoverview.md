<!-- image -->

# WOLA resource adapter

From the New External Service wizard, you can use WOLA to create services
that can make outbound calls from IBM Workflow
Server
to programs that run in an external address space on the same z/OS system.

<!-- image -->

WOLA provides high-performance interactions between WebSphere for z/OS and the COBOL, PL/I, C,
and C++ applications in external address spaces that run on the same z/OS system. These interactions are achieved by using the shared memory
between the processes and applications. Use WOLA developer proxy environment to access CICS, IMS, or Batch programs
that are local to your Workflow Server.

## Developing a WOLA import

Using an import, Workflow Server invokes a service
that is external to a business or mediation module. Using a WOLA import, Workflow Server invokes a local CICS, IMS, or Batch program through the WOLA proxy to a
WebSphere server that runs on a remote z/OS server. The remote z/OS WebSphere server forwards that
request to an external address space running the same z/OS server by using one of the native
Host Service or Receive Request WOLA APIs.

Using the New External Service wizard
in IBM Integration
Designer,
you can generate a WOLA import. You must specify information such
as the resource adapter to be used, security and connection  properties,
operations with input and output types and interaction properties,
and the name and location for WOLA import service.

## Using WOLA at run time

A WOLA import is created in an Integration Designer
module. At run time, the local Workflow Server uses the
import and the WOLA proxy to invoke the local COBOL, PL/I, C, and C++ program on the remote z/OS
server. The resulting response data is returned.

<!-- image -->