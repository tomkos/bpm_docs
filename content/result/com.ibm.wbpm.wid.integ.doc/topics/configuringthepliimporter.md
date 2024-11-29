<!-- image -->

# Configuring the PL/I importer for a PL/I program on an IMS
system

The message prefix style used by PL/I programs can either be LLZZ (4 bytes in all) or LLLL (4
bytes) followed by ZZ (2 bytes). All other IMS programs such as COBOL, C, or C++ use a two-byte LL
field.

To enable IMS support, configure the PL/I importer under IBM® Integration
Designer and
convert the LLLL (4 bytes) field into LL (2 bytes). You must select
the Enable IMS support option when working
with the IMS TM resource adapter, but this selection is optional when
working with WOLA.

When exchanging information between a WOLA external service and
the target PL/I IMS program, you must specify the format for the message
prefix style. For example, if you enabled IMS support for the PL/I
program, use the LLZZ prefix style. However, if you did not enable
the IMS support, you must use the LLLL prefix style with the appropriate
field length so that WOLA correctly parses the message at run time
and delivers it accordingly to IMS OTMA. The IMS Transaction Manager
(TM) ensures that correct LLLL size is used when delivering the message
to the PL/I IMS program.

When creating the WOLA import using the New External
Service wizard, you can set the values for the request
and response prefix styles under the IMS OTMA connection properties
area which is under Advanced.

To configure the PL/I importer, choose one of the following methods:

- When creating the WOLA import in the New External Service wizard,
define the operations in the New Business Object From External
Data  window where you can specify the mapping details
for the business objects that you want to create. Select PL/I
to Business Object and then select a PL/I program, the Select
Data Structures page opens. Under Advanced properties,
set Enable IMS support to true to
use the LLZZ prefix style for the target PL/I program on the IMS system.
This field is false by default.
- Set the mappings for the PL/I importer in the preferences window
in Integration Designer.
To set these preferences, from the menu, select Window  >  Preferences  >  Importer >  PL/I and select Enable
IMS support. This setting enables the LLZZ prefix style
for the target PL/I program on the IMS system.