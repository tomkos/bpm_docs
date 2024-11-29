<!-- image -->

# Reverse maps

Transforms are reversed where possible:

- Move - remains as Move with inputs and outputs reversed
- Extract - becomes Join
- Join - becomes Extract
- Custom - becomes Custom with no implementation
- Custom Assign - becomes Custom Callout with no implementation
- Custom Callout - becomes Custom Assign with no implementation
- Submap - remains as Submap with inputs and outputs reversed

- Creating a reverse map

You can use the business object map editor to create a new map that is the reverse of an existing one.