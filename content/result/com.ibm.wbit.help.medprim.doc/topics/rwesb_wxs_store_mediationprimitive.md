# WebSphere® eXtreme
Scale:
Store mediation primitive

## Introduction

You can use the eXtreme Scale Store
mediation primitive to store information within a message in a eXtreme Scale cache.

The eXtreme Scale Store
mediation primitive has an input terminal (in),
an output terminal (out), and a fail terminal
(fail) terminal. The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. If an exception occurs during the processing
of the input message, the fail terminal propagates
the original message, together with any exception information.

The in terminal
accepts an input message and stores a key and value that is normally
contained within the message within the eXtreme Scale cache.
The input message is then propagated from the output (out)
terminal.

If the connection to the eXtreme Scale cache
is unavailable, the fail terminal is fired.

## Details

The eXtreme Scale Store
mediation primitive stores information in a eXtreme Scale cache
using a key and an object. The key can be an XSD primitive type or
a business object. If the key is an XSD primitive type, such as xsd:string, xsd:int or xsd:float,
then the corresponding Java object type is used to store into the
cache. If the key is a business object, then the key is converted
to an XML String representation (without any namespaces or prefixes).
The Time to live field can be used to store
the information for a set amount of time (specified in seconds).

## Usage

It is often useful to combine the eXtreme Scale Store
mediation primitive with other mediation primitives. For example,
you might use the eXtreme Scale Retrieve
mediation primitive to retrieve data, after the eXtreme Scale Store
mediation primitive is used to store data previously within the cache.

If
the key is already contained within the eXtreme Scale cache,
the old value is overwritten with the new value.

- WebSphere eXtreme Scale: Store mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)