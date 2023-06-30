# license_detector

## Requirements

pkgname_analyzer


## Detect LICENSE File

### Example
```
# python license_detector.py license -f pkgs_70.txt -pf python- -fi python39-
[MISSING LICENSE] python39-openpyxl-3.0.9-2.0.1.el8.noarch
[MISSING LICENSE] python39-pyrsistent-0.18.1-2.0.1.el8.x86_64
[MISSING LICENSE] python39-xlwt-1.3.0-3.0.1.el8.noarch
```

### Debug Mode
```
# python license_detector.py license -f pkgs_70.txt -pf python- -fi python39- -d
[INFO] =============== python-attrs ===============
[DEBUG] search string: attrs
[DEBUG] [CMD] rpm -qa | grep attrs
[DEBUG] ['python39-attrs-21.4.0-2.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['python39-attrs-21.4.0-2.0.1.el8.noarch']
[DEBUG] package name: python39-attrs
[DEBUG] [CMD] repoquery --list python39-attrs | grep -i license
[DEBUG] license files: /usr/share/licenses/python39-attrs,/usr/share/licenses/python39-attrs/LICENSE,/usr/share/licenses/python39-attrs/license.rst
[INFO] =============== ansible-lint ===============
[DEBUG] search string: ansible-lint
[DEBUG] [CMD] rpm -qa | grep ansible-lint
[DEBUG] ['ansible-lint-5.0.8-4.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['ansible-lint-5.0.8-4.0.1.el8.noarch']
[DEBUG] package name: ansible-lint
[DEBUG] [CMD] repoquery --list ansible-lint | grep -i license
[DEBUG] license files: /usr/share/licenses/ansible-lint,/usr/share/licenses/ansible-lint/LICENSE
...

```

## Detect COMMITMENT file

### Example
```
# python license_detector.py commitment -f pkgs_70.txt -pf python- -fi python39-
[HAS COMMITMENT] python39-openpyxl-3.0.9-2.0.1.el8.noarch
[HAS COMMITMENT] python39-pyrsistent-0.18.1-2.0.1.el8.x86_64
[HAS COMMITMENT] python39-xlwt-1.3.0-3.0.1.el8.noarch
```


### Debug Mode
```
# python license_detector.py commitment -f pkgs_70.txt -pf python- -fi python39- -d
[INFO] =============== python-attrs ===============
[DEBUG] search string: attrs
[DEBUG] [CMD] rpm -qa | grep attrs
[DEBUG] ['python39-attrs-21.4.0-2.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['python39-attrs-21.4.0-2.0.1.el8.noarch']
[DEBUG] package name: python39-attrs
[DEBUG] [CMD] repoquery --list python39-attrs | grep -i commitment
[DEBUG] commitment files: 
[INFO] =============== ansible-lint ===============
[DEBUG] search string: ansible-lint
[DEBUG] [CMD] rpm -qa | grep ansible-lint
[DEBUG] ['ansible-lint-5.0.8-4.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['ansible-lint-5.0.8-4.0.1.el8.noarch']
[DEBUG] package name: ansible-lint
[DEBUG] [CMD] repoquery --list ansible-lint | grep -i commitment
[DEBUG] commitment files: 

...

```

## Usage
```
usage: license_detector.py [-h] [--package [PACKAGE]] [--file FILE]
                           [--prefix PREFIX] [--filter FILTER] [-d]
                           {license,commitment}

Lans License File Detect Tool

positional arguments:
  {license,commitment}  ***required*** detect LICENSE or COMMITMENT file

optional arguments:
  -h, --help            show this help message and exit
  --package [PACKAGE], -p [PACKAGE]
                        looking for specific package
  --file FILE, -f FILE  a list of package names to scan
  --prefix PREFIX, -pf PREFIX
                        A prefix in the file to remove
  --filter FILTER, -fi FILTER
                        A filter(also a prefix) to move the preferred pkg name
                        (starts with the filter prefix) to be picked up first
  -d, --debug           debug mode

```
