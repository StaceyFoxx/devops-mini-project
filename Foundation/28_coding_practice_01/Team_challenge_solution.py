"""
A&E Minimum Waiting Time Challenge -- SOLUTION

This is one of the multiple possible solutions (there might be many others)

This one is:
O(nlogn) time | O(1) space - where n is the number of patients
"""

#          0   1  2  3  4
patients = [3, 2, 1, 2, 6]
expected = 17

def min_waiting_time(patients):
    patients.sort()
    total = 0
    print('ordered patients', patients)

    for idx, time in enumerate(patients):
        patients_left = len(patients) - (idx + 1)
        print('patients left ', patients_left)

        total += time * patients_left
        print('current total ', total)

        print('patients seen ', patients[:idx+1])
    return total

print(min_waiting_time(patients))
