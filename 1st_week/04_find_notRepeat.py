input = "abadabac"

# 알파벳 빈도수 탐색 -> 하나만 나온 것들 중에서 반복되지 않는 문자가 존재함
# 1개만 나온 알파벳들 중 가장 먼저 등장하는 알파벳이 반복되지 않는 문자임

def find_not_repeating_first_character(string):
    repeating_array = [0] * 26
    for chr in string:
        if chr.isalpha():
            repeating_array[ord(chr) - ord('a')] += 1
    # 1개만 등장하는 알파벳들의 리스트 정의
    # 그 알파벳들의 string 안에서의 순서를 확인하기..?
        # 1번 등장하는 알파벳 기억
        # 해당 알파벳이 string을 순회하면서 가장 먼저 등장했는지 검사
    for chr in string:
        if repeating_array[ord(chr) - ord('a')] == 1:
            result = chr
            break
        else:
            result = '_'
    return result


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))