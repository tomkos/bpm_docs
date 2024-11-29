# Subflow mediation primitive

## Introduction

Use mediation subflows to reuse
common patterns in mediation flows, and also as a way to group primitives
in the Mediation Flow editor.

A mediation subflow can be created
in a module, mediation module, or library. A mediation subflow must
be used within a mediation flow. It is good practice to store subflows
in libraries so that they can be easily shared between mediation flows
in different modules.

A mediation subflow has one or more in nodes,
one or more mediation primitives, and one more out nodes.
The in and out nodes
become the input and output terminals
on the subflow mediation primitive.

Unlike mediation flows,
the inputs and outputs of a subflow are not tied to specific interfaces.
Instead, the in and out nodes represent the inputs and outputs of
the subflow. In a wired mediation flow, these nodes have message types
associated with them. The message types on these nodes are not defined
when the subflow is created; they can be changed later.

## Details

Promoting the property of a mediation
primitive in a mediation flow allows an administrator to change the
value of the property at run time. When you promote a property in
a subflow, it becomes a property of the subflow mediation primitive.
You can then set the value of the property in the mediation flow,
or further promote the property in the parent mediation flow.  You
might want to set the value of the property in the mediation flow
at development time. If you reuse the same subflow in multiple places
in a flow, you might not want to use the same alias name for the property
depending on the behavior you want to see.

For mediation primitives
contained in a subflow, promoting a property results in the creation
of a corresponding property on each subflow mediation primitive that
refers to that subflow. The property can then be promoted again until
eventually it reaches the top level request, response, or fault flow.

Any
property that you promote from a primitive in the top level request,
response, or fault flow is also a dynamic property. A dynamic property
can be overridden, at run time, using a mediation policy. Although
you can override promoted properties dynamically, you must always
specify a valid default value.

Promoted properties have an alias
name which, for a mediation primitive in the top level request, response,
or fault flow, is the name displayed on the runtime administrative
console. For a mediation primitive in a subflow, the alias name is
the name by which the property is known in the parent flow. You can
set the alias name and the alias value from WebSphere Integration
Developer. Multiple promoted properties can be given the same alias
name if they are of the same type. In one module or mediation module,
promoted properties that have the same alias name and group use the
same value. Generally, you should choose a suitable alias name for
your promoted properties rather than accept the default name: choosing
a suitable name helps you identify properties at run time.

## Usage

You can reuse mediation logic for
common tasks by creating mediation subflows. A mediation subflow can
be invoked from multiple mediation flows, or multiple times within
the same mediation flow. A mediation subflow is invoked from a parent
mediation flow using a subflow mediation primitive.

- Subflow mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)