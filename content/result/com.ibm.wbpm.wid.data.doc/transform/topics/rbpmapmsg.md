<!-- image -->

# XML maps versus business object maps

Although both types of maps perform transformations, there
are functional differences between them. When you use an XML map,
standard XSL is generated and used at run time to perform the data
transformation.  When you use a business object map, you can set the
order of the transforms within the business object map. You can use
the result of one transform as input to another transform, and also
override a transform.

- Mapping of business graphs. For example, you have a business graph
that needs its change summary updated. See Business graphs.
- Custom transformations based on SDO data access.
- Strict ordering of transformation steps, for example:
    - The use of temporary variables as collection points for data.
In this case, the transform or set of transforms that populates the
temporary variable must be executed before the resulting value of
the temporary variable value is moved or transformed into the target
field.
    - A target field needs to be populated first, and the data of that
field is then moved to another field.
    - Move a complex type and then move a field within the complex type.
- If you need to maintain non-static relationships across the mapping,
use a business object map in a business module.
- Static relationships with business object roles.