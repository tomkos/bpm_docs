# Removing the assignedToRole column

## Procedure

To remove the auto column assignedToRole,
complete the                 following steps:

1. In the appropriate 100Custom.xml file,
add the following                     elements to the properties element:
 <server>
      <rest>
          <compatibility-no-auto-column-assigned-to-role merge="replace">{boolean value}</compatibility-no-auto-column-assigned-to-role>
      </rest>
</server>
2. Restart the server.