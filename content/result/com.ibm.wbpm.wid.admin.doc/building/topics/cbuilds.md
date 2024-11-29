<!-- image -->

# Builds in IBM Integration
Designer

In IBM Integration
Designer, the following build activities can substantially increase the duration of a build:

- Validation of large XML schemas or WSDL files in libraries.
- Generation of deploy code for modules.
- Publishing of deploy code to servers.

Fortunately, you can control all of these build activities.

For example, if you have a library that you don't expect to change
and you want to exclude it from clean builds because it contains large
XML schemas or WSDL files that take a long time to validate, you can
accomplish this task in the Properties window for the library.

Similarly, if you do not want to have deploy code generated during
a build or you do not want to have integration modules or component
test projects updated on running servers when a build completes, you
can specify this in the Build Activities view. You can also use the
Build Activities view to invoke immediate manual builds that temporarily
override your build activity selections. Depending on the current
build state of your business integration projects, these manual builds
will validate your projects and generate deploy code, as well as optionally
update or replace your integration modules or component test projects
on running servers when the manual build completes.