<!-- image -->

# Synchronizing with the software configuration management system

## Before you begin

## About this task

Use the Team Synchronizing perspective to synchronize
the local and remote copies and to identify artifacts that need to
be committed or updated. Synchronize often to check for updates from
other users. Synchronizing is especially important for core artifacts
that may be used in multiple modules, such as libraries with WSDL
and XSD files.

If you try to commit items that have been modified
by other users, you will see a merge conflict. Although there are
merge tools within the Team Synchronizing perspective, these tools
are designed for traditional code such as Java™ and do not work well for XML-based business
process artifacts. Merge conflicts should be handled manually.

You
can only use the commit operation for modules that are already managed
in source control. If you are creating a new module, use the Share
Project window.

## Procedure

To synchronize the workspace module with the remote repository:

1. In the Business Integration view, right-click the module
name and select Team > Synchronize
with Repository.
2. Click Yes to open the Team Synchronizing
perspective. A list of modified artifacts will appear
in the Synchronize view.
3. Optional: Use filters to reduce the list of modified artifacts
that appears in the Synchronize view. By default, all changes
and conflicts appear in the synchronization list. You can change the
filter to show only outgoing changes, incoming changes, or conflicts.
4 Commit, update, or merge conflicts through the Synchronizeview. You can commit all the changes or individual changes. Right-clickthe module or artifact to make these changes. In CVS, adirty flag (>) in your workspace indicates that your local copy differsfrom the copy in the software configuration management system. Ifno differences are listed, no commits or updates are needed. Althoughyou can update or commit before synchronization, that is not a recommendedpractice. The synchronization wizard shows you a full list of changesthat have been made in the local and remote module versions. If youcommit or update these changes without synchronization, then you mightoverwrite critical work from other users. Avoid these problems byalways synchronizing first. Furthermore, when you are working withmodules that may see frequent revisions, synchronize often to verifythat your local working copy is current.
    1. To commit your work to the software configuration management
system, right-click either the module or artifact name and click Commit.
You need to save any changes that you made in the local working
copy to the remote repository before the changes take effect. When
you add a project to the software configuration management system,
an initial commit action saves all artifacts from the local working
copy to the repository.
    2. To update your local working copy, right-click either
the module or artifact name and click Update.
If other users have made changes to a module that you have checked
out, your local working copy is out of sync and needs to be updated.
An update is effectively the polar opposite of commit-instead of pushing
changes from the local workspace to the source control system, an
update loads any changes from the source control system that have
occurred from the time the module was checked out.
    3. Merge conflicts. There are a few options
you have when merging conflicts. For traditional source code, such
as Java, the best and easiest
option is to use the merge utility to assist with integration from
both versions of the code. However, this is not quite practical for
artifacts that you developed in the Integration Designer, because
they are XML-based and are usually very difficult to integrate in
raw-text format. Most often these artifacts are developed using GUI
tools, so performing text-based integration is risky and error-prone.
If a core artifact is improperly merged, the process needed to rectify
problems can be very time consuming and may adversely affect other
artifacts or modules. If you absolutely need to merge Integration
Developer artifacts due to conflict, make sure you keep local copies
of both artifacts in case you need to revert to one or the other.
If at all possible, try to avoid merge conflicts altogether. If you
know that multiple users will be working with a common module or library,
discuss this matter with your team and make certain that only one
person will make changes to an artifact at any given time. You can
also use the Lock and Unlock options in the Team menu to lock read
or write access to specific modules or artifacts.
    4. To prevent multiple users from having write-access to
a module or resource, set a lock on it. From the Business Integration
view, right-click the module and select Team > Lock. Select Lock
recursively and click OK. 
The module is now locked for your exclusive use. You will see
pink lock icons in your workspace. When a module or artifact is locked,
other users can still check out the module, but they will not be able
to commit any changes until after the lock is released. When you no
longer need exclusive access, make sure you unlock the module.
    5. To mark the file as merged, right-click a module or
artifact from the Synchronize view and select Mark as Merged.
The Mark as Merged option allows you to override the conflict
markers by marking the artifact as if it is already merged. Use this
option when you have manually merged the artifact in question and
do not want to use the text-based compare-and-merge utility to merge
conflicts. The merge-conflict indicator will be removed and the artifact
can now be committed or updated, accordingly. Locking only affects
write-access to an artifact. If a module is locked by one user, other
users can still check out a locked module, but they will not be allowed
to commit any changes until the lock is released.