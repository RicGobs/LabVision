import cv2 as cv
import numpy as np
import mediapipe as mp
import math
 
mp_face_mesh = mp.solutions.face_mesh



#
#
# POSSIBLE IMPROVEMENT -> CONTROL THE DIRECTION OF FACE WITH VECTOR Z OF MEDIAPIPE (and not geometry of faces)
#
#


LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]  

RIGHT_IRIS=[474,475,476,477]
LEFT_IRIS=[469,470,471,472]       

L_LEFT=[33]
L_LEFT_ESTERNO=[127]
L_RIGHT=[133]
L_UP=[159]
L_DOWN=[145]

R_RIGHT_ESTERNO=[356]
R_LEFT=[362]
R_RIGHT=[263]
R_UP=[386]
R_DOWN=[374]


# !!!!!!!
#
# CONTROLLARE ATTENZIONE SOPRA E SOTTO / CHECK ATTENTION ABOVE AND BELOW
#
# METTERE CONTROLLO DIVISIONE FLOAT / PUT CHECK FLOAT DIVISION
#
# !!!!!!!


#-----------FUNCTIONS---------

def distance_x(p1,p2):
    x1,y1=p1.ravel()
    x2,y2=p2.ravel()
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2) #così calcolo solo destra e sinistra
    if distance==0:
        distance=1
    return distance

def distance_y(p1,p2):
    x1,y1=p1.ravel()
    x2,y2=p2.ravel()
    distance=math.sqrt((y2-y1)**2+(x2-x1)**2) #così calcolo solo sopra e sotto
    if distance==0:
        distance=1
    return distance

def iris_right_horizontal(center,right,left):
    dist=distance_x(center,right)
    total_dist=distance_x(right,left)        
    val=dist/total_dist
    pos=""
    if val>0.41  and val<=0.53:
        pos="center"
        #pos="ATTENTO"
    elif val<=0.41:
        pos="right"
    else:
        pos="left"    
    return pos,val

def iris_left_horizontal(center,right,left):
    dist=distance_x(center,left)
    total_dist=distance_x(right,left)    
    val=dist/total_dist
    pos=""
    if val>0.41 and val<=0.55:
        pos="center"
        #pos="ATTENTO"
    elif val<=0.41:
        pos="left"
    else:
        pos="right"    
    return pos,val    

def iris_right_vertical(center,up,down):
    dist=distance_y(center,up)
    total_distance=distance_y(up,down)   
    val=dist/total_distance
    pos=""
    if val>0.40  and val<=0.54:
        pos="center"
        #pos="ATTENTO"
    elif val<=0.40:
        pos="up"
    else:
        pos="down"    
    return pos,val

def iris_left_vertical(center,up,down):
    dist=distance_y(center,up)
    total_distance=distance_y(up,down)   
    val=dist/total_distance
    pos=""
    if val>0.50  and val<=0.57:
        pos="center"
        #pos="ATTENTO"
    elif val<=0.40:
        pos="up"
    else:
        pos="down"    
    return pos,val

def i_function(center,right,left,esterno):
    dist1=distance_x(esterno,right)  
    dist2=distance_x(center,left)  
    pos=""
    if dist1>22  and dist1<=50:
        pos="fcentrale"
        #pos="ATTENTO"
    elif dist1<=22:
        pos="fdestra"
    else:
        pos="fsinistra"    
    return pos,dist1

#---------------MAIN------------


cap=cv.VideoCapture(0)
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=10, 
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame=cv.flip(frame, 1)
    rgb_frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    h,w=frame.shape[:2]
    results=face_mesh.process(rgb_frame)
    if results.multi_face_landmarks:
        i=0
        for face_landmarks in results.multi_face_landmarks: #####  ERROR -> I CAN'T VISUALISE MORE THAN A PERSON AT A TIME  ######

           punti_mesh_face=np.array([np.multiply([p.x,p.y],[w,h]).astype(int) for p in results.multi_face_landmarks[i].landmark])
           #I take all landmarks of a face

           (l_x,l_y), l_radius=cv.minEnclosingCircle(punti_mesh_face[LEFT_IRIS])
           (r_x,r_y), l_radius=cv.minEnclosingCircle(punti_mesh_face[RIGHT_IRIS])
           print([l_x,l_y],[r_x,l_y])
           center_left=np.array([l_x,l_y],dtype=np.int32) #dove sta guardando occhio sinistro
           center_right=np.array([r_x,r_y],dtype=np.int32) #dove sta guardando occhio destro

           cv.circle(frame,center_left,int(l_radius),(255,0,255),1,cv.LINE_AA)
           cv.circle(frame,center_right,int(l_radius),(255,0,255),1,cv.LINE_AA)        
           cv.circle(frame, center_left, radius=2, color=(0, 255, 0), thickness=-1)
           cv.circle(frame, center_right, radius=2, color=(0, 255, 0), thickness=-1)
           cv.circle(frame,punti_mesh_face[R_RIGHT][0],3,(255,255,255),-1,cv.LINE_AA)
           cv.circle(frame,punti_mesh_face[R_LEFT][0],3,(0,255,255),-1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[L_RIGHT][0],3,(255,255,255),-1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[L_LEFT][0],3,(0,255,255),-1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[R_DOWN][0],3,(255,255,255),-1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[R_UP][0],3,(0,255,255),-1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[L_DOWN][0],3,(255,255,255),-1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[L_UP][0],3,(0,255,255),-1,cv.LINE_AA)
           #cv.polylines(frame,[punti_mesh_face[LEFT_EYE]],True,(0,255,0),1,cv.LINE_AA)
           #cv.polylines(frame,[punti_mesh_face[RIGHT_EYE]],True,(0,255,0),1,cv.LINE_AA)
           #cv.polylines(frame,[punti_mesh_face[LEFT_IRIS]],True,(255,0,0),1,cv.LINE_AA)
           #cv.polylines(frame,[punti_mesh_face[RIGHT_IRIS]],True,(255,0,0),1,cv.LINE_AA)
           #cv.circle(frame,punti_mesh_face[L_LEFT_ESTERNO][0],3,(0,255,255),-1,cv.LINE_AA)
           cv.circle(frame,punti_mesh_face[R_RIGHT_ESTERNO][0],3,(0,255,255),-1,cv.LINE_AA)
           
           iris_pos1,val1=iris_right_horizontal(center_right,punti_mesh_face[R_RIGHT][0],punti_mesh_face[R_LEFT][0])
           iris_pos2,val2=iris_left_horizontal(center_left,punti_mesh_face[L_RIGHT][0],punti_mesh_face[L_LEFT][0])
           iris_pos3,val3=iris_right_vertical(center_right,punti_mesh_face[R_UP][0],punti_mesh_face[R_DOWN][0])
           iris_pos4,val4=iris_left_vertical(center_left,punti_mesh_face[L_UP][0],punti_mesh_face[L_DOWN][0])
           i+=1

           
           iris_pos,var1=i_function(center_right,punti_mesh_face[R_RIGHT][0],punti_mesh_face[R_LEFT][0],punti_mesh_face[R_RIGHT_ESTERNO][0])
           #iris_pos,val1,val2=iris_function(center_left,punti_mesh_face[L_LEFT_ESTERNO][0],punti_mesh_face[L_LEFT][0])

        
           cv.putText(frame,f"h_r: {iris_pos1} {val1: .2f}",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]),cv.FONT_HERSHEY_PLAIN,1.2,(0,255,0),1,cv.LINE_AA)
           cv.putText(frame,f"h_l: {iris_pos2} {val2: .2f}",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+30),cv.FONT_HERSHEY_PLAIN,1.2,(0,0,255),1,cv.LINE_AA)
           cv.putText(frame, f"v_r: {iris_pos3} {val3: .2f}",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+60), cv.FONT_HERSHEY_PLAIN, 1.2,(0,255,0), 1,cv.LINE_AA)
           cv.putText(frame, f"v_l: {iris_pos4} {val4: .2f}",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+90),cv.FONT_HERSHEY_PLAIN,1.2,(0,0,255),1, cv.LINE_AA)
           cv.putText(frame, f"v: {iris_pos} {var1: .2f} ",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+120),cv.FONT_HERSHEY_PLAIN,1.2,(0,255,255),1, cv.LINE_AA)
           #h_r=horizontal_right
           #h_l=horizontal_left
           #v_r=vertical_right
           #v_l=vertical_left
           #v=view of the face
      
 
        if (iris_pos1=="center" or iris_pos2=="center") and (iris_pos3=="center" or iris_pos4=="center") and iris_pos=="fcentrale": 
            cv.putText(frame,f"ATTENTO",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+150),cv.FONT_HERSHEY_PLAIN, 2, (255,0,255), 1,cv.LINE_AA)
        
        if (iris_pos1=="right" or iris_pos2=="right") and (iris_pos3=="center" or iris_pos4=="center") and iris_pos=="fsinistra": 
            cv.putText(frame,f"ATTENTO",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+150),cv.FONT_HERSHEY_PLAIN, 2, (255,0,255), 1,cv.LINE_AA)
        
        if (iris_pos1=="left" or iris_pos2=="left") and (iris_pos3=="center" or iris_pos4=="center") and iris_pos=="fdestra" : 
            cv.putText(frame,f"ATTENTO",(punti_mesh_face[R_RIGHT_ESTERNO][0][0],punti_mesh_face[R_RIGHT_ESTERNO][0][1]+150),cv.FONT_HERSHEY_PLAIN, 2, (255,0,255), 1,cv.LINE_AA)

        #I have written "down" and "up", but they are not accurate. I am not using them.

        cv.imshow('img',frame)
        if cv.waitKey(5) & 0xFF == 27:
            break
cap.release()
cv.destroyAllWindows()