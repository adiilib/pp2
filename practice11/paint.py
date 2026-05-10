import pygame
import math


def draw_shape(surface, stype, color, sp, ep, radius=15):
    if stype == "dot":
        pygame.draw.circle(surface, color, sp, radius)

    elif stype == "rect":
        x = min(sp[0], ep[0])
        y = min(sp[1], ep[1])
        w = abs(ep[0] - sp[0])
        h = abs(ep[1] - sp[1])
        if w > 0 and h > 0:
            pygame.draw.rect(surface, color, (x, y, w, h))

    elif stype == "square":
        side = min(abs(ep[0] - sp[0]), abs(ep[1] - sp[1]))
        if side > 0:
            dx = side if ep[0] >= sp[0] else -side
            dy = side if ep[1] >= sp[1] else -side
            x = min(sp[0], sp[0] + dx)
            y = min(sp[1], sp[1] + dy)
            pygame.draw.rect(surface, color, (x, y, side, side))

    elif stype == "circle":
        r = int(math.hypot(ep[0] - sp[0], ep[1] - sp[1]) / 2)
        cx = (sp[0] + ep[0]) // 2
        cy = (sp[1] + ep[1]) // 2
        if r > 0:
            pygame.draw.circle(surface, color, (cx, cy), r)

    elif stype == "right_tri":
        pts = [sp, (ep[0], sp[1]), ep]
        pygame.draw.polygon(surface, color, pts)

    elif stype == "eq_tri":
        bx1 = min(sp[0], ep[0])
        bx2 = max(sp[0], ep[0])
        base = bx2 - bx1
        if base > 0:
            h = int(base * math.sqrt(3) / 2)
            by = max(sp[1], ep[1])
            cx = (bx1 + bx2) // 2
            pts = [(bx1, by), (bx2, by), (cx, by - h)]
            pygame.draw.polygon(surface, color, pts)

    elif stype == "rhombus":
        cx = (sp[0] + ep[0]) // 2
        cy = (sp[1] + ep[1]) // 2
        pts = [(cx, sp[1]), (ep[0], cy), (cx, ep[1]), (sp[0], cy)]
        pygame.draw.polygon(surface, color, pts)


def main():
    pygame.init()
    screen = pygame.display.set_mode((900, 650))
    pygame.display.set_caption("Paint")
    clock = pygame.time.Clock()

    radius = 15
    drawing_mode = "line"
    color = (0, 0, 255)
    shapes = []
    start_pos = None

    freehand_modes = ("line", "eraser")
    shape_modes = ("rect", "square", "circle", "right_tri", "eq_tri", "rhombus")

    font = pygame.font.SysFont("Arial", 13)
    mode_font = pygame.font.SysFont("Arial", 14, bold=True)

    while True:
        screen.fill((255, 255, 255))

        instr = "L:Line  R:Rect  S:Square  C:Circle  T:Right-Tri  G:Eq-Tri  H:Rhombus  E:Eraser  |  1:Red  2:Green  3:Blue"
        screen.blit(font.render(instr, True, (0, 0, 0)), (10, 8))
        screen.blit(mode_font.render(f"Mode: {drawing_mode}", True, (60, 60, 200)), (10, 26))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                mode_map = {
                    pygame.K_l: "line",
                    pygame.K_r: "rect",
                    pygame.K_s: "square",
                    pygame.K_c: "circle",
                    pygame.K_t: "right_tri",
                    pygame.K_g: "eq_tri",
                    pygame.K_h: "rhombus",
                    pygame.K_e: "eraser",
                }
                if event.key in mode_map:
                    drawing_mode = mode_map[event.key]
                if event.key == pygame.K_1:
                    color = (220, 0, 0)
                if event.key == pygame.K_2:
                    color = (0, 180, 0)
                if event.key == pygame.K_3:
                    color = (0, 0, 220)

            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP and start_pos:
                if drawing_mode in shape_modes:
                    shapes.append((drawing_mode, color, start_pos, event.pos))
                start_pos = None

        if pygame.mouse.get_pressed()[0] and drawing_mode in freehand_modes:
            pos = pygame.mouse.get_pos()
            c = color if drawing_mode == "line" else (255, 255, 255)
            shapes.append(("dot", c, pos, pos))

        for stype, scolor, sp, ep in shapes:
            draw_shape(screen, stype, scolor, sp, ep, radius)

        if start_pos and pygame.mouse.get_pressed()[0] and drawing_mode in shape_modes:
            cur = pygame.mouse.get_pos()
            draw_shape(screen, drawing_mode, (190, 190, 190), start_pos, cur, radius)

        pygame.display.flip()
        clock.tick(60)


main()
