def constrol_display(loop_status: number, display_status: number):
    if display_status == 1:
        if loop_status == 1:
            basic.show_icon(IconNames.YES)
        else:
            basic.show_icon(IconNames.NO)
    else:
        basic.clear_screen()

def on_button_pressed_a():
    global display_flag
    if display_flag:
        display_flag = 0
        basic.clear_screen()
    else:
        display_flag = 1
        if flag == 1:
            basic.show_icon(IconNames.YES)
        else:
            basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global flag, timer
    if flag:
        flag = 0
        timer = 0
        basic.show_icon(IconNames.NO)
    else:
        flag = 1
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.clear_screen()
    if timer / 1000 < 60:
        basic.show_string("" + str(timer / 1000) + "s")
    else:
        basic.show_string("" + str(Math.round(timer / 60000)) + "min")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

pause_time = 0
timer = 0
display_flag = 0
flag = 0
mouse.start_mouse_service()
flag = 1
display_flag = 1
timer = 0
pause_time += 2500

def on_forever():
    global timer
    constrol_display(flag, display_flag)
    if flag:
        mouse.movexy(222, 0)
        basic.pause(pause_time)
        mouse.movexy(-222, 0)
        basic.pause(pause_time)
        timer = timer + pause_time * 2
basic.forever(on_forever)
