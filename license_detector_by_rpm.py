#!/usr/bin/python3
import subprocess
import sys
import third_party_generator
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

def scan_license_rpm(rpm_stored_path, l_license, rpmname):
    if not rpm_stored_path:
        print("[Error] Please provide the path to the physical rpm stored by using --rp")
        exit(1)
    rpm_stored_path = rpm_stored_path + "/" if rpm_stored_path[-1] != "/" else rpm_stored_path
    has_license = False
    map_missed_license = []
    for lname in l_license:
        lname = lname.lower()
        cmd = "rpm -qlp " + rpm_stored_path + rpmname + " | grep -i " + lname
        debug("[CMD] " + cmd)
        r = subprocess.getoutput(cmd)
        debug("Scanning for " + lname + ": \n" + r)

        # Judgement to detect if a package doesn't have a license file
        if lname in r.lower():
            return True
        else:
            print("[MISSING " + lname + "] " + rpmname)

def main():
    if args.prefix:
        prefix = args.prefix
        prefix = prefix + "-" if prefix[-1] != "-" else prefix
    else:
        prefix = ""
    if args.filter:
        filter_prefix = args.filter
        filter_prefix = filter_prefix + "-" if filter_prefix[-1] != "-" else filter_prefix
    else:
        filter_prefix = ""
    filename = args.file
    license_names = args.license
    map_pkgname = {}

    fo = open(filename, "r+")
    lines = fo.readlines()
    for line in lines:
        full_rpmname = line.replace(prefix, "").replace("\n", "").replace(" ","")

        if not full_rpmname.strip():
            continue

        debug("===============" + full_rpmname + "===============")
        if full_rpmname == "repodata":
            continue

        pkgname = pkgname_analyzer.analyze_pkgname(full_rpmname, "name")
        pkgver = pkgname_analyzer.analyze_pkgname(full_rpmname, "version")
        if pkgname not in map_pkgname.keys():
            map_pkgname[pkgname] = full_rpmname
        else:
            if pkgver > pkgname_analyzer.analyze_pkgname(map_pkgname[pkgname], "version"):
                map_pkgname[pkgname] = full_rpmname
    fo.close()

    for k,v in map_pkgname.items():
        debug("key: " + k + ", value: " + v)
        scan_license_rpm(args.rpmpath, license_names, v)

if __name__ == "__main__":
    main()
