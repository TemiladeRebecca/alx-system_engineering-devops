# 0x10-https_ssl

## Task description:

* [0-world_wide_web](./0-world_wide_web): Bash script that displays
  information about subdomains on my configured servers.
  * Usage: `./1-world_wide_web <domain> <subdomain>`
  * Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
  * If no `subdomain` parameter is passed, displays information about the
  subdomains `www`, `lb-01`, `web-01` and `web-02`, in that order.

* [2-haproxy_ssl_termination](./2-haproxy_ssl_termination): HAproxy
  configuration file that accepts encrypted SSL traffic for the subdomain using `certbot`
  `www.` on TCP port 443.

* [3-redirect_http_to_https](./3-redirect_http_to_https): HAproxy
  configuration file that redirects HTTP traffic to HTTPS.
