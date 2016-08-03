#!c:/python34/python.exe
# -*- coding: utf-8 -*-
import math as m
from time import sleep
import os
def import_config(infile):
    objects = []
    file_dir = os.getcwd() +"\\"+ infile
    f = open(file_dir,"r+")
    for line in f:
        try:
            name, mass, fi, x, y, vx, vy, ax, ay = line.split(" ", 8)
            objects.append(Object(name, mass, fi, x, y, vx, vy, ax, ay))
        except ValueError:
        
            try:
                name, mass, fi, x, y = line.split(" ", 4)
                objects.append(Object(name, mass, fi, x, y ))
            except ValueError:
                name, mass, fi = line.split(" ", 2)
                objects.append(Object(name, mass, fi))
        
    return objects
class Stale:
    G = 6.674083*10**-11
    resTime = 10.0 #sekundy
    loopTimeout = 10000 # mikrosekundy
    
class Object:
    def __init__(self, name, mass, fi, x=0, y=0, vx=0, vy=0, ax=0, ay=0):
        self.name = name
        self.mass = float(mass)
        self.fi = float(fi)
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
        self.ax = float(ax)
        self.ay = float(ay)
    def __str__(self):
        return self.name+" (x:"+str(self.x)+" y:"+str(self.y)+", mass:"+str(self.mass) +")"
    def __repr__(self):
        return self.name+" (x:"+str(self.x)+" y:"+str(self.y)+", mass:"+str(self.mass) +")"
        
class ObjectManager():
    def __init__(self, obj):
        self.obj = obj
        
    def cartesianDist(self, b):
    
        dist = m.sqrt(pow(self.obj.x-b.x,2)+pow(self.obj.y-b.y,2))
        if(dist==0):
            print("[+]ERROR: odległosc kartezjanska(dzielenie przez 0)")
            return 10e-20
        else:       
            return dist
    
    def checkCollision(self, b):
        return self.cartesianDist(b) <= self.obj.fi+b.fi
    
    def changeMoment(self, b):
        self.obj.vx += (b.mass*b.vx-self.obj.vx*b.mass)/(self.obj.mass+b.mass)
        self.obj.vy += (b.mass*b.vy-self.obj.vy*b.mass)/(self.obj.mass+b.mass)
    def acceleration(self, b):
        self.obj.ax += (self.cos(b)*Stale.G*b.mass)/(self.cartesianDist(b)**2)
        self.obj.ay += (self.sin(b)*Stale.G*b.mass)/(self.cartesianDist(b)**2)
    def ifColide(self, b):
        
        if self.checkCollision(b):
            if self.obj.mass >= b.mass:
                self.changeMoment(b)
                self.obj.mass+=b.mass
                self.fi = m.sqrt(self.obj.fi**2+b.fi**2)
                return [b,b.name+"=>"+self.obj.name]
            else:
                self.changeMoment(self.obj)
                b.mass+=self.obj.mass
                b.fi = m.sqrt(self.obj.fi**2+b.fi**2)
                return [self.obj,self.obj.name+"=>"+b.name]
        return None
        
    def velocity(self):
        self.obj.vx = self.obj.vx + Stale.resTime/10**6*self.obj.ax
        self.obj.vy = self.obj.vy + Stale.resTime/10**6*self.obj.ay
    
    def sin(self, b):
        return (b.y-self.obj.y)/self.cartesianDist(b)
    def cos(self, b):
        return (b.x-self.obj.x)/self.cartesianDist(b)
    
    def position(self):
        self.obj.x += self.obj.vx
        self.obj.y += self.obj.vy
        
    def theOtherStuff(self):
        self.velocity()
        self.position()
    #def output(self):
    #    return self.obj.name+" (x:"+str(self.obj.x)+" y:"+str(self.obj.y)+", mass:"+str(self.obj.mass) +")"
temp_objcts=[]

class Universe:
    def __init__(self, objcts):
        self.objcts = objcts
        
    
    def action(self):
        for obj in self.objcts:
     
            temp_objcts = self.objcts[:]
            temp_objcts.remove(obj)
            
            obj.ax = 0
            obj.ay = 0
            
            for obj2 in temp_objcts:
                
                collide = ObjectManager(obj).ifColide(obj2)
               
                if collide:
                    print("[+]BUM " + collide[1])
                    
                    self.objcts.remove(collide[0])
                    for x in self.objcts: print(x)
                    break
                ObjectManager(obj).acceleration(obj2)
            #print(ObjectManager(obj).output())
            ObjectManager(obj).theOtherStuff()
          
    def START_THE_UNIVERSE(self):
        while(True):
            try:
             
                self.action()
            except KeyboardInterrupt:
                break
        
    

planety=[
    Object('Slonce',3000E10,1000,0,700),
    Object('Merkury',300E15,100,1,0),
    Object('Mars',100111,100,2000,300),
    Object('ISIS',10123,100,3000,400),
    Object('Pandora',100233,100,3500,9000),
]
#planety = import_config('config.txt')
#Universe(planety).START_THE_UNIVERSE()