# 0x0F-load_balancer

## Task description:

 * [0-custom_http_response_header](./0-custom_http_response-header): Bash
  script that installs and configures Nginx on a server with a custom HTTP
  response header.
    * The name of the HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.
    * Other server configurations identical to previous server configurations in project 0x0C-web_server.

* [1-install_load_balancer](./1-install_load_balancer): Bash script that
  installs and configures HAproxy version 1.5 on a server.
    * Enables management via the init script.
    * Requests are distributed using a round-robin algorithm.

* [100-puppet_custom_http_response_header.pp](./100-puppet_custom_http_response_header.pp): Just like the first task, Puppet manifest
   that configures a brand new server :
    * The name of the HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.
