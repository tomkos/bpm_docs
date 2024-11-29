<!-- image -->

# Security identity qualifier

Location: A security identity qualifier is set on an implementation.

When this qualifier is used, the configured user will be used to run the component overriding the
caller's identity. Otherwise, the caller's identity would be propagated. Roles are associated with
the identity and the roles dictate if the implementation is authorized to invoke other
components.

- By using the SCA deployment descriptor. For more information, see Binding roles defined in assembly diagrams.
- During deployment. For more information, see Assigning users to roles.
- After deployment by following these steps:
    1. Open the application in the administrative console.
    2. Open the Security role to user/group mapping
options for the
application.
    3. Select the role you want to modify and click Map Users.
    4. Select the user you want to set as the RunAs user and click OK.
    5. Click OK to complete the changes. Then save to commit the changes.
    6. Open the User RunAs roles options for the application.
    7. Select the RunAs role, enter the appropriate user name and password, and
then click Apply.
    8. Click OK to complete the changes. Then save to commit the changes.