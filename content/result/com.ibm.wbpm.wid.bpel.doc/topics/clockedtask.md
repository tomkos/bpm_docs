<!-- image -->

# Locked tasks

In creating BPEL processes a typical workflow involves iterative
development between IBM
WebSphere Business Modeler and IBM Integration
Designer.
When you import a process from IBM
WebSphere Business Modeler that
contains human tasks some of the properties of those tasks will be
locked. Locked properties are displayed with a padlock icon.

You can modify unlocked properties and still maintain interoperability
with IBM
WebSphere Business Modeler.

When you select a locked property, in the Properties view you will
see the message The property\_type property is
currently locked because the human task was created in IBM
WebSphere Business Modeler,
where property\_type is the locked property that
you have selected. You cannot modify a locked property.

It is strongly recommended that you do not unlock properties. Once
a property is unlocked, and the task is saved, the property cannot
be locked again.

Provided that you do not modify locked properties, when you Synchronize
with Modeler Export (to update the task with new changes
made in IBM
WebSphere Business Modeler),
you will find that there are no conflicting changes. See the related
topic Synchronizing human tasks in iterative development for
more details on synchronizing.