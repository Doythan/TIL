## 강의 내용 요약

### 1. `getElementsByClassName` 셀렉터
```html
<p class="title1"> 테스트1 </p>
<p class="title1"> 테스트2 </p>
<script>
  document.getElementsByClassName('title1')[0].innerHTML = '안녕';
</script>
```
- 위 코드를 실행하면 첫 번째 `<p>` 태그의 내용이 '안녕'으로 바뀝니다.
- `getElementsByClassName('클래스명')[순서]` 형태로 사용합니다.
- `[0]`은 찾은 요소 중 몇 번째 요소를 선택할지를 나타냅니다.
- `getElementsByClassName` 셀렉터는 일치하는 모든 HTML 요소를 찾아주기 때문에 순서를 명시해야 합니다.

### 2. 이벤트 리스너
```js
document.getElementById('어쩌구').addEventListener('click', function(){
    // 실행할 코드 
});
```
- 위 코드는 'id가 어쩌구인 요소를 클릭하면 안의 코드를 실행해주세요'라는 의미입니다.
- 이 방법을 사용하면 버튼 등에서 `onclick`을 따로 사용할 필요가 없습니다.

### 3. 더 배워볼 개념 1: 이벤트
- 유저가 웹페이지에서 클릭, 스크롤, 키보드 입력, 드래그 등을 하는 것을 전문용어로 **이벤트**라고 부릅니다.
  - 클릭: `click` 이벤트
  - 마우스 오버: `mouseover` 이벤트
  - 스크롤: `scroll` 이벤트
  - 키 입력: `keydown` 이벤트
- 이벤트가 발생하길 기다리는 것이 **이벤트 리스너**입니다.
```js
셀렉터로찾은요소.addEventListener('mouseover', function(){ 
  실행할코드
});
```
- 마우스를 요소에 올리면 특정 코드를 실행합니다.
- 이벤트 종류는 수십 가지가 있으며, 필요할 때 [MDN 이벤트 목록](https://developer.mozilla.org/en-US/docs/Web/Events)에서 찾아보세요.
- 이런 목록을 미련하게 외우지 말고 필요할 때 찾아쓰십시오.

### 4. 더 배워볼 개념 2: 콜백 함수
```js
셀렉터로찾은요소.addEventListener('scroll', function(){} );
```
- 이벤트 리스너의 구조를 보면 함수처럼 생겼습니다.
- `addEventListener()` 함수에는 두 개의 파라미터가 들어갑니다.
- 둘째 파라미터로 들어가는 함수를 **콜백 함수**라고 합니다.
- 콜백 함수는 순차적으로 실행하고 싶을 때 자주 사용됩니다.
- 코드 작성 시 콜백 함수의 자리가 있으면 잘 활용하면 됩니다.
