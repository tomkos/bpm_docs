<!-- image -->

# Rules-based dynamic endpoint selection artifacts

## About this task

- A BPEL process component "<<Service\_Name>>\_SelectionProcess"
- An export for the Service Interface configured with SCA binding
- An import for the Service Interface configured with SCA binding.
- An import for the Decision Service (Rules based) Interface configured
with SCA binding of the Decision Service implementation. •
- WS-Addressing schemas imported as pre-defined resources in the
SCA module are required to consume the evaluated endpoint from the
Decision Service response
- A faultVariable created and used in BPEL for fault management