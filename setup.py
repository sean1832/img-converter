import json

from setuptools import find_packages, setup

manifest = json.load(open("pix/manifest.json", "r"))

setup(
    name=manifest["name"],
    version=manifest["version"],
    author=manifest["author"],
    description=manifest["description"],
    url=manifest["url"],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": [
            "manifest.json",
        ]
    },
    install_requires=["pillow", "pillow-avif-plugin", "pillow-heif"],
    entry_points={
        "console_scripts": [
            "pix = pix.main:main",
        ],
    },
)
