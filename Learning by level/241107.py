#1."화면에 `Hello World` 문자열을 출력하세요."
print('Hello World')
#2."화면에 `Mary's cosmetics`을 출력하세요. (중간에 '가 있음에 주의하세요)"
print('Mary\'s cosmetics')
#5."화면에 아래 문장을 출력하세요. (중간에 \"가 있음에 주의하세요.)",
#신씨가 소리질렀다. "도둑이야"
print('신씨가 소리질렀다. "도둑이야"')
#4.화면에 `C:\\Windows`를 출력하세요.
print('C:\Windows')
#5.다음 코드를 실행해보고 \\t와 \\n의 역할을 설명해보세요.
#print("안녕하세요.\n만나서\t\t반갑습니다.")

#정답 = \n은 줄바꿈 \t는 탭간격 

#6.print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
#print ("오늘은", "일요일")

#정답 = 오늘은 일요일

#7.print() 함수를 사용하여 다음과 같이 출력하세요.
#naver;kakao;sk;samsung

print('naver','kakao','sk','samsung',sep=';')
#sep= 구분자 현재는 ;로 구분해서 출력해달라는 뜻

#파라미터의 간단개념
#print 내부함수는 기본적으로 구분을 ''으로 진행하기때문에 우리는 간단히 사용할수있는것인데,
#print(조건=파라미터1,조건=파라미터2) 해당 함수를 사용하기위한 조건이라고 생각하면된다.
#print에 sep의 기본적으로 정해진 defalut 값은 ''이기때문에 평소에 사용하지 않고 사용하지만
#sep도 파라미터의 하나이다.  

#8.print() 함수를 사용하여 다음과 같이 출력하세요
#naver/kakao/sk/samsung
print('naver','kakao','sk','samsung',sep='/')


#9.다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
#print("first");print("second")

print('first\nsecond')

#end 사용해보기
print('hello',end=' ' )
print('world')

#10.5/3의 결과를 화면에 출력하세요.

print(5/3)
