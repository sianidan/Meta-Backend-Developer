# BUILT-IN SCOPE
# can be accessed anywhere

# GLOBAL SCOPE (also accessed anywhere)
global_var = 10

def fn1():
  # ENCLOSED SCOPE
  # fn1 has access to global_var and enclosed_var
  # enclosed_var can't be accessed outside of fn1
  enclosed_var = 8

  def fn2():
    # LOCAL SCOPE
    # fn2 has access to global_var, enclosed_var, and local_var
    # local_var can't be accessed outside of fn2
    local_var = 5 
    print('Access to Global Variable', global_var)
    print('Access to Enclosed Variable', enclosed_var)
  
  # fn2 can't be accessed outside of fn1
  fn2()

fn1()