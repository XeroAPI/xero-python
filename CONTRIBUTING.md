# Contributing to Xero-Python
We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:
:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

We want to make contributing to this project as easy and transparent as possible, whether it's:

The following is a set of guidelines for contributing to Xero and its projects, which are hosted in the [XeroAPI Organization](https://github.com/XeroAPI) on GitHub. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

### Table Of Contents
[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Pull Requests](#pull-requests)
  * [Local installation](#local-installation)


## Code of Conduct
Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## I don't want to read this whole thing I just have a question!!!

> **Note:** Please don't file an issue to ask a question. You'll get faster results by using the resources below.

We have an official [message board](https://community.xero.com/developer) where Xero API support and the community chimes in with helpful advice if you have questions.

* [API Documentation](https://developer.xero.com/documentation/)
* [Xero FAQ](https://developer.xero.com/faq)
* [Community, the official Xero message board](https://community.xero.com/developer)
* [Stackoverflow - Xero related](https://stackoverflow.com/questions/tagged/xero-api?sort=Newest)
* [Submit requests for support](https://developer.xero.com/contact-xero-developer-platform-support/) to our API Support team.

# How Can I Contribute?

You can contribute by reporting bugs, suggesting enhancements, improving documentation i.e. [README](README.md) or submitting a pull request.


## Reporting Bugs

Bugs are tracked as issues in this repository.

Before opening a new issue:
* **check [the README](README.md)** to see if the behavior you observed might be expected and if configuration options are available to provide you with the desired behavior.

* **perform a cursory search** to see if there's [an existing issue](https://github.com/xero-github/xero-python/issues) covering your feedback. If there is one and the issue is still open, **add a :+1: reaction** on the issue to express interest in the issue being resolved. That will help the team gauge interest without the noise of comments which trigger notifications to all watchers. Comments should be used only if you have new and useful information to share.

### Write bug reports with detail, background, and sample code

- Which version of the SDK are you using?
- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Suggesting Enhancements

When opening an issue for a feature request:
* **use a clear and descriptive title** for the issue to identify the problem.
* **include as many details as possible in the body**. Explain your use-case, the problems you're hitting and the solutions you'd like to see to address those problems.

## Pull requests

We welcome your feedback and pull requests. Be aware some code is generated and pull requests may not be the best solution -  see below.

### We Use OpenAPI Generator
The best way to propose changes to the codebase is to open an [issue](https://github.com/XeroAPI/xero-python/issues) and discuss with our team.

We are using [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) and [our OpenAPI specs](https://github.com/XeroAPI/Xero-OpenAPI), to create and update our models and client classes.  Improvements may require updates to our OAS or our customized mustache templates instead of modifying via pull request.

### Submit a pull request

1. Fork and clone the repository
1. Create a new branch: `git checkout -b my-branch-name`
1. Make your change, add tests if needed
1. Make sure the tests pass on your machine: `tox` read more in [local installation](#local-installation).
1. Push to your fork and submit a pull request
1. Pat your self on the back and wait for your pull request to be reviewed and merged.

Here are a few things you can do that will increase the likelihood of your pull request being accepted:

- Follow the [style guide](#style-guide).
- Write tests.
- Keep your change as focused as possible. If there are multiple changes you would like to make that are not dependent upon each other, consider submitting them as separate pull requests.
- Write a [good commit message](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

### Style Guide

* 4 spaces for indentation rather than tabs
* See [.editorconfig](.editorconfig) for more styling rules
* We us [black](https://github.com/psf/black) code formatter and
  [flake8](https://flake8.pycqa.org/en/latest/) to enforce style requirements.
* Activate virtual environment by running `source venv/bin/activate`
* Execute `flake8 xero_python tests` to check your code passes style requirements.
* If you see `BLK100 Black would make changes.` error Execute `black <file/path.py>` to correct it.

### Local development requirements

* Python3.5+ installed.

### Local installation

* To speed up local tests install [libyaml](https://pyyaml.org/wiki/LibYAML) library.
    ```bash
    brew install libyaml         # Mac with Homebrew
    apt-get install libyaml-dev  # Ubuntu
    dnf install libyaml-devel    # Fedora
    ```
* Create new python virtual environment `python3 -m venv venv`
* Activate new virtual environment by running `source venv/bin/activate`
* Install project dependencies by running `pip install -r requirements.txt -r requirements/dev.txt`

### Running tests
* Activate virtual environment by running `source venv/bin/activate`
* Execute `pytest` to run tests.

### Running tests for all python versions
* We use [tox](https://tox.readthedocs.io/en/latest/) to create different python environments and execute tests.

#### Local installation requirements
* You need to have python interpreters for python 3.5, 3.6, 3.7, and 3.8 installed locally.
* You can install them using [pyenv](https://github.com/pyenv/pyenv)
* Install `pyenv` - follow https://github.com/pyenv/pyenv#installation
* Install python versions required
    ```bash
    pyenv install 3.5.9 && \
    pyenv install 3.6.10 && \
    pyenv install 3.7.6 && \
    pyenv install 3.8.2
    ```

#### Running all tests
* Activate pyenv installed python versions `pyenv local 3.5.9 3.6.10 3.7.6 3.8.2`
* Activate virtual environment by running `source venv/bin/activate`
* Execute `tox` to run all tests in all python versions

## License
By contributing, you agree that your contributions will be licensed under its MIT License.
