import os as installer
import time

try:
    import sympy as s
    from sympy import cos,sin,tan,pi,csc,sec,cot,ln,euler
except ImportError:
    installer.system("pip install sympy --user")
    print("All packages successfully installed.")
    import sympy as s
    from sympy import cos,sin,tan,pi,csc,sec,cot,ln,euler    

class MultiVariableChainRule():
    def __init__(self):
        self.x, self.y, self.t= s.symbols('x y t')
        self.zEqu=input("Input in a valid sympy syntax for the Z equation\n")
        self.xEqu=input("Input a valid sympy syntax for the x(t) equation\n")
        self.yEqu=input("Input a valid sympy syntax for the y(t) equation\n")
        try:
            self.deriveDelz()
            self.deriveDxDy()
            self.combine()
        except: 
            self.syntaxError()
            
    def deriveDelz(self):
        self.delzX=s.diff(self.zEqu,self.x)
        self.delzY=s.diff(self.zEqu,self.y)
        
    def deriveDxDy(self):
        self.Dx=s.diff(self.xEqu, self.t)
        self.Dy=s.diff(self.yEqu, self.t)
        
    def combine(self):
        finalDelx=self.delzX.subs(self.x,self.Dx)
        finalDely=self.delzY.subs(self.y,self.Dy)
        print(f"delZ/delX = {self.delzX}\ndelZ/delY = {self.delzY}\nDx/Dt = {self.Dx} \nDy/Dt = {self.Dy}\n result = ")
        final=(self.delzX*self.Dx).subs(self.y,self.yEqu).subs(self.x,self.xEqu)+(self.delzY*self.Dy).subs(self.y,self.yEqu).subs(self.x,self.xEqu)
        print(final,"\n")
        
    def syntaxError(self):
        print("Make sure you use the proper syntax.",
              "IE, Don't use 3x^2, use 3*x^2 or sint, you should use sin(t)")
        
