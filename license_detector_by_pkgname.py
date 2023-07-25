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

#===============================================================
import pkgname_analyzer

def scan_license(names, short_pkgname, pkgname):
    has_license = False
    map_missed_license = []
    for lname in names:
        lname = lname.lower()
        cmd = "repoquery --list " + short_pkgname + " | grep -i " + lname
        debug("[CMD] " + cmd)
        r = subprocess.getoutput(cmd)
        debug("Scanning for " + lname + ": \n" + r)

        # Judgement to detect if a package doesn't have a license file
        if lname.upper() in r:
            has_license = True
        else:
            map_missed_license.append(lname.upper())
    if not has_license:
        for t in map_missed_license:
            print("[MISSING " + t + "] " + pkgname)

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

    fo = open(filename, "r+")
    lines = fo.readlines()
    for line in lines:
        input_pkg = line.replace(prefix, "").replace("\n", "").replace(" ","")

        if not input_pkg.strip():
            continue

        debug("===============" + input_pkg + "===============")

        full_pkgname = third_party_generator.get_full_pkgname_rpm_qa(partial_name=input_pkg, match=filter_prefix+input_pkg)
        info("[Found Package To Process] " + full_pkgname)
        if not full_pkgname:
            warn("no packages found: " + args.package)
            exit(0)
        
        short_pkgname = pkgname_analyzer.analyze_pkgname(full_pkgname, "name")
        debug("short package name: " + short_pkgname)
       
        scan_license(license_names, short_pkgname, full_pkgname)
    fo.close()

if __name__ == "__main__":
    main()
