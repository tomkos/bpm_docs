# Decision service limitations (deprecated)

- You cannot create complex rules that use decision tables and Business
Action Language (BAL) rules in a single rule component.
- You cannot write rules that include behaviors (methods).
- The rule editor does not support rules that include data with
complex (many-to-many) relationships.
- The rule editor does not support the following business objects(variable types):
    - SQLResult
    - XMLDocument
    - XMLElement
    - XMLNodeList

- Decisions that require complex algorithms such as chaining, Rete,
or stateful execution are not supported; only sequential execution
is supported.
- Decisions that reference runtime process instance data cannot be exported for use in IBM® Operational Decision
Manager.
- Multi-channel decisions are not supported.
- Decisions that use methods, custom verbalization and model abstraction
are not supported.