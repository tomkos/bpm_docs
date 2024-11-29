# Database Lookup mediation primitive

## Introduction

The Database Lookup mediation
primitive can add to, or change, messages. It does this using information
from a user-supplied database.

You configure the Database Lookup
mediation primitive by specifying the database, database table, primary
key column, and database column from which to get information. You
must also specify where, in the input message, to find the value that
is used as the database key.

The Database Lookup mediation primitive
has one input terminal (in), two output terminals
(out and keyNotFound),
and a fail terminal (fail). The in terminal
is wired to accept a message and the other terminals are wired to
propagate a message. The out terminal is used
if the key is located both in the message and the database. In this
case, the information obtained from the database is stored in the
message and the updated message is propagated. The keyNotFound terminal
is used if the key is found in the message, but not in the database.
In this case, the original message is propagated unchanged. If an
exception occurs during the processing of the input message, the fail terminal
propagates the original message, together with any exception information.

## Details

Given a database key, the Database
Lookup mediation primitive looks up values in a database and stores
them as elements in the message.

The information obtained from
the database might need converting before it can be stored in the
message; you can specify the information type using the Type property.
At run time, if the information obtained from the database cannot
be converted to the type expected by the message, an exception occurs.

If
a message element already exists in the message, the old value is
overwritten with the new value.

## Usage

You can use the Database Lookup mediation
primitive to ensure information in a message is up-to-date.

You
can use the Database Lookup mediation primitive to add information
to a message, using a key contained in a message. For example, the
key could be an account number.

It is often useful to combine
the Database Lookup mediation primitive with other mediation primitives.
For example, you might use a Mapping mediation primitive to manipulate
data, before or after the Database Lookup is invoked.

- Database Lookup mediation primitive properties

You can specify values for mediation primitive properties either by using the property fields in the IBM® Integration Designer user interface or by using an XML format. The property field names displayed in IBM Integration Designer are generally different from the property names used when building a mediation flow using XML code. In the following information, icons are used to identify each property name used in IBM Integration Designer and the corresponding XML name. (Where applicable, XML names that are required, but not shown in IBM Integration Designer, are also described.)