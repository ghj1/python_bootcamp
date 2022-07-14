# excercise_8_1 페인트 면적 계산기 

import math 
def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    return number_of_cans
    

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
result = math.ceil(paint_calc(height=test_h, width=test_w, cover=coverage))
print(f"You'll need {result} cans of paint")

# excercise_8_1 강사님 solution 
import math 
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
