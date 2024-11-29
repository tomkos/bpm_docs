# Returning a list of reference links

This tw.system.model.processApp.getLinks() method
allows for returning reference links in the toolkits referenced by
the process application, and results can be filtered. The tw.system.model.processApp.getLinks() link
property returns only the reference links for the current process
application (not its children), and the results are not filtered.

## Parameters

The signature of the linkFilter argument
function is boolean linkFilterFunction(TWLink twlink),
 and that the filter function is called for each reference link result.
The filter function returns true if the TWLink value
in question is filtered out (excluded), or false if
it is not filtered out.

You can collect the names and URLs of the links using
the assetType Change Request from your process application and its
children, and then assign them to local variables in your process.

This
example assumes that the following two private variables have been
defined: requestLinksName of type String
List, and requestLinksURL of type String
List. Make sure to select Has Default for
both. The requestLinksName variable is an array that
contain the names of all the links, and the requestLinksURL variable
is an array that contain the URLs of all the links obtained by getLinks() that
were not filtered out by the linkFilter function.

The
following example is an specific example of how to narrow down the
list of returned links to be only those of the Change Request asset
type for that process application (and child projects). However, getLinks() can
be used to return all reference links.

```
var linkFilter = function (twlink) {
	if (twlink != null && TWLink.AssetTypes.CHANGE\_REQUEST == twlink.assetTypeNamespace){
		return false;
	}else{
		return true;
	}
} 
var requestLinks = tw.system.model.processApp.getLinks(true, linkFilter);
if(requestLinks != null){
    for(var i=0; i<requestLinks.length; i++){
        tw.local.requestLinksName[i] = requestLinks[i].name;
        tw.local.requestLinksURL[i] = requestLinks[i].url;
    }
}
```