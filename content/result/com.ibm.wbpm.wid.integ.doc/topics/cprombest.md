<!-- image -->

# Tips for deciding which properties to promote

For example, you might want to promote the validate input property,
which enables message validation. A message validation ensures that
the message type at run time matches the message type definition.
Because message validation can negatively impact performance, it is
a good idea to disable the property; and promote it so that you can
enable message validation at run time if you are trying to debug a
problem and want to see if the message type is valid.

When you create ServiceInvoke and Callout mediation primitives,
the retry properties (Retry on, Retry count and Retry delay) are automatically
selected to be promoted.