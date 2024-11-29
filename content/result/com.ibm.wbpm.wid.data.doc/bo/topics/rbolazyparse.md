<!-- image -->

# Considerations when working with business objects in lazy parsing mode

## Considerations

- Business object data is not loaded until it is needed.
- Business objects are accessed by using the Service Data Object (SDO) API.
- To ensure that items in the list are loaded and cached before performing operations on the data
in the list, the SDO API implements the List interface and overrides some methods.