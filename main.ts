function constrol_display (loop_status: number, display_status: number) {
    if (display_status == 1) {
        if (loop_status == 1) {
            basic.showIcon(IconNames.Yes)
        } else {
            basic.showIcon(IconNames.No)
        }
    } else {
        basic.clearScreen()
    }
}
input.onButtonPressed(Button.A, function () {
    if (display_flag) {
        display_flag = 0
        basic.clearScreen()
    } else {
        display_flag = 1
        if (flag == 1) {
            basic.showIcon(IconNames.Yes)
        } else {
            basic.showIcon(IconNames.No)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    if (flag) {
        flag = 0
        timer = 0
        basic.showIcon(IconNames.No)
    } else {
        flag = 1
        basic.showIcon(IconNames.Yes)
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
    if (timer / 1000 < 60) {
        basic.showString("" + timer / 1000 + "s")
    } else {
        basic.showString("" + Math.round(timer / 60000) + "min")
    }
})
let pause_time = 0
let timer = 0
let display_flag = 0
let flag = 0
mouse.startMouseService()
flag = 1
display_flag = 1
timer = 0
pause_time += 2500
basic.forever(function () {
    constrol_display(flag, display_flag)
    if (flag) {
        mouse.movexy(222, 0)
        basic.pause(pause_time)
        mouse.movexy(-222, 0)
        basic.pause(pause_time)
        timer = timer + pause_time * 2
    }
})
