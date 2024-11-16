# def test1():
#     time.sleep(5)
#     send_msg(port, 'hello!')
#     time.sleep(3)
#     send_msg(port, MsgOne(0, 160))
#     time.sleep(3)
#     send_msg(port, MsgAll([60, 100, 80, 80]))

# def main_old(port: serial.Serial):
#     global IS_CHANGED
#     # print(f"Control speed: {[e / CYCLE_TIME for e in ADD_POS]} deg/sec")
#
#     # Events
#     # keyboard.on_press_key('f2',    set_is_control)
#     keyboard.on_press_key('enter', print_cur_pos)
#
#     keyboard.on_press_key('up',    control_with_keys)
#     keyboard.on_press_key('down',  control_with_keys)
#     keyboard.on_press_key('left',  control_with_keys)
#     keyboard.on_press_key('right', control_with_keys)
#     keyboard.on_press_key('w',     control_with_keys)
#     keyboard.on_press_key('a',     control_with_keys)
#     keyboard.on_press_key('s',     control_with_keys)
#     keyboard.on_press_key('d',     control_with_keys)
#
#     while True:
#         if keyboard.is_pressed('esc'):
#             break
#
#         get_msg_all(port, debug=(not IS_CONTROL))
#
#         # Control
#         if IS_CONTROL:
#             pass
#             # if IS_CHANGED:
#             #     print('seng change')
#             #     send_msg(port, MsgAll(CUR_POS))
#             #     IS_CHANGED = False
#         else:
#             line = input("Command in<: ")
#             # Check line
#             send_msg(port, line)

# def test(port: serial.Serial, debug: bool):
#     send_msg(port, 'Hello', debug=debug)
#
#     t1 = time.time()
#     msg_late_task(port, 2000, MsgOne(0, 90))
#     msg_late_task(port, 2000, MsgAll([120, 95, 85, 60]))
#     print(f"{time.time() - t1} seconds")
#     msg_late_task(port, 2000, MsgAll([120, 95, 85, 60]))
#     print(f"{time.time() - t1} seconds")
#     msg_late_task(port, 2000, MsgAll([20, 90, 90, 90]))
#     print(f"{time.time() - t1} seconds")
#     msg_late_task(port, 2000, MsgOne(n_servo=0, servo_pos=90))
#     print(f"{time.time() - t1} seconds")
#
#     return

# def save_key():
#     print("Saving key...")
#     key = input("Key: ").lower()  # keyboard.read_key().strip().lower()
#     print(key, CUR_POS)
#     if len(key) == 1:
#         with open('kb.txt', 'w') as f:
#             f.write(f'{key};{" ".join(map(str, CUR_POS))}\n')
