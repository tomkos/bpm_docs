<!-- image -->

# Considerations when using shared libraries

Take these tips into consideration when you use shared libraries.

Avoid having duplicated assets within the classloader scope which generally is the application
and all shared libraries deployed to a particular scope. When there are duplicates, it can be
unpredictable which one will be used.

- Constrain the use of target namespaces so that they do not exist in both the WebSphere shared
library and the SCA modules that are scoped to the WebSphere® Application
Server shared library.
- Ensure SCA modules don't define, redefine, extend, or restrict artifacts of an existing
namespace that is in a WebSphere shared library.
- Ensure assets in a WebSphere shared library don't define, redefine, extend, or restrict
artifacts that are in the SCA modules that are scoped to it.

For Java binaries, the server runtime environment relies on the inherent class-loading strategies
in the Java virtual machine (JVM), and duplication of Java binaries can result in unpredictable
behavior or a runtime exception. SCA modules exist in their own class loader and delegate to the
class loader for the WebSphere shared library. Therefore, Java binaries that are included in the
WebSphere shared library have preference in loading.

Mediation subflows are normally used over several mediations. Shared libraries do not support
subflows that contain any business object map (BOMap). To share a BOMap across mediations, you must
implement it by using an SCA library that is deployed with the mediation module or SCA module
(shared by copying) or by sharing these artifacts by-reference. For information about sharing these
artifacts by-reference, see Configuring a shared library to support a business object map. For
information about sharing these artifacts by-reference, see Configuring a shared library to support a business object
map.

Business object parsing mode considerations for shared Java Code

If you plan to share Java code across applications running with different business object parsing
modes, you must be aware of incompatible differences between the two business object modes: Eager
and Lazy.

In this case, the shared Java code should be business object mode-agnostic. That is, the code
should be independent of behavior differences between the two business-object parsing modes. If this
separation can't be achieved, the shared Java code can use a published BOMode API to inquire the
actual mode. Depending on the response (Eager parsing or Lazy parsing), a dedicated
code path can be taken, dealing with business object mode-specific behavior.