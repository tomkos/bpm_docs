# Particular case instance resource

You can also use the POST method of
this resource to split an existing case to form two cases. For example,
an insurance claim for a car accident might initially be filed as
a single case. After further investigation, you might decide to split
the original case into two cases. The original case tracks the claim
for damage to the car, and the second case covers the claim for injuries.

- GET method for the particular case instance resource

The GET method for the particular case instance resource returns the properties that are defined for a case.
- POST method for the particular case instance resource

The POST method for the particular case instance resource returns information for a specific case. You can call this method to create a new case from an existing case. You can also call this method to return information for a case. If you use an external data service, you can pass client context information in the request to provide contextual information about work items.
- PUT method for the particular case instance resource

The PUT method for the particular case instance resource updates the case properties in the specified case folder with new values. Optionally, the method returns the full list of case properties with the updated values.