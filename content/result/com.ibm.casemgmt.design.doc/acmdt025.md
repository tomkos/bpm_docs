# Translating case management applications

## About this task

Figure 1. Default Pages

<!-- image -->

- Predefined or user-created case folders, task instances, comments,
solution name and description, and history entries
- Integrated inbox

When you design and create a solution, you must decide what the solution locale
is. The solution locale refers to the locale of display names, such as case properties, case types,
activities, and other solution artifacts that you create with Case Builder. When you deploy the solution to a target environment
for the first time, you must deploy the solution under the same locale to ensure that the display
names are preserved.

If you use Case Builder to deploy the solution,
change the browser locale.

If you use the Case administration client to
deploy the solution, change the browser locale or change the application language value in the
Change Language and Locale Settings window.

If you use the Case configuration tool
to deploy the solution, change the JVM locale in which the Case configuration tool runs. Edit the
configmgr.ini or configmgr\_cl.ini file in the
ICM\_install\_dir\configure folder and change the
nl value to specify your language locale. The default value is en\_US.

- Translating custom strings

You can add a custom string, such as a page name, a label, or help text, to     a page or a properties view. This custom string is not translated automatically. Instead, you     must use a localized resource file to display the translated string for the custom string in       Case Client.
- Translating solution workflow assets that are stored in Content Platform Engine

You can translate your solution workflow assets that are stored in Content Platform Engine by exporting and translating an XLIFF file that contains the strings for the artifacts.
- Translating content solution assets that are stored in Content Platform Engine

You can translate content assets of your solution, which are stored in Content Platform Engine, by translating the display names of case types, document classes, activities, case properties, and choice list items by using the Administration Console for Content Platform Engine.
- Translating content solution assets that are stored in other repositories

You can search for and add content assets from repositories other than the case management repositories. You can translate these content assets by using the translation instructions for the repository.
- Creating translated form templates for your case management application (deprecated)

To make forms available in different languages to your users, you can create translated versions of the form templates, and then map the translated form templates to different locales in the localization proxy document that is used by your case management application.