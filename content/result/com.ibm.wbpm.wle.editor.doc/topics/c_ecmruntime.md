# Runtime behavior for inbound content events

- Event source ID
- Object type ID
- Event type

- Tip (Workflow Center)
- Default snapshot (Workflow Server)

Each event subscription has an attached service that must include the ECMContentEvent business
object as an input parameter. When an event subscription is triggered, the attached service is
started asynchronously and an instance of the ECMContentEvent business object is created. The
running service may invoke the undercover agent (UCA) that is attached to the Start Content Event or
the Intermediate Content Event that is defined in the business process definition (BPD).