# BPMMigrationPreValidation troubleshooting

1. Open the com.ibm.bpm.migration.validation.jar file
in the install\_root\plugins folder.
2. Open the plugin.xml file. You can see that
all validation rules are registered as a extension of the BPM-Migration-PreValidation extension
point. For example, the validation for the source product looks similar
to the following code:<!--To implement the extenstion, you must implement the interface com.ibm.bpm.migration.prevalidation.IPreValidation	
	-->
	<extension-point id="BPM-Migration-PreValidation" />
	<extension point="com.ibm.bpm.migration.validation.BPM-Migration-PreValidation">
	   	<components>
	   		<component startup="1" class="com.ibm.bpm.migration.prevalidation.profile.ProductPreValidation" isOmitted="false" isOutputReportModel="false"/>
	   	</components>
	</extension>
3 For each validation rule, you can change the following:
    - If you change isOmitted="false" to isOmitted="true",
the validation rule does not run.
    - If you change isOutputReportModel="false" to isOutputReportModel="true",
then the report model in XML format is sent to report\_folder/xml\_folder.