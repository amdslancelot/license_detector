#!/usr/bin/python3
import subprocess
import sys
import args_parser
parser = args_parser.get_parser()
args = parser.parse_args()
#print(args)

is_debug = False
filename = args.file
prefix = args.prefix
dl_filter = [args.filter]



def debug(s):
    if is_debug or args.debug:
      print("[DEBUG] %s" % (s))

def info(s):
    if is_debug or args.debug:
      print("[INFO] %s" % (s))

def warn(s):
    if is_debug or args.debug:
      print("[WARN] %s" % (s))

def remove_expiration_msg(s):
    #debug("s:" + str(s))
    l_s = s.split(sep="\n")
    #debug("before remove msg: " + ",".join(l_r4))
    for n in range(0, len(l_s)):
        #debug("n: " + str(n))
        if l_s[n].startswith("Last metadata expiration check"):
            l_s.remove(l_s[n])
            break
    return l_s


# Read from file
fo = open(filename, "r+")
lines = fo.readlines()
for line in lines:
    line = line.replace("\n", "").replace(" ","")
    info("=============== " + line + " ===============")
    line_new = line.replace(prefix, "")

    # Look for specific package
    if args.package and line_new != args.package:
        continue

    debug("search string: " + line_new)
    cmd_rpm = "rpm -qa | grep " + line_new
    debug("[CMD] " + cmd_rpm)
    r1 = subprocess.getoutput(cmd_rpm)
    #debug(r1)
    
    # rpm -qa result (multiple packages) into one list
    l_pkgs = r1.split(sep="\n")
    debug(l_pkgs)

    if l_pkgs[0] == "":
        warn("no packages found: " + line)
        continue

    # Put the element with the dl_filter string to the 1st element
    debug("length: " + str(len(l_pkgs)))
    for n in range( 1, len(l_pkgs) ):
        debug("current: " + l_pkgs[n])
        if l_pkgs[n].startswith(dl_filter[0]):
            debug("FOUND element to swap! index: " + str(n))
            l_pkgs[0], l_pkgs[n] = l_pkgs[n], l_pkgs[0]
            break
    debug(l_pkgs)

    # Get package name 
    cmd_pkgname = "./pkgname_analyzer/pkgname_analyzer " + l_pkgs[0] + " name"
    r2 = subprocess.getoutput(cmd_pkgname)
    debug("package name: " + r2)

    # Detect License file
    if args.action == "license":
        cmd_repoquery = "repoquery --list " + r2 + " | grep -i license"
        debug("[CMD] " + cmd_repoquery)
        r3 = subprocess.getoutput(cmd_repoquery)
        l_r3 = remove_expiration_msg(r3)
        debug("license files: " + ",".join(l_r3))

        # Judgement to detect if a package doesn't have a license file
        if "LICENSE" not in r3 and "COPYING" not in r3:
            print("[MISSING LICENSE] " + l_pkgs[0])
            #print(l_pkgs[0])

    # Detect Commitment file
    if args.action == "commitment":
        cmd_repoquery_commit = "repoquery --list " + r2 + " | grep -i commitment"
        debug("[CMD] " + cmd_repoquery_commit)
        r4 = subprocess.getoutput(cmd_repoquery_commit)
        l_r4 = remove_expiration_msg(r4)
        debug("commitment files: " + ",".join(l_r4))

        # Judgement to detect if a package doesn't have a license file
        if "COMMITMENT" in r4:
            print("[HAS COMMITMENT] " + l_pkgs[0])
            #print(l_pkgs[0])

fo.close()
