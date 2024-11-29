# Your LDAP account is locked after the password is changed

When a process app or toolkit is imported from Workflow Center into Integration Designer, the Workflow Center URL and the user name is stored in the
project settings in the Integration Designer workspace. The
password can also be saved in Eclipse secure storage. When the Integration Designer workspace is open, continuous checks determine
whether Workflow Center is connected so it can
display the status in the Business Integration view. If the password is not correct for the
project's user name setting, you might still be locked out although you provided new credentials
when prompted.

This issue likely occurs because process apps or toolkits are in the Integration Designer workspace. Therefore, to avoid this problem, keep
Advanced Integration services (AISs) in stand-alone modules, as described in Implementing an Advanced Integration service. After the AI service is implemented and the library project is
copied, you can remove the toolkit from the Integration Designer workspace, as described in Develop Advanced Integration services.

1. Publish any changes to Workflow Center and
delete the process app and toolkit projects from the Integration Designer workspace.
2. In Window > Preferences > Business Integration > Workflow Center, clear the Password field.
3. After the password has been changed, restart Integration Designer.
4. Switch to Workflow Center and enter the new
password when prompted.
5. Import any process apps or toolkits that were deleted.

1. Shut down Integration Designer.
2. Open Integration Designer with a new temporary workspace
that will be used only to clear the secure storage.
3. In Window > Preferences > General > Security > Secure Storage, select the Contents tab, select Default Secure
Storage and then click Delete.
4. Restart the Integration Designer workbench when prompted
and open the original workspace. You will be prompted to enter the credentials. Note: You might have
to switch to Workflow Center and restart Integration Designer before each project status shows as connected. If
any other Eclipse application is using secure storage, the passwords will be removed.