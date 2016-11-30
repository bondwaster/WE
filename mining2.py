from mcpi.minecraft import Minecraft
from time import sleep	
mc=Minecraft.create()
			
x,y,z=mc.player.getPos()	
				
type= 0				
 
length=10
width=5
height=5
z=z-3 
x=x-3	
y=y-1		
	
def bomb(a,b):
  print("house complete???")
bomb(1,2)

mc.setBlocks(x,y,z,x+length,y,z+width,type) #floor

for j in range(1,height):
  for i in range (0,length+1):		
    mc.setBlock(x+i,y+j,z,type)													
    mc.setBlock(x+i,y+j,z+width,type)


  for i in range (0,width+1):
    mc.setBlock(x,y+j,z+i,type)
    mc.setBlock(x+length,y+j,z+i,type)																									

mc.setBlocks(x,y+height,z,x+length,y+height,z+width,type) #ceiling

#roof_layer_1
mc.setBlocks(x+1,y+height+1,z+1,x+length-1,y+height+1,z+width-1,type)

#roof_layer_2
mc.setBlocks(x+2,y+height+2,z+2,x+length-2,y+height+2,z+width-2,type)

