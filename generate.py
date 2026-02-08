# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "jinja2",
#     "PyYAML",
# ]
# ///
import argparse
import sys
import os
from pathlib import Path
import webbrowser

import yaml
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = "templates"
PALETTES_SOURCE = "templates/palettes.yaml"


def generate_html(template_name: str, data: dict, css: str, env: Environment):
    template = env.get_template(template_name)
    return template.render(data | {"css_content": css})


def data_from_yaml(src: Path) -> dict:
    if not src.exists():
        print(f"Error: File {src} not found.")
        sys.exit(1)
    try:
        with src.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as err:
        print(f"Error: Failed to parse {src}. Is it valid YAML? Error: {err}")
        sys.exit(1)
    return data


def get_themes_css(themes: str, env: Environment) -> dict:
    css_template = env.get_template("theme_template.css.j2")

    with open(PALETTES_SOURCE, "r") as f:
        palettes = yaml.safe_load(f)

    rendered_styles = dict()
    if "all" in themes:
        for theme_name, palette in palettes.items():
            rendered_styles[theme_name] = css_template.render(palette)
    else:
        for theme_name in themes:
            try:
                palette = palettes[theme_name]
            except KeyError:
                print(f"Could not find the `{theme_name}` theme. It will be skipped")
                continue
            rendered_styles[theme_name] = css_template.render(palette)
    return rendered_styles


def main():
    parser = argparse.ArgumentParser(
        description="Generate a simple static CV site from yaml."
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the resume.yaml file",
    )
    parser.add_argument(
        "--template",
        type=str,
        default="template.html.j2",
        help="path to the html template file",
    )
    parser.add_argument(
        "--themes",
        type=str,
        default="nord-light",
        nargs="*",
        help="theme names, space separated, or `all`",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default="index.html",
        help="Output HTML filename",
    )
    parser.add_argument(
        "--open",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="Whether to open the results in a browser",
    )
    args = parser.parse_args()

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    data = data_from_yaml(args.source)
    css_styles = get_themes_css(args.themes, env)
    add_prefix = True if len(css_styles) > 1 else False

    try:
        os.mkdir("output")
    except Exception:
        pass

    for theme_name, style in css_styles.items():
        html_content = generate_html(
            template_name=args.template,
            data=data,
            css=style,
            env=env,
        )
        filename = (
            f"output/{theme_name}__{args.output}"
            if add_prefix
            else f"output/{args.output}"
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated {filename}")
        if args.open:
            webbrowser.open(filename)
    print("Finished.")


if __name__ == "__main__":
    main()
