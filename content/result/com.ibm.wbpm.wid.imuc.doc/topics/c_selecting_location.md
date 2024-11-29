# Package groups and the shared resources directory

When you install the IBM® Integration
Designer package
using IBM Installation Manager,
you must choose a shared resources directory (if IBM Integration
Designer is
the first product to be installed using Installation Manager) and
a package group.

## Package groups

During the
installation process, you must specify a package group for
the IBM Integration
Designer package.
A package group represents a directory in which packages share a common
user interface or workbench with other packages in the same group.
When you install the IBM Integration
Designer package
using Installation Manager, you can create a new package group or
install the packages into an existing package group. Some packages
might not be able to share a package group, in which case the option
to use an existing package group will be disabled.

Note
that when you install multiple packages at the same time, all the
packages are installed into the same package group.

A package
group is assigned a name automatically; however, you choose the installation
directory for the package group.

- Generate a new repository for packages
- Copy packages to a new repository
- Delete packages that are no longer needed.

After
you create the package group by successfully installing a product
package, you cannot change the installation directory. The installation
directory contains files and resources specific to the IBM Integration
Designer package
installed into that package group. Eclipse plug-ins in the product
package that can potentially be used by other package groups are placed
in the shared resources directory.

## Shared resources directory