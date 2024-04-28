#!/usr/bin/env python3
import pathlib
import sys
import tomllib


def link_for(name: str, url: str, svg: str) -> str:
    img_url = f"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/{svg}/{svg}-original.svg"

    return f'<a href="{url}" target="_blank" rel="noreferrer"><img src="{img_url}" width="36" height="36" alt="{name}" /></a>'


def create_link(data):
    name, url, svg = data["name"], data["url"], data["name"].lower().replace(" ", "").replace(".", "")
    return link_for(name=name, url=url, svg=svg)


def update_readme(links):
    start_tag, end_tag = "<!-- SKILLS:START -->", "<!-- SKILLS:END -->"
    readme = pathlib.Path("README.md")

    content = readme.read_text()
    start = content.index(start_tag) + len(start_tag)
    end = content.index(end_tag, start)

    updated_content = content[:start] + "\n".join(links) + content[end:]
    readme.write_text(updated_content)


def main():
    with pathlib.Path(".github/skills.toml").open("rb") as f:
        data = tomllib.load(f)

    update_readme(map(create_link, data["skills"]))


if __name__ == "__main__":
    main()
