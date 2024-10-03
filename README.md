# Hubsite

[![status-badge](https://woodpecker.hyteck.de/api/badges/102/status.svg)](https://woodpecker.hyteck.de/repos/102)

Hubsite is an ansible role to run a simple, static site that shows an overview of available services.

It is powered by the official nginx docker image.

You can alternativly use it manually with

```bash
python cli.py render -i services_example.yml
```

## How does it look?

![A screenshot of hubsite hosting different services like Miniflux and Nextcloud. The site and service logos are expressed in grey an white tones](assets/hubsite_desktop.png)

It uses `prefers-color-scheme` to automatically set the color scheme to light or dark. Check out  [this **live preview**](https://hubsite.hyteck.de) to see an example with all pre-configured services.

## Configuration

You can use the following variables to control your hubsite:

```yaml
hubsite_enabled: true
hubsite_hostname: "example.com"
hubsite_title: "My services"
hubsite_subtitle: "Just click on a service to use it"

# Use `hubsite_service_list_auto` if you develop a playbook. A user can then add additional services via `hubsite_service_list_additional`

# Nextcloud
hubsite_service_nextcloud_enabled: "{{ nextcloud_enabled }}"
hubsite_service_nextcloud_name: Nextcloud
hubsite_service_nextcloud_url: "'https://{{ nextcloud_hostname }}{{ nextcloud_path_prefix }}"
hubsite_service_nextcloud_logo_location: "{{ role_path }}/assets/nextcloud.png"
hubsite_service_nextcloud_description: "Sync your files & much more"
hubsite_service_nextcloud_priority: 1000

# Peertube
hubsite_service_peertube_enabled: "{{ peertube_enabled }}"
hubsite_service_peertube_name: Peertube
hubsite_service_peertube_url: "'https://{{ peertube_hostname }}{{ peertube_path_prefix }}"
hubsite_service_peertube_logo_location: "{{ role_path }}/assets/peertube.png"
hubsite_service_peertube_description: "Watch and upload videos"
hubsite_service_peertube_priority: 1000

hubsite_service_list_auto: |
  {{
    ([{'name': hubsite_service_nextcloud_name, 'url': hubsite_service_nextcloud_url, 'logo_location': hubsite_service_nextcloud_logo_location, 'description': hubsite_service_nextcloud_description, 'priority': hubsite_service_nextcloud_priority}] if hubsite_service_nextcloud_enabled else [])
    +
    ([{'name': hubsite_service_peertube_name, 'url': hubsite_service_peertube_url, 'logo_location': hubsite_service_peertube_logo_location, 'description': hubsite_service_peertube_description, 'priority': hubsite_service_peertube_priority}] if hubsite_service_peertube_enabled else [])
  }}

```

If you don't have a fitting logo for your service just use `logo_location': ''`


## Logos

There are some logos provided, so you can get started with a nice look immediately.

| Service/Purpose   | Licence                                                                                                        | Author                               | Changes made | Use it with                               |
|-------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------|--------------|-------------------------------------------|
| Generic Docs Icon | CCO                                                                                                            | moanos                               | ❌            | `{{ role_path }}/assets/docs.png`         |
| Generic Shield    | CC0                                                                                                            | moanos                               | ❌            | `{{ role_path }}/assets/shield.png`       |
| Generic Mail Icon | CCO                                                                                                            | moanos                               | ❌            | `{{ role_path }}/assets/mail.png`         |
| Appsmith          | [Apache License](https://github.com/appsmithorg/appsmith/blob/release/LICENSE)                                 | Appsmith contributers                | ✅            | `{{ role_path }}/assets/appsmith.png`     |
| Authentik         | [CC-BY-SA 4.0](https://github.com/goauthentik/authentik/blob/main/LICENSE)                                     | Jens Langhammer                      | ✅            | `{{ role_path }}/assets/authentik.png`    |
| Docker            | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)                                                      | dotCloud, Inc.                       | ✅            | `{{ role_path }}/assets/docker.png`       |
| Firezone          | [Apache License](https://github.com/firezone/firezone/blob/master/LICENSE)                                     | Firezone contributers                | ✅            | `{{ role_path }}/assets/firezone.png`     |
| Focalboard        | [AGPL v.3.0](https://github.com/mattermost/focalboard/blob/main/LICENSE.txt)                                   | Mattermost, Inc.                     | ✅            | `{{ role_path }}/assets/focalboard.png`   |
| FreshRSS          | [AGPL v.3.0](https://github.com/FreshRSS/FreshRSS/blob/edge/LICENSE.txt)                                       | FreshRSS contributors                | ✅            | `{{ role_path }}/assets/freshrss.png`     |
| Funkwhale         | [CC BY-SA 3.0](https://dev.funkwhale.audio/funkwhale/funkwhale/-/blob/stable/front/src/assets/logo/License.md) | Francis Gading                       | ✅            | `{{ role_path }}/assets/funkwhale.png`    |
| Gitea             | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)                                                | Lauris BH                            | ✅            | `{{ role_path }}/assets/gitea.png`        |
| GoToSocial        | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)                                                | Anna Abramek                         | ✅            | `{{ role_path }}/assets/gotosocial.png`   |
| Grafana           | [AGPL v3.0](https://github.com/grafana/grafana/blob/main/LICENSE)                                              | Grafana Labs                         | ✅            | `{{ role_path }}/assets/grafana.png`      |
| Healthchecks      | [BSD 3-Clause](https://github.com/healthchecks/healthchecks/blob/master/LICENSE)                               | Pēteris Caune and other contributors | ✅            | `{{ role_path }}/assets/healthchecks.png` |
| Jitsi             | [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)                                              | Jitsi contributers                   | ✅            | `{{ role_path }}/assets/jitsi.png`        |
| Keycloak          | [Apache License 2.0](https://github.com/keycloak/keycloak/blob/main/LICENSE.txt)                               | Keycloak contributers                | ✅            | `{{ role_path }}/assets/keycloak.png`     |
| Lago              | [AGPL v3.0](https://github.com/getlago/lago/blob/main/LICENSE)                                                 | Lago contributers                    | ✅            | `{{ role_path }}/assets/lago.png`         |
| Linkding          | [MIT](https://github.com/sissbruecker/linkding/blob/master/LICENSE.txt)                                        | Linkding                             | ✅            | `{{ role_path }}/assets/linkding.png`     |
| Miniflux          | [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)                                                      | Frédéric Guillot                     | ✅            | `{{ role_path }}/assets/miniflux.png`     |
| Mobilizon         | [AGPL v.3.0](https://framagit.org/framasoft/mobilizon/-/blob/main/LICENSE)                                     | Mobilizon contributers               | ✅            | `{{ role_path }}/assets/mobilizon.png`    |
| n8n               | [Sustainable Use License](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)                                | n8n                                  | ✅            | `{{ role_path }}/assets/n8n.png`          |
| Navidrome         | [GPL 3.0](https://github.com/navidrome/navidrome/blob/master/LICENSE)                                          | Navidrome contributers               | ✅            | `{{ role_path }}/assets/navidrome.png`    |
| Nextcloud         | Public Domain                                                                                                  | Nextcloud                            | ✅            | `{{ role_path }}/assets/nextcloud.png`    |
| Owncast           | [MIT](https://github.com/owncast/owncast/blob/develop/LICENSE)                                                 | Owncast contributors                 | ✅            | `{{ role_path }}/assets/owncast.png`      |
| Peertube          | Public Domain                                                                                                  | PeerTube contributors                | ✅            | `{{ role_path }}/assets/peertube.png`     |
| Prometheus        | [Apache 2.0](https://github.com/prometheus/prometheus/blob/main/LICENSE)                                       | -                                    | ✅            | `{{ role_path }}/assets/prometheus.png`   |
| Radicale          | [GPL 3.0](https://github.com/Kozea/Radicale/blob/master/COPYING.md)                                            | Unrud                                | ✅            | `{{ role_path }}/assets/radicale.png`     |
| Redmine           | [CC-BY-SA 2.5](http://creativecommons.org/licenses/by-sa/2.5/)                                                 | Martin Herr                          | ✅            | `{{ role_path }}/assets/redmine.png`      |
| Semaphore         | [MIT](https://github.com/ansible-semaphore/semaphore)                                                          | Castaway Consulting LLC              | ✅            | `{{ role_path }}/assets/semaphore.png`    |
| Syncthing         | [MPLv2](https://github.com/syncthing/syncthing/blob/main/LICENSE)                                              | Syncthing contributors               | ✅            | `{{ role_path }}/assets/syncthing.png`    |
| Uptime Kuma       | [MIT](https://github.com/louislam/uptime-kuma/blob/master/LICENSE)                                             | Louis Lam                            | ✅            | `{{ role_path }}/assets/uptime-kuma.png`  |
| Vaultwarden       | [AGPL v3.0](https://github.com/dani-garcia/vaultwarden/blob/main/LICENSE.txt)                                  | Mathijs van Veluw                    | ✅            | `{{ role_path }}/assets/vaultwarden.png`  |
| WG Easy           | [custom](https://github.com/wg-easy/wg-easy/blob/master/LICENSE.md)                                            | Emile Nijssen                        | ✅            | `{{ role_path }}/assets/wg_easy.png`      |
| Woodpecker CI     | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)                                                      | Woodpecker contributors              | ✅            | `{{ role_path }}/assets/woodpecker.png`   |


# Custom CSS

If you want to provide custom styling (CSS), you can add it (by appending it **on top of** the [default styles](https://github.com/mother-of-all-self-hosting/ansible-role-hubsite/blob/main/templates/html/styles.css.j2)) via the `hubsite_extra_css` variable like this:

```yaml
hubsite_extra_css: |
  html {
    background-color: #001a28;
    color: white;
  }

  .flexblock a {
      border: 5px solid #906000;
      padding: 20px;
      border-radius: 30px;
      margin: 15px;
      text-align: center;
      background-color: #046;
      width: 25%;
  }

  .logo {
      background-color: #046;
  }
```
