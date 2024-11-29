# Creating a user attribute definition

## About this task

This procedure triggers dynamic group creation, which can be time consuming. You can use
configuration to deactivate these triggers.

```
Name: skill, type: integer
```

The values for an attribute are maintained using one of the following methods:

- The Process Admin Console (by selecting User management > Bulk User
Attribute Assignment)
- REST APIs (a bulk version of
/rest/bpm/wle/v1/user/a?action=setPreference&key=...&value=...)
- JS APIs

Some customers and business partners have built tools to synchronize user attributes from various
outside sources into the database for use in different contexts. In many instances, only the
predefined attributes are used – especially email address. However, organizations could also
replicate elements from an external registry into the database.

For example, custom portal implementations could use this approach for personalization by storing
user preferences like startPage or preferredLanguage in user attributes.

- server/user-attributes/rest-authorization/public-attribute
- server/user-attributes/rest-authorization/self-manageable-attribute

- Can only see attributes of themselves and other users listed as public-attribute
- Can only see and update own attributes listed as self-manageable-attribute

```
<server>
<user-attributes merge="mergeChildren">
<rest-authorization merge="mergeChildren">
<self-manageable-attribute merge="append">CustomAttribute</self-manageable-attribute>
</rest-authorization>
</user-attributes>
</server>
```

To create a user attribute definition:

## Procedure

1. Open your process application.
2. Click the plus (+) sign next to Data and
select User Attribute Definition from the list
of components.
3. In the New User Attribute Definition window,
provide a unique name for the attribute, and click Finish.
4. Supply the following requested information about the user
attribute definition: 
Table 1.  Input required for the user attribute
definition

Dialog area
Field or link
Description

Common
Name
Displays the name that you provided in step 4.

Documentation
(Optional) Provides a description of the attribute in this
field.

Type
Business Object
Specifies the business object type. The default type is String.
Click Select to choose a different type.

Possible values
Source
Specifies the sources of other possible values for the user
attribute. Select the source from the list, Any valid value,
or List. The choice that you make determines
the information that is required.

If you select Any valid value...
Specifies that the possible values for the attribute are limited
only by its business object type.

If you select List...
Add new values to the list by clicking the + button.
Remove values from the list by clicking the x button.
Change the order of the values that are displayed in the list by clicking
the Up arrow and Down arrow
buttons.
5. Click Save to save the user attribute definition.