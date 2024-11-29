<!-- image -->

# Versioning considerations for process applications that contain business rules and
selectors

The dynamic metadata for a business rule or selector component is defined at run time by the
component name, component target namespace, and component type. If two or more versions of a process
application containing a business rule or selector are deployed to the same runtime environment,
they will share the same rule logic (business rule) or routing (selector) metadata.

To enable each version of the business rule or selector component of the process application to
use its own dynamic metadata (rule logic or routing), refactor the target namespace so that it is
unique for each version of the process application.