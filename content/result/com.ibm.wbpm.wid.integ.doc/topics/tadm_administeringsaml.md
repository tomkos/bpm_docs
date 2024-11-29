<!-- image -->

# Importing SAML policy sets

## Before you begin

The SAML policy sets are typically located in the profile
configuration directory:

profile\_root/config/templates/PolicySets

- SAML11 Bearer WSHTTPS default
- SAML20 Bearer WSHTTPS default
- SAML11 Bearer WSSecurity default
- SAML20 Bearer WSSecurity default
- SAML11 HoK Public WSSecurity default
- SAML20 HoK Public WSSecurity default
- SAML11 HoK Symmetric WSSecurity default
- SAML20 HoK Symmetric WSSecurity default
- Username WSHTTPS default

If the directories are not in the profile configuration
directory, copy them to that directory from the following location:

app\_server\_root/profileTemplates/default/documents/config/templates/PolicySets

## About this task

You import the policy sets into the administrative console,
select the ones you want to make available to Integration Designer, and then
save a .zip file for each of those policy sets to a location that
is accessible by Integration Designer.

## Procedure

1 Import the policy sets by following thesesteps:
    1. From the administrative console, click Services > Policy Sets > Application policy sets.
    2. Click Import > From Default Repository.
    3. Select the SAML default policy sets, and click OK.
2 Export the policy sets so that they can be used by Integration Designer :

1. From the Application policy sets page,
select the SAML policy set you want to export, and click Export.
Note: If the Application policy sets page is not currently displayed,
click Services > Policy
Sets > Application Policy Sets from the administrative console.
2. On the next page, click the .zip file link for the policy
set.
3. In the File Download window, click Save and
indicate a location that is accessible by Integration Designer.
4. Click Back.
5. Complete steps 2.a through 2.d for each policy set you want to export.

## Results

## What to do next