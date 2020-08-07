def alternating_harmonic(n):
    sol = 0.0
    for i in range(1, n):
        if i % 2 == 0:
            sol -= 1 / i
        else:
            sol += 1 / i
    return sol


print(alternating_harmonic(1000))


def remove_duplicates(list):
    res = []
    [res.append(x) for x in list if x not in res]
    return res


test_list = [1, 9, 3, 12, 11, 1, 3, 3, 21]
print((remove_duplicates(test_list)))


def count_stuff(str):
    dict = {}
    digit = sum(c.isdigit() for c in str)
    spaces = sum(c.isspace() for c in str)
    letters = len(str) - digit - spaces
    dict.update({'digits': digit, 'letters': letters})
    return dict


print(count_stuff('Eleni is the cutest in the world! 52'))

filename = 'C:/Mid_term_test/exercises.csv'


def get_data(filename):
    with open(filename, "r") as f:
        data = []
        rows = f.readlines()
        i = 0
        while i in range(len(rows)):
            rows[i].rstrip('\n')
            if int(rows[i]) < 3:
                i += 2

            else:
                data1 = [[int(rows[i])]]
                i += 1
                data1.append([int(j) for j in rows[i].split(",")])
                i += 1
                data1.append([int(j) for j in rows[i].split(",")])
                data.append(tuple(data1))
            i += 1
        return data


print(get_data(filename))


def return_max(data):
    max = 0
    mx1 = 0
    for rows in data:
        if max < rows[0][0]:
            max = rows[0][0]
        if mx1 < len(remove_duplicates(rows[1])):
            mx1 = len(remove_duplicates(rows[1]))
    return max, mx1


data_list = get_data(filename)

print(return_max(data_list))
