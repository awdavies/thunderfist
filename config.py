# Copyright 2013 -- Andrew Davies <andavies@cs.washington.edu>
#
# This is an automated grader (originally built for cse333).
# Codename: thunderfist.
#
# This file handles parsing the configuration for later use.
#
# TODO(awdavies) Perhaps just raise an exception in the event of a failed
# config file parse.
#
# TODO(awdavies) It might be a better idea to offload the options parsed in
# the main module into the config parser.  This way we can supply multiple
# grading directories/log files, etc etc.
#
# TODO(awdavies) Convert this to work with shlex, as we can make more complex
# config file commands that parse securely (or so the python library says....)
import ConfigParser
import logging
import traceback
import os
from subprocess import call

logger = logging.getLogger(__name__)

class _DirSwitcher:
  '''
  A simple class for switching back and forth between directories.

  TODO(awdavies) Maybe log or print that we're changing directories.
  '''
  def go(self, path):
    '''
    Attempts to go to the path in question, saving the last known
    location.
    '''
    self.saved_path = os.getcwd()
    os.chdir(path)

  def ret(self):
    '''
    Returns to the last known directory, else
    nothing happens.
    '''
    if self.saved_path:
      os.chdir(self.saved_path)

class _Grader:
  """
  A class representing an automated grader.  A grader is generated from
  a config file and consists of two main functions.

  1) A builder.
  2) The actual grader.

  The builder prepares a specific directory for grading (compiling source code,
  for example), and then runs one or more commands as part of the grader.

  This class should not need to be instantiated.  The grader will be created
  by the factory method in this module.
  """
  def __init__(self,
      build_cmd=None, run_cmd=None, regexes=None, out_file=None):
    self.build_cmd = build_cmd
    self.run_cmd = run_cmd
    self.regexes = regexes
    self.dir_switcher = _DirSwitcher()
    self.out_file = out_file

  def _build(self, path):
    '''
    Goes to the path in question and runs the build command, returning the
    result of said command.

    Returns the result of the build command in the form of an integer (it's 
    the exit code of the program).
    '''
    self.dir_switcher.go(path) 
    res = call(self.build_cmd)
    if res == 0:
      res = call(["chmod", "755", self.out_file])
    self.dir_switcher.ret()
    return res

  def grade(self, path):
    '''
    NOT IMPLEMENTED
    
    Goes to the path in question and runs the commands, comparing the output to
    the regexes in question.

    Returns

    True -- In the event that at least one regex successfully matches the output
            of the command.
    False -- In the event that no regexes match, or the assignment could not be
             built.
    '''
    res = self._build(path)
    if res != 0:
      return False
    binary = os.path.join(path, self.run_cmd[0])
    args = self.run_cmd[1:]
    print [binary] + args
    return call([binary] + args)

def create_grader(config_file):
  '''
  Creates a grader based on the parsing of the config file.

  Returns:

  Grader -- In the event of a successfully parsed config file.
  None   -- In the event that parsing the config file fails for some reason.
  '''
  parser = ConfigParser.SafeConfigParser()
  parser.read(config_file)
  tb = None
  try:
    # TODO(awdavies) This should be expanded to contain more params.
    # right now this is really for testing.
    grader = _Grader(
      build_cmd=parser.get("Builder", "cmd").split(','),
      run_cmd=parser.get("Grader", "cmd").split(','),
      regexes=parser.get("Grader", "regex"),
      out_file=parser.get("Builder", "out_file"),
    )
  except Exception as e:
    logger.error("Could not initialize grader.")
    tb = traceback.format_exc()
    return None
  finally:
    if tb is not None:
      logger.error(str(tb))
      return None
  logger.info("Grader initialized")
  logger.info("Grader params: [[ {0}, {1}, {2} ]]".format(
    grader.run_cmd,
    grader.build_cmd,
    grader.regexes,
  ))
  return grader
