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

import config
import glob
import io_util as util
import logging
import os
import optparse
import sys

DEFAULT_LOG = "log.log"

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
      help='Assignment directory',
      )
  p.add_option(
      '--log',
      '-l',
      help="Path to log file",
      default=DEFAULT_LOG,
      )
  options, arguments = p.parse_args()

  # The program will not run without a config
  # or a directory.
  if not options.config or not options.directory:
    p.print_help()
    sys.exit(1)
  return options, arguments

def grade(netid, path, grader):
  '''
  Grades the assignment based on the expected outputs.
  If the outputs do not match, then an error logged and the user
  receives no points.
  '''
  print("[------- GRADING: {0} -------]".format(netid))

  score = 0
  for f in util.all_files(path):
    if util.extract_files(f, path):
      break
  score = grader.grade(path)
  # Prints the username and the score.
  print("[------- SCORE: {0} -- {1} -------]".format(netid, score))
  print("")

def _init_logging(log=DEFAULT_LOG):
  '''
  Initializes the log files.
  '''
  logging.basicConfig(filename=log, level=logging.INFO)

def main():
  # For each folder in the root directory, assumes the
  # directory under will be the UW Netid of the next
  # person to be graded.
  opts, args = parse_options()
  _init_logging(opts.log)
  grader = config.create_grader(opts.config)
  if grader is None:
    print("[Err] Could not initialize grader.  Exiting. . .")
    sys.exit(1)
  for d in util.get_dirs(opts.directory):
    netid = os.path.basename(d)
    grade(netid, d, grader)

if __name__ == '__main__':
  main()
