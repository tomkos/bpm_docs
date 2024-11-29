# Customizing translation strings for Process Portal

## Before you begin

## About this task

Process Portal includes
web application components that are based on JavaScript files, and process application
components that are based on IBM® BPM
export (.twx) files. Customize web application
translations by updating JavaScript files.
Use resource bundles in the process application to customize the .twx file-based
process application translations.

## Procedure

1. Look in the translation resources to identify if the translation
that you would like customized is in the JavaScript files or the process application
resource bundles.
2 Complete the following steps for translations in the JavaScript files:
    1. For each locale that you would like to customize, open
the social\_base\_xx.js and social\_diagram\_xx.js files
at server\_root\UIStaticContent\process-server\portal.ear\process-portal.war\portal-nlv.zip\layers\bpmsocial\com\ibm\bpm\nls.
    2. Customize the translation strings in both social\_base\_xx.js and social\_diagram\_xx.js files.
For example, you search for the keyword notFollowed and
see the associated string You are not following this process.
Click to follow.. You change it to You are not following
this process. Click the star to follow it.
3 Complete the following steps for translations in the processapplication resource bundles:

1 In Process Designer, open the appropriate resource bundlegroups:
    - In the Process Portal process application: the ProcessPortal and PortalControls resource
bundle groups
    - In the dashboard toolkit: the Dashboards resource
bundle group
2. Find the string that you would like to customize in
the resource bundle group, then update the translation strings for
each locale that you would like to customize.
4. Deploy the updated snapshot of the Process Portal application.

## Results

Process Portal displays
the updated text.

## What to do next

You must reapply the customizations each time you upgrade IBM BPM or apply fix packs.