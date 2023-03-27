import argparse
import logging
import os
import yaml
from distutils.dir_util import copy_tree
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Service:
    def __init__(self, service_dict):
        self.name = service_dict['name']
        self.description = service_dict['description']
        self.url = service_dict['url']
        self.logo_location = service_dict['logo_location']

def load_service_file(filename: str) -> list[Service]:
    with open(filename, "r") as f:
        loaded_data = dict(yaml.safe_load(f))
    services = []
    for service_dict in loaded_data["services"]:
        service = Service(service_dict)
        services.append(service)
    title = loaded_data["title"]
    subtitle = loaded_data["subtitle"]
    
    return {"services": services, "title": title, "subtitle": subtitle}

def cli():
    parser = argparse.ArgumentParser(description='Create a static html page to display a list of services')
    parser.add_argument('action', choices=['render'],
                        help="Use `render` to export a ready-to-use single page")
    parser.add_argument('-i', '--input-file', help="The service list to use")
    parser.add_argument('-o', '--output', help="Output directory, defaults to public/")
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARN)

    """if there is a remote blocklist provided load this instead of fetching it from a server (for debugging reasons)"""

    if args.input_file:
        input_filename = args.input_file
    else:
        input_filename = "../services.yml"
    try:
        data = load_service_file(input_filename)
    except FileNotFoundError:
        print("Local service file was not found. Make sure to specify it's location via -i")
        exit()
    

    # Render the templats
    env = Environment(
        loader=FileSystemLoader('templates/html'),
        autoescape=select_autoescape()
    )
    html_template = env.get_template("index.html.j2")
    css_template = env.get_template("styles.css.j2")
    html = html_template.render(hubsite_service_list=data["services"], hubsite_title=data["title"], hubsite_subtitle=data["subtitle"])
    css = css_template.render()

    if args.output:
        output_dir = args.output
    else:
        output_dir = "public"
    
    # Ensure the output directory exists
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Write the rendered output into the corresponding files
    with open(f"{output_dir}/index.html", "w") as f:
        f.write(html)
    with open(f"{output_dir}/styles.css", "w") as f:
        f.write(css)

    # Copy the assets (logos) to the public folder
    copy_tree("assets/", f"{output_dir}/assets/")



if __name__ == "__main__":
    cli()
