result = []
lists = [el for el in input().split("|")]
lists = lists[::-1]
for li_st in lists:
    result += [el for el in li_st.split()]
print(*result)
