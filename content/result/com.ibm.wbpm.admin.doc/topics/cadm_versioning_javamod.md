<!-- image -->

# Versioning considerations for process applications that contain
Java modules and projects

Note that custom Java EE modules and Java projects are deployed
to a server if they are deployed with an SCA module that has a dependency
declared on them. If you do not select Deploy with module (which
is the default) when you declare the dependency, you need to deploy
the module or project manually.