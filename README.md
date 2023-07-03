# license_detector

## Requirements

- [pkgname_analyzer](https://github.com/amdslancelot/pkgname_analyzer)
```
export PATH="$PATH:/root/git/pkgname_analyzer/"
```
- [thirdpartygenerator](https://github.com/amdslancelot/thirdpartygenerator)
```
export PYTHONPATH="/root/git/thirdpartygenerator/"
```


## Example: Scan license and commitment file
```
# python license_detector.py -l license commitment -f pkgs_70_short.txt -pf python- -fi python39-
[MISSING LICENSE] python39-openpyxl-3.0.9-2.0.1.el8.noarch
[MISSING COMMITMENT] python39-openpyxl-3.0.9-2.0.1.el8.noarch
[MISSING LICENSE] python39-pyrsistent-0.18.1-2.0.1.el8.x86_64
[MISSING COMMITMENT] python39-pyrsistent-0.18.1-2.0.1.el8.x86_64
[MISSING LICENSE] python39-xlwt-1.3.0-3.0.1.el8.noarch
[MISSING COMMITMENT] python39-xlwt-1.3.0-3.0.1.el8.noarch
[MISSING LICENSE] python39-cchardet-2.1.7-4.0.1.el8.x86_64
[MISSING COMMITMENT] python39-cchardet-2.1.7-4.0.1.el8.x86_64
[MISSING LICENSE] python39-ldap-3.4.2-1.0.1.el8.x86_64
[MISSING COMMITMENT] python39-ldap-3.4.2-1.0.1.el8.x86_64
```

## Debug Mode
```
# python license_detector.py -l license commitment -f pkgs_70_short.txt -pf python- -fi python39- -d
...

```
