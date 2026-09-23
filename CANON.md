# quilt-fleet-publish

**What this repo is**: one tool to publish all 19+ quilt repos to npmjs/PyPI/crates.io.

Substrate transition in 24 lines:
- discover all quilt-* repos
- detect available registries per repo
- build sdist/wheel/cargo
- publish via twine / npm / cargo
- track in witness log

Layered navigation: README.md → docs/FLEET_PUBLISH.md → fleet_publish.py → tests/test_publish.py
