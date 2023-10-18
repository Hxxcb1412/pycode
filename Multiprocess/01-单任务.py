import time

# Sing
def sing():
    for i in range(3):
        print("Sing...")
        time.sleep(0.5)

def dance():
    for i in range(3):
        print("Dance...")
        time.sleep(0.5)

if __name__ == '__main__':
    sing()
    dance()