#!/usr/bin/env python

import cmd
from lru import LruCache

class LruRepl(cmd.Cmd):
  """LruRepl:  The LruCache shell (Read Eval Print loop)
  """
  intro = "Welcome to LruCache shell.\n\nType help or ? to list commands.\nCtrl-d or exit to exit.\n"
  prompt = "lrucache> "

  cache = None
  
  def precmd(self, line):
    """accept command as upper or lower case"""
    line = line.lower()
    return line

  def default(self, line):
    """overrides the default error message."""
    print 'ERROR'
    return False

  def command_preproc(self, line, expected_len):
    if self.cache == None:
      print "Cache not initialized.  Use SIZE command first."
      return None

    args = line.split()

    if len(args) != expected_len:
      print "Syntax Error.  Expected %d arguments, got %d" % (expected_len, len(args))
      return None

    return args

  def do_size(self, line):
    """size n - sets the maximum size of the cache to n objects"""
    if self.cache == None:
      args = line.split()

      if len(args) != 1:
        print "Syntax Error.  Expected 1 arguments, got %d" % len(args)
        return False

      self.cache = LruCache(int(args[0]))
      print("SIZE OK")
    else:
      print("ERROR")
    
  def do_set(self,line):
    """set key value - puts the key/value pair into the cache if the key does not exist
    or overwrites the value of an existing pair
    """
    args = self.command_preproc(line,2)

    if args != None:
      self.cache.put(args[0], args[1])
      print("SET OK")

  def do_get(self, line):
    """get key -- prints the value associated the the key if found"""
    args = self.command_preproc(line,1)

    if args != None:
      v = self.cache.fetch(args[0])
      if v == None:
        print("NOTFOUND")
      else:
        print("GOT %s" % v)
  
  def do_stats(self,line):
    """stats - print the cache stats"""
    if self.cache == None:
      print "Cache not initialized.  Use SIZE command first."
      return False

    print("Cache max size: %d" % self.cache.max_size)
    print("Current size: %d" % self.cache.current_size)
    
  def do_dump(self,line):
    """dump - dump the cache"""
    if self.cache == None:
      print "Cache not initialized.  Use SIZE command first."
      return False

    self.cache.data.dump()

  def do_eof(self, line):
    """Ctrl-D to exit"""
    print '\n'
    return True

  def do_exit(self, line):
    """exits shell"""
    print "\n"
    return True

##############################################################################

if __name__ == '__main__':
  LruRepl().cmdloop()
