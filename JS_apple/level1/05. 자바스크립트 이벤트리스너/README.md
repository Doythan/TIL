## 강의 내용 요약
1. getElementsByClassName 셀렉터
```js
<p class="title1"> 테스트1 </p>
<p class="title1"> 테스트2 </p>
<script>
  document.getElementsByClassName('title1')[0].innerHTML = '안녕';
</script>
```
이러면 첫 <p> 태그 내용이 안녕으로 바뀝니다.
getElementsByClassName('클래스명')[순서] 이렇게 쓰면 됩니다.
[0] 이렇게 순서를 넣는 이유는

getElementsByClassName 셀렉터는 일치하는 class가 들어있는 모든 html 요소를 찾아주기 때문입니다.

그래서 그 중에 몇번째 요소를 바꿀지 [순서]를 꼭 뒤에 붙여줘야합니다.

2. 이벤트 리스너
```js
document.getElementById('어쩌구').addEventListener('click', function(){
    //실행할 코드 
});
```
이렇게 작성하면 'id가 어쩌구인 요소를 클릭하면 안의 코드를 실행해주세요~' 라는 뜻입니다.
이거 쓰면 버튼 같은 곳에 onclick 넣을 필요가 없겠군요 ㄷㄷ

3. 더 배워볼 개념 1. event
유저가 웹페이지 접속해서 클릭, 스크롤, 키보드입력, 드래그 등을 할 수 있는데 이걸 전문용어로 이벤트라고 부릅니다.

어떤 요소 클릭시엔 click 이벤트

마우스갖다대면 mouseover 이벤트 

스크롤하면 scroll 이벤트

키입력하면 keydown 이벤트

그리고 이벤트가 일어나길 기다리는 친구가 이벤트 리스너입니다.

이벤트 리스너는 이벤트가 일어나면 내부 코드를 실행해주는 고마운 기본 문법입니다.

```js
셀렉터로찾은요소.addEventListener('mouseover', function(){ 
  실행할코드
});
```
이러면 셀렉터로찾은요소에 마우스를 스윽 갖다대면 특정 코드를 실행해줍니다.
이벤트 종류는 수십가지가 있습니다. 

https://developer.mozilla.org/en-US/docs/Web/Events

▲ 이벤트 목록인데 이런거 미련하게 외우지 마시고 필요할 때 찾아쓰십시오.

4. 더 배워볼 개념 2. 콜백함수
```js
셀렉터로찾은요소.addEventListener('scroll', function(){} );
```

이벤트 리스너 생김새를 잘 보면 함수같이 생겼습니다.

실은 뒤에 소괄호 붙으면 다 함수입니다.

 

근데 addEventListener() 함수에는 파라미터 자리에 2개의 자료를 집어넣죠?

맞습니다 자바스크립트 addEventListener 문법 만든 사람이 그렇게 쓰라고 해서 그렇게 쓸 뿐인데

둘째 파라미터로 함수가 들어가네요? 

그래도 됩니다. 

 

저렇게 함수 파라미터자리에 들어가는 함수를 전문용어로 '콜백함수'라고 합니다.

콜백함수는 그냥 뭔가 순차적으로 실행하고 싶을 때 많이 보이는 함수형태며

그냥 함수안에 함수 넣으라고 하면 "아 저건 콜백함수구나~" 라는 반응만 보이면 됩니다. 

 

지금 코드짤 때는 우리가 콜백함수를 직접 작성하고 그럴 일은 없고

콜백함수 쓰라고 하는 자리가 있으면 잘 쓰기만 하면 됩니다. 