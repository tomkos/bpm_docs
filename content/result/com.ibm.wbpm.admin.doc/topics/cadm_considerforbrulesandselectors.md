<!-- image -->

# Considerations for modules containing business rules and selectors

Business rules and selectors add flexibility to your modules. The
added flexibility affects how you install or delete a module because
the server saves business rules and selectors in a central repository.

## Considerations for changing business rules or selectors

You
can change business rules and selectors in your production environment
without reassembling and reinstalling the affected modules. These
changes are made directly to the repository and are not copied into
any of the files that contain the business rules or the selectors.
After making a change to business rules or selectors, export the business
rules or selectors and import them into your development environment.
If you are unfamiliar with exporting and importing business rules
and selectors, see the topics that describe those tasks.

## Considerations for replacing a module containing business
rules or selectors

When you replace a module that contains
business rules or selectors, the server overwrites the copies of the
business rules and selectors in the repository. When you replace a
module, any changes that you made dynamically are lost. To prevent
that loss, export the business rules and selectors used by the module,
re-import them into your development environment, and rebuild the
module before replacing the module on your production system.

If
you have made changes to the business rules or selectors implemented
by one module, other modules running in the server may need the current
copies of the business rules or selectors. If this is the case, you
will have to configure different repositories so that the updated
module has no effect on the other modules when you install that module
in the server. The topic Configuring the environment describes
configuring the databases.

## Considerations for deleting a module containing business
rules or selectors

When you delete a module that contains
business rules or selectors from the server, the server does not remove
the business rules and selectors from the repository. It keeps these
artifacts because it cannot determine if another application or module
requires the rules.

If you determine that there is no requirement
for a business rule or selector, remove it from the repository. Removing
business rule and selector data from the repository describes
how to clear out unneeded business rules or selectors.

- Removing business rule and selector data from the repository

When you uninstall an application that uses business rules or selectors, the server does not remove these artifacts from the repository. Delete the unused artifacts from the database manually after you uninstall applications that use them. Remove the artifacts using the tools supplied by the database platform of your repository. The reason this is done is that business rules and selectors contain business logic which may have been updated when the application was installed, and we do not want to delete this important business data when the application is removed.

## Related concepts

- Overview of business rules
- Business process rules manager
- Overview of selector components

## Related information

- Business Rules