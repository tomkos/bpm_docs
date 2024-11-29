<!-- image -->

# Testing XML maps

## About this task

To
test an XML map:

## Procedure

1 Invoke the test client in one of the following ways: The test client uses an Invoke XML Map Event totest the map. Note that only map files that reside in mediation modulescan be tested using the integration test client. If the map file isin a library, you cannot use the test client to test it. To test mapfiles that are in libraries, see the topic "Testing maps during iterativedevelopment".
    - In the Business Integration view, right-click the map that
you want to test and select Test.
    - In the mediation flow editor, right-click the Mapping
primitive that is associated with the map and select Test
XML Map. The integration test client opens.
2. If you want to test a different map, select it from the Map
File list. To open the selected map in the XML map editor,
click the Map File link.
3. If you want to pause the test and open the Debug perspective
before any transformations are performed, select the Stop
for debug before transformations check box. If you have
any local breakpoints set in the XML map, the Debug perspective opens
automatically.
4 Choose whether you want to use the default values or asample input file already associated with the XML map in the InitialInput Selection section.

- When you select Generate default input values,
previously specified or modified values in the value editor are erased
and replaced with default values that are created based on the XSD
for the input element. You can update these values and, if you want
to reuse the values, export them to an XML file or save them to the
data pool.
- For information on creating your own sample input files and
associating them with XML maps, see the topic "Using a sample input
file to test XML maps".
5. Click Continue to run the test and
generate output XML based on the input values and the mappings.
6. Select the Completed XML Map Event to
see the result of the mapping. To see the XML source, click the XML
Source tab, as shown in the following figure:
7. If you want to save the output of the transformation, right-click
the root element in the value editor and select Export
to XML file. You can also copy the XML source from the XML
Source tab.