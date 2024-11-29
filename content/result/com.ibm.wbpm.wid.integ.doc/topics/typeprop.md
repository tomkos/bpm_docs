<!-- image -->

# Type propagation in mediation flows

- Primitives that propagate the input message to the output message
without changing the message type. An example of such a primitive
is the Message Logger. The message types of the all terminals of the
primitive must be the same. If you change the message type of a terminal,
all the other terminals are changed to the same type
- Primitives that allow the message type to be changed as part of
the primitive's function, for example Mapping, Business
Object Map and Database Lookup. For these primitives, the message
type of the input terminal may be different from the message type
of the output terminal.
- Regardless of the type of primitive, the input and fail terminals
must be of the same type. If you change the type of one of these terminals,
the other is changed to the same type

When you drop a primitive onto the editor, the terminals have no
message type. When the terminal is wired, its message type is deduced
by the mediation flow editor. Typically, it takes on the type of the
terminal to which it is wired.

You can also configure a terminal to a specific message type.

- Changing the message type of a mediation primitive terminal

The input and output terminals of mediation primitives in a flow are configured to accept messages of a certain type, based on the validation rules of the mediation flow editor. You can change the input or output message type of a mediation primitive.