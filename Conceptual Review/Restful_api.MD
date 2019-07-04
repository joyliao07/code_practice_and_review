# RESTful API

## REST - Representational State Transfer:

        REST != HTTP

REST is an architectural style for "distributed hyptermedia systems" that follows the five guiding principles and aims to be simple, lightweight, and fast. It was first invented by Roy Fielding in 2000 in his famous dissertation.

In simplest words, in the REST architectural style, data and functionality are considered resources and are accessed using Uniform Resource Identifiers (URIs). The clients and servers exchange representations of resources by using a standardized interface and protocol – typically HTTP.

Resources are decoupled from their representation so that their content can be accessed in a variety of formats, such as HTML, XML, plain text, PDF, JPEG, JSON, and others.


## Guiding Principles of REST:

1. Client-server: There must be client and server in the architecture.

2. Stateless: Each request from client to server must contain all of the information necessary to understand the request; server must not store any application data. In case of partial failure of a system it is easy to recover because every client request is self contained ( not dependent on previous or future request). It allows the server to focus on only one request at a time, without worrying about the pending or previous requests. This allows scalibility because the workload can be shared among many servers. 

3. Cacheable: Because the need to send data repetitively to the server, network performance can be compromised. Therefore, here comes the solution of cache. A response to a request be labeled as cacheable or non-cacheable. If a response is cacheable, then a client cache is given the right to reuse that response data for later, equivalent requests. It means REST architecture could have multi level cache at client and server ends. This constraint was added to improve network efficiency.

4. Uniform interface
   Every REST architecture should have these elements:

        1) resources (i.e. unique url in REST APIs)

        2) representations: When a client holds a representation of a resource, it has enough information to modify or delete the resource. The state of resource at any particular timestamp is known as resource representation. A representation consists of data, metadata describing the data and hypermedia links which can help the clients in transition to next desired state.
        
        3) self-descriptive message: When server returns resource representation to the client then server should tell the client how to process the representation. Basically in terms of HTTP, content-type header should tell whether it is JSON or XML or some other format so that client can parse this representation.
        
        4) hypermeida as the engine of application state: It means, once a client have initial response, then response should contains hyperlinks which allows a client to move to the next state of the application. Consider an example of web-browser accessing a url, once browser get the response then it automatically requests all resources needed to render the page completely.

5. Layered System: An architecture to be composed of hierarchical layers by constraining component behavior such that each component cannot “see” beyond the immediate layer with which they are interacting.

## Resource:

The key abstraction of information in REST is a resource. Any information that can be named can be a resource.

**Resource Identifier:** REST uses a resource identifier to identify the particular resource involved in an interaction between components.


**Resource Representation:** The state of resource at any particular timestamp is known as resource representation. A representation consists of data, metadata describing the data and hypermedia links which can help the clients in transition to next desired state.

According to Roy Fielding:

    Hypertext (or hypermedia) mean the simultaneous presentation of information and controls such that the information becomes the affordance through which the user (or automaton) obtains choices and selects actions. 

## Resource Methods:
        - Get
        - Post
        - Put
        - Delete  







Source: https://restfulapi.net/ 
Source: https://restful.io/rest-api-back-to-basics-c64f282d972 
Source: https://stackoverflow.com/questions/25172600/rest-what-exactly-is-meant-by-uniform-interface 