# Generating a unique ID for a view

## About this task

## Procedure

- Open the view.
- Switch to the Layout page.
- Create a custom HTML view.
- Enter custom HTML code, and use $$viewDOMID$$ in the id
attribute:
<div id="$$viewDOMID$$\_myId1">   
 <span id="$$viewDOMID$$\_myId2"></span>   
 <input id="$$viewDOMID$$\_myId3" type="button" class="Jquerybutton" name="jbtnName" value="default"></input>
</div>
Note: To avoid potential conflicts, use a meaningful suffix after
$$viewDOMID$$, for example
$$viewDOMID$$\_buttonDiv.