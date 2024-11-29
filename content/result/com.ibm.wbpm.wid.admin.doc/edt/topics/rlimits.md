<!-- image -->

# Limitations for the event definition editor

From time to time, you may encounter some limitations in using
the event definition editor. In most situations, you can successfully work
around these limitations.

A known limitation is:

- Refactoring still occurs when you choose not to refactor references

This limitation is discussed in the following section.

## Refactoring still occurs when you choose not to refactor references

In
the event definition editor, you can rename and refactor event definitions
using the Refactor Event Definition Name menu item
and the Rename Artifact window.

If you clear the Update references check
box in the Rename Artifact window, this should prevent any references
to your event definition from being refactored. However, due to a limitation,
any references to your event definition will still be refactored if you clear
the check box.