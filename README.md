# Hubsite

Hubsite is ansible an role to run a simple, static site that shows an overview of available services.

It is powered by the official nginx docker image.

You can use the following variables to control your hubsite:

```yaml
hubsite_enabled: true
hubsite_domain: "example.com"
hubsite_title: "My services"
hubsite_subtitle: "Just click on a service to use it"
hubsite_service_list: |
  {{
    ([{'name': 'Miniflux', 'url': 'https://' +  miniflux_hostname + miniflux_path_prefix, 'logo_location': '{{ role_path }}/assets/miniflux.png', 'description': 'An opinionated feed reader '}] if miniflux_enabled else [])
    +
    ([{'name': 'Uptime Kuma', 'url': 'https://' + uptime_kuma_hostname + uptime_kuma_path_prefix, 'logo_location': '{{ role_path }}/assets/uptime-kuma.png', 'description': 'Check if the status of services'}] if uptime_kuma_enabled else [])
    +
    ([{'name': 'Nextcloud', 'url': 'https://' + nextcloud_hostname + nextcloud_path_prefix, 'logo_location': '{{ role_path }}/assets/nextcloud.png', 'description': 'Sync your files & much more'}] if nextcloud_enabled else [])
    +
    ([{'name': 'Peertube', 'url': 'https://' + peertube_hostname + peertube_path_prefix, 'logo_location': '{{ role_path }}/assets/peertube.png', 'description': 'Watch videos '}] if peertube_enabled else [])
    +
    ([{'name': 'Vaultwarden', 'url': 'https://' + vaultwarden_hostname + vaultwarden_path_prefix, ' logo_location': '{{ role_path }}/assets/vaultwarden.png', 'description': 'Securly access your passwords'}] if vaultwarden_enabled else [])
    +
    ([{'name': 'Gitea', 'url': 'https://' + gitea_hostname + gitea_path_prefix, 'logo_location': '{{ role_path }}/assets/gitea.png', 'description': 'A git service'}] if gitea_enabled else [])
  }}
```

If you don't have a fitting logo for your service just use `logo_location': ''`


# Logos

There are some logos provided, so you can get started with a nice look immediately.

| Service     | Licence                                                                       | Author                | Changes made | Use it with                              |
|-------------|-------------------------------------------------------------------------------|-----------------------|--------------|------------------------------------------|
| Uptime Kuma | [MIT](https://github.com/louislam/uptime-kuma/blob/master/LICENSE)            | Louis Lam             | ✅            | `{{ role_path }}/assets/uptime-kuma.png` |
| Gitea       | CC BY-SA 4.0                                                                  | Lauris BH             | ✅            | `{{ role_path }}/assets/gitea.png`       |
| Grafana     | [AGPL v3.0](https://github.com/grafana/grafana/blob/main/LICENSE)             | Grafana Labs          | ✅            | `{{ role_path }}/assets/grafana.png`     |
| Miniflux    | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)                     | Frédéric Guillot      | ✅            | `{{ role_path }}/assets/miniflux.png`    |
| Peertube    | Public Domain                                                                 | PeerTube contributors | ✅            | `{{ role_path }}/assets/peertube.png`    |
| Nextcloud   | Public Domain                                                                 | Nextcloud             | ✅            | `{{ role_path }}/assets/nextcloud.png`   |
| Vaultwarden | [AGPL v3.0](https://github.com/dani-garcia/vaultwarden/blob/main/LICENSE.txt) | Mathijs van Veluw     | ✅            | `{{ role_path }}/assets/vaultwarden.png` |