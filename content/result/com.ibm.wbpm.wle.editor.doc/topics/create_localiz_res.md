# Creating localization resources

## About this task

## Procedure

1. Open your process application or toolkit.
2. In the library, click the plus (+) sign next to User
Interface and select Localization Resource.
3. Provide a name for your new resource bundle and click
Finish.
4. For each translatable string in your process
application, enter a translation key and a default
value for that key. The default value is the value that is displayed if no translation is
available.
5. After you have defined all of your translation keys, you can export the
resource bundle for translation. Click Export to export the existing set of
keys to a .zip file to which you will add the corresponding translated
properties files.
6. In the editor,  you need to manually create a new properties file for
each language locale that you will translate your user interface into. For each language that you
want your process application to
support, create a copy of the exported properties file, renaming it according to the language that
it will be supporting. For example, if your default properties file is
my\_application.properties and you want your process
application to support Japanese, create a copy of
the file called my\_application\_ja.properties.

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
7 Have each of the files translated into the corresponding languages. Note: The files must meet the following requirements:
    - The key-value pairs must conform to the format required by the Java specification. For more
information, see https://docs.oracle.com/javase/7/docs/api/java/util/Properties.html#load(java.io.InputStream).
    - Characters that cannot be directly represented in this encoding must be escaped by using Unicode
escapes as defined in the Java Specification. For example,for the German character Umlaut you would
use the unicode escape sequence \u00dc as the value in your key-value pair. There
are tools you can use to automate the conversion of characters. For example, native2ascii - Native-to-ASCII Converter.
8. Zip your properties files into a single .zip file.
9. To import your resource bundle into your process
application, open the localization resource file
and click Import.
10. Browse to your updated .zip file to select it and
click Finish.  If you select to overwrite the
values for all existing keys, then for any given language, key values in the imported files that do
not match the existing key values will replace the existing values. Any new keys are added to the
existing set of keys in the existing localization resource.
If there are any missing keys in any of the translated files, warnings are displayed. Click each
of the languages that are flagged with a warning to see which key translations are missing. If you
do not supply translations for these keys, the default value is displayed in any interfaces that
reference this key.

## What to do next