import cv2 
import mediapipe as mp
import pygame
import sys
import random
import time
import math

def makebackground(image_path):
    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print("Unable to load image:", image_path)
        print(e)
        sys.exit()
    r_image = pygame.transform.scale(image, (1000,1000))
    screen.blit(r_image, (0, 0)) 

def Game(Time,Number,BaseSpeed):
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode([1000, 1000])

    # Set up the ball
    width, height = 500,400
    ball_radius = 30 
    num_balls =Number
    c=0
    ball_color=(0,0,0)
    ball_color1=(0,0,0)
    def color():
        x=random.uniform(0,255)
        y=random.uniform(0,255) 
        z=random.uniform(0,255)
        ball_color=((x,y,z))
        ball_color1=((z,y,x))

    # Generate random starting positions for each ball
    ball_positions = [[random.uniform(0, 600), ball_radius] for j in range(num_balls)]

    # Set up the clock
    clock = pygame.time.Clock()

    # Initialize mediapipe
    mp_hands = mp.solutions.hands
    mp_pose=mp.solutions.pose
    hands = mp_hands.Hands()
    pose = mp_pose.Pose()

    # Open webcam
    cap = cv2.VideoCapture(0)

    def getpose(pos):
        landmarks=results_pose.pose_landmarks
        point=landmarks.landmark[pos]
        x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
        return x,y

    #Recording Initial Time
    Initial=time.time()

    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up timer
    total_time = Time  # Total time in seconds
    current_time = total_time

    # A function to draw a line between two given landmarks.
    def drawlinepose(pos1, pos2):
        try:
            pygame.draw.line(screen,(0,0,0), (getpose(pos1)), (getpose(pos2)),5)
        except:
            print()
        
    while cap.isOpened() and time.time()-Initial<Time:
        ret, frame = cap.read()
        if not ret:
            break
        
         #Flipping Video
        frame = cv2.flip(frame, 1)
        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 

        # Process the frame with mediapipe hands
        results_hands = hands.process(rgb_frame)
        results_pose = pose.process(rgb_frame)
        
        screen.fill((255, 255, 255))
        #makebackground("bg1.jpeg")
        font = pygame.font.Font(None, 30)

        # Display "Time Left:" text
        text_time_left = f"TIME LEFT: {Time-math.floor(time.time()-Initial)} seconds"
        text_surface_time_left = font.render(text_time_left, True, (0, 0, 0))

        # Get the rectangle of the text surface
        text_rect_time_left = text_surface_time_left.get_rect()

        # Set the position of the text to the top-right corner
        text_rect_time_left.center = (500,100)

        # Blit the "Time Left:" text surface onto the screen
        screen.blit(text_surface_time_left, text_rect_time_left)

        # Display "Time Left:" text
        text_score= f"POINTS SCORED:{c}"
        text_surface_score = font.render(text_score, True, (0, 0, 0))

        # Get the rectangle of the text surface
        text_rect_score = text_surface_score.get_rect()

        # Set the position of the text to the top-right corner
        text_rect_score.center = (500,130)

        # Blit the "Time Left:" text surface onto the screen
        screen.blit(text_surface_score, text_rect_score)
        pygame.draw.line(screen,(0,100,0),(350,0),(350,160),3)
        pygame.draw.line(screen,(0,100,0),(650,0),(650,160),3)
        pygame.draw.line(screen,(0,100,0),(350,160),(650,160),3)

        # Create empty lists to store the x & y values of the landmarks. The lists will contain n sub-lists where n is the number of hands seen
        coordsx_hands=[]
        coordsy_hands=[]
        
        coordsx_pose=[]
        coordsy_pose=[]
        
        # Iterative variable
        i=0
        
            # BODY STUFF STARTS
        


        try:
            # Check if bodies are detected
            if results_pose.pose_landmarks:
                landmarks=results_pose.pose_landmarks
                
                # A function to fet the position of a particular landmark.
                
                # Drawing landmarks in opencv display.
                for point in landmarks.landmark:
                    # Extract landmarks (x, y, z) and put them in the respective sub-list.
                    x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
                    #cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
                

            # Body Drawing:

            #print(coordsx_hands)
            #for itr in range(len(coordsx_hands)):
                
            drawlinepose(15,13)
            drawlinepose(13,11)
            drawlinepose(11,12)
            drawlinepose(12,14)
            drawlinepose(14,16)
            drawlinepose(11,23)
            drawlinepose(12,24)
            drawlinepose(23,24)
            drawlinepose(23,25)
            drawlinepose(25,27)
            drawlinepose(24,26)
            drawlinepose(26,28)
            try:
                x_a,y_a=getpose(0)
                x_b,y_b=getpose(9)
                
                radius=((x_a-x_b)**2+(y_a-y_b)**2)**(0.5)
                
                pygame.draw.circle(screen,(0,0,0), (getpose(0)), radius,width=4)
            except:
                print()
            
            
            # BODY STUFF ENDS
        
    #face details
            
            x1,y1= getpose(14)
            x2,y2= getpose(16)
            x3,y3= getpose(13)
            x4,y4= getpose(15)
            a,b=getpose(2)
        
            cm,d=getpose(5)
            
            e,f=getpose(0)
            
            g,h=getpose(10)
            r,s=getpose(9)
            l,m=getpose(12)
            o,t=getpose(11)
        
            pygame.draw.circle(screen, (255,0,0),(e-20,f-10), 7)
            pygame.draw.circle(screen, (255,0,0),(e+20,f-10), 7)
        #eyebrows
            pygame.draw.line(screen,(255,255,255), (e-25,(f-23)),(e-5,(f-23)),4)
            pygame.draw.line(screen,(255,255,255), (e+15,(f-23)),(e+35,(f-23)),4)


            pygame.draw.line(screen,(0,0,0), (e-25,(f-23)),(e-5,(f-23)),2)
            pygame.draw.line(screen,(0,0,0), (e+15,(f-23)),(e+35,(f-23)),2)
            #eyes
            pygame.draw.circle(screen, (255,255,255),(e-20,f-10), 5)
            pygame.draw.circle(screen, (255,255,255),(e+20,f-10), 5)

            pygame.draw.circle(screen, (0,0,0),(e-20,f-10), 2)
            pygame.draw.circle(screen, (0,0,0),(e+20,f-10), 2)
            
            #nose
            pygame.draw.line(screen,(0,0,0), (e,(f-10)),(e,(f+10)),2)
            pygame.draw.line(screen,(0,0,0), (e,(f-10)),(e,(f+10)),2)
            
            '''pygame.draw.circle(screen, (0,0,0),(e-3,f+15), 3)
            pygame.draw.circle(screen, (0,0,0),(e+3,f+15), 3)
            pygame.draw.circle(screen, (255,255,255),(e-3,f+15), 2)
            pygame.draw.circle(screen, (255,255,255),(e+3,f+15), 2)'''

        #mouth
            pygame.draw.line(screen,(0,0,0), (r-10,s-15),(g+10,h-15),5)
            pygame.draw.line(screen,(255,0,0), (r-10,s-15),(g+10,h-15),3)
            
            #neck
            pygame.draw.line(screen,(0,0,0), (g,h+5),(g,h+60),2)
            pygame.draw.line(screen,(0,0,0), (l,m),(g,h+60),2)
            pygame.draw.line(screen,(0,0,0), (o,t),(r,s+60),2)
            pygame.draw.line(screen,(0,0,0), (r,s+60),(r,s+5),2)
            
            #hair
            '''pygame.draw.line(screen,(0,0,0), (c,d-2),(c,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c+30,d-5),(c+30,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c+10,d-2),(c+10,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c+40,d-2),(c+40,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c+20,d-5),(c+20,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c+50,d-1),(c+50,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c+60,d+5),(c+60,d-20),2)
            pygame.draw.line(screen,(0,0,0), (c-10,d+5),(c-10,d-20),2)'''


            #chest 
            '''pygame.draw.circle(screen, (0,0,0),(g-20,h+200), 40)
            pygame.draw.circle(screen, (0,0,0),(r+20,s+200), 40)
            pygame.draw.circle(screen, (255,255,255),(g-20,h+200), 38)
            pygame.draw.circle(screen, (255,255,255),(r+20,s+200), 38)
            pygame.draw.circle(screen, (0,0,0),(g-20,h+200), 5)
            pygame.draw.circle(screen, (0,0,0),(r+20,s+200), 5)

            #6packs
            pygame.draw.line(screen,(0,0,0), (e,f+300),(e,f+500),2)
            pygame.draw.line(screen,(0,0,0), (e-50,f+350),(e+50,f+350),2)
            pygame.draw.line(screen,(0,0,0), (e-50,f+400),(e+50,f+400),2)
            pygame.draw.line(screen,(0,0,0), (e-50,f+450),(e+50,f+450),2)'''
            


                # HAND STUFF STARTS
            # Check if hands are detected
            if results_hands.multi_hand_landmarks:
                for landmarks in results_hands.multi_hand_landmarks:

                    # Create an empty sub-list for each hand.
                    coordsx_hands.append([])
                    coordsy_hands.append([])
                    
                    for point in landmarks.landmark:
                        
                        # Extract hand landmarks (x, y, z) and put them in the respective sub-list.
                        x, y, _ = int(point.x * frame.shape[1]), int(point.y * frame.shape[0]), int(point.z * frame.shape[0])
                        coordsx_hands[i].append(x)
                        coordsy_hands[i].append(y)
                        
        
                        # Draw a circle at each hand landmark
                        #pygame.draw.circle(screen, (0,0,255), (x,y), 5)
                        #cv2.circle(frame, (x, y), 5, (0,255, 0), -1)
                    
                    i+=1
                
            # Hand Drawing
            if coordsx_hands!=[]:
                #print(coordsx_hands)
                for itr in range(len(coordsx_hands)):
                    
                    # Thumb
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][0],coordsy_hands[itr][0]), (coordsx_hands[itr][1],coordsy_hands[itr][1]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][1],coordsy_hands[itr][1]), (coordsx_hands[itr][2],coordsy_hands[itr][2]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][2],coordsy_hands[itr][2]), (coordsx_hands[itr][3],coordsy_hands[itr][3]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][3],coordsy_hands[itr][3]), (coordsx_hands[itr][4],coordsy_hands[itr][4]),3)
                    
                    # Middle
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][9],coordsy_hands[itr][9]), (coordsx_hands[itr][10],coordsy_hands[itr][10]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][10],coordsy_hands[itr][10]), (coordsx_hands[itr][11],coordsy_hands[itr][11]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][11],coordsy_hands[itr][11]), (coordsx_hands[itr][12],coordsy_hands[itr][12]),3)
                    
                    # Ring
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][13],coordsy_hands[itr][13]), (coordsx_hands[itr][14],coordsy_hands[itr][14]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][14],coordsy_hands[itr][14]), (coordsx_hands[itr][15],coordsy_hands[itr][15]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][15],coordsy_hands[itr][15]), (coordsx_hands[itr][16],coordsy_hands[itr][16]),3)
                    
                    # Little
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][17],coordsy_hands[itr][17]), (coordsx_hands[itr][18],coordsy_hands[itr][18]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][18],coordsy_hands[itr][18]), (coordsx_hands[itr][19],coordsy_hands[itr][19]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][19],coordsy_hands[itr][19]), (coordsx_hands[itr][20],coordsy_hands[itr][20]),3)
                    
                    # Index
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][5],coordsy_hands[itr][5]), (coordsx_hands[itr][6],coordsy_hands[itr][6]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][6],coordsy_hands[itr][6]), (coordsx_hands[itr][7],coordsy_hands[itr][7]),3)
                    pygame.draw.line(screen,(0,0,0), (coordsx_hands[itr][7],coordsy_hands[itr][7]), (coordsx_hands[itr][8],coordsy_hands[itr][8]),3)
                    

            for i in range(num_balls):
                if(ball_positions[i][1]<=600):
                    ball_speed=random.uniform(BaseSpeed,BaseSpeed+8)
                    ball_positions[i][1] += ball_speed

                else:
                    x=random.uniform(0,255)
                    y=random.uniform(0,255) 
                    z=random.uniform(0,255)
                    ball_color=((x,y,z))
                    ball_color1=((z,y,x))
                    ball_positions[i][0]=random.uniform(0,width)
                    ball_positions[i][1]=0

        # Clear the screen
        #screen.fill((255, 255, 255))  # White

        # Draw each ball
            for i in range(num_balls):
                p,q=int(ball_positions[i][0]), int(ball_positions[i][1])
                pygame.draw.circle(screen, ball_color, (int(ball_positions[i][0]), int(ball_positions[i][1])), ball_radius)
                cv2.circle(frame,(int(ball_positions[i][0]), int(ball_positions[i][1])), ball_radius, ball_color1,-1)
                area=abs(((x1)*(y2-q)+(x2)*(q-y1)+(p)*(y1-y2)))
                area1=abs(((x3)*(y4-q)+(x4)*(q-y3)+(p)*(y3-y4)))
                d1=((p-x1)**2+(q-y1)**2)**0.5
                d2=((p-x2)**2+(q-y2)**2)**0.5
                d3=((x2-x1)**2+(y2-y1)**2)**0.5
                d4=((p-x3)**2+(q-y3)**2)**0.5
                d5=((p-x4)**2+(q-y4)**2)**0.5
                d6=((x4-x3)**2+(y4-y3)**2)**0.5

                if(d1>d2):
                    if((area<1000) and ((d1**2)<=(d2**2 + d3**2))):
                        c=c+1
                        ball_positions[i][1]=0
                        ball_positions[i][0]=random.uniform(0,width)
                        x=random.uniform(0,255)
                        y=random.uniform(0,255) 
                        z=random.uniform(0,255)
                        ball_color=((x,y,z))
                        ball_color1=((z,y,x))
                        #print("ball ",i," ",area)
                if(d2>d1):
                    if((area<1000) and (d2**2)<=(d1**2 + d3**2)):
                        c=c+1
                        ball_positions[i][1]=0
                        ball_positions[i][0]=random.uniform(0,width)
                        x=random.uniform(0,255)
                        y=random.uniform(0,255) 
                        z=random.uniform(0,255)
                        ball_color=((x,y,z))
                        ball_color1=((z,y,x))
                        

                if(d4>d5):
                    if((area1<1000) and (d4**2)<=(d5**2 + d6**2)):
                        c=c+1
                        ball_positions[i][1]=0
                        ball_positions[i][0]=random.uniform(0,width)
                        x=random.uniform(0,255)
                        y=random.uniform(0,255) 
                        z=random.uniform(0,255)
                        ball_color=((x,y,z))
                        ball_color1=((z,y,x))
                        
                if(d5>d4):
                    if(( area1<1000) and (d5**2)<=(d4**2 + d6**2)):
                        c=c+1
                        ball_positions[i][1]=0
                        ball_positions[i][0]=random.uniform(0,width)
                        x=random.uniform(0,255)
                        y=random.uniform(0,255) 
                        z=random.uniform(0,255)
                        ball_color=((x,y,z))
                        ball_color1=((z,y,x))
        except:
            print()
        
        # Cap the frame rate
        clock.tick(60)
        # HAND STUFF ENDS
    
        # Display the frame
        cv2.imshow('Hand Tracking', frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Flip display to show stuff
        pygame.display.flip()


    # Set up display
    width, height = 1000,1000
    '''screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Picture Display")

    # Load image
    image_path = "Ballpit2.jpg"
    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print("Unable to load image:", image_path)
        print(e)
        sys.exit()'''

    # Set up font
    font = pygame.font.Font(None, 80)  # You can adjust the font size and style as needed

    # Define the statement
    statement_text1 = "   GAME OVER"

    # Render the text
    text_surface1 = font.render(statement_text1, True, (255,255,255))

    # Define the statement
    statement_text2 = f"YOUR SCORE:  {c}"
    font = pygame.font.Font(None, 50)
    # Render the text
    text_surface2 = font.render(statement_text2, True, (255,255,255))
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                cap.release()
                cv2.destroyAllWindows()
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the image on the screen
        #makebackground("p1.jpg")
        # screen.blit(image, (0, 0))

        # Draw the text on top of the image
        screen.blit(text_surface1, (300,350))  # Adjust the position of the text as needed
        # Draw the text on top of the image
        screen.blit(text_surface2, (300,425))  # Adjust the position of the text as needed

        # Update the display
        pygame.display.flip()

    # Release the webcam and close all windows
    #pygame.quit()    
    #cap.release()
    #cv2.destroyAllWindows()


# Initialize Pygame
pygame.init()

# Set up display
width, height = 800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Entry Point")
screen.fill((255,255,255))
#makebackground("p1.jpg")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Define the buttons
button1_width, button1_height = 200, 50
button1_x, button1_y = 100, 200

button2_width, button2_height = 200, 50
button2_x, button2_y = 500, 200

# Define the button texts
button1_text = "Easy Mode"
button2_text = "Difficult Mode"

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if Button 1 is clicked
            if button1_x <= mouse_x <= button1_x + button1_width and button1_y <= mouse_y <= button1_y + button1_height:
                print("Button 1 clicked!")
                Game(45,4,0)

            # Check if Button 2 is clicked
            elif button2_x <= mouse_x <= button2_x + button2_width and button2_y <= mouse_y <= button2_y + button2_height:
                print("Button 2 clicked!")
                Game(30,5,8)

    # Clear the screen
   

    # Draw Button 1
    pygame.draw.rect(screen, black, (button1_x, button1_y, button1_width, button1_height))
    text_surface1 = font.render(button1_text, True, white)
    text_position1 = ((button1_x + button1_width // 2) - text_surface1.get_width() // 2,
                      (button1_y + button1_height // 2) - text_surface1.get_height() // 2)
    screen.blit(text_surface1, text_position1)

    # Draw Button 2
    pygame.draw.rect(screen, black, (button2_x, button2_y, button2_width, button2_height))
    text_surface2 = font.render(button2_text, True, white)
    text_position2 = ((button2_x + button2_width // 2) - text_surface2.get_width() // 2,
                      (button2_y + button2_height // 2) - text_surface2.get_height() // 2)
    screen.blit(text_surface2, text_position2)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

