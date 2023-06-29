#!/usr/bin/python3
import subprocess
import sys
import args_parser
parser = args_parser.get_parser()
args = parser.parse_args()

is_debug = False
filename = args.file
prefix = args.prefix
dl_filter = [args.filter]

def debug(s):
    if is_debug or args.debug:
      print("[DEBUG] %s" % (s))

fo = open(filename, "r+")
lines = fo.readlines()
for line in lines:
    line = line.replace(prefix, "").replace("\n", "").replace(" ","")
    debug("===============" + line + "===============")
    #r = subprocess.run(["rpm", "-qa", "|", "grep", line], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    cmd_rpm = "rpm -qa | grep " + line
    debug("[CMD] " + cmd_rpm)
    r1 = subprocess.getoutput(cmd_rpm)
    debug(r1)
    
    # rpm -qa result (multiple packages) into one list
    l_pkgs = r1.split(sep="\n")
    debug(l_pkgs)

    # Put the element with the dl_filter string to the 1st element
    debug("length: " + str(len(l_pkgs)))
    for n in range( 1, len(l_pkgs) ):
        debug("current: " + l_pkgs[n])
        if l_pkgs[n].startswith(dl_filter[0]):
            debug("FOUND! " + l_pkgs[n])
            l_pkgs[0], l_pkgs[n] = l_pkgs[n], l_pkgs[0]
            break
    debug(l_pkgs)

    # 
    cmd_pkgname = "./pkgname_analyzer/pkgname_analyzer " + l_pkgs[0] + " name"
    r2 = subprocess.getoutput(cmd_pkgname)
    debug("package name: " + r2)

    cmd_repoquery = "repoquery --list " + r2 + " | grep -i license"
    debug("[CMD] " + cmd_repoquery)
    r3 = subprocess.getoutput(cmd_repoquery)
    debug("license: \n" + r3)

    # Judgement to detect if a package doesn't have a license file
    if "LICENSE" not in r3 and "COPYING" not in r3:
        debug("[MISSING LICENSE] " + l_pkgs[0])
        print(l_pkgs[0])
fo.close()
