# Split Case Properties widget outgoing events

## Cell added event

| Description   | A new cell was added to a property table in the view.                                                                                                                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellAdded                                                                                                                                                                                                                                                                                                                                                                      |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                          |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was added. property A pvr.widget.Property object that represents the property that is associated with the new cell. row The row index of the new cell. error A single value string or array that represents the error message of the new cell. value The value of the new cell. |

## Cell changed event

| Description   | The value of a property table cell in the view was changed.                                                                                                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellChanged                                                                                                                                                                                                                                                                                                                                                                                            |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                                  |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell value was changed. property A pvr.widget.Property object that represents the property that is associated with the updated cell. row The row index of the updated cell. error A single value string or array that represents the error message of the updated cell. value The updated value of the cell. |

## Cell clicked event

| Description   | A cell was clicked within a property table in the view.                                                                                                                                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellClicked                                                                                                                                                                                                                                                                                                                                                                                      |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                            |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was clicked. property A pvr.widget.Property object that represents the property that is associated with the clicked cell. row The row index of the clicked cell. value The value of the clicked cell. error A single value string or array that represents the error message of the clicked cell. |

## Cell double clicked event

| Description   | A cell was double clicked within a property table in the view.                                                                                                                                                                                                                                                                                                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellDoubleClicked                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was double-clicked. property A pvr.widget.Property object that represents the property that is associated with the double-clicked cell. row The row index of the double-clicked cell. value The value of the double-clicked cell. error A single value string or array that represents the error message of the double-clicked cell. |

## Cell inserted event

| Description   | A new cell was inserted into a property table in the view.                                                                                                                                                                                                                                                                                                                                                |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellInserted                                                                                                                                                                                                                                                                                                                                                                                          |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                                 |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was inserted. property A pvr.widget.Property object that represents the property that is associated with the inserted cell. row The row index of the inserted cell. error A single value string or array that represents the error message of the inserted cell. value The value of the inserted cell. |

## Cell moved event

| Description   | A cell was moved within a property table in the view.                                                                                                                                                                                                                                                                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellMoved                                                                                                                                                                                                                                                                                                                                                                                  |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                      |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was moved. property A pvr.widget.Property object that represents the property that is associated with the moved cell. row The new row index of the moved cell. error A single value string or array that represents the error message of the moved cell. value The value of the moved cell. |

## Cell removed event

| Description   | A cell was removed from a property table in the view.                                                                                                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellRemoved                                                                                                                                                                                                                                                                                                                                                                                      |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                            |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was removed. property A pvr.widget.Property object that represents the property that is associated with the removed cell. row The row index of the removed cell. error A single value string or array that represents the error message of the removed cell. value The value of the removed cell. |

## Cell updated event

| Description   | The cell in the property table in the view was updated.                                                                                                                                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.CellUpdated                                                                                                                                                                                                                                                                                                                                                                                      |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                            |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a cell was updated. property A pvr.widget.Property object that represents the property that is associated with the updated cell. row The row index of the updated cell. error A single value string or array that represents the error message of the updated cell. value The updated value of the cell. |

## Field updated event

| Description   | The value of a field was updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.FieldUpdated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Payload       | changes A JSON object that contains the unique identifier and value for the property that was modified. The structure is:change:[   {   id: prop1,   value: value1   } ] The collectionId value identifies the type of properties that were updated. This parameter will have one of the following values. F\_CaseFolder Indicates that this is a case property. F\_CaseTask Indicates that this is a task property. F\_WorkflowField Indicates that this is a work group or workflow data field.   The data type of the value corresponds to the data type of the property, or is null. For properties that support multiple values, the value is an array of the corresponding data type. |

## Field focused event

| Description   | The field got focus for user input.                                                          |
|---------------|----------------------------------------------------------------------------------------------|
| Event ID      | icm.FieldFocused                                                                             |
| Type          | Broadcast                                                                                    |
| Payload       | id A string that contains the identifier of the property with which the field is associated. |

## Field blurred event

| Description   | The field lost focus for user input.                                                         |
|---------------|----------------------------------------------------------------------------------------------|
| Event ID      | icm.FieldBlurred                                                                             |
| Type          | Broadcast                                                                                    |
| Payload       | id A string that contains the identifier of the property with which the field is associated. |

## Property updated event

| Description   | The value of a property in the view was updated.                                                                                                                                                                                                                                                                                                                                                      |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.PropertyUpdated                                                                                                                                                                                                                                                                                                                                                                                   |
| Type          | Broadcast                                                                                                                                                                                                                                                                                                                                                                                             |
| Payload       | property A pvr.widget.Property object that represents the property whose value was updated.  value The updated value of the property. The data type of the value corresponds to the data type of the property, or is null. For properties that support multiple values, the value is an array of the corresponding data type. error A single value string or array that represents the error message. |

## Row added event

| Description   | A new row was added to a property table in the view.                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowAdded                                                                                                                               |
| Type          | Broadcast                                                                                                                                  |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was added. row The index of the new row. |

## Row changed event

| Description   | A row was changed within a property table in the view.                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowChanged                                                                                                                                   |
| Type          | Broadcast                                                                                                                                        |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was changed. row The index of the changed row. |

## Row clicked event

| Description   | A row was clicked within a property table in the view.                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowClicked                                                                                                                                   |
| Type          | Broadcast                                                                                                                                        |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was clicked. row The index of the clicked row. |

## Row double clicked event

| Description   | A row was double clicked within a property table in the view.                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowDoubleClicked                                                                                                                                           |
| Type          | Broadcast                                                                                                                                                      |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was double-clicked. row The index of the double-clicked row. |

## Row inserted event

| Description   | A new row was inserted into a property table in the view.                                                                                          |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowInserted                                                                                                                                    |
| Type          | Broadcast                                                                                                                                          |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was inserted. row The index of the inserted row. |

## Row moved event

| Description   | A row was moved within a property table in the view.                                                                                             |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowMoved                                                                                                                                     |
| Type          | Broadcast                                                                                                                                        |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was moved. row The new index of the moved row. |

## Row removed event

| Description   | A row was removed from a property table in the view.                                                                                             |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowRemoved                                                                                                                                   |
| Type          | Broadcast                                                                                                                                        |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was removed. row The index of the removed row. |

## Row selected event

| Description   | The row selection changed in a property table in the view.                                                                                         |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowSelected                                                                                                                                    |
| Type          | Broadcast                                                                                                                                          |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was selected. row The index of the selected row. |

## Row updated event

| Description   | A row was updated within a property table in the view.                                                                                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Event ID      | icm.RowUpdated                                                                                                                                   |
| Type          | Broadcast                                                                                                                                        |
| Payload       | propertyTable A pvr.widget.PropertyTable object that represents the property table in which a row was updated. row The index of the updated row. |