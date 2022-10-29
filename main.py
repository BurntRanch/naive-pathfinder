import numpy as np
import cv2
import sys
import threading

cursor_pos = (0, 0)
width = 100
height = 100
sys.setrecursionlimit(10**6)
path_color = np.array([255, 255, 255])
pot_color = np.array([255, 0, 255])

def recursive_traverse(x, y, img):
    next_x = x
    next_y = y
    if next_x == 0 and next_y == 0:
        print("Searching for entrance!")
        while next_x < len(img) and not np.array_equal(img[next_x][0], path_color):
            next_x += 1
        if np.array_equal(img[next_x if next_x < len(img) else len(img) - 1][0], path_color):
            print("Found entrance!")
        else:
            while next_y < len(img[0]) and not np.array_equal(img[0][next_y], path_color):
                next_y += 1
            if np.array_equal(img[0][next_y if next_y < len(img[0]) else len(img[0]) - 1], path_color):
                print("Found entrance!")
            else:
                return
    if next_x >= len(img):
        return
    if next_y >= len(img[next_x]):
        next_y = 0
        next_x += 1
    moved = False
    print("Currently in", next_x, next_y)
    if np.array_equal(img[next_x][next_y], path_color):
        if next_x < len(img) - 1 and np.array_equal(img[next_x + 1][next_y], path_color):
            moved = True
            print("Going down!")
            while next_x < len(img) - 1 and np.array_equal(img[next_x + 1][next_y], path_color):
                out[next_x][next_y] = [255, 255, 0]
                next_x += 1
                if next_y < len(img[next_x]) - 1 and np.array_equal(img[next_x][next_y + 1], path_color) and np.array_equal(img[next_x + 1][next_y], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x, next_y + 1, img))
                    t1.start()
                    print("We can go to the right @", next_y, next_x)
                    t1.join()
                if next_y > 0 and np.array_equal(img[next_x][next_y - 1], path_color) and np.array_equal(img[next_x + 1][next_y], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x, next_y - 1, img))
                    t1.start()
                    print("We can go to the left @", next_y, next_x)
                    t1.join()
        elif next_y < len(img[next_x]) - 1 and np.array_equal(img[next_x][next_y + 1], path_color):
            moved = True
            print("Going right!")
            while next_y < len(img[next_x]) - 1 and np.array_equal(img[next_x][next_y + 1], path_color):
                out[next_x][next_y] = [255, 255, 0]
                next_y += 1
                if next_x < len(img) - 1 and np.array_equal(img[next_x + 1][next_y], path_color) and np.array_equal(img[next_x][next_y + 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x + 1, next_y , img))
                    t1.start()
                    print("We can go down @", next_y, next_x)
                    t1.join()
                if next_x > 0 and np.array_equal(img[next_x - 1][next_y], path_color) and np.array_equal(img[next_x][next_y + 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x - 1, next_y, img))
                    t1.start()
                    print("We can go up @", next_y, next_x)
                    t1.join()
        elif next_y > 0 and np.array_equal(img[next_x][next_y - 1], path_color):
            moved = True
            print("Going left!")
            while next_y > 0 and np.array_equal(img[next_x][next_y - 1], path_color):
                out[next_x][next_y] = [255, 255, 0]
                next_y -= 1
                if next_x < len(img) - 1 and np.array_equal(img[next_x + 1][next_y], path_color) and np.array_equal(img[next_x][next_y - 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x + 1, next_y , img))
                    t1.start()
                    print("We can go down @", next_y, next_x)
                    t1.join()
                if next_x > 0 and np.array_equal(img[next_x - 1][next_y], path_color) and np.array_equal(img[next_x][next_y - 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x - 1, next_y , img))
                    t1.start()
                    print("We can go up @", next_y, next_x)
                    t1.join()
        if not moved and next_x > 0 and np.array_equal(img[next_x - 1][next_y], path_color):
            moved = True
            print("Going up!")
            while next_x > 0 and np.array_equal(img[next_x - 1][next_y], path_color):
                out[next_x][next_y] = [255, 255, 0]
                next_x -= 1
                if next_y < len(img[next_x]) - 1 and np.array_equal(img[next_x][next_y + 1], path_color) and np.array_equal(img[next_x - 1][next_y], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x, next_y + 1, img))
                    t1.start()
                    print("We can go to the right @", next_y, next_x)
                    t1.join()
                if next_y > 0 and np.array_equal(img[next_x][next_y - 1], path_color) and np.array_equal(img[next_x - 1][next_y], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x, next_y - 1, img))
                    t1.start()
                    print("We can go to the left @", next_y, next_x)
                    t1.join()
        elif not moved and next_y < len(img[next_x]) - 1 and np.array_equal(img[next_x][next_y + 1], path_color):
            moved = True
            print("Going right!")
            while next_y < len(img[next_x]) - 1 and np.array_equal(img[next_x][next_y + 1], path_color):
                out[next_x][next_y] = [255, 255, 0]
                next_y += 1
                if next_x < len(img) - 1 and np.array_equal(img[next_x + 1][next_y], path_color) and np.array_equal(img[next_x][next_y + 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x + 1, next_y , img))
                    t1.start()
                    print("We can go down @", next_y, next_x)
                    t1.join()
                if next_x > 0 and np.array_equal(img[next_x - 1][next_y], path_color) and np.array_equal(img[next_x][next_y + 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x - 1, next_y , img))
                    t1.start()
                    print("We can go up @", next_y, next_x)
                    t1.join()
        elif not moved and next_y > 0 and np.array_equal(img[next_x][next_y - 1], path_color):
            moved = True
            print("Going left!")
            while next_y > 0 and np.array_equal(img[next_x][next_y - 1], path_color):
                out[next_x][next_y] = [255, 255, 0]
                next_y -= 1
                if next_x < len(img) - 1 and np.array_equal(img[next_x + 1][next_y], path_color) and np.array_equal(img[next_x][next_y - 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x + 1, next_y , img))
                    t1.start()
                    print("We can go down @", next_y, next_x)
                    t1.join()
                if next_x > 0 and np.array_equal(img[next_x - 1][next_y], path_color) and np.array_equal(img[next_x][next_y - 1], path_color):
                    t1 = threading.Thread(target=recursive_traverse, args=(next_x - 1, next_y , img))
                    t1.start()
                    print("We can go up @", next_y, next_x)
                    t1.join()
        if not moved:
            return
    if (next_y == len(img[next_x]) - 1 or next_x == len(img) - 1) and moved:
        print("Found exit at", next_x, next_y)
        out[next_x][next_y] = [255, 255, 0]
        return
    else:
        recursive_traverse(next_x, next_y, img)
        
img = cv2.imread('maze.png', 1)
out = img
recursive_traverse(0, 0, img)
cv2.imwrite("output.png", out)
