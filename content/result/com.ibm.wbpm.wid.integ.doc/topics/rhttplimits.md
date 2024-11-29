<!-- image -->

# Limitations of the HTTP binding

## HTTPStreamDataBindingBytes data binding

This
data binding requires that a request (and response for a two-way operation)
service data object (SDO) be based on the shipped XML Schema Definition
(XSD). If the SDO is not based on this XSD, an error is issued during
validation. To add this XSD, that is, this business object, to your
module, open the dependencies editor. Under Predefined
Resources, select Native Body schema for Native
Body Datahandler. Save your work and close the dependencies
editor. In the navigation view under Data,
the business object is listed.

## Default content encoding with a POST operation

Default
content encoding assumes an XML format is used. In a POST operation,
this encoding will cause errors. You must specify a non-XML format
such as text/plain.

## Related concepts

- HTTP binding overview
- Uses of the HTTP binding
- HTTP data bindings

## Related tasks

- Generating an HTTP import binding
- Generating an HTTP export binding

## Related reference

- Example of the HTTP binding