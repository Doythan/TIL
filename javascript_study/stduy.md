## 강의 중 중요한 내용 정리

### 변수 선언 키워드

1. **let**
   - 블록 스코프를 갖는 지역 변수를 선언
   - 재할당 가능, 재선언 불가능
   - ES6에서 추가

2. **const**
   - 블록 스코프를 갖는 지역 변수를 선언
   - 재할당 불가능, 재선언 불가능
   - 선언할 때 초기값이 필요
   - ES6에서 추가

**let**과 **const**의 차이는 **재할당 여부**입니다.  
- **const**는 선언 시 반드시 초기값이 필요합니다.  
- **let**은 선언 시 초기값이 없다면 `undefined`가 초기화 시에 할당됩니다.  
기본적으로는 **const**를 사용하나, 필요한 경우에만 **let**으로 전환합니다.

---

### JavaScript의 목적
- 프로그래밍 언어
- 웹 브라우저

### 웹 브라우저에서의 JavaScript
- 웹 페이지의 동적인 기능을 구현

### JavaScript 실행 환경 종류
- HTML `<script>` 태그
- `.js` 확장자 파일
- 브라우저 Console

### DOM (Document Object Model)
- 웹 페이지를 Document라고 부르며, 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공합니다.
- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 합니다.

**DOM의 핵심**: 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API.

#### DOM 조작 순서
1. 조작하고자 하는 요소를 선택(또는 탐색)
2. 선택된 요소의 콘텐츠 또는 속성을 조작 

#### DOM 선택 메서드
- `document.querySelector()`: 요소 한 개 선택
- `document.querySelectorAll()`: 요소 여러 개 선택 

#### DOM 조작
1. **속성(attribute) 조작**
   - 클래스 속성 조작
     - `classList` property: 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
       - classList 메서드: `.add()`, `.remove()`, `.toggle()`
       - 예시: `element.classList.add()`
   - 일반 속성 조작 
     - 일반 속성 조작 메서드
       1. `.getAttribute()`: 해당 요소에 지정된 값을 반환(조회)
       2. `.setAttribute(name, value)`: 지정된 요소의 속성 값을 설정, 속성이 이미 있으면 기존 값을 갱신(그렇지 않으면 지정된 이름과 값으로 새 속성이 추가)
       3. `.removeAttribute()`: 요소에서 지정된 이름을 가진 속성 제거 
2. **HTML 콘텐츠 조작**
   - `textContent` property: 요소의 텍스트 콘텐츠를 표현
3. **DOM 요소 조작**
   - DOM 요소 조작 메서드
     1. `document.createElement(tagName)`: 작성한 tagName의 HTML 요소를 생성하여 반환
     2. `Node.appendChild()`: 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입, 추가된 Node 객체를 반환
     3. `Node.removeChild()`: DOM에서 자식 Node를 제거, 제거된 Node를 반환
4. **스타일 조작**  
   - `style` property: 해당 요소의 모든 style 속성 목록을 포함하는 속성

### 용어 정리 
- **Node**: DOM의 기본 구성 단위 
- **NodeList**: DOM 메서드를 사용해 선택한 Node의 목록 
- **Element**: Node의 하위 유형 

### Parsing 
- 구문 분석, 해석, 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

### var (바)
- 변수 선언 키워드, 재할당 및 재선언 가능, 함수 스코프를 가짐

---

## 어려웠던 내용 + 이해 안 되는 내용
