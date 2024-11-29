# Text in case package PDF file is not displayed correctly

## Symptoms

## Causes

## Resolving the problem

1 Verify that the font directory is specified correctly in the case package configuration file. Inmost cases, the font directory is automatically detected. But if the font directory is not in thedefault location, you might need to manually specify the path to the font directory:
    1. Open the
network\_shared\_directory/AddOns/casePackage/userconfig.xml
file in your development and production environments.
    2. In the <fonts> element, verify that the value of the
<directory> element is correct. For example, the default font directory on
Windows is C:\Windows\Fonts. If the value is not correct, update the file.
2 Ensure that the required font for your locale is installed on the computer:

1. Open the
network\_shared\_directory/AddOns/casePackage/casepackage\_font.properties
file in your development and production environments to determine which font is required to generate
PDF files for your locale.
2. Install the specified font on your computer, or update the file to specify a different font that
is already installed on your computer.