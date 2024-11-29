# Setting up a repeatable air-gap process

## About this task

The following steps show you how to save the CASE files to multiple registries (per environment),
and use the same saved CASE cache (~/.ibm-pak/$CASE\_NAME/$CASE\_VERSION) to
mirror the CASE without repeating the save process. As a result of not needing to save the CASE each
time, you do not have to worry about introducing newer versions of the dependencies to the CASE
cache.

## Procedure

1. Run the following command to save the CASE to 
~/.ibm-pak/data/cases/$CASE\_NAME/$CASE\_VERSION. 
oc ibm-pak get $CASE\_NAME \
   --version $CASE\_VERSION
This CASE can be used as an input for the mirror manifest generation.
2. Run the oc ibm-pak generate mirror-manifests command to generate the
image-mapping.txt file. 
oc ibm-pak generate mirror-manifests $CASE\_NAME $TARGET\_REGISTRY \
   --version $CASE\_VERSION
3. Add the image-mapping.txt to the oc image mirror
command. 
oc image mirror -f ~/.ibm-pak/data/mirror/$CASE\_NAME/$CASE\_VERSION/images-mapping.txt \
   --filter-by-os '.*' -a $REGISTRY\_AUTH\_FILE \
   --insecure \
   --skip-multiple-scopes \
   --max-per-registry=1