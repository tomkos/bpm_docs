<!-- image -->

# Security considerations for runtime installation and deployment

- Only certain roles have the authority to install or deploy on the runtime server. Make sure that
the user who is performing the installation or deployment operation is assigned to the appropriate
administrative security role. See Restricting installation access to runtime servers.
- An application developed in IBM Integration Designer can have its own security
constraints. In order to deploy a secured application, ensure that users and groups have been
assigned to the roles that were defined when the application was constructed. See Deploying secure applications.