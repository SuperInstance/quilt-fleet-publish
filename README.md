# quilt-fleet-publish

> **Publish the fleet in one shot.**

## TL;DR

```bash
PYTHONPATH=. python3 fleet_publish.py
```

## What it does

Discovers all `quilt-*` repos, detects available registries (PyPI, npmjs,
crates.io), builds sdist/wheel/cargo, and publishes.

## Status

```
npmjs: [@superinstance/canary-hash]
pypi: [quilt-egg, quilt-spreadsheet]
crates: [quilt-egg]
```

## License

MIT — Casey / SuperInstance, Sept 23, 2026
