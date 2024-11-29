<!-- image -->

# Protocol header propagation from non-SCA export bindings

When the context service propagation is bi-directional, the response context always overwrites
the current context. When you are running an invocation from one SCA component to another, a
response contains a different context. A service component has an incoming context, but when you
invoke another service, the other service overwrites the original outgoing context. The response
context becomes the new context.

When the context service propagation is one way, the original context remains the same.

The lifecycle of the context service is associated with an invocation. A request has associated
context, and the lifecycle of that context is bound to the processing of that particular request.
When that request is finished processing, then the lifecycle of that context ends.

For a short-running Business Process Execution Language (BPEL) process, the
response context overwrites the request context. It takes back the response context from the first
request and pushes it to the next request. For a long-running BPEL process, the response context is
discarded by the BPEL framework. It stores the original context and uses that context when making
other outgoing calls.

Context services have configurable rules and tables that dictate the binding behavior. For more
information, see the Generated API and SPI documentation that is available in the Reference section.
During development in the IBM® Integration
Designer, you can set the context service on
import-export properties. For more details, see the import and export bindings information in the
IBM Integration
Designer documentation.

<!-- image -->