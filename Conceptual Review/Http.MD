# HTTP

## What Is HTTP

The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems. 

HTTP is the foundation of data communication for the World Wide Web, where hypertext documents include hyperlinks to other resources that the user can easily access, for example by a mouse click or by tapping the screen in a web browser. HTTP was developed to facilitate hypertext and the World Wide Web.

Development of HTTP was initiated by Tim Berners-Lee at CERN, the European Particle Physics Laboratory in Geneva, in 1989. 

<img src="https://github.com/joyliao07/code_practice_and_review/blob/conceptual/Conceptual%20Review/assets/berners-lee.jpg" width="450">

## HTTP Request / Response:

Communication between clients and servers is done by requests and responses:

        1. A client (a browser) sends an HTTP request to the web
        2. An web server receives the request
        3. The server runs an application to process the request
        4. The server returns an HTTP response (output) to the client browser

Three parts of an HTTP Request:
    1. URL
    2. Headers (Example – Accept-Language: EN)
    3. Message body which is optional


Three parts of an HTTP Response:
    1. Headers (Example – Content-Type: html)
    2. Message body which is optional
    3. Status code

## HTTPS

HTTPS is the secured HTTP protocol required to send and receive information securely over internet. Nowadays it is mandatory for all websites to have HTTPS protocol to have secured internet.


## The HTTP Request Circle:

A typical HTTP request / response circle:

        1. The browser requests an HTML page. The server returns an HTML file.
        2. The browser requests a style sheet. The server returns a CSS file.
        3. The browser requests an JPG image. The server returns a JPG file.
        4. The browser requests JavaScript code. The server returns a JS file
        5. The browser requests data. The server returns data (in XML or JSON).



Source: https://www.w3schools.com/whatis/whatis_http.asp 
Source: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol 
Source: https://www.webnots.com/what-is-http/ 
