# # def add_number():
# #     data = [1,2,3,4,5,5,6]
# #     total = 0
# #     for i in data:
# #         total = total + i
# #     return total



# # print(add_number())




# def user_info(fname):
#     result = f'my name is {fname}'
#     return result


# print(user_info("sudan"))
# print(user_info("hari"))
# print(user_info("suman"))
# print(user_info("ramesh"))
# print(user_info("rachit"))


# print("---------------------->")
# def world_cup(winner, runner_up):
#     print(f'Winner of fifa 2026 is {winner}')
#     print(f'Runner Up of fifa 2026 is {runner_up}')

# world_cup("ESP","Arg")

# world_cup(1,2)


# world_cup([1,2,2],[99])



# def add_number(numbers):
#     if (isinstance(numbers, list) or isinstance(numbers, tuple)):
#         total = 0
#         for i in numbers:
#             total = total + i
#         return total
#     else:
#         return "Number should be in list or tuple"



# print(add_number([1,2,3,4]))
# print(add_number([70,90,77,22]))

# print(add_number((1,2,3,4)))


# # print(add_number(123)) => numbers should be in list or tuple
# print(add_number(123))




print("------------"* 10)
def world_cup(winner, runner_up):
    print(f'Winner of fifa 2026 is {winner}')
    print(f'Runner Up of fifa 2026 is {runner_up}')

# positional args
# world_cup("ESP","Arg")

# # keyword args
world_cup(runner_up="ESP", winner="ARG")
world_cup(winner="ARG", runner_up="ESP",)