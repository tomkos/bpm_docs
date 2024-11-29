<!-- image -->

# Business graphs

Business graphs are available in the runtime to provide supporting metadata to
adapters connecting to back-end systems. Depending on the adapter, a business graph may or may not
be required to indicate to the back-end system what this data represents, or what action should be
taken regarding it.

There are back-end systems which, when they receive a container of data (a business
object) will recognize that it has been received, yet still needs to know what to do with this
container. The business graph provides a verb, such as "Create" or "Delete". For "Create", the
business graph would take a customer business object and create an entry in your database for it.
For "Delete", the business graph would take the customer business object and delete the
corresponding entry from your database as well as change-tracking information. Change-tracking
information basically means, that the business graph recognizes that information was updated as it
passes through an application such as an address change of a customer prompting a new purchase order
being added to the list of previous orders.

- Creating a business graph from an existing business object

A business graph can be created from an existing business object.