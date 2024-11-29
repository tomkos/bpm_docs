# Successful installation reported after profile creation failure

The
failure of the profile creation step is indicated in the profile creation log. For example, you
might see the following error: INSTCONFFAILED: Profile augmentation failed.

1. Check the profile creation log, which is located in the <install\_root>/logs/manageprofiles directory,
to determine the cause of the error.
2 Complete one of the following steps:
    - Delete the profile that contains the error. Then, use the manageprofiles command
or the Profile Management Tool to create a new profile.
    - Install the product with a custom installation, but do not create
a profile. Then, after installation, use the manageprofiles command
or the Profile Management Tool to create the profile.