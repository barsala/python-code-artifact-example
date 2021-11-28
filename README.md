# Example python package through AWS CodeArtifact

Just a demonstration how to use [AWS CodeArtifact]() for deploying private Python packages.

See [medium.com/@rare](https://medium.com/@rare/private-python-package-repository-aws-codeartifact-is-your-new-friend-3daa4968e222) for the original instructions 🔥.

## Pre-requisites

Make sure you have:
- An access token that grants you access to AWS CodeArtifact
- Set up your AWS CLI through `aws configure` to be pointing at `us-east-2` (this is specific to Barsala)

## Setup

Install some dependencies:

```shell script
pip install wheel twine
```

This python package is super hot and can do incredible stuff.

```shell script
python setup.py test
python setup.py sdist bdist_wheel
```

## Push to AWS CodeArtifact

```
aws codeartifact login --tool twine --domain barsala --repository test-package
twine upload --repository codeartifact dist/*
```

This creates/updates a package called `barsala-test-package` in our AWS account.

## Installation and usage in other repositories
1. Add `barsala-test-package==1.0.0` to the `requirements.txt` (or whichever version we are on)
2. Configure pip to use CodeArtifact: `aws codeartifact login --tool pip --domain barsala --repository test-package`
3. Re-install requirements: `pip install -r requirements`

Usage in code:
```
from barsala_example.tools import is_palindrome
```

