for i in range(10):
  if i%2==0:
    print(i)
  elif False:
    # this condition is never reached
    pass # pass does nothing
  else:
    print("odd number")