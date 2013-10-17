# Copyright 2013 -- Andrew Davies <andavies@cs.washington.edu>
#
# This is an automated grader (originally built for cse333).
# Codename: thunderfist.
#
# This is the util file for things related to file IO, etc.

import os
import glob
import logging
import mimetypes
import traceback
from subprocess import call, Popen, PIPE

logger = logging.getLogger(__name__)

# A list of extractor functions that can be passed to the 
# "call" command.  The elements in the extractor list are lambdas
# that must be supplied a file name and a path.
#
# If there's an extractor not listed here, then feel free to add
# one in!  The first element is the name of the command, and the
# rest of the elements are the function's arguments.  Please keep
# the names of the extractors in alphabetical order, and in all caps.
#
# Also feel free to edit the arguments to your liking.
EXTRACTORS = {
    "TAR_GZ": lambda f_name, path: ["tar", "xf", f_name, "-C", path],
    "ZIP": lambda f_name, path: ["unzip", f_name, "-d", path],
}

def get_dirs(directory):
  '''
  Generates all directories within a specified directory one level deep.
  '''
  files = glob.glob("{0}/*".format(directory))
  for d in filter(lambda f: os.path.isdir(f), files):
    yield d

def all_files(directory):
  '''
  Generates all files within a specified directory.
  '''
  for path, dirs, files in os.walk(directory):
    for f in files:
      yield os.path.join(path, f)

def extract_files(file_name, path):
  '''
  Attempts to extract from a file from the path.
  Assumes there is only one tar file.

  Returns:
      False -- If the file could not be extracted.
      True -- If the file could be extracted and built.
  '''
  rs = 1

  # Attempt to extract the file!
  print "  EXTRACTING -- {0}\n".format(file_name)
  for fn_name, ex_fn in EXTRACTORS.iteritems():
    print "    Attempting {0}\t\t".format(fn_name),
    tb = None
    try:
      proc = Popen(ex_fn(file_name, path), stdout=PIPE, stderr=PIPE)
      out = proc.communicate()
      if rs is None:
        print("[ Success ]")
        break
      else:
        logger.error(out[1])
        print("[ Failure ]") 
    except Exception as e:
      print("ERR: Running extract command.")
      tb = traceback.format_exc()
      print("[ Failure ]") 
    finally:
      if tb is not None:
        logger.error(str(tb))
  print ""
  if rs is None:
    return True
  return False
