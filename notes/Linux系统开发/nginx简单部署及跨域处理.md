As for the front-end project, you should use vite's build to make the project to build folder. This folder should be put in a proporiate site.

Firstly, deploying the front-end project, you should add a attribute in the http of the config file of nginx. You should set the port and ip will be listened, and the set the target folder which is the dist just put. When you working it, please refer the document on the internet or ask ai.

As a project which front-end and back-end are seperate, you should config proxy to handle across area problem.

==In the front end project, you should use the server's ip to post or get. In nginx, add a new 'location' of /api, instruct the server ip to localhost, your back end server.==