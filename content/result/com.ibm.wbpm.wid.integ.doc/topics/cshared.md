<!-- image -->

# Shared context

The shared context area of the message is the point of aggregation. Much
like the transient and correlation context, shared context is a user-provided
business object that is set at the input node of a mediation flow. The shared
context is where data is placed in a mediation flow for Fan In
primitives to access during an aggregation.

Use shared context for Fan Out and Fan In aggregation and not for general
data storage during a mediation flow. Use transient or correlation context
for general data storage during a mediation flow.