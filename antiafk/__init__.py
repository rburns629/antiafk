"""
    Author: Robert Burns
    Date:   01/09/2019 
    Version: 1.0.0
    Overview: The Antiafk CLI Python package was created to allow users the option to trigger keyboard events on specified intervals for a specified duration of time. 
"""
from pynput.keyboard     import Key, Controller
from .utils              import std_keys, spec_keys, get_time
import click, time, datetime


@click.command()
@click.option('-k', '--key', required=True, type=str, help='Specify the key that you want to trigger in intervals')
@click.option('-i', '--interval', nargs=2, default=('5', 'Minutes'), type=str, help='Set the interval at which the specified key is triggered. Default is set to: 5 Minutes')  # Default: 5 minutes
@click.option('-s', '--stop', nargs=2, default=('1', 'Hour'), type=str, help='Set the stop timer for the program to trigger a StopExecution and exit. Default is set to: 1 Hour')  # Default: 1 hour
def cli(key: str, interval: tuple, stop: tuple) -> None:
    """
        Welcome to the Anti-AFK program. Where we say NO to being AFK and disconnected from our precious. Even for a moment, damnit. \n
        The purpose of this program is to give you the option to choose a key that you want the program to execute periodically. \n
        You can also choose your own interval at which the key specified is pressed, which is set to 5 minutes by default. \n
        The -s / --stop agurment has been provided to you as an optional argument if you want the program to trigger a StopExecution, and exit automatically.
        Supported keys are as followed: \n
        Standard keys: \n
            !, ", #, $, %, &, ', (, ), *, +, ,, -, ., /, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, :, ;, <, =, >, ?, @, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, [, \\, ], ^, _, `, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, {, |, }, ~\n
        Special Keys: \n
            alt, alt_r, backspace, caps_lock, cmd, cmd_r, ctrl, ctrl_r, delete, down, end, enter, esc, f1, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f2, f20, f3, f4, f5, f6, f7, f8, f9, home, left, page_down, page_up, right, shift, shift_r, space, tab, up\n
    """
    try:
        standard_keys   = std_keys()
        special_keys    = spec_keys()
        btn_interval    = get_time(int(interval[0]), interval[1])   # 5 Minutes
        interval_stop   = time.localtime(time.time() + get_time(int(stop[0]), stop[1]))           # 1 Hour

        if key and btn_interval:
            key_pressed     = key if key in standard_keys else special_keys[key]
            keyboard        = Controller()

            while time.localtime(time.time()) < interval_stop:
                keyboard.press(key_pressed)
                print(f'{key_pressed} pressed at {time.strftime("%D %T", time.localtime(time.time()))}')
                keyboard.release(key_pressed)
                print(f'{key_pressed} released at {time.strftime("%D %T", time.localtime(time.time()))}')
                time.sleep(btn_interval)

    except Exception as e:
        raise e
    finally:
        print(f'The time specified in stop timer has been exhausted! Exiting...')
        exit()


if __name__ == "__main__":
    cli()
