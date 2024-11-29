<!-- image -->

# Business graph model instance

The business graph is composed of more than just the business graph containment object. It also
contains two headers, plus the top-level business object. None of the headers is
represented in memory as a DataObject, and neither of the headers enables a DataObject API access
mechanism.

## Change summary header

A capability provided by business graphs is the ability to implicitly track changes to the
business object in the business graph as the business graph is passed between several different
business processes. As each process changes the business graph, a change log is generated in memory.
Once the business graph is serialized, the change log is written out in a format that enables the
next process to see the types of changes that have been made to the business graph. This technique
enables adapter and Data Mediator services to efficiently update their persistence data stores by
optimizing the data they have to focus on.

In addition, the change summary is also used when an adapter generates an After Image event to
describe data that was updated in an EIS system. In particular, the ability of the change summary to
annotate object and property changes is used in the After Image use model (as well as the verb for
the business graph).

## Implicit change summary usage

When applications cause changes to the business object, the applications can turn on change
logging so change events are automatically logged to the change summary. The change summary is
included in the business graph at a peer level of the top-level business object. Change events are
defined at two levels, for business objects, and for business object properties. Business objects
have create, update, and delete change types, while properties have set and unset change types.
Change events are only tracked for modifications to the business object portion of the business
graph. A change in the event summary does not result in an implicit update of the change summary for
the business graph.

## Explicit change summary modification

There are several use models in the IBM® Business Automation Workflow components that require the ability to explicitly write to the change summary header. For
example, an adapter that generates an EIS event explicitly creates the object change types, and
potentially the property change types. An application-specific business object/general business
object (ASBO/GBO) map transforms the change summary from one business graph to another, creating a
new version of the change summary in an output business graph. This capability is provided by the
business object framework.

## Event summary header

The event summary provides the ObjectEventID, which is the mechanism used to
uniquely identify an instance of an object that appears in the runtime. This information is carried
in the event summary, where the unique identifier is associated with a given DataObject in the
business object hierarchy of the business graph.

Event information can also be carried in the event summary. This information is a string that can
be used to add additional metadata associated with each object in the business object hierarchy for
the business graph. One potential use model for event information is to mark up contained business
objects with a verb other than the standard Create, Update, and Delete verbs supported by change
summary.

## Verb header

- The change summary is empty. This situation occurs when an EIS knows about the type of update to
a set of data, but does not have specifics on which objects in the graph have been created, updated,
or deleted. The result is that a downstream mediation, map, relationship, or adapter, must use the
information in the business graph plus additional data to determine the actual update to
perform.
- The change summary has object level change event annotations. This case is typical where the EIS
system recognizes what has happened to each object in the business graph, but lacks the granularity
to determine whether specific properties of the objects have been updated.
- The change summary has object level change event annotations and property level get/set
annotations. This situation is the most granular case, and all adapters strive to obtain this level
of an After Image if their EIS system makes the appropriate data available. The advantage of a fully
specified After Image is that it enables property level implicit property change event management to
occur. Therefore, it much easier for After Image business graphs to interoperate with the
disconnected Delta-based Business Graphs.