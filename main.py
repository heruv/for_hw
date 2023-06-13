def cheker(line):
  #line = line.replace(" ", "") возможно пригодится
  #line = line.lower() 
  rewersed_line = line[:: -1] # разворачиваем строку в другую сторону
  if line == rewersed_line: # сверяем сторки, посимволно
      return True
  else:
      return False
      
  
   


