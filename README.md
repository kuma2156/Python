# 🐍 Python 학습 기록

Python 기초 문법부터 데이터 처리 라이브러리인 Pandas까지, 수업에서 실습한 내용을 정리한 학습 로그입니다.  
매 수업마다 어떤 개념을 배우고, 어떤 실습을 했는지 날짜별로 정리했습니다.

<div align="left">
    <h1>💻 학습자</h1>
    <table>
        <tr>
            <td align="center"><img src="https://github.com/user-attachments/assets/61049fd5-5e06-4b17-bb51-d925ea3e68dc" width="250"></td>
        </tr>
        <tr>
            <td align="center"><b>김명규</b></td>
        </tr>
        <tr>
            <td align="center"><b>https://github.com/kuma2156</b></td>
        </tr>
    </table>
</div>

---

## 🗓️ 학습 일지 요약

| 날짜         | 챕터/주제        | 주요 학습 내용                                                                  |
|--------------|------------------|----------------------------------------------------------------------------------|
| 9월 13일     | ch1 ~ ch3        | Python 기초 문법 / 변수 선언 / 출력문 / 연산자 / 연습문제 실습                |
| 9월 20일     | ch4              | 조건문 (`if`, `else`, `elif`) / 심화 예제 풀이                                 |
| 9월 27일     | ch5              | 반복문 `for` / `range` 사용법 / 중첩 반복문 실습                               |
| 10월 4일     | ch6              | `while`, `break`, `continue` 반복 제어문 실습                                  |
| 10월 11일    | ch7              | 함수 정의와 호출 / 매개변수, 반환값, `return` 사용법                           |
| 10월 18일    | ch8              | 리스트(List) 생성, 접근, 메소드 (`append`, `remove` 등)                        |
| 11월 1일     | ch9              | 튜플(Tuple) 자료형 실습                                                         |
| 11월 8일     | 없음             | 집합(Set), 딕셔너리(Dictionary) 개념 및 실습                                   |
| 11월 15일    | 없음             | 문자열(String) 슬라이싱, 인덱싱, 주요 메소드 사용 (`split`, `join`, `find`)   |
| 12월 6일     | Pandas 실습      | `pandas` 라이브러리 소개 / `DataFrame` 생성, 인덱싱 / `.head()`, `.info()` 등  |

---

## 🧠 기억할 개념들 요약

### ✅ Python 기초 문법

- 변수 선언: `x = 10`, `name = "명규"`
- 출력: `print("Hello, world!")`
- 연산자: `+`, `-`, `*`, `/`, `//`, `%`, `**`

### ✅ 조건문 & 반복문

- 조건문: `if`, `elif`, `else`
- 반복문: `for`, `while`
- 반복 제어: `break`, `continue`

### ✅ 함수(Function)

- 정의: `def 함수명(매개변수):`
- 반환: `return` 문
- 기본값 매개변수, 키워드 인자 등 활용

### ✅ 주요 자료형

- 리스트: `[]` / `.append()`, `.remove()`, `.sort()`
- 튜플: `()` / 불변성
- 집합: `{}` / 중복 제거, 집합 연산
- 딕셔너리: `{key: value}` / `.keys()`, `.values()`
- 문자열: 슬라이싱 `[start:end]`, `.split()`, `.replace()`, `.find()`

### ✅ Pandas

- `import pandas as pd`
- `DataFrame`, `Series` 생성
- `.head()`, `.tail()`, `.info()`, `.describe()` 등 데이터 요약
- `.loc[]`, `.iloc[]`로 행/열 접근

---

## 🗂️ 프로젝트 디렉토리 구조

```
📦Python_Study/
├── 📁ch01~03/                 - 9월 13일 기초 실습 코드
├── 📁ch04_if/                 - 9월 20일 조건문 실습
├── 📁ch05_for/                - 9월 27일 반복문 실습
├── 📁ch06_while/              - 10월 4일 while 반복 제어 실습
├── 📁ch07_function/           - 10월 11일 함수 실습
├── 📁ch08_list/               - 10월 18일 리스트 실습
├── 📁ch09_tuple/              - 11월 1일 튜플 실습
├── 📁ch10_set_dict/           - 11월 8일 집합 & 딕셔너리 실습
├── 📁ch11_string/             - 11월 15일 문자열 실습
├── 📁pandas_1206/             - 12월 6일 Pandas 실습 (📄1206_판다스_김명규.ipynb)
├── 📄README.md                
```


> 📌 모든 실습 디렉토리는 날짜별로 정리되어 있으며, 핵심 개념과 예제 코드가 포함되어 있습니다.  
> 📌 Pandas 실습은 Jupyter Notebook 형태로 작성되어 있으며, 데이터 처리 연습 중심입니다.


