import pygame, sys, random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 640
HEIGHT = 480
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)

pygame.display.set_caption('Merge Sort')
clock = pygame.time.Clock()

#WIDTH of the bars
n = 4

w = int(WIDTH/n)
h_arr = []
state = []
for i in range(w):
    height = random.randint(0, 450)
    h_arr.append(height)
    state.append(1)


def mergeSort(a):  
      
    current_size = 1
      
    # Outer loop for traversing Each  
    # sub array of current_size  
    while current_size < len(a) - 1:  
          
        left = 0
        # Inner loop for merge call  
        # in a sub array  
        # Each complete Iteration sorts  
        # the iterating sub array  
        while left < len(a)-1:  
              
            # mid index = left index of  
            # sub array + current sub  
            # array size - 1  
            mid = min((left + current_size - 1),(len(a)-1)) 
              
            # (False result,True result)  
            # [Condition] Can use current_size  
            # if 2 * current_size < len(a)-1  
            # else len(a)-1  
            right = ((2 * current_size + left - 1,  
                    len(a) - 1)[2 * current_size  
                        + left - 1 > len(a)-1])  
                              
            # Merge call for each sub array  
            merge(a, left, mid, right)  
            left = left + current_size*2
              
        # Increasing sub array size by  
        # multiple of 2  
        current_size = 2 * current_size  
  
# Merge Function  
def merge(a, l, m, r):  
    n1 = m - l + 1
    n2 = r - m  
    L = [0] * n1  
    R = [0] * n2  
    for i in range(0, n1):  
        L[i] = a[l + i]
        state[i] = 0 
        for j in range(len(h_arr)):
            if state[j] == 0:
                color = RED
            elif state[j] == 2:
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(win, color, pygame.Rect(j*n, HEIGHT - h_arr[j], n, h_arr[j])) 
        state[i] = 1
    for i in range(0, n2):  
        R[i] = a[m + i + 1]  
        state[i] = 0
        for j in range(len(h_arr)):
            if state[j] == 0:
                color = RED
            elif state[j] == 2:
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(win, color, pygame.Rect(j*n, HEIGHT - h_arr[j], n, h_arr[j]))
        state[i] = 1
    i, j, k = 0, 0, l  
    while i < n1 and j < n2:  
        if L[i] > R[j]:  
            a[k] = R[j]  
            j += 1
        else:  
            a[k] = L[i]  
            i += 1
        k += 1 
    while i < n1:  
        a[k] = L[i]  
        i += 1
        k += 1
    while j < n2:  
        a[k] = R[j]  
        j += 1
        k += 1

current_size = 1

while True:
    win.fill((10, 10, 10))

    if current_size < len(h_arr) - 1:       
        left = 0
        while True:
            if left < len(h_arr)-1:  
                mid = min((left + current_size - 1),(len(h_arr)-1)) 
                right = ((2 * current_size + left - 1, len(h_arr) - 1)[2 * current_size + left - 1 > len(h_arr)-1])  
                n1 = mid - left + 1
                n2 = right - mid  
                L = [0] * n1  
                R = [0] * n2  
                for i in range(0, n1):  
                    L[i] = h_arr[left + i]
                for i in range(0, n2):  
                    R[i] = h_arr[mid + i + 1]  
                i, j, k = 0, 0, left  
                while i < n1 and j < n2:  
                    if L[i] > R[j]:  
                        h_arr[k] = R[j]
                        state[k] = 0
                        state[j] = 0
                        win.fill((10, 10, 10))
                        for _ in range(len(h_arr)):
                            if state[_] == 0:
                                color = RED
                            elif state[_] == 2:
                                color = GREEN
                            else:
                                color = WHITE
                            pygame.draw.rect(win, color, pygame.Rect(_*n, HEIGHT - h_arr[_], n, h_arr[_]))
                        state[k] = 1
                        state[j] = 1
                        j += 1
                    else:  
                        h_arr[k] = L[i]
                        state[k] = 0
                        state[i] = 0
                        win.fill((10, 10, 10))
                        for _ in range(len(h_arr)):
                            if state[_] == 0:
                                color = RED
                            elif state[_] == 2:
                                color = GREEN
                            else:
                                color = WHITE
                            pygame.draw.rect(win, color, pygame.Rect(_*n, HEIGHT - h_arr[_], n, h_arr[_]))
                        state[k] = 1 
                        state[i] = 1 
                        i += 1
                    k += 1 
                while i < n1:  
                    h_arr[k] = L[i] 
                    state[k] = 0
                    state[i] = 0
                    win.fill((10, 10, 10))
                    for _ in range(len(h_arr)):
                        if state[_] == 0:
                            color = RED
                        elif state[_] == 2:
                            color = GREEN
                        else:
                            color = WHITE
                        pygame.draw.rect(win, color, pygame.Rect(_*n, HEIGHT - h_arr[_], n, h_arr[_]))
                    state[k] = 1 
                    state[i] = 1
                    i += 1
                    k += 1
                while j < n2:  
                    h_arr[k] = R[j] 
                    state[k] = 0
                    state[j] = 0
                    win.fill((10, 10, 10))
                    for _ in range(len(h_arr)):
                        if state[_] == 0:
                            color = RED
                        elif state[_] == 2:
                            color = GREEN
                        else:
                            color = WHITE
                        pygame.draw.rect(win, color, pygame.Rect(_*n, HEIGHT - h_arr[_], n, h_arr[_]))
                    state[k] = 1 
                    state[i] = 1
                    j += 1
                    k += 1 
                left = left + current_size*2
            else:
                break

        current_size = 2 * current_size
    else:
        for i in range(len(h_arr)):
            if state[i] == 0:
                color = RED
            elif state[i] == 2:
                color = GREEN
            else:
                color = WHITE
            pygame.draw.rect(win, color, pygame.Rect(i*n, HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)
    pygame.display.flip()