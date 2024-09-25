def count_calls():
    global calls
    calls += 1
    return calls

def string_info(str_):
    count_calls()
    var = (len(str_), str_.upper(), str_.lower())
    return var

def is_contains(str_, list_):
    count_calls()
    for i in range(len(list_)):
        if isinstance(list_[i], str):
            list_[i] = list_[i].lower()
        else: continue
    str_ = str_.lower()

    if str_ in list_:
        return True
    else: return False

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNan', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

