
 
import pygame
import math 

# Initialize Pygame
pygame.init()
gameClock = pygame.time.Clock()

# Set window dimensions
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
# Colors
white = (255, 255, 255)
gray = (120, 120, 120)
black = (0, 0, 0)
green = (20, 255, 20)

radius = 35
line_width = 2


Screen_Offset_x = 0 
Screen_Offset_y = 0 

font = pygame.font.SysFont('Times New Roman', 30)
k_image = font.render('K', False, (0, 0, 0)); 
s_image = font.render('S', False, (0, 0, 0)); 


NODE_TYPE_KEY = "key"
NODE_TYPE_START = "start"
NODE_TYPE_EMPTY = "empty"

def draw_line(screen, sx, sy, ex, ey, locked, has_end_node):
    global black 
    global radius 
    global Screen_Offset_x 
    global Screen_Offset_y
    global line_width
     
    to_x = ex - sx 
    to_y = ey - sy 

    mag = math.sqrt(to_x*to_x + to_y*to_y)
    if mag == 0: 
        return 
    
    to_x /= mag 
    to_y /= mag

    lwx = (-to_y)*line_width
    lwy = (to_x)*line_width

    to_x *= radius 
    to_y *= radius 

    perp_x = -to_y 
    perp_y = to_x 


    tex = ex
    tey = ey
    tsx = sx + to_x 
    tsy = sy + to_y

    if has_end_node:
        tex -= to_x
        tey -= to_y 

    if locked:
        cx = (tex + tsx) * 0.5    
        cy = (tey + tsy) * 0.5

        pygame.draw.aaline(screen, black, (cx + perp_x + Screen_Offset_x, cy + perp_y + Screen_Offset_y), (cx - perp_x + Screen_Offset_x, cy - perp_y + Screen_Offset_y))
    
    pygame.draw.aaline(screen, black, (tsx + Screen_Offset_x, tsy + Screen_Offset_y), (tex + Screen_Offset_x, tey + Screen_Offset_y))

def add_edge(id1, id2, locked):
    global edges 
    already_exists = False 
    for (nid1, nid2, _) in edges: 
        if nid1 == id1 and nid2 == id2:
            already_exists = True 
            break 
        if nid1 == id2 and nid2 == id1:
            already_exists = True 
            break
    
    if not already_exists:
        edges.append((id1, id2, locked))

def draw_node(screen, node_type, x, y, highlight):
    global black 
    global white 
    global radius 
    global green 
    global NODE_TYPE_KEY 
    global NODE_TYPE_START
    global k_image
    global s_image

    pygame.draw.circle(screen, black, (x + Screen_Offset_x, y + Screen_Offset_y), radius)
    if not highlight:
        pygame.draw.circle(screen, white, (x + Screen_Offset_x, y + Screen_Offset_y), radius - 2)
    else: 
        pygame.draw.circle(screen, green, (x + Screen_Offset_x, y + Screen_Offset_y), radius - 2)
    
    if node_type == NODE_TYPE_KEY:
        screen.blit(k_image, (x - k_image.get_width() / 2.5 + Screen_Offset_x, y - k_image.get_height() / 2.1 + Screen_Offset_y))
    elif node_type == NODE_TYPE_START:
        screen.blit(s_image, (x - k_image.get_width() / 2.5 + Screen_Offset_x, y - k_image.get_height() / 2.1 + Screen_Offset_y))    


nodes = [] 
edges = []


toggle = False 
dragging = False 
dragging_node = -1 


# Game loop
running = True
while running:
    deltaTime = gameClock.tick(144)

    # Handle events
    mouse_buttons = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    
    x -= Screen_Offset_x
    y -= Screen_Offset_y

    c_x = float(int(x / (radius) + 0.5) * radius) 
    c_y = float(int(y / (radius) + 0.5) * radius) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if keys[pygame.K_s]: 
                nodes.append((c_x, c_y, NODE_TYPE_START))
            elif keys[pygame.K_k]: 
                nodes.append((c_x, c_y, NODE_TYPE_KEY))
            elif keys[pygame.K_e]: 
                nodes.append((c_x, c_y, NODE_TYPE_EMPTY))
            


    # Clear the screen
    screen.fill(gray)


    if keys[pygame.K_s]: 
        draw_node(screen, NODE_TYPE_START, c_x, c_y, False) 
    elif keys[pygame.K_k]: 
        draw_node(screen, NODE_TYPE_KEY, c_x, c_y, False) 
    elif keys[pygame.K_e]: 
        draw_node(screen, NODE_TYPE_EMPTY, c_x, c_y, False) 

    speed = 0.5 
    if keys[pygame.K_UP]:  
        Screen_Offset_y += speed*deltaTime
    if keys[pygame.K_DOWN]:  
        Screen_Offset_y -= speed*deltaTime 
    if keys[pygame.K_LEFT]:  
        Screen_Offset_x += speed*deltaTime 
    if keys[pygame.K_RIGHT]:  
        Screen_Offset_x -= speed*deltaTime 
        


    closest_node_id = -1  
    closest_node_x = 0 
    closest_node_y = 0 
    closest_d = 10000

    node_id = 0 
    for (mx, my, nt) in nodes:
        d = ((mx - x)*(mx - x) +(my - y)*(my - y)) 
        if d < closest_d:
            closest_d = d 
            closest_node_x = mx 
            closest_node_y = my 
            closest_node_id = node_id 
        node_id += 1

    

    if closest_node_id != -1:
        if mouse_buttons[0] and not dragging:
            dragging = True 
            dragging_node = closest_node_id
 
    if dragging: 
        if not keys[pygame.K_SPACE]:
            is_locked = True 
        else: 
            is_locked = False 

        if not mouse_buttons[0]:
            if closest_node_id != -1 and closest_node_id != dragging_node:   
                add_edge(dragging_node, closest_node_id, is_locked)
            dragging = False 
        else: 
            (nx, ny, _) = nodes[dragging_node]
            
            if closest_node_id != -1 and closest_node_id != dragging_node:   
                (nx2, ny2, _) = nodes[closest_node_id]
                draw_line(screen, nx, ny, nx2, ny2, is_locked, True)
            else:
                draw_line(screen, nx, ny, x, y, is_locked, False)
    
    for (id1, id2, locked) in edges:
        (nx1, ny1, _) = nodes[id1]
        (nx2, ny2, _) = nodes[id2]
        draw_line(screen, nx1, ny1, nx2, ny2, locked, True)
        

    if not dragging:
        if keys[pygame.K_DELETE]:
            if not toggle:
                toggle = True 
                if closest_node_id != -1: 
                    edge_id = 0 
                    edges_to_remove = [] 
                    for (id1, id2, _) in edges: 
                        if id1 == closest_node_id or id2 == closest_node_id: 
                            edges_to_remove.append(edge_id - len(edges_to_remove))
                        edge_id += 1 
                    
                    for i in edges_to_remove:
                        edges.pop(i) # Index already corrected for future removals 

                    for i in range(len(edges)):
                        (id1, id2, locked) = edges[i]
                        if id1 > closest_node_id:
                            id1 -= 1 
                        if id2 > closest_node_id:
                            id2 -= 1 
                        
                        edges[i] = (id1, id2, locked)

                    nodes.pop(closest_node_id)
        else: 
            toggle = False     

    node_id = 0 
    for (mx, my, nt) in nodes:
        draw_node(screen, nt, mx, my, node_id == closest_node_id) 
        node_id += 1


    # Draw the circle
    
    # pygame.draw.arc(screen, black, (x - radius, y - radius, radius * 2, radius * 2), 0, 2.0*3.141592653, 1)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()