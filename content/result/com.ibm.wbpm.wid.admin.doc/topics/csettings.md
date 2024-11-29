<!-- image -->

# Physical Resources view: The .settings folder

When you check out files from a repository, a clean build might
show that these files have changed when, in fact, the content has
stayed the same. For example, this change indicator occurs when a
module contains a BPEL business process or a business object map.
It occurs because the time stamp changes on the org.eclipse.core.resources.prefs
file in the .settings directory during a clean build. There is code
in IBM® Integration
Designer that
ignores the changes to the .settings folder in the data used by the
Build Activities view, but the server marks these changes. This difference
in behavior results in a distinction where a module might show as
"Synchronized" in the Build Activities view but "Republish" in the
Servers view. The Build Activities view is correct; you do not need
to republish.

You can access the .settings folder from the Physical Resources
view. The .settings folder contains properties that are used by IBM Integration
Designer and
should be shared with each project. For that reason, the .settings
folder should be added to team repositories. Some settings made to
this folder will be updated during a clean build. Therefore, running
a clean build on certain projects will cause outgoing changes in this
folder. Changes made to this folder can be safely committed when outgoing
changes are detected.