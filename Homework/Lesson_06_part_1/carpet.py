def draw_carpet(w, h):
    if h >= 2 and w > 4:
        print("▓" + "░" * (w - 2) + "▓")

        if h > 2:
            for i in range(0, h - 2):
                print("▓" + "░" + "▒" * (w - 4) + "░" + "▓")
        print("▓" + "░" * (w - 2) + "▓")

    else:
        print("Ошибка. Минимальное значение w=5, h=2")


draw_carpet(5, 2)
draw_carpet(5, 3)
draw_carpet(6, 3)
draw_carpet(6, 4)
draw_carpet(6, 7)
draw_carpet(10, 4)
