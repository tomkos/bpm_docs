# Disabling updates for user names with trailing blanks

## About this task

If you set the property to
false, Business Automation Workflow discontinues the updates
for the user name with trailing blanks and sets the full name and provider name values to null.
However, the user's associations with applications and their components are maintained and the user
can continue to work with Business Automation Workflow without any other
changes.

## Procedure

- Traditional: To set this property to false in the 100Custom.xml files, complete the following steps:
    1. Stop the servers for Workflow Server or Workflow Center.
    2. Locate and open the appropriate 100Custom.xml files in a text editor.
    3. Add the following code to the files:<common>
    <security>
        <update-user-ignoring-trailing-blanks merge="replace">false</update-user-ignoring-trailing-blanks>
    </security>
</common>
    4. Save your changes to each 100Custom.xml file.
    5. Start the server for Workflow Server or Process Center.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Optional: Customizing Business Automation Workflow
properties.