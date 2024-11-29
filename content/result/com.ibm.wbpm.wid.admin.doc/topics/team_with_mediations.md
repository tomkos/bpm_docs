<!-- image -->

# Team development with mediations

By default, a new mediation flow is saved as a single .medflow
file for all operations. Thus, if you have a flow with five operations,
all logic will exist in a single .medflow file.

You can also choose to save the mediation flow as multiple files.
In that case, you would have a .medflow file for each operation mapping.
Multiple files are useful for collaborative development, because each
developer can work on an operation flow without worrying about conflicts.
Of course, if your mediation flow only uses a single operation, there
is no benefit in enabling the team development option.

- The mediation flow operation mappings must exist in the same module,
whether the team development option is enabled or not. Do not create
a separate module for each operation flow.
- Each user should check out the module from source control. Since
each operation has its own .medflow file, merge conflicts for the
mediation flow logic cannot occur if developers do not work on the
same operation. However, merge conflicts can occur if artifacts that
are not part of the mediation flow are modified by multiple users.