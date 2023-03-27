# Shows help
default:
    @just --list --justfile {{ justfile() }}

# Runs ansible-lint against the role
lint:
    ansible-lint

# Renders the services_example.yml to public/
render:
  python cli.py render -i services_example.yml
