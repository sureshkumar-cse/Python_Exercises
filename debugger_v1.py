# Automated Debug Mode

import random_Generator
import linear_Search_v1
import binary_Search_v1
    
def debug():
    test_cases = 10000
    for _ in range(test_cases):
        a, x = random_Generator.generate_input()
        no_brainer_output = linear_Search_v1.no_brainer(a, x)
        solution_output = binary_Search_v1.solution(a, x)
        if no_brainer_output != solution_output:
            print("Test Case:")
            print(a, x)
            print("Solution Output:", solution_output)
            print("No-Brainer Output:", no_brainer_output)
            exit()
    print("All test cases passed succesfully")
    
if __name__ == "__main__":
    debug()
