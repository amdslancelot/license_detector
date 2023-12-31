import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Lans License File Detect Tool')
    #parser.add_argument('-u', '--user', required=True,
    #                    help='***required*** Put your username to login to Bugdb service')
    #parser.add_argument('-p', '--password', required=True,
    #                    help='***required*** Put your user password to login to Bugdb service')
    #parser.add_argument('-b', '--url', required=True,
    #                    help='***required*** Put Bugdb api url (production or staging)')
    #parser.add_argument('action', choices=['create', 'get', 'generate_notes', 'post_notes'],
    #                    help='***required*** Bugz tool supported actions')
    #parser.add_argument('--cve', metavar=('CVE-YYYY-NNNN'), nargs='*',
    #                    help='CVE-YYYY-NNNN'),
    #parser.add_argument('--arch', metavar=('ARCHITECTURE'),
    #                    help='ex: x86_64, aarch64'),
    #parser.add_argument('--path', metavar=('(JENKINS)BUILD_LOG_PATH'),
    #                    help='path to build.log'),
    #parser.add_argument('--feature', action='store_true')
    #parser.add_argument('--no-feature', dest='feature', action='store_false')
    parser.add_argument('--file', '-f', required=True,
                        help='path to a file contains package names to scan')
    parser.add_argument('-l', '--license', nargs='+', required=True,
                        help='a list of  names to scan')
    parser.add_argument('--prefix', '-pf',
                        help='A prefix in the file to remove')
    parser.add_argument('--filter', '-fi',
                        help='A filter(also a prefix) to move the preferred pkg name (starts with the filter prefix) to be picked up first')
    parser.add_argument('-rp', '--rpmpath',
                        help='Path to the physical rpms stored')
    parser.add_argument('-ssh', '--sshcmd',
                        help='SSH command to repo server (ssh key need to be setup prior to use this feature)')
    parser.add_argument('-d', '--debug', action='store_true',
                        help='debug mode')
    #parser.set_defaults(feature=True)
    return parser
