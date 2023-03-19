# Hubsite

Hubsite is ansible role to run a simple, static site that shows an overview of available services.

It is powered by the official nginx docker image.

You can use the following variables to control your hubsite:

```yaml
hubsite_enabled: true
hubsite_domain: "example.com"
hubsite_title: "My services"
hubsite_subtitle: "Just click on a service to use it"
hubsite_service_list: |
  {{
    ([{'name': 'Miniflux', 'logo_location': '', 'description': 'An opinionated feed reader'}] if miniflux_enabled else [])
    +
    ([{'name': 'Nextcloud', 'logo_location': '', 'description': 'Sync your files'}] if nextcloud_enabled else [])
  }}
```