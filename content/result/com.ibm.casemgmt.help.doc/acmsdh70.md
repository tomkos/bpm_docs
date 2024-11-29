# Property editor settings

- The data type of the property
- Whether the property is single-valued or multivalued
- Whether a choice list is associated with the property
- The type of container in which you place the property

In addition, the editor that you select might have related settings. For example, if
you select Date text box for a DateTime property, the Include time
portion check box is shown in the settings. If you select this check box, the time is
shown in the same text box as the date. When the check box is not selected, the Default
time portion setting is available to change the default time portion of the date field
from 12:00 AM to any other value. If you select Select, Filtering
select, or Radio button set for a Boolean property, the
False when empty check box is shown. If you select this check box, the
property value is set to false if the user does not select a value.

By default, if you select Filtering select, the Filtering
select editor includes an empty value in the choices. Clear the Include empty
choice check box to remove the empty choice.

## Editors for multivalued properties

You define two editors for a multivalued property. The first editor determines the
                editing of the property as a whole. The second editor determines the editing of the
                individual values within the multivalued property.

| Editor               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inline editable list | This option provides for faster entry of property values. The                                     user can press Enter to enter the next value. However, the user                                     cannot edit the value in the list. Instead, the user must delete                                     an incorrect value and then enter the correct value. Values are                                     always added to end of the list. The user can move the value up                                     and down. |
| Editable entry list  | This option provides more flexibility in editing a list. The                                     user can modify values and insert values anywhere in the list.                                     However, it is a bit slower to add values because the user must                                     click the Add                                     button                                     to add each                                     value.                                                                  |

If you add a multivalued property to a Property Table
                container, the first editor is set automatically to be an inline editable list.

You set the editor for the individual values in a multivalued property in the
                    Value Editor Settings area. The editors that are
                available depend on the data type of the property.