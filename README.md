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
    ([{'name': 'Miniflux', 'logo_location': '{{ role_path }}/assets/miniflux.png', 'description': 'An opinionated feed reader '}] if miniflux_enabled else [])
    +
    ([{'name': 'Uptime Kuma', 'logo_location': '{{ role_path }}/assets/uptime-kuma.png', 'description': 'Check if the status of services'}] if uptime_kuma_enabled else [])
  }}
```

If you don't have a fitting logo for your service just use `logo_location': ''`