<!-- image -->

# Routing Messages Within a Mediation Flow

Figure 1.  Mediation primitive

<!-- image -->

- Messages might leave an out terminal one or more times.
- Messages might leave the fail terminal once.
- Messages might not leave any of the terminals.

## Flow branching

Figure 2.  Branched mediation primitive

<!-- image -->

Figure 2 shows how a mediation primitive can have
multiple wires from one output terminal branching to several services. You cannot specify the order
in which messages will leave the terminal. If you need to send the message through a specific wire
first, then you must use multiple output terminals each with a single wire. You can also select a
mediation primitive that will allow you to control the order in which output terminals are invoked
(for example see Figure 3).

- Example scenarios

This section describes example scenarios that a fictitious company want to implement. It then goes on to discuss the different mediation primitive options that can be used in the implementation.

<!-- image -->