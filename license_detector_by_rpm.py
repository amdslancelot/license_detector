#!/usr/bin/python3
import subprocess
import sys
import args_parser
parser = args_parser.get_parser()
args = parser.parse_args()

is_debug = False

def debug(s):
    if is_debug or args.debug:
      print("[DEBUG] %s" % (s))

def info(s):
    if is_debug or args.debug:
      print("[INFO] %s" % (s))
 
def warn(s):
    if is_debug or args.debug:
      print("[WARN] %s" % (s))

#==============================================================================
import pkgname_analyzer
import pkgname_analyzer_helper
from license_detector_by_pkgname import scan_license

def scan_license_rpm(rpm_stored_path, l_license, rpmname):
    if not rpm_stored_path:
        print("[Error] Please provide the path to the physical rpm stored by using --rp")
        exit(1)
    rpm_stored_path = rpm_stored_path + "/" if rpm_stored_path[-1] != "/" else rpm_stored_path

    pkgname = pkgname_analyzer.analyze_pkgname(rpmname, "name")
    scan_license("rpm -qlp " + rpm_stored_path + rpmname, l_license, pkgname, rpmname)

def main():
    filename = args.file
    license_names = args.license
    map_pkgname = {}

    fo = open(filename, "r+")
    lines = fo.readlines()
    for line in lines:
        full_rpmname = line.replace("\n", "").replace(" ","")

        if not full_rpmname.strip():
            continue

        debug("===============" + full_rpmname + "===============")
        if full_rpmname == "repodata":
            continue

        pkgname = pkgname_analyzer.analyze_pkgname(full_rpmname, "name")
        pkgver = pkgname_analyzer.analyze_pkgname(full_rpmname, "longver")
        debug("lans1: " + pkgver)
        if pkgname not in map_pkgname.keys():
            map_pkgname[pkgname] = full_rpmname
        else:
            if pkgname_analyzer_helper.is_later_pkg_version(pkgname_analyzer.analyze_pkgname(map_pkgname[pkgname], "longver"), pkgver):
                map_pkgname[pkgname] = full_rpmname
    fo.close()

    for k,v in map_pkgname.items():
        debug("key: " + k + ", value: " + v)
        scan_license_rpm(args.rpmpath, license_names, v)

if __name__ == "__main__":
    main()
