# 풀이 3 슬라이싱 사용

 def isPalindrome(self, s : str) -> bool:
     s = s.lower() # 소문자로 다 바꾸고
     # 정규식으로 불필요한 문자 필터링
     s = re.sub('[^a-z0-9]', '', s) # 영어 소문자, 숫자 아닌것들은 다 공백으로(지운다는 말)

     return s = s[::-1] # 슬라이싱