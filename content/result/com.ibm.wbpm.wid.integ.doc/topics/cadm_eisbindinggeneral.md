<!-- image -->

# EIS bindings overview

1. The SCA component named ContactSync listens
(by way of an EIS application export named Siebel Contact) for changes
to Siebel contacts.
2. The ContactSync SCA component itself makes
use of an SAP application (through an EIS application import) in order
to update the SAP contact information accordingly.

Figure 1. Flow from a Siebel system to an SAP system

<!-- image -->

The Siebel Contact export and the SAP Contact import have the appropriate
resource adapters configured.