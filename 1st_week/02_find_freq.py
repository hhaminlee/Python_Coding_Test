# 최빈값 찾기
# 가장 많이 등장한 알파벳 찾아서 리턴해주기
# 파이썬에서는 어떻게 문자열을 다루는지 찾아보기
# 아스키 코드를 다루는 ord, chr을 이용해서 문자열 계산해보기
# ord - 문자 -> 아스키 코드로 변환
# chr - 아스키 코드 -> 문자

def find_max_occurred_alphabet(string):
    counts = [0] * 26
    for max_string in string:
        if 'a' <= max_string <= 'z':
            counts[ord(max_string) - ord('a')] += 1
        # 풀이에서는 isalpha() 메소드를 사용해서 알파벳을 걸러냈음
    max = 0;
    for count in counts:
        if count > max:
            max = count
            max_index = counts.index(count)
    return chr(max_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))