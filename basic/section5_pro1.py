# Day-5-1 exercise _ Average Height 
# len(), sum() 함수 사용이 안된다. 
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# height_sum = 0 
# student_number = 0 
# for stdent in student_heights:
#     height_sum += stdent
#     student_number += 1

# total = height_sum / student_number
# total_final = round(total)
# print(total_final)    



# day-5-2-exercise
# max(), min() 함수 사용 불가 
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])

# hightest_score = 0 

# for score in student_scores:
#     if score > hightest_score:
#         hightest_score = score

# print(f"The hightest score in the class is: {hightest_score}")


# day-5-3-exercise 짝수 더하기 
# total = 0 
# for i in range(2,101,2):
#     total += i 
    
# print(total)

# # another answer
# total2 = 0 
# for number in range(1,101):
#     if number % 2 == 0:
#         total2 += number
# print(total2)

# day-5-4-exercise_ Fizz Buzz 면접 문제 

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


