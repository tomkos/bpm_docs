<!-- image -->

# Versioning in service applications

## What can be versioned?

Libraries can also be versioned. Modules that use a library have a dependency on a specific
version of that library, and libraries can also have dependencies on specific versions of other
libraries.

## Considerations for deploying versioned modules

- Installing a versioned module to a server or cluster in a cell
- Installing the same version of a module once to each of one or more servers or clusters in a
cell
- Installing different versions of a module on the same server or cluster

Deploying a new version of a module does not replace any previous versions of the module.
Previous versions of cell-scoped application artifacts are overwritten.

If you want to update an application (for example, to make minor corrections or improvements)
without changing the version, that updated application and its artifacts will replace the existing
application and artifacts, with the exception of any defined security policies. All security policy
artifacts are preserved during an application update.

```
moduleName\_vversionValue\_uniqueCellID
```

## Considerations for binding versioned modules

- Static binding: If you are using static binding, use the existing administrative tools to bind a
versioned module to a client. You must specify the module version number in the static binding.
- Dynamic binding: To use dynamic binding with versioned modules, use a mediation flow component
that contains the module version metadata (versionValue and versionProvider) and
service-version-aware routing. Note that in order to use service-version-aware routing to
dynamically bind versioned modules, all modules must be registered with WebSphere® Service Registry and Repository (WSRR).