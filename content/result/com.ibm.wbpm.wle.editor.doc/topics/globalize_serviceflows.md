# Globalizing service flows

## About this task

A localization resource (also known as a resource bundle) contains a set of identifiers called
property names with a default value for each property name, and the translated values for each
supported language. When you first create a localization resource, typically you define property
names and default values only; the translations are added later.

## Procedure

1 Create localization resources for the service flows:
    1. Open your process application or toolkit.
    2. In the library, click the plus (+) sign next to User
Interface and select Localization Resource.
    3. Provide a name for your new resource bundle and click
Finish.
    4. For each translatable string in your application, enter a translation key and a default value
for that key. The default value is the value that is used if no translation is available.
2. After you have created your localization resources, you can associate them with your service
flows. In the Variables tab of the service flow, click the plus sign next to
Localization Resources, and select a localization resource that you want to
reference. Repeat this process until you have selected all the localization resources that you want
to use.
3 Modify the scripts, including script tasks and pre- and post-scripts of activities to replaceliteral strings with references to the properties from localization resources.

1 For references to localization resources defined in the same process application or toolkit,replace the literal string with the syntax tw.resource.lrname.propname .
    - lrname represents the name of the localization resource.
    - propname represents the name of a property in the localization resource.
2 For references to localization resources defined in a dependent toolkit, replace the literalstring with the syntax tw.resource.toolkit.tkname.lrname.propname . Tip: Use content assist (Ctrl-space) to help you pick the correct reference withouttypos.

- tkname represents the name of a dependent toolkit.
- lrname represents the name of a localization resource in that toolkit.
- propname represents the name of a property in the localization resource.
4 Add translations to the service flows:

1. Export the resource bundle for translation. Click Export to export the
existing set of keys to a .zip file to which you will add the corresponding
translated properties files.
2. You must manually create a new properties file for each language locale that you will translate
your user interface into. For each language that you want your application to support, create a copy
of the exported properties file, renaming it according to the language that it will be supporting.
For example, if your default properties file is my\_application.properties and
you want your application to support Japanese, create a copy of the file called
my\_application\_ja.properties.

Note: Language support also extends to specific countries. For example,
different locale options are provided for English (en\_US, en\_CA), French (fr and fr\_CA), and
Portuguese (pt and pt\_BR). If you add a locale for a language variant, such
as British or Australian English, or Colombian or Mexican
Spanish, you must update the available.locales mashup configuration property
from the WebSphere® Application
Server
administration console. Make sure that you write the values for this property in lowercase, separate
the value elements with a dash (-), and separate the values with commas, as follows:
en-gb,en-au,es-co,es-mxFor more information about
custom properties for Process Portal, see Configuring custom properties.
The file naming scheme follows that of the Java
specification, and is as follows:my\_application\_ll.propertieswhere
ll is the lowercase language code (fr, pt,
en, and so on), or my\_application\_ll\_CC.propertieswhere
ll is the lowercase language code (fr, pt,
en, and so on), and CC is the uppercase country code
(CA, US, BR, and so on).
3. Have each of the files translated into the corresponding languages.
4. To import your resource bundle into your process
application, open the localization resource file
and click Import.
5. Browse to your updated .zip file to select it and
click Finish. 
If you select to overwrite the
values for all existing keys, then for any given language, key values in the imported files that do
not match the existing key values will replace the existing values. Any new keys are added to the
existing set of keys in the existing localization resource.

If there are any missing keys in any of the translated files, warnings are displayed. Click each
of the languages that are flagged with a warning to see which key translations are missing. If you
do not supply translations for these keys, the default value is used in any service flows that
reference this key.