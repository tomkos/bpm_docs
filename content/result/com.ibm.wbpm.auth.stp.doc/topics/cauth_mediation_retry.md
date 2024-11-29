<!-- image -->

# Mediation flow retries

On the last retry, if a runtime exception is raised and the fail
terminal is wired, the exception flows back to the mediation to be
handled. Otherwise, if the fail terminal is not wired, it goes to
the failed event manager. However, the error handling for store and
forward qualifier takes precedence when you have it configured.

When creating the ServiceInvoke or Callout primitives,
the retry properties are selected by default on the Promotable
Properties tab to be available for administrators to change
the retry properties at run time. If the mediation primitives are
in a subflow, the retry properties are promoted again when the subflow
is added to a mediation flow.

If the Promotable check box for the ServiceInvoke or Callout primitives
is selected, administrators can change those retry properties on the
administrative console. If you do not want to promote the properties
to administrators, clear the Promotable check
box.