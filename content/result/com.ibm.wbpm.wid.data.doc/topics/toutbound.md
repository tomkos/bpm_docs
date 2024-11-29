<!-- image -->

# Calling static relationships in an outbound map

## About this task

## Procedure

1. Create a map AddressToClarifyAddress.
2. Create a custom transformation between Address and ClarifyAddress:
3. Click Details on the Properties tab:
4. Add the code shown above to the Java code section. This code will
call the retrieveParticipants API of the relationship service. This API will
return a List of ClarifyAddress business objects. Note that in this example,
this is a one to one relationship, therefore, there will be only one ClarifyAddress
business object in the list.
5. Get the value of "state" from the ClarifyAddress business object
returned from the relationship call.
6. Set the "state" value in ClarifyAddress business object that is
the output of the map.