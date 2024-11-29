# Related cases for a particular case resource

| Relationship   | Description                                                   |
|----------------|---------------------------------------------------------------|
| split source   | The related case was created when the current case was split. |
| split target   | The current case was created when the related case was split. |

- GET method for the related cases for a particular case resource

The GET method for the related cases for a particular case resource returns information for each case that is related to a specified case. Related cases include the case that was split to create the current case and any cases that were created by splitting the current case. Results can be filtered by type or category of relationship.