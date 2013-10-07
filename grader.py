#!/usr/bin/env python
# Copyright 2013 -- Andrew Davies <andavies@cs.washington.edu>
#
# This is an automated grader (originally built for cse333).
# Codename: thunderfist.
#
# TODO(awdavies) Add in more documentation.

# TODO List:
# 
# -- Support a list of regexes, with point values.
#
# -- Allow modifiable score.  For now it is only binary.
#
# -- Parse the commands to run/regexes to check against.

import glob
import os
import optparse
import io_util as util
import sys

def parse_options():
  # Creates an instance of OptionParser Module.
  p = optparse.OptionParser(
      description='Autograder for cse333',
      prog='grader.py',
      version='0.1a',
      usage= '%prog [assignment_dir] [config_file]',
      )
  p.add_option('--config','-c', help='Config file')
  p.add_option(
      '--directory', 
      '-D', 
      help='Assignment directory'
      )
  options, arguments = p.parse_args()

  if not options.config or not options.directory:
    p.print_help()
    sys.exit(1)
  return options, arguments

def build_assignment(path):
  '''
  Attempts to build from the source directory specified in the
  path. Make sure that extract_assignment was first run.

  TODO(awdavies) In the event that there is no Makefile AND there is only
  one C file, run a generic command.  Else run a command as provided in
  some sort of grade-config file (packaged with the assignments).

  Returns:
    False -- If the build failed in some way.
    True -- If the build succeeded.
  '''
  return False

def grade(netid, path):
  '''
  Grades the assignment based on the expected outputs.
  If the outputs do not match, then an error logged and the user
  receives no points.
  '''
  print("GRADING: {0}".format(netid))

  score = 0
  for f in util.all_files(path):
    if util.extract_files(f, path) or build_assignment(path):
      score = 1

  # Prints the username and the score.
  print("SCORE: {0} -- {1}".format(netid, score))

def main():
  # For each folder in the root directory, assumes the
  # directory under will be the UW Netid of the next
  # person to be graded.
  opts, args = parse_options()
  for d in util.get_dirs(opts.directory):
    netid = os.path.basename(d)
    grade(netid, d)

if __name__ == '__main__':
  main()
