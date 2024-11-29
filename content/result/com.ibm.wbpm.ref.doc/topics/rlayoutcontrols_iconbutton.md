# Icon Button

- The Gantt Chart button in the header of
a details page of an instance
- The Reset and Save buttons
in the header of the Gantt Chart view

## Restrictions and limitations

## Data binding

| Description                               | Data type   |
|-------------------------------------------|-------------|
| Indicates whether the button was clicked. | (Boolean)   |

## Configuration properties

| Configuration property   | Configuration variable           | Description                                                                                                                      |
|--------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Enabled                  | enabled (Boolean)                | Indicates whether the button can be clicked.Default: false                                                                       |
| Error condition          | errorCondition (Boolean)         | Indicates an error condition that disables the button.Default: false                                                             |
| Send error notification  | doErrorConditionAction (Boolean) | Indicates whether notifications are sent when an error occurs. You can bind other coach controls to this property.Default: false |