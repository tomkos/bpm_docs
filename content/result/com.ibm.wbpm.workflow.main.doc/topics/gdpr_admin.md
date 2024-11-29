# GDPR-related administrative tasks

- Removing personal data from solutions and cases

Personal data in IBM® Business Automation Workflow can be found in the properties that are used in cases and in the lists of case owners, case team members, and solution role members.
- Retrieving personal data of BPM users

To comply with the General Data Protection Regulation (GDPR) requirement that EU data subjects have a right to find out what personal data an organization has stored about them, users that are assigned to the action policy roles ACTION\_VIEW\_USER\_PERSONAL\_DATA or ACTION\_DELETE\_USER\_PERSONAL\_DATA can use REST API calls to retrieve the personal data that is associated with a specific BPM user.
- Deleting personal data of BPM users

To comply with the General Data Protection Regulation (GDPR) requirement that EU data subjects have a right to be forgotten, users that are assigned to the action policy role ACTION\_DELETE\_USER\_PERSONAL\_DATA can use REST API calls to delete personal data that is associated with a specific BPM user.
- Synchronizing users between the BPM database and the user registry

Before a user's personal data can be deleted, their account must be deactivated by removing them from the user registry and then synchronizing the internal user data with the external user registry.