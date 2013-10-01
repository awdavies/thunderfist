#!/usr/bin/env python2
# Copyright 2013 -- Andrew Davies <andavies@cs.washington.edu>
#
# This is an automated grading script (codename "thunderfist").
#
# TODO(awdavies) Add in some more documentation!
import datetime
import getpass
import optparse
import re
import signal
import sys
import time
import urllib
import web_util as wu

# This will be where we log in.
WEBLOGIN_URL = "https://weblogin.washington.edu/"

# This is the url for the time schedule server (ASP... gross).
SCHEDULE_URL = "https://sdb.admin.washington.edu/timeschd/uwnetid/sln.asp"

# The cookie domains we're interested in.  If these expire, they need to be
# reacquired (that rhymes!).
WEBLOGIN_REGEX = re.compile(r'weblogin.washington.edu', re.IGNORECASE)
CATALYST_URL = "https://catalyst.uw.edu/collectit/dropbox/summary/zahorjan/28608"

def sigint_handler(signal, frame):
    print '\n\nSIGINT Caught. Exiting . . .'
    sys.exit(0)

def parse_options():

    def sln_callback(option, opt, value, parser):
        setattr(parser.values, option.dest, value.split(','))

    # Create instance of OptionParser Module, included in Standard Library
    p = optparse.OptionParser(
        description='Downloads homework for grading, and then auto-grades!',
        prog='grader.py',
        version='0.1a',
        usage= '%prog [username] [pass]',
    )
    p.add_option('--user','-u', help='User name')
    p.add_option(
        '--password', 
        '-p', 
        help='Password. If ommitted, will be requested as user input.'
    )

    options, arguments = p.parse_args()

    '''
    if not options.user:
        setattr(options, 'user', raw_input('[?] UW Netid: '))
    if not options.password:
        setattr(options, 'password', getpass.getpass('[?] Password: '))
    '''
    return options

    p.print_help()
    sys.exit(1)

def uw_netid_login(netid, password):
    login_params = wu.parse_hidden_params(wu.send_get_request(WEBLOGIN_URL))
    login_params['user'] = netid
    login_params['pass'] = password

    ''' 
    TODO: Handle a) The WEBLOGIN_URL not opening, b) The username/pass being wrong
    '''
    wu.send_post_request(WEBLOGIN_URL, login_params)

def validate_login_cookie(cookie_jar, user, password):
    '''
    This determines if any of the necessary cookies are expired, and if so, we
    will reacquire them.
    '''
    login = True
    for cookie in cookie_jar:
        if re.match(WEBLOGIN_REGEX, cookie.domain):
            if not cookie.is_expired():
                login = False
    if login:
        uw_netid_login(user, password)

def download_submissions(cookie_jar, user, password):
    '''
    This downloads and extracts the homework submissions.

    TODO(awdavies) Implement me!
    '''

def main():
    # Set the cookie handler so we can pass around cookies 
    # for POST requests.
    cookies = wu.set_url_opener()
    opts = parse_options()
    # download_submissions(cookies, opts.user, opts.password)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    main()
