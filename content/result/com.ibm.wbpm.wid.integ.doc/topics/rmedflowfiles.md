<!-- image -->

# Considerations for team development of mediation flows

Important:
Always synchronize at the project level, so that you can see the .mfcflow
files of added and deleted operations.

1. In the Physical Resources view, select the mediation flow project,
and synchronize.
2. Update new, changed or deleted file from the repository.
3. Make changes to your mediation flow.
4. Synchronize the mediation flow project.
5. You may now see changes that other developers may have made, in
addition to your local changes
6. Accept changes from the repository, and commit your own changes.

- Adding, deleting, or changing source interfaces, source operations,
target interfaces or target operations results in changes to the .mfc
file, which is shared among all the developers of the mediation flow.
- When a source operation is deleted, the corresponding .mfcflow
file is also deleted. However, you will not know that the operation
has been deleted unless you synchronize at the project level.
- Promoting properties results in changes to the common .mfc file.
- Adding, deleting or editing sticky notes results in changes to
the common .mfcflow file.