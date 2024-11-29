# Defining validation behavior for business objects

## About this task

In its default settings, IBM Business Automation
Workflow
ignores precision settings in processes or services but checks them in heritage coaches. The scale
setting is checked in both processes or services and heritage coaches. The check is performed for
equality, meaning that a variable with a scale of 2 must have exactly 2 digits after the decimal
point.

## Procedure

To change the precision and scale settings in the 100Custom.xml file,
complete the following steps:

1. Stop the server for IBM Workflow
Server or
IBM Workflow
Center.
2. Open the appropriate 100Custom.xml configuration file in a
					text editor. See The 100Custom.xml file and configuration.
3. Add the following code to the file:

<server>
	<business-object merge="mergeChildren">
		<precision-validation-on-server-enabled>true</precision-validation-on-server-enabled>
		<precision-validation-strip-trailing-zeros>true</precision-validation-strip-trailing-zeros>
		<precision-validation-type merge="replace">lessOrEquals</precision-validation-type>
		<scale-validation-strip-trailing-zeros>true</scale-validation-strip-trailing-zeros>
		<scale-validation-type>lessOrEquals</scale-validation-type>
	</business-object>
</server>
4. Save your changes to the 100Custom.xml file.
5. Start the server for Workflow Server or
Workflow Center.