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

#===============================================================
import pkgname_analyzer

def scan_license(cmd, license_fnames, short_pkgname, rpmname):
    has_license = False
    l_missed_license = []
    for lname in license_fnames:
        cmd_new = cmd + " | grep -i " + lname
        debug("[CMD] " + cmd_new)
        r = subprocess.getoutput(cmd_new)
        debug("Scanning for " + lname + ": \n" + r)

        # If: short_pkgname has any matching license file. Print it.
        # Else: Add the missing license to l_missed_license
        if lname in r:
            has_license = True
            print(short_pkgname, "has license:", lname)
        else:
            l_missed_license.append(lname)

    # Only print MISSING licenses msg when NO licenses found at all
    # (not when there's any missing licenses)
    if not has_license:
        for t in l_missed_license:
            print("[MISSING " + t + "] " + rpmname)

def get_full_pkgname_from_repo(partial_name, ssh_cmd, path):
    cmd2 = "ls " + path + " | grep -i " + partial_name
    cmd = "ssh " + ssh_cmd + " " + cmd2
    debug("[CMD] " + cmd)
    r = subprocess.getoutput(cmd)

    # rpm -qa result (multiple packages) into one list
    l_pkgs = r.split(sep="\n")
    debug("[CMD] [Return] " + " / ".join(l_pkgs))

    if l_pkgs[0] == "" or len(l_pkgs) == 0:
        return None

    l_pkgs_new = []
    for t in l_pkgs:
        if t[len(partial_name)+1].isdigit():
            l_pkgs_new.append(t)

    debug("[CMD] [Return] length: " + str(len(l_pkgs_new)))
    debug(l_pkgs_new)
    return l_pkgs_new[-1] #Get the latest version

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

        debug("=============== " + prefix + input_pkg + " ===============")

        #full_pkgname = third_party_generator.get_full_pkgname_rpm_qa(partial_name=input_pkg, match=filter_prefix+input_pkg)
        rpmname = get_full_pkgname_from_repo(partial_name=filter_prefix+input_pkg, path=args.rpmpath, ssh_cmd=args.sshcmd)

        if not rpmname:
            print("[ERROR] no packages found: " + filter_prefix + input_pkg)
            exit(0)
        info("[Found Package To Process] " + rpmname)
        
        short_pkgname = pkgname_analyzer.analyze_pkgname(rpmname, "name")
        pkgver = pkgname_analyzer.analyze_pkgname(rpmname, "version")
        debug("short package name: " + short_pkgname)
        debug("package version: " + pkgver)
       
        scan_license("repoquery --list " + short_pkgname, license_names, short_pkgname, rpmname)
    fo.close()

if __name__ == "__main__":
    main()
