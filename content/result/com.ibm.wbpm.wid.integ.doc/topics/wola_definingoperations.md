<!-- image -->

# Defining operations for a WOLA service

- COBOL to business object
- C to business object
- PL/I to business object

In the Select Data Structures page of the New
External Service wizard, the properties available are according
to the target platform (z/OS® or
non-z/OS) where the target
program runs. By default for WOLA, the target Platform is
set to z/OS. For a COBOL program, the default properties
are according to the preferences set for the COBOL importer in the
preferences page in IBM® Integration
Designer.
To see these preferences, select Window > Preferences > Importer > COBOL. You can modify the default
properties in the Select Data Structures page.

For CICS programs, you must specify the name of the CICS program
to invoke in the InteractionSpec Service name property
for the selected operation. For batch programs, you must specify the
name of the batch program you want to invoke in the InteractionSpec Service
name property.