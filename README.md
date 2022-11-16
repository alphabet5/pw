# pw
 Application to type credentials for you.

Credentials are saved in your local keychain. By default if you do not have a local keychain it will use a .json file. This is insecure and not recommended. File permissions should be limited on this .json document if it is to be used.

## Building / Installing

```bash
python3 -m pip uninstall pw -y
rm dist/pw-*-py2.py3-none-any.whl
python3 setup.py bdist_wheel --universal
python3 -m pip install dist/pw-*-py2.py3-none-any.whl
```

## Usage


## Changelog

### 0.0.1
- Initial Release

