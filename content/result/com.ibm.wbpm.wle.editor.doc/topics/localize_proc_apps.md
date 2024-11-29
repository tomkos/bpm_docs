# Localizing process applications

- Creating localization resources

Localization resources for a process application are contained in localization resource bundles, which are a set of files that define key-value pairs for all the strings that are displayed. For each supported language, a file contains translated values for all of the keys.
- Localizing user interfaces

You can provide localized interfaces for your users by replacing strings for labels and hover help with localization keys. When the user runs the process application, the interface text appears in the language associated with their locale if the translated string is available. Otherwise, the default text that is specified in the resource bundle is used.
- Localizing configuration options for views

You can provide localized configuration options for your coach authors at design time by replacing strings for configuration option labels and hover help with localization keys. Since the predefined configuration options are already set up for localization, localizing your user-defined configuration options results in a more seamless, fully-localized design environment.