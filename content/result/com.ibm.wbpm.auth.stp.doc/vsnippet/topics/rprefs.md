<!-- image -->

# Preferences view: visual snippet editor

Launch the preferences view from the main menu by clicking Window > Preferences > Business Integration > Visual Snippet
Editor.

Use the Generate
snippet Java files to derived folder setting to control
how Java™ files that are generated for visual snippets
are derived to a CVS repository.

By default, the check box
is cleared, and custom visual snippets are generated to ,<module>/<folder>.

If
you select the check box, the files are instead generated to <module>\gen\src\<folder>,
and the derived flag is set. This flag indicates
that these files are derived from other files during a build process,
and so therefore do not need to be kept in a CVS repository because
they can be generated at any time.

## Related reference

- Visual snippets view: visual snippet editor