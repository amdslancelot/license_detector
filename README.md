# license_detector

## Requirements

pkgname_analyzer

## Usage
```
# python license_detector.py.py -f pkgs_70.txt -pf python- -fi python39- -d
python39-openpyxl-3.0.9-2.0.1.el8.noarch
python39-pyrsistent-0.18.1-2.0.1.el8.x86_64
python39-xlwt-1.3.0-3.0.1.el8.noarch
python39-cchardet-2.1.7-4.0.1.el8.x86_64
```

## Debug Mode
```
# python license_detector.py -f pkgs_70.txt -pf python- -fi python39- -d
[DEBUG] ===============attrs===============
[DEBUG] [CMD] rpm -qa | grep attrs
[DEBUG] python39-attrs-21.4.0-2.0.1.el8.noarch
[DEBUG] ['python39-attrs-21.4.0-2.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['python39-attrs-21.4.0-2.0.1.el8.noarch']
[DEBUG] package name: python39-attrs
[DEBUG] [CMD] repoquery --list python39-attrs | grep -i license
[DEBUG] license: 
Last metadata expiration check: 0:48:14 ago on Thu 29 Jun 2023 10:10:39 PM GMT.
/usr/share/licenses/python39-attrs
/usr/share/licenses/python39-attrs/LICENSE
/usr/share/licenses/python39-attrs/license.rst
[DEBUG] ===============ansible-lint===============
[DEBUG] [CMD] rpm -qa | grep ansible-lint
[DEBUG] ansible-lint-5.0.8-4.0.1.el8.noarch
[DEBUG] ['ansible-lint-5.0.8-4.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['ansible-lint-5.0.8-4.0.1.el8.noarch']
[DEBUG] package name: ansible-lint
[DEBUG] [CMD] repoquery --list ansible-lint | grep -i license
[DEBUG] license: 
Last metadata expiration check: 0:48:19 ago on Thu 29 Jun 2023 10:10:39 PM GMT.
/usr/share/licenses/ansible-lint
/usr/share/licenses/ansible-lint/LICENSE
[DEBUG] ===============aiodns===============
[DEBUG] [CMD] rpm -qa | grep aiodns
[DEBUG] python39-aiodns-3.0.0-3.0.1.el8.noarch
[DEBUG] ['python39-aiodns-3.0.0-3.0.1.el8.noarch']
[DEBUG] length: 1
[DEBUG] ['python39-aiodns-3.0.0-3.0.1.el8.noarch']
[DEBUG] package name: python39-aiodns
[DEBUG] [CMD] repoquery --list python39-aiodns | grep -i license
[DEBUG] license: 
Last metadata expiration check: 0:48:24 ago on Thu 29 Jun 2023 10:10:39 PM GMT.
/usr/share/licenses/python39-aiodns
/usr/share/licenses/python39-aiodns/LICENSE

...

```
