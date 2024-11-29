# Troubleshooting on password match failed for the 'Admin' principal name

After upgrading to Business Automation Workflow, you might be unable to run the
createObjectStoreForContent command and see the following error:

```
CWTDS0001E: The object definition 'The user is not authenticated. Message was: CWWIM4513E The password match failed for the 'Admin' principal name. Root cause:com.ibm.websphere.wim.exception.PasswordCheckFailedException: CWWIM4513E The password match failed for the 'Admin' principal name.' cannot be created. Details: '{1}'
```

OR:

```
After changing the deadmin password (BPM 8.6.0CF2018.03 or BAW:18.0.0.1) you see the above exception.
```

- First, it is important to check whether the password is changed recently. If the password is
changed, the known issue occurs that does not persist the change to the bootstrap user (usually
default is the deadmin) in FileNet (IBM BPM's Document Store). See the technote  Workflow System unable to start after changing password of the
bootstrap user.
- Know whether you are affected: Content Platform Engine 5.5.0 is part of the embedded DocumentStore for the following versions:
    - BPM 8.6.0CF2018.03
    - BAW:18.0.0.1
- If you have changed the passwords or you are upgrading from these versions, it is likely you
would have seen these errors in the logs before the upgrade as well. Functions in the product are
not affected by these errors but do consistently persist in the SystemOut.logs.
You should still be able to work with the Document Store.

Solutions

The issue has been resolved in Business Automation Workflow 18002 and newer versions since the
Document Store uses Content Platform Engine 5.5.2 and higher version. However, follow the steps:

1 A) It is advised to revert the password back for the DeAdmin role to the original password via:
    1. Change the password back in the Manage Users section in the WebSphere Admin Console.
    2. Sync the DeAdmin alias via the updateBPMAliasesAndRunAsRolesPasswords
command. See Changing IBM Business Automation Workflow passwords.
.
2 B) If you do not know the password and are still moving forward with the upgrade, do thefollowing steps:

1. Continue the upgrade and skip the steps to enable the Case Management, see Upgrading to IBM Business Automation Workflow.
2. Enable the ACCE console. If you are using the command line, use
registeracceplugin.xml. See Using the IBM Administration Console for Content Platform Engine.
3. In ACCE, go to the following: Properties > System User Password, and
update the password. The change does not require a restart.
4. Run the storePasswords command. Remove the passwords from the
registertargetenv.xml file before running the command. See storePasswords command.
5. You should now be able to run the createObjectStoreForContent command
successfully.
3 C). If you cannot upgrade or revert, you can temporarily turn off the wim class logging.Eventually, you need to perform A or B above.

1. Turn the wim logging off in the WebSphere Admin Console.
2. *=info: com.ibm.websphere.wim.*=off

For more information, see CWWIM4513E.