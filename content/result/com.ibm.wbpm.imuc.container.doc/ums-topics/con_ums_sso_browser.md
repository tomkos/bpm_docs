# How a browser or mobile application obtains an access token from UMS

## Understanding the Implicit flow

In the Implicit flow, the client is issued an access token directly. This contrasts with the
Authorization flow, which issues the client with an authorization code.

When UMS issues an access token, the client identity is verified by using the redirection URI
that is used to deliver the access token to the client. The URI must be registered when the client
application is registered with UMS SSO. It is not possible to make use of a client secret because a
browser cannot keep secrets.

## Design Considerations for the custom app

1 The client app must register with UMS SSO as an OIDC Relying Party. For example:curl -v -k -s -X POST -H "Content-Type:application/json" -u "umsadmin:passw0rd" -d @- "https://<ums-host>/oidc/endpoint/ums/registration" <<+++ { "scope": "openid", "preauthorized\_scope": "openid", "introspect\_tokens": true, "client\_id": "browser", "client\_name": "browser", "response\_types": ["token"], "grant\_types": ["implicit"], "redirect\_uris": [ "https://your-browser-app-IP/tokenReceiver.html " ] }+++ Where

```
curl -v -k -s -X POST -H "Content-Type:application/json" -u "umsadmin:passw0rd" -d @- "https://<ums-host>/oidc/endpoint/ums/registration" <<+++ 
{
 "scope": "openid",
 "preauthorized\_scope": "openid",
 "introspect\_tokens": true,
 "client\_id": "browser",
 "client\_name": "browser",
 "response\_types": ["token"],
 "grant\_types": ["implicit"],
 "redirect\_uris": [ "https://your-browser-app-IP/tokenReceiver.html " ] 
}
+++
```

    - grant\_types must be set to implicit.
    - response\_types must be set to token.
    - redirect\_uris acts as a whitelist, you can specify a list of URIs. Tip: If you want to use wild-cards or regular expressions in the
redirect\_uris, you must include
"allow\_regexp\_redirects": trueFor more information, see Configuring an OpenID Connect Provider to accept client registration
requests.
2 The browser application requests an access token from the OAuth authorization server, forexample, by making the user's browser visit the /authorize endpoint and including alink that redirects to UMS SSO for authentication. Forexample:<body> <h1>OAuth 2.0 Implicit</h1> <p>Have a look at the URL bar. If there is no token, click <a href="https://<ums-host>/oidc/endpoint/ums/authorize?response\_type=token&client\_id=browser&scope=openid&state=none&redirect\_uri=http://192.168.99.100:8080">here</a></p> </p>...</body> Inthis example, the browser application passes the following parameters:

```
<body>
  <h1>OAuth 2.0 Implicit</h1>
  <p>Have a look at the URL bar. If there is no token, click
  <a href="https://<ums-host>/oidc/endpoint/ums/authorize?response\_type=token&client\_id=browser&scope=openid&state=none&redirect\_uri=http://192.168.99.100:8080">here</a></p>
  </p>
...
</body>
```

- response\_type=token because the app is requesting an
access\_token (not an id\_token)
- client\_id=browser: The app needs to identify itself so that the authorization
server can verify that the redirect\_uri is one of the preregistered URLs and so
that it can also include the client\_id in the token information.
- scope=openid is pre-authorized.
- state=none is a short-cut in this example. This parameter is meant to allow the
client (browser app) to make sure that it sent the user to the authorization server and prevent any
unsolicited invocations. It can also help re-establishing context if the browser app had saved
several parameters, such as in HTML5 session storage.
- redirect\_uri is the URI to come back to after the user has authenticated and
given their consent (depending on the scopes).
3. When the request is redirected back to the browser application, several parameters are passed in
the URL, including the access token. In the following code snippet,
readTokenFromUrl() demonstrates how to parse name value pairs out of the URL bar
and store them in a complex variable named
params.var api\_base\_url = "https://sample.api.server/rest/objectstore" //construct the target API URL for the service you want to invoke
var params = {};

function readTokenFromUrl() {
	var queryString = location.hash.substring(1);
	var regex = /([^&=]+)=([^&]*)/g;
	var m;
	while (m = regex.exec(queryString)) {
	  params[decodeURIComponent(m[1])] = decodeURIComponent(m[2]);
	}

	if (params.access\_token==undefined) {
    addTextNode("access\_token", "not available yet");
	} else {
    addTextNode("access\_token", params.access\_token);
    addTextNode("scopes", params.scope);
    addTextNode("token\_type", params.token\_type);
    addTextNode("expires\_in", params.expires\_in);
  }
}

function getValue() {
  var key = document.getElementById("key").value;
	var xmlhttp = new XMLHttpRequest();
	try {
		xmlhttp.onreadystatechange=function() {
			  	if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			  		     document.getElementById("response").innerText=xmlhttp.responseText;
    			}
	  }
		xmlhttp.open("GET",api\_base\_url+"/" + key, true);
		xmlhttp.setRequestHeader("Authorization","Bearer " + params.access\_token);
		xmlhttp.send();
	} catch (err) { Console.log(err.message); }
}

function setValue(key, value) {
  var key = document.getElementById("key").value;
  var value = document.getElementById("value").value;
	var xmlhttp = new XMLHttpRequest();
	try {
		xmlhttp.onreadystatechange=function() {
			  	if (xmlhttp.readyState==4) {
            if (xmlhttp.status==200) { document.getElementById("response").innerText="success" }
          } else if (xmlhttp.satus==403) {  document.getElementById("response").innerText="not authorized" }
		}
		xmlhttp.open("PUT",api\_base\_url+"/" + key, true);
		xmlhttp.setRequestHeader("Authorization","Bearer " + params.access\_token);
		xmlhttp.setRequestHeader("Content-Type","application/json");
		xmlhttp.send(value);

	} catch (err) {return err.message; }
}

function addTextNode(elementId, text) {
  var textnode = document.createTextNode(text);
  var parent = document.getElementById(elementId);

  parent.appendChild(textnode);
}
4. The code in the custom application can now use the access token to make XML HTTP Requests (XHR)
to invoke OAuth 2.0 protected REST APIs. It must pass the value of the access token with each API
request in the request header Authorization.