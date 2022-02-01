## HOW TO USE

1. Clone this repo
1. create your new module directory `mkdir MODULE`, generally something like "octodns_provider"
1. cd into that directory `cd MODULE`
1. Initialize git for the new directory `git init`
1. run ../octodns-template/script/template to fill out the skeletal module structure
1. Create an initial skeleton commit, `git add . && git commit -m "Import skeleton"`
1. Find and work through all TODOs with `grep -r TODO .`, committing changes as makes sense
1. If you're extracting a provider from octoDNS core, see https://github.com/octodns/octodns/pull/822 for an example of the changes that need to be made there
1. ...

{EOH}

TODO: Review this README and add or modify as necessary.

## {NAME} provider for octoDNS

An [octoDNS](https://github.com/octodns/octodns/) provider that targets [{NAME}]({LINK}).

### Installation

#### Command line

```
pip install {MODULE}
```

#### requirements.txt/setup.py

Pinning specific versions or SHAs is recommended to avoid unplanned upgrades.

##### Versions

```
# Start with the latest versions and don't just copy what's here
octodns==0.9.14
{MODULE}==0.0.1
```

##### SHAs

```
# Start with the latest/specific versions and don't just copy what's here
-e git+https://git@github.com/octodns/octodns.git@9da19749e28f68407a1c246dfdf65663cdc1c422#egg=octodns
-e git+https://git@github.com/octodns/{MODULE}.git@ec9661f8b335241ae4746eea467a8509205e6a30#egg={MODULE}
```

### Configuration

```yaml
providers:
  {MODULE_STRIPPED}:
    class: {MODULE}.{PROVIDER}
    # TODO
```

### Support Information

#### Records

TODO: All octoDNS record types are supported.

#### Dynamic

TODO: {PROVIDER} does not support dynamic records.

### Development

See the [/script/](/script/) directory for some tools to help with the development process. They generally follow the [Script to rule them all](https://github.com/github/scripts-to-rule-them-all) pattern. Most useful is `./script/bootstrap` which will create a venv and install both the runtime and development related requirements. It will also hook up a pre-commit hook that covers most of what's run by CI.

TODO: any provider specific setup, a docker compose to run things locally etc?
