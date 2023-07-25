# license_detector

## Requirements

- [pkgname_analyzer](https://github.com/amdslancelot/pkgname_analyzer)
```
export PYTHONPATH="$PYTHONPATH:/root/git/pkgname_analyzer/"
```
- [thirdpartygenerator](https://github.com/amdslancelot/thirdpartygenerator)
```
export PYTHONPATH="$PYTHONPATH:/root/git/thirdpartygenerator/"
```

## Scan License by RPM Name List
- Run on the machine which physically store the rpms.
```
# python license_detector_by_rpm.py -l license -f package_list.txt -pf python- -fi python39- -rp /PATH/TO/RPMS/
[MISSING license] python39-cchardet-2.1.7-4.0.1.el8.20230130060220.1eb888b.x86_64.rpm
[MISSING license] python39-git3.1.26-3.0.2.el8.20230615155549.aa6e917.noarch.rpm
[MISSING license] python39-ldap-3.4.2-1.0.1.el8.20230202030948.4c89ef9.x86_64.rpm
[MISSING license] python39-pyrsistent-0.18.1-2.0.1.el8.20230203045240.c4bec4f.x86_64.rpm
[MISSING license] python39-urlman-1.4.0-3.0.1.el8.20230127040403.5071025.noarch.rpm
[MISSING license] python39-webencodings-0.5.1-3.0.1.el8.20230131050117.6e463c9.noarch.rpm
```

## Scan License and Commitment file by Package Name List
- Run on the machine that has the package installed
```
# python license_detector_by_pkgname.py -l license commitment -f pkgs_70_short.txt -pf python- -fi python39-
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
# python license_detector_by_pkgname.py -l license commitment -f pkgs_70_short.txt -pf python- -fi python39- -d
...

```
