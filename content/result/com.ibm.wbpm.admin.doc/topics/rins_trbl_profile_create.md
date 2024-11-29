# Profile creation failure due to insufficient free space

- BPMConfig -create -profile
- BPMConfig -create -de (when
the profiles do not yet exist)
- manageprofiles

To confirm whether the profile creation failure is due to
insufficient space in the /tmp directory, open
the wsadminListener.out file that is located
in the path of the newly created profile directory, and then look
for an error message that is similar to the following example:

```
JVMSHRC561E Failed to initialize the shared classes cache, there is not
enough space in the file system. Available free disk space bytes = 
249856, requested bytes = 16777216.
JVMJ9VM015W Initialization error for library j9shr26(11): JVMJ9VM009E
J9VMDllMain failed
Could not create the Java virtual machine.
```

The /tmp directory
is needed to initialize the shared class cache for the JVM. A /tmp/javasharedresources directory
will be created.

To resolve the problem and allow profile creation
to complete successfully, ensure that there is at least 20MB of free
space in the /tmp directory.