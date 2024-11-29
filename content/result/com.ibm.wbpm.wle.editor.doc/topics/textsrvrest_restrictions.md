# OpenAPI support for invoking a REST service

## Unsupported OpenAPI specifications

- Operations of the PATCH or TRACE methods cannot be invoked in IBM® Business Automation Workflow Traditional or on
Containers environments. However, they can be used in IBM Cloud Pak for Business
Automation.
- Properties allOf, oneOf, anyOf, and
not are not supported.
- Type integer with format int64 is not supported. If the value of the integer is
greater than the supported integer number, you will encounter issues. For information about the
range that is supported for the integer type, see Variable types. Note:
If you want to invoke a REST service that returns int64 format integers, you can
use JavaScript to invoke the REST service and then parse the string result that is returned in the
content property of the BPMRESTResponse object.
- OpenAPI v2 input files with $ref properties that reference elements in other
locations than #/definitions/name (for schemas),
#/parameters/name (for parameters),
#/responses/name (for responses) are not supported.
- OpenAPI v3 input files with $ref properties that
reference elements in other locations than
#/components/schemas/name (for schemas),
#/components/parameters/name (for parameters),
#/components/responses/name (for responses),
#/components/requestBodies/name (for request bodies), or
#/components/securitySchemes/name (for security schemes) are not
supported.
- OpenAPI v3 input files with $ref properties that reference properties in schema
objects are not supported unless the type of the referenced property is a primitive data type.
- In OpenAPI v2 input files, header parameters with name Accept,
Content-Type, or Authorization are ignored.
- Paths that contain a semicolon are not supported, even though they are valid in a URI.

## Ignored OpenAPI specifications

- For the HTTP methods GET, HEAD, OPTIONS, and DELETE, any request body is ignored.
- Property default is ignored for all types.
- Properties maxLength and minLength for type string are ignored
for parameters.
- Property multipleOf for types integer and decimal is ignored.
- Property allowEmptyValue is ignored.
- Business object properties maxProperties, minProperties, and
additionalProperties are ignored.
- Business object array properties maxItems and minItems are
ignored.
- Formats email, password and hostname for type
string are ignored.

## Limitations

- Because the maximum name length of business objects is 64 characters, any objects in an OpenAPI
file that have names longer than 64 characters cannot be created one-to-one in the process application. During discovery of an
OpenAPI file that contains such objects, their names are automatically shortened. To find the
original name for such renamed objects, look at the Type name field in the
Advanced Properties section of the Business Object editor.