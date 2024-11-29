<!-- image -->

# Coexistence considerations

## Offering coexistence
considerations

Some products are designed to coexist and
share function when they are installed in the same package group.
A package group is a location where you can install one or more software
products or packages to share a common user interface or workbench.
When you install each package, you select whether you want to install
the package to an existing package group, or whether you want to create
a new one. IBM Installation
Manager will block products that are not designed to share a package
group or do not meet version tolerance and other requirements. If
you want to install more than one product at a time, the products
must be able to share a package group.

Any number of eligible
products can be installed to a package group. When a product is installed,
its function is shared with all of the other products in the package
group. If you install a development product and a testing product
into one package group, when you start either of the products, you
have both the development and testing functionality available to you
in your user interface. If you add a product with modeling tools,
all of the products in the package group will have the development,
testing, and modeling functionality available.

If you want IBM Integration
Designer
24.0.0.0 to coexist with a Rational® software product (for example, Rational Application
Developer for WebSphere® Software), the Rational software product
must be at version 8.5.x or higher. When you have
an earlier version of the Rational software product you
must correct this incompatibility by updating the version to 8.5.x or higher, or choose a new package group. When
you want to add a Rational software product to the same
package group as IBM Integration
Designer
24.0.0.0, you must install it directly at the required
8.5.x (or higher) level by searching for available
updates during the Rational installation (using
Check for Other Versions and Extensions), or by pointing to the 8.5.x update repository location along with the base
Rational repository location.

## Coexisting
installations of IBM Integration
Designer

You can install IBM Integration
Designer
24.0.0.0 onto a system with an existing installation
of IBM Integration
Designer
24.0.0.0, but the two cannot be part of the same
package group.

Similarly, you can install IBM Integration
Designer
24.0.0.0 onto a system with an earlier installation of
IBM Integration
Designer, but the two cannot be part of the
same package group.