# WebSphere® eXtreme
Scale:
Retrieve mediation primitive

## Introduction

You can use the eXtreme Scale Retrieve
mediation primitive to retrieve information from a eXtreme Scale cache.
By combining the eXtreme Scale Store
and Retrieve mediation primitives you can cache the response from
a back-end system, which means future requests do not require access
to that back-end system.

The eXtreme Scale Retrieve
mediation primitive has an input terminal (in),
two output terminals (out and notFound),
and a fail terminal (fail) terminal. The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. The out terminal is used
if the key results in information being returned from the cache. In
this case, the information obtained from the cache is stored in the
message and the updated message is propagated. The notFound terminal
is used if the key results in no information being returned by the
cache. In this case, the original message is propagated unchanged.
If an exception occurs during the processing of the input message,
the fail terminal propagates the original message,
together with any exception information.

If no connection to
WebSphere eXtreme Scale can be found, the fail terminal
is fired.

## Details

The eXtreme Scale Retrieve
mediation primitive looks up values in the cache and stores them as
elements in the message using a key.

If the
key is an XSD primitive type, such as xsd:string, xsd:int or xsd:float,
then the corresponding Java object type is used to retrieve from the
cache. If the key is a business object, then this (key) is converted
to an XML String representation (without any namespaces or prefixes)
to look up from the eXtreme Scale cache.

The
information obtained from the cache should be of the same type specified
by the XPath of the data to store the result from the cache property.
If the data type obtained from the cache is assigned to a string then
a string representation of that information will be used, where possible.
If the information obtained from the cache cannot be converted to
the type expected by the message, an exception occurs.

## Usage

You can use the eXtreme Scale Retrieve
mediation primitive to add information to a message, using a key contained
within that message.

By combining the eXtreme Scale Store
and Retrieve mediation primitives you can cache the response from
a back-end system, which means future requests do not require access
to that back-end system.

- WebSphere eXtreme Scale: Retrieve mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)