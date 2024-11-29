<!-- image -->

# Submaps with <any> and <anyType> elements

| Source                                             | Target is xsd:any   | Target is xsd:anyType   | Target is a regular complex type   |
|----------------------------------------------------|---------------------|-------------------------|------------------------------------|
| xsd:any                                            |                     | Supported               | Supported                          |
| xsd:anyType (complex type in the runtime instance) |                     | Supported               | Supported                          |
| Regular complex type                               |                     | Supported               | Supported                          |

In addition to the submaps for these types as indicated
in the table above, arrays of <any> and <anyType> can
also be submapped.