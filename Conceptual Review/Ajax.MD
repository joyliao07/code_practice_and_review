
# AJAX

## What Is AJAX

AJAX is not a programing language
AJAX is a technique for accessing web servers from a web page
AJAX stands for Asynchronous JavaScript And XML (i.e. Asynchronous HTTP Request)

## What Can AJAX Do

With AJAX, you can:

    - Update a web page without reloading the page
    - Request and receive data from a server - after the page has loaded
    - Send data to a server - in the background
    
Example HTML:

        <!DOCTYPE html>
        <html>
        <body>

        <div id="demo">
            <h2>Let AJAX change this text</h2>
            <button type="button" onclick="loadDoc()">Change Content</button>
        </div>

        </body>
        </html> 


Example JavaScript:

        function loadDoc() {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200) {
                document.getElementById("demo").innerHTML = this.responseText;
                }
            };
            xhttp.open("GET", "ajax_info.txt", true);
            xhttp.send();
        }


AJAX applications might use XML to transport data, but it is equally common to transport data as plain text or JSON text.


Source: https://www.w3schools.com/xml/ajax_intro.asp 

*****************************************************************************
****                            XHR                                     ****
*****************************************************************************
*****************************************************************************

Source: https://www.w3schools.com/whatis/whatis_http.asp 


All browsers have a built-in XMLHttpRequest Object (XHR). XHR is a JavaScript object that is used to transfer data between a web browser and a web server.


With XHR, you can:
    - Update a web page without reloading the page
    - Request and receive data from a server - after the page has loaded
    - Send data to a server - in the background


The XHR Object is the underlying concept of AJAX and JSON.


