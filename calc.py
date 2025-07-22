import tkinter as tk
import math
root=tk.Tk()
root.title('Calculator')
root.config(bg='#0000FF')
root.resizable(0,0)
ent=tk.Entry(root,bg='#ADD8E6',fg='#000080',font=('Arial',25),borderwidth=10,justify='right')
ent.grid(row=0,columnspan=10,padx=10,pady=10,sticky='nsew')
ent.insert(0,'0')
class Calc:
 def __init__(self):
  self.current=''
  self.reset=True
 def upd(self,val):
  ent.delete(0,'end')
  ent.insert(0,val)
 def num(self,n):
  if self.reset:
   self.current=str(n)
   self.reset=False
  else:
   self.current=ent.get()+str(n)
  self.upd(self.current)
 def op(self,o):
  if o=='=':
   try:self.current=str(eval(ent.get()))
   except:self.current='Error'
   self.reset=True
  else:self.current=ent.get()+o
  self.upd(self.current)
 def clr(self):
  self.current='0'
  self.reset=True
  self.upd('0')
 def f(self,fn,deg=False):
  try:
   v=float(ent.get())
   if deg:v=math.radians(v)
   self.current=str(fn(v))
   self.upd(self.current)
   self.reset=True
  except:self.upd('Error')
c=Calc()
def b(t,r,col,cmd):
 tk.Button(root,text=t,font=('Arial',10),fg='black',highlightbackground='#ADD8E6',highlightthickness=2,width=6,height=2,command=cmd).grid(row=r,column=col,sticky='nsew',padx=10,pady=10)
nums='7894561230'
for i,n in enumerate(nums):
 b(n,(i//3)+2,i%3 if n!='0' else 0,lambda x=n:c.num(x))
b('CE',1,0,c.clr)
b('√',1,2,lambda:c.f(math.sqrt))
b('.',5,2,lambda:c.op('.'))
b('=',5,3,lambda:c.op('='))
b('+',1,3,lambda:c.op('+'))
b('-',2,3,lambda:c.op('-'))
b('*',3,3,lambda:c.op('*'))
b('/',4,3,lambda:c.op('/'))
b('π',1,4,lambda:c.upd(str(math.pi)))
b('e',1,5,lambda:c.upd(str(math.e)))
b('x²',1,7,lambda:c.f(lambda x:x**2))
b('x³',2,7,lambda:c.f(lambda x:x**3))
b('10^x',3,7,lambda:c.f(lambda x:10**x))
b('1/x',4,7,lambda:c.f(lambda x:1/x))
b('Abs',5,7,lambda:c.f(abs))
b('sin',3,4,lambda:c.f(math.sin,True))
b('cos',3,5,lambda:c.f(math.cos,True))
b('tan',3,6,lambda:c.f(math.tan,True))
b('sinh',4,4,lambda:c.f(math.sinh))
b('cosh',4,5,lambda:c.f(math.cosh))
b('tanh',4,6,lambda:c.f(math.tanh))
b('ln',5,4,lambda:c.f(math.log))
b('log10',5,5,lambda:c.f(math.log10))
b('log2',5,6,lambda:c.f(lambda x:math.log(x,2)))
b('x!',2,5,lambda:c.f(lambda x:math.factorial(int(x))))
root.mainloop()
