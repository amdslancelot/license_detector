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
- ***CAN ONLY*** Run on the machine which physically store the rpms.
- Only print MISSING licenses msg when NO licenses found at all (not when there's any missing licenses)
```
# python license_detector_by_rpm.py -l LICENSE COMMITMENT licenses.rst LICENSE.txt license.txt -f <PKGNAME_LIST>.txt -rp <PATH_TO_REPO_DIR>
ansible-collection-ansible-posix has license: license.txt
ansible-collection-pulp-pulp_installer has license: COMMITMENT
python39-pyasn1-modules has license: LICENSE.txt
python39-urllib3 has license: LICENSE.txt
python39-xlwt has license: licenses.rst
[MISSING license] python39-cchardet-2.1.7-4.0.1.el8.20230130060220.1eb888b.x86_64.rpm
[MISSING license] python39-git3.1.26-3.0.2.el8.20230615155549.aa6e917.noarch.rpm
[MISSING license] python39-ldap-3.4.2-1.0.1.el8.20230202030948.4c89ef9.x86_64.rpm
[MISSING license] python39-pyrsistent-0.18.1-2.0.1.el8.20230203045240.c4bec4f.x86_64.rpm
[MISSING license] python39-urlman-1.4.0-3.0.1.el8.20230127040403.5071025.noarch.rpm
[MISSING license] python39-webencodings-0.5.1-3.0.1.el8.20230131050117.6e463c9.noarch.rpm
```

## Scan License file by Package Name List
- Only print MISSING licenses msg when NO licenses found at all (not when there's any missing licenses)
```
# python license_detector_by_pkgname.py -l third_party_licenses -f <PKGNAME_LIST>.txt -pf python- -fi python39- -rp <PATH_TO_REPO_DIR> -ssh <SSH_USER>@<REPO_HOSTNAME>
python39-drf-access-policy has license: third_party_licenses
python39-pyjwt has license: third_party_licenses
python39-ldap has license: third_party_licenses
python39-defusedxml has license: third_party_licenses
[MISSING license] python39-openpyxl-3.0.9-2.0.1.el8.noarch
[MISSING license] python39-pyrsistent-0.18.1-2.0.1.el8.x86_64
[MISSING license] python39-xlwt-1.3.0-3.0.1.el8.noarch
[MISSING license] python39-cchardet-2.1.7-4.0.1.el8.x86_64
```

