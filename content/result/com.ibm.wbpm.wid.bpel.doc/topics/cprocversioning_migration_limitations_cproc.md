<!-- image -->

# Additional considerations for BPEL process instance migration

- In Integration Designer
- In IBM®
WebSphere® Business Modeler Version
7.0.0.2 or later, and then exported to Integration Designer so that
it can be enabled for process migration

- Compensation logic is not supported in either the source or the
target process versions.
- SQL snippets are not supported in either the source or the target
process versions.
- Correlation sets cannot be added, removed, or modified.
- Custom properties cannot be added, removed, or modified.
- Administration tasks for processes and activities cannot be added,
removed, or modified.
- Variables cannot be removed or modified.
- Partner links cannot be modified.
- Changes to data map activities are not detected. This means that
a process instance will be migrated, even if the current position
of the process navigation is after the modified data map activity.
- Activities can be part of a construct, for example, a loop construct,
fault handler, or a case, and this construct is not contained in a
sequence or flow activity. Activities cannot be added to or removed
from the construct.