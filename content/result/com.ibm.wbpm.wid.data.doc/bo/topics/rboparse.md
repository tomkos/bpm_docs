<!-- image -->

# Considerations when choosing the business object parsing mode

The business object parsing mode is set
at the module and library level. Modules that were created in a version
of IBM® Integration
Designer before
version 7 will run in the eager parsing mode without any changes required.
By default, modules and libraries that are created in IBM Integration
Designer version
7 and later versions will be given the most suitable parsing mode
depending on a number of factors such as the parsing mode of existing
projects in your workspace, or the parsing mode of dependent projects
or other projects in the same solution and so on. You can change the
business object parsing mode of a module or library to suit your implementation,
however you should be aware of the following considerations.

- The lazy business object parsing mode processes XML data faster;
however there are compatibility differences between the eager mode
and the lazy mode that you need to be aware of before changing the
configuration of a module or library. These differences will affect
the runtime behavior of the modules. For information on which parsing
mode is optimal for your application, see "Benefits of using lazy
versus eager parsing mode" in the related links.
- A module can only be configured to run in one parsing mode. Libraries
can be configured to support either parsing modes or both parsing
modes. A library that is configured to support both parsing modes
may be referenced by both a module using the eager parsing mode and
a module using the lazy parsing mode. The parsing mode of a library
at run time is determined by the modules that reference the library.
At run time, a module declares its parsing mode, and that parsing
mode is used by the module and any libraries that the module uses.
- Modules and libraries that are configured for different parsingmodes are compatible in the following cases:
    - Modules and libraries configured with the lazy parsing mode are
compatible with libraries that use either the lazy parsing mode, or
both the eager and the lazy parsing modes.
    - Modules and libraries configured with the eager parsing mode
are compatible with libraries that use either the eager parsing mode,
or both the eager and the lazy parsing modes.
    - Libraries configured with the lazy and eager parsing modes are
compatible only with libraries that use both lazy and eager parsing
modes.
- Use the same parsing mode for interacting modules that communicate
using the SCA binding. If modules communicate using different parsing
modes, performance problems may result.

- Benefits of using lazy versus eager parsing mode

Some applications benefit from lazy XML parsing mode, while others see improved performance with eager parsing mode. It is recommended that you benchmark your application in both parsing modes to determine which mode best suites the specific characteristics of your application.
- Considerations when working with business objects in lazy parsing mode

Consider the following behaviors when you work with business objects in lazy parsing mode.
- Application migration and development considerations

If you are configuring an application that was originally developed using eager parsing mode to now use lazy parsing mode, or if you are planning to switch an application between lazy and eager parsing mode, be aware of the differences between modes and the considerations when switching modes.