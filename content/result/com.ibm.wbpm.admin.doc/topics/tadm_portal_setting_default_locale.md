# Setting the default locale

## Before you begin

## About this task

- For the available.locales property, see available.locales.
- For localization resources, see Creating localization resources.
- For custom properties, see Configuring custom properties.

## Procedure

- If the locale is listed, you have nothing more to do.
- If the language is listed but not the country variant, the country variant might still be
partially supported (date formats should be). Add the ll-cc code (lowercase and
dash separator) to the list in available.locales. Note: Language support also extends to specific countries. For example, different locale options are
provided for English (en\_US, en\_CA), French (fr and fr\_CA), and Portuguese (pt and pt\_BR).
 If you add a locale for a language
variant, such as British or Australian English, or Colombian or Mexican Spanish, you must update the
available.locales mashup configuration property from the WebSphere Application
Server administration console.
Make sure that you write the values for this property in lowercase, separate the value elements with
a dash (-), and separate the values with commas, as follows:
en-gb,en-au,es-co,es-mx
- If a language is not listed, it is not supported.