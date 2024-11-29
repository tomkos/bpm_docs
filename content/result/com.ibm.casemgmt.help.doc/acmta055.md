# Older versions of an audit or security configuration in the Case administration client might not be re-imported

You can use the Case administration client to import an audit or
security configuration that you created on another object store. For example, you might create a
security configuration in your development environment, export that configuration, and then import
that configuration to your production environment.

If you then change the security configuration in your production environment, that newer version
becomes different from the version that you imported from your development environment. However, the
names of the security configurations in both environments remain the same.

If you subsequently decide that you want to roll back the changes that you made to the security
configuration in your production environment and you attempt to re-import the security configuration
from your development environment, the production security configuration is not overwritten. This
result occurs because the security configuration in your development environment has the same file
name as the security configuration in your production environment, but the development version is
older than the production version. The Case administration client
does not overwrite a newer configuration with an older configuration of the same name.

To roll back the changes that you made to the security configuration in your production
environment, first delete the changed configuration from the production environment. Then, export
the security configuration from your development environment and re-import it to your production
environment. The Case administration client does re-import the
security configuration if a newer configuration of the same name does not already exist in the
production environment.