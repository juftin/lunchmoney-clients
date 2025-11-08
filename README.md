# openapi-generator

## How does this repository work?

This repository is designed to automate the generation, testing, and publishing of
OpenAPI client code using OpenAPI Generator. It includes GitHub Actions workflows to handle
the entire lifecycle of the client code, from generation to release.

Checks for updates to the OpenAPI specification are run daily. If changes are detected,
the client code is regenerated, tested, and a pull request is created for review. When
changes are merged into the main branch, a new versions of the clients are automatically
released and published.

## Clients

### Python

The `python` client is a synchronous, `urllib3` based client for Lunch Money's API with
`pydantic` data models. See the [documentation](./clients/python/README.md) for more details.

```shell
pip install git+https://github.com/juftin/lunchmoney-clients/#subdirectory=clients/python
```

## Adding a New Client

1. Add the details of your new client to thr [openapitools.json](./openapitools.json)
   file. You can refer to the existing entries for guidance on the required fields. Make
   sure to use the same version across OpenAPI clients.
2. Add a TaskFile in the [tasks](./tasks) directory. TaskFile's must implement the
   following tasks. You can refer to existing TaskFiles for examples.
    - `test`: Run tests on your client generated code.
    - `publish`: Publish your client's artifacts to the appropriate package registry.
    - `postprocess`: Any post-processing steps needed after code generation.
    - `version`: Set your client's version in the `openapitools.json` file.
    - `clean`: Clean up any generated files or artifacts.
3. Add your client to the `CLIENTS` variable in the root [Taskfile.yaml](./Taskfile.yaml) file,
   and link yo your TaskFile created in step 2 in the `includes` section.
4. Add any installation steps to the GitHub Actions workflows in the
   [.github/workflows](./.github/workflows) directory if your client
   requires any special dependencies.
5. Add some detail about your client to this [README.md](./README.md) file.
6. That's it! You can test the whole process by running tasks like `task clean` / `task generate`
   / `task test` locally.
