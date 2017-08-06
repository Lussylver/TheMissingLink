import pprint
import numpy as np
import re
import csv


def is_there_a_x(word):
	return word.startswith("X")
	
def is_there_a_y(word):
	return word.startswith("Y")
	
def is_there_a_z(word):
	return word.startswith("Z")
	
def is_there_a_g(word):
	return word.startswith("G")
	
def remove_first_char(word):
	return word[1:]
#print f

#print f.read()

def Gcode_to_array(txtfile):

	f = open('C:\Gcode\\Foot Insole extruded.txt','r')
	#print f.read() 
	GCODE = f.read()
	couchej = str("layer:1")
	couchej1 = str("layer:2")
	LISTFINAL=[]
	j=1

		
	while True:
		try:
			
			print j
			
			#print couchei
			#print couchei1
			
			#print "Index Layer:"
			A=GCODE.index(couchej)
			#print A
			#print "TotalLength"
			B=GCODE.index(couchej1)
			#print B
			TroncText = GCODE[A:B]
			#print TroncText	
			Split = re.split('; | |\r|\n',TroncText)
			#print Split
			
			#print A
			#print B
			#print TroncText
			X_list=filter(is_there_a_x,Split)
			Y_list=filter(is_there_a_y,Split)
			Z_layer=filter(is_there_a_z,Split)
			G_list=filter(is_there_a_g,Split)
			
			
			X_list_filtered=map(remove_first_char,X_list)
			Y_list_filtered=map(remove_first_char,Y_list)
			G_list_filtered=map(remove_first_char,G_list)
			#print G_list_filtered
			
			#pprint.pprint(X_list_filtered)
			#print Z_layer
			#pprint.pprint(X_list_filtered)
			#pprint.pprint(Y_list_filtered)
			
			Z_str = ', '.join(Z_layer)
			#print Z_str
			
			#X_and_Y_list = zip((X_list_filtered,Y_list_filtered))
			
			#pprint.pprint(X_and_Y_list)
			#print X_and_Y_list
			length_of_list=len(X_list)
			
			#print Z_str
			Z_split = Z_str.split('\n')
			Z_value=Z_split[0]
			#print Z_value
			
			Z_value_filtered = 35.9-float(Z_value[1:])
			#print Z_value_filtered
			
			
			Z=[]
			for i in range(0,length_of_list):
				Z.append(Z_value_filtered)
				
			#XY_and_Z_list = zip(X_list_filtered,Y_list_filtered,Z)
			#print Z
			
			R=[]
			for i in range(0,length_of_list):
				R.append(0)
			#print R
			
			#for i in range(0,length_of_list):
				#S.append(10)
				
			D=[]
			for i in range(0,length_of_list):
				D.append(0.1)
				
			Status=[]
			#print D
			
			for i in range(0,length_of_list):
				if G_list_filtered[i]=='0':
					Status.insert(i,'CP Passing Point')
				else:
					Status.insert(i, 'Line Passing')
					
			S=[]
			
			#for i in range(0,length_of_list):
				#if G_list_filtered[i]=='0':
					#S.insert(i,'5')
				#else:
					#S.insert(i, '1')
				
			for i in range(0,length_of_list):
				S.append(5)
			
			
			#for i in range(0,length_of_list):
				#Status.append('Line Passing')
				
				#print G_list_filtered
			XY_and_Z_list = zip(Status,G_list_filtered,X_list_filtered,Y_list_filtered,Z,R,S,D)
			
			#pprint.pprint(XY_and_Z_list)
			
			
			j+= 1
			
			#print j
			
			couchej ="layer:"+str(j)
			couchej1="layer:"+str(j+1)
				
			#print couchej
			#print couchej1
				
				
			LISTFINAL.extend(XY_and_Z_list)
			
			#pprint.pprint(LISTFINAL)
		except:
			#pprint.pprint(LISTFINAL)
			print "REKT"
			break
	return LISTFINAL

List_of_Lists = Gcode_to_array('/home/lussylver/Downloads/cube.txt')

#print List_of_Lists

Array=np.array(List_of_Lists)

Transposed_array = map(list,zip(*List_of_Lists))

pprint.pprint(List_of_Lists)
#pprint.pprint(Transposed_array)

with open("output.csv","wb") as csvfile:
	writer=csv.writer(csvfile)
	writer.writerows(Transposed_array)
