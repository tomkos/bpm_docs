<!-- image -->

# A closer look at business objects from data structures

After using the external service wizard or the external
data wizard, you will have business objects generated. These business
objects typically represent the data structures and variables from
applications on the EIS systems. We will look at the typical type
of business object created and presented in the business object editor
and focus on the type descriptor information you may want to examine
and change. The type descriptor section allows the editing of application-specific
information on business objects. Currently, this feature applies to
C, COBOL and PL/I and is applicable to business objects created from
using the external service wizard on CICS® and IMS systems.

An important point to note is that the business objects created conform to the Enterprise
Metadata Discovery specification. In particular, the business objects contain information described
in the Application Specific Information (ASI) section. It provides a means to describe
application-specific information. Using the business object editor on the business objects created
by using the external service wizard, you can edit the application-specific information.

- Looking at business objects created from the wizards
- Type descriptor information in business objects

## Looking at business objects created
from the wizards

The business objects created by the wizards
are placed in the Data folder of the navigation. Right-click
a business object and from the menu select Open With >
Business Object Editor. The business object editor opens
with the fields and data types of the business object. The structure
and relationship of the business object to other business objects
is shown in the References view.

<!-- image -->

Selecting
a field provides lower level fields of it in the properties view such
as the data type and length of the field, which you can alter.

<!-- image -->

## Type descriptor information in business
objects

When working with business objects created from
discovering EIS systems, one set of fields you might typically change
is the type descriptor fields, which are shown when you select the Application
Info tab. For example, you might want to add a recognition
description. Right-click the appropriate element of the business object
and select Add Child > td:RecognitionDesc.
Type descriptor fields currently apply only to business objects created
from using the external service wizard on CICS and IMS systems.

The td:RecognitionDesc element
is used in applications with multiple possible outputs at run time.

<!-- image -->

Other
type descriptor fields that can be changed in your business object
include code pages and endian characteristics should you change platforms
for example. The values in these fields can be changed by selecting
the field and changing the value beside it.

<!-- image -->

## Related concepts

- Pattern of accessing external services with adapters
- Developing services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports