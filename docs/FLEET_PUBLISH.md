# Fleet Publish Doctrine

The Quilt fleet has many repos. Each repo can publish to one or more
registries (PyPI, npmjs, crates.io, CF Workers). Fleet-publish
discovers repos, detects registries, builds artifacts, and publishes.

## Pipeline

1. **Discover**: find all quilt-* and superinstance-* repos
2. **Detect**: per-repo, what registries are configured (setup.py, package.json, Cargo.toml)
3. **Build**: sdist for PyPI, tarball for npmjs, cargo package for crates.io
4. **Publish**: twine upload / npm publish / cargo publish
5. **Track**: log to witness log

## License

MIT — Casey / SuperInstance, Sept 23, 2026
