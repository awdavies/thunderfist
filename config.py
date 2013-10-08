# Copyright 2013 -- Andrew Davies <andavies@cs.washington.edu>
#
# This is an automated grader (originally built for cse333).
# Codename: thunderfist.
#
# This file handles parsing the configuration for later use.
#
# TODO(awdavies) Perhaps just raise an exception in the event of a failed
# config file parse.

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
  def __init__(self, build_cmd=None, run_cmd=None, regexes=None):
    self.build_cmd = build_cmd
    self.run_cmd = run_cmd
    regexes = regexes

  def build(self, path):
    '''
    NOT IMPLEMENTED

    Goes to the path in question and runs the build command, returning the
    result of said command.

    Returns the result of the build command in the form of an integer (it's 
    the exit code of the program).
    '''
    pass

  def grade(self, path):
    '''
    NOT IMPLEMENTED
    
    Goes to the path in question and runs the commands, comparing the output to
    the regexes in question.

    Returns

    True -- In the event that at least one regex successfully matches the output
            of the command.
    False -- In the event that no regexes match.
    '''
    pass

def create_grader(config_file):
  '''
  Creates a grader based on the parsing of the config file.

  Returns:

  Grader -- In the event of a successfully parsed config file.
  None   -- In the event that parsing the config file fails for some reason.
  '''
  return None
