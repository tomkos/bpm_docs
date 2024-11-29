<!-- image -->

# Dynamic override of a fixed endpoint

This capability is used when the service is available from a different endpoint than originally
specified when the mediation module was created and deployed.

Dynamic override of a fixed endpoint can be considered if a company is carrying out maintenance
on the fixed service. In this instance, the company does not need to change their entire mediation
flow to accommodate for a back up service. The company must modify the target address in the SMO
header, which is done by registering the Back up Service in WebSphere Service Registry and
Repository (WSRR) and using an Endpoint Lookup mediation primitive to retrieve the Back up Service
target address details.

Figure 1 shows how a message received by this
module would usually be sent to the fixed endpoint for the Internal Service. The SMO can be modified
to override the fixed endpoint and route the message to a Back up Service.

Figure 1. Dynamic override of a fixed endpoint using an Endpoint Lookup mediation primitive

<!-- image -->