# Shows help
default:
    @just --list --justfile {{ justfile() }}

# Pulls external Ansible roles
roles:
    #!/usr/bin/env sh
    set -euo pipefail
    if [ -x "$(command -v agru)" ]; then
    	agru
    else
    	rm -rf roles/galaxy
    	ansible-galaxy install -r requirements.yml -p roles/galaxy/ --force
    fi

# Runs ansible-lint against the role
lint:
    ansible-lint

# Renders the services_example.yml to public/
render:
  python cli.py render -i services_example.yml
