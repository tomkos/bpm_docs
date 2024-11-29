# Restrictions invoking a REST API 3.0 service

## Unsupported OpenAPI specifications

The following OpenAPI specifications are ignored:

- allOf, oneOf, anyOf and not
properties
- OpenAPI 2.0 input files
- OpenAPI 3.0 input files with $ref properties to
#/components/parameters/name for parameters,
#/components/responses/name for responses or
#/components/securitySchemes/name for security schemes
- OpenAPI 3.0 input files with $ref properties that refer to elements in other
locations than #/components/schemas/name for schemas, or
#/components/requestBodies/name for request bodies
- maxLength and minLength properties for type string for
parameters
- multipleOf property for types Integer and Decimal
- allowEmptyValue property
- maxProperties, minProperties, and
additionalProperties business object properties
- maxItems and minItems business object array properties
- email, password, and hostname formats for type String
- OpenAPI sections security, tags, and
externalDocs

Type mappings between OpenAPI and XSD

| <OpenAPI> format   | XSD-type   |
|--------------------|------------|
| number             | decimal    |
| number (double)    | double     |
| number (float)     | float      |
| integer            | integer    |
| integer (int32)    | int        |
| integer (int64)    | long       |
| string             | string     |
| string (byte)      | string     |
| string (binary)    | hexBinary  |
| string (date)      | date       |
| string (date-time) | dateTime   |
| string (password)  | string     |

Default for types without a format element are

- integer -> integer
- number -> decimal
- string -> string

## Supported media types

- application/json
- application/xml
- text/xml
- text/plain

## Composition and Inheritance (Polymorphism)

The element allOf is not supported.

If allOf is detected, a warning message displays and the WSDL artifacts are not
generated for this construct.

```
Dog:
      allOf:
        - $ref: '#/components/schemas/Animal'
        - type: object
          properties:
            breed:
              type: string
```

The following message displays:

```
2021-05-27 16:13:27 WARNING com.ibm.ws.bpm.openapi.discovery.walker.OpenApiWalker walkSchema Construct'allOf'for schema 'Dog'not supported
```

Defined server elements

The following is an example of an OpenAPI definition:

```
servers:
  - url: http://localhost:9080/test
  - url: https://localhost:9080/test
```

```
2021-05-27 16:12:06 WARNING com.ibm.ws.bpm.openapi.discovery.walker.OpenApiWalker walkServers Server element https://localhost:9080/test is ignored
```

Unsupported media type

The following is an example of an unsupported media type OpenAPI definition:

```
requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                name:
                  description: Updated name of the pet
                  type: string
                status:
                  description: Updated status of the pet
                  type: string
```

The following log message displays:

```
2021-05-27 16:15:07 WARNING com.ibm.ws.bpm.openapi.discovery.walker.wsdl.WSDLModel setSupported OperationId 'updatePetWithForm' (operation 'Post\_updatePetWithForm) will be ignored because no supported Media type found in 'requestBody element
```