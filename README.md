# tamba_evals

## Conflict of interest disclosure

This repository is the sole work of its author, Hiroki Tamba. The author is
not affiliated with any university, company or government agency, receives no
external funding for this work, and has no financial relationship with any
model provider whose systems may be evaluated here. Names of other
organisations appear in this repository only as references to their public
work and do not indicate affiliation, endorsement or partnership.

## What this is

An independent, Japan-based collection of AI evaluation tasks built on top of
the Inspect framework (`inspect_ai`). The package follows Inspect's convention
for distributing components: tasks are registered through the `inspect_ai`
entry point in `pyproject.toml` and, once installed, are referenced as
`tamba_evals/<task>`.

No evaluation tasks are included yet. The current contents are the package
skeleton and a smoke test that checks the skeleton imports.

## Layout

```
pyproject.toml              package metadata and the inspect_ai entry point
src/tamba_evals/__init__.py package root
src/tamba_evals/_registry.py registry module loaded by Inspect
tests/test_import.py        import smoke test
```

## Development

```
pip install -e ".[dev]"
pytest
```

Once tasks exist they will be run with:

```
inspect eval tamba_evals/<task> --model <provider>/<model>
```

## Related prior work by the author

- Pull request merged into `inspect_ai`:
  [UKGovernmentBEIS/inspect_ai#4170](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4170),
  "docs(model-graded): document grader generation config and reproducible grading".
- Issues submitted by the author to Japan-AISI/aisev on evaluation
  reproducibility:
  [Japan-AISI/aisev#25](https://github.com/Japan-AISI/aisev/issues/25)
  (grader temperature/seed left uncontrolled, so near-threshold items flip
  between runs) and
  [Japan-AISI/aisev#27](https://github.com/Japan-AISI/aisev/issues/27)
  (cross-model ranking in ExploitBench capability notes rests on a single
  trial, with no trial-to-trial variance reported).

## License

MIT. See `LICENSE`.
