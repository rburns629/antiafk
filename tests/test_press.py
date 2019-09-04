from pynput.keyboard import Key, Controller
import time

class TestKey:
    __key__      = 'space'
    __keyboard__ = Controller()

    def has_attr(self):
        assert getattr(Key, self.__key__)

    def test_keypress(self):
        assert self.__keyboard__.press(getattr(Key, self.__key__)) == None
        
    def test_keypress_release(self):
        assert self.__keyboard__.release(getattr(Key, self.__key__)) == None

    def test_keypress_interval(self):
        interval    = 10
        start       = time.time()

        self.__keyboard__.press(getattr(Key, self.__key__))
        self.__keyboard__.release(getattr(Key, self.__key__))

        time.sleep(interval)

        self.__keyboard__.press(getattr(Key, self.__key__))
        self.__keyboard__.release(getattr(Key, self.__key__))

        assert int(time.time() - start) >= interval 

    def test_keypress_stop(self):
        iteration       = 10
        start           = time.time()
        stop_iteration  = 30

        while int(time.time() - start) < stop_iteration:
            self.__keyboard__.press(getattr(Key, self.__key__))
            self.__keyboard__.release(getattr(Key, self.__key__))
            time.sleep(iteration)

        assert int(time.time() - start) >= stop_iteration

