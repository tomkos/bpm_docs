# Example data flow for case creation

- Retrieval of initial information for a new case

The first step in creating a case is to retrieve the properties that are defined for the case type. As part of this process, the workflow REST API obtains data from the external data service for any properties that the service manages.
- Update of a property that has dependencies

The new case is displayed with the property values that are returned by the workflow REST protocol. The case worker then edits the values as needed. If the case worker changes the value of a property that has dependent properties, another call is made to the external data service to update the values of the dependent properties.
- Creation of the new case

After the case worker enters the data for the case, the final step in creating a case is to add the case to the repository. The external data service is called again to validate the data.