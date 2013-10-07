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
#
# -- Add in command line args a la optparse (or something).

import os
import glob
import io_util as util
from subprocess import call

ASSIGNMENT_DIR = "TEST"  # TODO(awdavies) Make this a param.

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
  for d in util.get_dirs(ASSIGNMENT_DIR):
    netid = os.path.basename(d)
    grade(netid, d)

if __name__ == '__main__':
  main()
