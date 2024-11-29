<!-- image -->

# Considerations when versioning

The considerations listed in this topic help you version
modules and libraries in IBM® Integration
Designer.

- By default, modules and libraries are not versioned. You can change
that default in the Window preferences. From the main menu, select Window > Preferences > Business Integration > Module And Library
Versions and select the IBM Supplied
Version Scheme from the drop-down list. Now the system
will assign version numbers for new libraries and modules.
- The IBM Supplied Version Scheme uses major, minor, and servicenumeric components in the format <major>.<minor>.<service> where An example is 3.1.5 . A change in the majornumber indicates a breaking API change. Other changes should be backwardscompatible.
    - <major> indicates an increment for incompatible changes
    - <minor> indicates an increment for compatible changes
    - <service> indicates an increment for bug fixes
- Dependent projects can have mixed versioned and nonversioned states.
- The following considerations apply when you plan to deploy twoor more versions of the same module in the same run time environment:

- If the module contains business processes, you need to update
the validFrom value.
- If the module contains human tasks, you need to update the validFrom
value. You must also change context root.  For versioned modules,
the context root is always updated during module rename to include
the module version.
- If the module contains business state machines, you need to update
the validFrom value. You must, at times, also change context root.
- If the module contains business rules, you need to rename and
refactor the business rule group component and each rule set or decision
table. For selectors and rules, their repository uses namespace plus
name plus type to create unique keys, for example, //mynamespace +
myBusinessRuleGroup + brg,  or //mynamespace + myDecisionTable + dt.
So, in these cases, you can leave the namespace intact, but you must
change the name of the selector.
- If the module contains selectors, you need to rename and refactor
the selector component. For selectors and rules, their cell-wide repository
at run time uses namespace plus name plus type to create unique keys,
for example, //mynamespace + myselector + selt. So, in these cases,
you can leave the namespace intact, but you must change the name of
the selector.
- If the module contains any non-SCA binding, you need to update
the endpoint to be unique, that is, different from previous versions.
For non-sca bindings, the binding value (address, queue name, and
so on.) is defined, owned, and managed by either the deployment or
administrator role. There is no automated name mangling that occurs
to force these values to be unique for module versions.
- Do not export EAR files for versioned modules. Versioned modules
should be exported for command line service deployment and deployed
using the serviceDeploy command to create a version-aware
EAR file. Versioned modules exported as EAR files are not version-aware.
For that reason, the integration module exporter prevents you from
exporting versioned modules as EAR files.
- In the production environment, deploying a new version of a module
does not replace any previous versions of the module. However, when
testing a versioned module or library in IBM Integration
Designer in
the unit test and component test environments, the module does not
publish to the UTE server as a version-aware module or EAR file. Versioning
is not applied in the UTE environment.