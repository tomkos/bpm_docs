# Recovering from profile creation failure after using the BPMConfig command

1. For each profile that you attempted to create, run the manageprofiles command
to delete the profiles. For example, manageprofiles -delete
-profileName profile\_name.
2. Delete the profile folders.
3. From the install\_root/bin folder,
run manageProfiles -validateAndUpdateRegistry
4. Drop the databases if you have already created them.