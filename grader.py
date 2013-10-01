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

import os
import logging
import mimetypes
from subprocess import call

ASSIGNMENT_DIR = "HW0"  # TODO(awdavies) Make this a param.
EXPECTED_MIMETYPE = ('application/x-tar', 'gzip')

def all_dirs(directory):
  '''
  Generates all directories within a specified directory.
  '''
  for path, dirs, files in os.walk(directory):
    for d in dirs:
      yield os.path.join(path, d)

def all_files(directory):
  '''
  Generates all files within a specified directory.
  '''
  for path, dirs, files in os.walk(directory):
    for f in files:
      yield os.path.join(path, f)

def extract_assignment(path):
  '''
  Attempts to extract from a tar file from the path.
  Assumes there is only one tar file.

  Returns:
      False -- If the file could not be extracted.
      True -- If the file could be extracted and built.
  '''
  try:
    tar_file = None
    for f in all_files(path):
      mime = mimetypes.guess_type(f)
      if mime != EXPECTED_MIMETYPE:
        print("OH NOES!  {0}".format(f))
      else:
        tar_file = f
    if not tar_file:
      return False
    # Extract the file!
    rs = call(["tar", "xvf", tar_file, "-C", path])
  except:
    print("ERR: Running tar command")
    return False
  if rs != 0:
    return False
  return True

def build_assignment(path):
  '''
  Attempts to build from the source directory specified in the
  path. Make sure that extract_assignment was first run.

  TODO(awdavies) In the event that there is no Makefile AND there is only
  one C file, run a generic compilation command (or something).

  Returns:
    False -- If the build failed in some way.
    True -- If the build succeeded.
  '''

def grade(netid, path):
  '''
  Grades the assignment based on the expected outputs.
  If the outputs do not match, then an error logged and the user
  receives no points.
  '''
  if extract_assignment(path) or build_assignment(path):
    score = 1
  else:
    score = 0

  # Prints the username and the score.
  print("{0} -- {1}".format(netid, score))

def main():
  # For each folder in the root directory, assumes the
  # directory under will be the UW Netid of the next
  # person to be graded.
  for d in all_dirs(ASSIGNMENT_DIR):
    netid = os.path.basename(d)
    grade(netid, d)

if __name__ == '__main__':
  main()
