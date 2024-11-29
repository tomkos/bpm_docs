# Applying customizations

Ensure that you applied customized settings for the following artifacts:

- Configuration files and settingsNote: If you customized the length
of tracked fields in the Performance Data Warehouse database, update
the value of the max-length-of-string-columns property
for the database. For more information, see Extending the maximum number of characters in tracked performance data.
- Application server database connection pool settings and tuning
parameters
- Email templates
- Logging configurations
- Customized files such as CSS files, CoachDesigner.xsl ,images, HTML files, and JAR files, by taking the following steps:
    - Include as managed assets the customized files in your current
version that are not yet added to process applications or toolkits.
    - If you customized CoachDesigner.xsl, upload it as a managed asset so that
you can use it in place of the default .xsl file that is installed as part of the migration.