<!-- image -->

# Calling static relationships from an inbound map

## About this task

## Procedure

1. Create a map called SAPAddressToAddress (for
example).
2. Create a custom transformation from SAPAddress to Address:This custom transformation will call the static relationship
API.
3. Click Details on the Properties tab. This will show the
Java code window.
4. Call the retrieveInstanceIds API passing in the relationshipName,
roleName and the input business object. A list of instanceIds will
be returned. Note that in this example, this is a one to one relationship,
therefore, there will be only one value in the list.  Also note that
when passing in relationship and role names into the APIs, they must
be prefixed with the namespace. In the example, "http://Test/StateRelationship" and "http://Test/SAPAddressRole" are
used.
5. Set the instanceId value to the state property in output
business object Address.
6. In the outbound map, AddressToClarifyAddress,
use this state value from Address to get the state value for ClarifyAddress.
7. To do this, the piece of custom code above will need the
following imports shown below. Click Java Imports on
the Properties tab: