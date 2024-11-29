<!-- image -->

# Locked activities

In creating BPEL processes a typical workflow involves iterative
development between IBM
WebSphere Business Modeler and IBM Integration
Designer.
A process imported from IBM
WebSphere Business Modeler might
contain activities that are locked. The locking occurs when you export
the process model from WebSphere WebSphere Business
Modeler. You can
see which activities are locked in the canvas by right-clicking and
selecting Highlight all locked items. Locked
activities are highlighted and are displayed with a padlock icon.

In addition to individually locked items there are also pattern
groups. These groups are identified and defined when the transform
from IBM
WebSphere Business Modeler to IBM Integration
Designer is
made. The pattern groups are regions (not necessarily contiguous regions)
of the flow that were artificially created during code export from IBM
WebSphere Business Modeler. The
pattern groups must be maintained in order to guarantee interoperability.
To display the pattern groups right-click in the canvas and select Highlight pattern group > pattern\_group\_name where pattern\_group\_name is the name of one of the identified
pattern groups. All locked activities are part of a pattern group.

- Add new elements (for example, activities or partners) to the
process.
- Modify any unlocked elements in the process.
- Delete any unlocked elements from the process.

In the Properties view of a locked activity you will see the message The element is locked and cannot be modified, where element can be activity, link or gateway. You cannot modify any properties of a locked
element but you can add and remove sticky notes. This feature provides
a communication mechanism between IBM
WebSphere Business Modeler and IBM Integration
Designer developers,
for example an IBM Integration
Designer developers
might use a sticky note to ask a IBM
WebSphere Business Modeler developer
to make a specific change within a locked activity.

It is strongly recommended that you do not unlock activities. Once
an activity is unlocked, and the process is saved, it cannot be locked
again. If you make only minor changes to the unlocked activity you
may find that the process can still be imported into IBM
WebSphere Business Modeler, however
there is no guarantee that this will be the case.

Any new activities you add to your BPEL process will be unlocked.