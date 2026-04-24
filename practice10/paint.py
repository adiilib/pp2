import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    
    radius = 15
    drawing_mode = 'line' 
    color = (0, 0, 255) 
    
    
    points = [] 

    while True:
        screen.fill((255, 255, 255))
        
        
        instr = "L: Line, R: Rect, C: Circle, E: Eraser | 1: Red, 2: Green, 3: Blue"
        txt = pygame.font.SysFont("Arial", 18).render(instr, True, (0,0,0))
        screen.blit(txt, (10, 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l: drawing_mode = 'line'
                if event.key == pygame.K_r: drawing_mode = 'rect'
                if event.key == pygame.K_c: drawing_mode = 'circle'
                if event.key == pygame.K_e: drawing_mode = 'eraser'
                
                if event.key == pygame.K_1: color = (255, 0, 0)
                if event.key == pygame.K_2: color = (0, 255, 0)
                if event.key == pygame.K_3: color = (0, 0, 255)

        
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if drawing_mode == 'line':
                points.append(('circle', color, pos, radius))
            elif drawing_mode == 'eraser':
                points.append(('circle', (255, 255, 255), pos, radius))
            elif drawing_mode == 'rect':
                points.append(('rect', color, (pos[0], pos[1], 50, 50)))
            elif drawing_mode == 'circle':
                points.append(('circle', color, pos, 30))

        
        for p in points:
            if p[0] == 'circle':
                pygame.draw.circle(screen, p[1], p[2], p[3])
            elif p[0] == 'rect':
                pygame.draw.rect(screen, p[1], p[2])

        pygame.display.flip()
        clock.tick(60)

main()
