# 클래스

## 객체 지향 프로그래밍(OOP)

소프트웨어를 개발할 때 부품에 해당하는 객체들을 먼저 만들고, 이것들을 하나씩 조립해서 완성된 프로그램을 만드는 기법이다.

### 객체(Object)란?

물리적으로 존재하거나 추상적으로 생각할 수 있는 것 중에서 자신의 속성을 가지고 있고 다른 것과 식별 가능한 것을 말한다. 객체는 속성과 동작으로 구성되어 있다. 자바는 이 속성과 동작들을 각각 **필드(field)**와 **메소드(method)**라 부른다.

객체 모델링(Object Modeling)이란 현실 세계 객체의 속성과 동작을 추려내어 소프트웨어 객체의 필드와 메소드로 정의하는 과정으로 볼 수 있다.

### 객체의 상호작용

소프트웨어에서 객체들은 각각 독립적으로 존재하고, 다른 객체와 서로 상호작용하면서 동작한다. 객체들 사이의 상호작용 수단은 메소드이다. 객체가 다른 객체의 기능을 이용하는 것이 바로 **메소드 호출**이다.

### 객체간의 관계

객체는 개별적으로 사용될 수 있지만, 대부분 다른 객체와 관계를 맺고 있다.

- 집합 관계 : 하나는 부품, 하나는 완성품
- 사용 관계 : 객체 간의 상호작용, 다른 객체의 메소드를 호출하여 원하는 결과를 얻어낸다.
- 상속 관계 : 상위(부모) 객체를 기반으로 하위(자식) 객체를 생성하는 관계를 말한다. 일반적으로 상위 객체는 종류, 하위 객체는 구체적인 사물에 해당한다.

객체 지향 프로그래밍(OOP)은 만들고자 하는 완성품인 객체를 모델링하고, 집합 관계에 있는 부품 객체와 사용 관계에 있는 객체를 하나씩 설계한 후 조립하는 방식으로 프로그램을 개발하는 기법이다.

### 객체 지향 프로그래밍 특징

#### 캡슐화(Encapsulation)
객체의 필드, 메소드를 하나로 묶고, 실제 구현 내용을 감추는 것을 말한다. 외부 객체는 객체의 내부의 구조를 알지 못하며 객체가 노출해서 제공하는 필드와 메소드만 알 수 있다.

필드와 메소드를 캡슐화해서 보호하는 이유는 외부의 잘못된 사용으로 인해 객체가 손상되지 않도록 하기위해서이다. 자바에서는 캡슐화된 멤버를 노출시킬 것인지, 숨길 것인지를 결정하기 위해 접근 제한자(Acess Modifier)를 사용한다. 접근 제한자는 객체의 필드와 메소드의 사용 범위를 제한함으로써 외부로부터 보호한다.

#### 상속(Inheritance)

상위(부모) 객체는 자기가 가지고 있는 필드와 메소드를 하위(자식) 객체에게 물려주어 하위 객체가 사용할 수 있도록 해준다.

상속은 상위 객체를 재사용해서 하위 객체를 쉽고 빨리 설계할 수 있도록 도와주고, 코드 재사용으로 반복된 코드의 중복을 줄여주며, 효율적이고 개발 시간을 절약시켜준다. 또한 상속은 상위 개체의 수정으로 모든 하위 객체들의 수정 효과를 가져오므로 유지 보수 시간을 최소화시켜주기도 한다.

#### 다형성(Polymorphism)

다형성은 같은 타입이지만 실행 결과가 다양한 객체를 이용할 수 있는 성질을 말한다. 코드 측면에서 보면 다형성은 하나의 타입에 여러 객체를 대입함으로써 다양한 기능을 이용할 수 있도록 해준다.

자바에서는 다형성을 위해 부모 클래스 또는 인터페이스의 타입 변환을 허용한다. 부모 타입에는 모든 자식 객체가 대입될 수 있고, 인터페이스 타입에는 모든 구현 객체가 대입될 수 있다.

## 객체와 클래스

현실에서 객체는 설계도를 바탕으로 만들어진다. 객체 지향 프로그래밍에서도 마찬가지이다. 메모리에서 사용하고 싶은 객체가 있다면 우선 설계도로 해당 객체를 만드는 작업이 필요하다. 자바에서 설계도가 바로 클래스(`class`)이다.

클래스에는 객체를 생성하기 위한 필드와 메소드가 정의되어 있다. 클래스로부터 만들어진 객체를 해당 클래스의 **인스턴스(instance)**라고 한다. 그리고 클래스로부터 객체를 만드는 과정을 인스턴스화라고 한다. 하나의 클래스로부터 여러 개의 인스턴스를 만들 수 있다.

### 객체 지향 프로그래밍 개발 3단계
1. 클래스 설계
2. 설계된 클래스를 가지고 사용할 객체 생성
3. 생성된 객체 이용

## 클래스 선언

클래스 이름은 다른 클래스와 식별할 목적으로 사용되므로 자바의 식별자 작성 규칙에 따라서 만들어야한다.

| 작성규칙 | 예 |
|------|------|
|하나 이상의 문자로 이루어져야 한다.|Car, SportsCar|
|첫 번째 글자는 숫자가 올 수 없다.|Car,3Car(X)|
|`$`,`_`외의 특수 문자는 사용할 수 없다.|$Car, _Car, @Car(x)|
|자바 키워드는 사용할 수 없다.|int(x), for(x)|

자바는 영어 대소문자를 다른 문자로 취급하기 때문에 클래스 이름도 영어 대소문자를 구분한다. 관례적으로 클래스 이름이 단일 단어라면 첫 자를 대문자로 하고 나머지는 소문자로 작성한다. 다른 단어가 혼합된 이름은 각 단어의 첫 머리 글자는 대문자로 작성하는 것이 관례이다.

```
Calculator, Car, ChatClient
```

- `Class이름.java`로 소스파일을 생성

```java
public class 클래스이름{
}
```

일반적으로 소스 파일당 하나의 클래스를 선언한다. 하지만, 두 개 이상의 클래스 선언도 가능하다. 이때 컴파일된 바이트 코드파일(`.class`)는 클래스를 선언한 개수만큼 생긴다.
```java
public class Car{
}

class Tire{
}
```
여기서 주의할 점은 파일이름`ClassName.java`와 동일한 일므의 클래스 선언에만 `public`접근 제한자를 붙일 수 있다.

** 소스 파일 하나당 동일한 이름의 클래스 하나를 선언하는 것이 좋다. **

## 객체 생성과 클래스 변수

```java
new 클래스();
```
`new`는 클래스로부터 객체를 생성시키는 연산자이다. `new` 연산자 뒤에는 생성자가 오는데, 생성자는 `클래스()` 형태를 가지고 있다. 이때 생성된 객체는 메모리 힙(heap) 영역에 생성되고, 객체의 주소를 리턴하도록 되어있다. 이 주소를 참조 타입인 클래스 변수에 저장해 두면 변수를 통해 객체를 사용할 수 있다.

```java
클래스 변수;
변수 = new 클래스();

클래스 변수 = new 클래스();
```

** 클래스는 두 가지 용도가 있다. **
1. 라이브러리(API)용 : 다른 클래스에서 이용할 목적으로 설계된다.
2. 실행용 : 프로그램의 실행 진입점인 `main()` 메소드를 제공하는 역할을 한다.(단 한개만 존재)

## 클래스의 구성 멤버

클래스에는 객체가 가져야 할 구성 멤버가 선언된다. `Field`(필드), `Constructor`(생성자), `Method`(메소드)가 있다. 이 구성 멤버들은 생략되거나 복수 개가 작성될 수 있다.

```java
public class ClassName{
	//필드 : 객체의 더이터가 저장되는 곳
    int fieldName;
    
    //생성자 : 객체 생성시 초기화 역할 담당
	ClassName(){...}
    
    //메소드 : 객체의 동작에 해당하는 실행 블록
    void methodNmae(){...}
}
```

## 필드

필드는 객체의 고유 데이터, 부품 객체, 상태 정보를 저장하는 곳이다. 변수는 생성자와 메소드 내에서만 사용되고 생성자와 메소드가 실행 종료되면 자동 소멸된다. 하지만 필드는 생성자와 메소드 전체에서 사용되며 객체가 소멸되지 않는 한 객체와 함께 존재한다.

### 필드 선언
클래스 중괄호 `{}`블록 어디서든 존재할 수 있다. 하지만 생성자와 메소드 중괄호 블록 내부에는 선언될 수 없다. 생성자와 중괄호 블록 내부에 선언된 것은 모두 로컬 변수가 된다.

```java
type fieldName [ = 초기값 ];
```

초기값이 지정되지 않은 필드들은 객체 생성시 자동으로 기본 초기값으로 설정된다.

### 필드 사용

필드를 사용한다는 것은 필드값을 읽고, 변경하는 작업을 말한다.
- 클래스 내부의 생성자나 메소드에서 사용할 경우 단순히 플드 이름을 읽고 변경

```java
// Car class

//필드
int speed;

//생성자
Car(){
	speed = 0;
}

//메소드
void method(...){
	speed = 10;
}
```

- 클래스 외부에서 사용할 경우 우선적으로 클래스로부터 객체를 생성한 뒤 필드 사용

```java
//Person 클래스

void method(){
	//Car 객체생성
    Car myCar = new Car();
    
    //필드사용
    myCar.speed = 60;
}
```

## 생성자

생성자의 역할은 객체 생성 시 초기화를 담당한다. 필드를 초기화하거나, 메소드를 호출해서 객체를 사용할 준비를한다. 생성자는 클래스의 이림으로 되어있고, 리턴 타입이 없다.
생성자를 실행시키지 않고는 클래스로부터 객체를 만들 수 없다.

### 기본 생성자

모든 클래스는 생성자가 반드시 존재하며, 하나 이상을 가질 수 있다. 우리가 클래스 내부에 생성자 선언을 생략했다면 **컴파일러는 기본 생성자(Default Constructor)를 바이트 코드에 자동 추가**시킨다.

그렇기 때문에 클래스에 생성자를 선언하지 않아도 다음과 같이 new 연산자 뒤에 기본 생성자를 호출해서 객체를 생성시킬 수 있다.
```java
Car myCar = new Car();
```

### 생성자 선언

```java
클래스(매개변수선언, ...){
	// 객체의 초기화 코드
}
```
일반적으로 필드에 초기값을 저장하거나 메소드를 호출해 객체 사용전 필요한 준비를 한다. 이때 매개 변수 선언은 생략할 수도 있고, 여러 개를 선언해도 좋다.

클래스에 생성자가 명시적으로 선언되어 있을 경우에는 반드시 선언된 생성자를 호출해서 객체를 생성해야만한다.

```java
Car myCar = new Car("그랜저", "검정", 300);
```
```java
public class Car{
	Car(String model, String color, int maxSpeed){...}
}
```

### 필드 초기화

- 필드를 선언할 때 초기값을 주는 방법 : 동일한 클래스로부터 생성되는 객체들은 모두 같은 값을 가짐
- 생성자에서 초기값을 주는 방법

#### `this.`

`this`는 객체 자신의 참조이다. `this.필드`는 this라는 참조 변수로 필드를 사용하는 것과 동일하다.

```java
public Korean(String name, String ssn){
	this.name = name;
    this.ssn = ssn;
}
```

실제로는 중요한 몇 개 필드만 매개 변수를 통해 초기화되고 나머지 필드들은 선언 시에 초기화하거나 생성자 내부에서 임의의 값 또는 계산 값으로 초기화한다.

### 생산자 오버로딩(Overloading)

자바는 다양한 방법으로 객체를 생성할 수 있도록 생성자 오버로딩을 제공한다. 생성자 오버로딩이란 매개 변수를 달리하는 생성자를 여러 개 선언하는 것을 말한다.

```java
public class Car{
	Car(){...}
	Car(String model){...}
    Car(String model, String color){...}
    Car(String model, String color, int maxSpeed){...}
}
```

생성자 오버로딩 시 주의할 점은 매개 변수의 타입과 개수 선언된 순서가 똑같을 경우 매개 변수 이름만 바꾸는 것은 생성자 오버로딩이라 볼 수 없다.

```java
Car(String model, String color){...}
Car(String color, String model){...} // 생성자 오버로딩 아님
```

### 다른 생성자 호출(`this()`)

생성자 오버로딩이 많아질 경우 생성자 간의 중복된 코드가 발생할 수 있다. 필드 초기화 내용은 한 생성자에서만 집중적으로 작성하고 나머지 생성자는 초기화 내용을 가지고 있는 생성자를 호출하는 방법으로 개선할 수 있다.
```java
클래스([매개변수선언, ...]){
	this(매개변수, ... , 값, ...);
    실행문;
}
```

`this()`는 자신의 다른 생성자를 호출하는 코드로 반드시 **생성자의 첫줄**에서만 허용된다.

```java
public class Car{

	String company = "현대자동차";
    String model;
    String color;
    int maxSpeed;
    
    Car(){}
    
    Car(String model){
    	this(model, "은색", 250);
    }

    Car(String model, String color){
    	this(model, color, 250);
    }
    
	Car(String model, String color, int maxSpeed){
		this.model = model;
        this.color = color;
        this.maxSpeed= maxSpeed;
    }
}
```

## 메소드

객체의 동작에 해당한다. 메소드를 호출하게 되면 중괄호 블록에 있는 모든 코드들이 일괄적으로 실행된다. 메소드는 필드를 읽고 수정하는 역할 + 다른 객체를 생성해 다양한 기능 수행을 하며, 객체 간의 데이터 전달의 수단으로 사용된다. 외부로부터 매개값을 받을 수 있고, 실행 후 어떤 값을 리턴할 수도 있다.

### 메소드 선언

메소드 선언은 선언부(리턴타입, 메소드이름, 매개변수선언)와 실행 블록으로 구성된다. 메소드 선언부를 메소드 시그너처(signature)라고도 한다.

- 리턴 타입 : 메소드가 실행 후 리턴하는 값의 타입
- 메소드 이름 : 자바 식별자 규칙에 맞게 작성하면된다.
	- 관례적으로 메소드명은 소문자로 작성
	- 서로 다른 단어가 혼합된 이름이라면 뒤이어 오는 단어의 첫머리 글자는 대문자로 작성

- 매개 변수 선언 : 매개 변수는 메소드가 실행할 때 필요한 데이터를 외부로부터 받기 위해 사용된다.

```java
double divide(int x, int y){...}
```
```java
double result = divide(10,20);
```

- 매개 변수의 수를 모를 경우
	- 매개 변수를 배열 타입으로 선언하기
```java
int sum1(int[] values){}
```
```java
int[] values = {1,2,3};
int result = sum1(values);
int result2 = sum1(new int[] {1,2,3,4,5});
```

	- 매개 변수를 리스트 넘겨주기
```java
int sum2(int ... values){}
```
```java
int result = sum2(1,2,3);
int result = sum2(1,2,3,4,5);
```

### return

리턴문 사용시 주의할 점은 return문 이후에 실행문이 오면 "Unreachable code"라는 컴파일 오류가 발생한다. return문 이후의 실행문은 실행되지 않는다.

- 리턴값이 있는 메소드  : `return 리턴값;`
- 리턴값이 없는 메소드(void) : `return;`을 사용하면 메소드를 강제 종료함.
	- `break;`를 사용할 수 도 있다.

### 메소드 호출

메소드는 클래스 내,외부의 호출에 의해 실행된다.

- 객체 내부에서 호출 : `메소드(매개값,...);`
- 객체 외부에서 호출 : `클래스 참조변수 = new 클래스(매개값,...);`

### 메소드 오버로딩

클래스 내에 같은 이름의 메소드를 여러개 선언하는 것을 메소드 오버로딩이라고 한다. 메소드 오버로딩의 조건은 매개 변수의 타입, 개수, 순서 중 하나가 달라야한다.

## 인스턴스 멤버와 this

instance(인스턴스) 멤버란 객체(인스턴스) 생성한 후 사용할 수 있는 필드와 메소드를 말하는데, 이들을 각각 인스턴스 필드, 인스턴스 메소드라고 부른다. 인스턴스 필드와 메소드는 객체에 소속된 멤버이기 때문에 객체 없이는 사용할 수 없다.

객체 내부에서도 인스턴스 변수에 접근하기 위해 `this`를 사용할 수 있다.
```java
Car(String model){
 	this.model = model;
}

void setModel(String model){
	this.model = model;
}
```

## 정적 멤버와 static

정적(static) 멤버는 클래스에 고정된 멤버로서 객체를 생성하지 않고 사용할 수 있는 필드와 메소드를 말한다. 이들을 각각 정적 필드, 정적 메소드라고 부르며, 객체(인스턴스)에 소속된 멤버가 아니라 클래스에 소속된 멤버이다.

### 정적 멤버 선언

```java
public class 클래스{
	//정적필드
    static 타입 필드 [= 초기값];
    
    //정적메소드
    static 리턴 타입 메소드(매개변수선언, ...){...}
}
```

객체마다 가지고 있어야 할 데이터라면 인스턴스 필드로 선언하고, 객체마다 가지고 있을 필요성이 없는 공용적인 데이터라면 정적 필드로 선언하는 것이 좋다.

인스턴스 필드를 이용해서 실행해야 한다면 인스턴스 메소드로 선언하고, 인스턴스 필드를 이용하지 않는다면 정적 메소드로 선언한다.

### 정적 멤버 사용

클래스가 메모리로 로딩되면 정적 멤버를 바로 사용할 수 있다. 이때 `.`연산자로 접근한다.

```java
클래스.필드;
클래스.메소드(매개값,...);
```

원칙적으로 정적 멤버는 클래스 이름으로 접근해야 하지만 다음과 같이 객체 참조 변수로도 접근이 가능하다.
하지만 클래스 이름으로 접근하는 것이 좋다.

### 정적 초기화 블록

정적 필드는 필드 선언과 동시에 초기값을 주는 것이 보통이다.
정적 필드의 복잡한 초기화 작업을 위해서 정적 블록을 제공한다.
```java
static{
...
}
```

### 정적 메소드와 블록 선언 시 주의할 점

정적 메소드와 정적 블록을 선언할 때 주의할 점은 객체가 없이도 실행된다는 특징 때문에, 이들 내부에 인스턴스 필드나 인스턴스 메소드를 사용할 수 없다. `this`키워드도 사용이 불가능하다.

### [싱글톤(Singleton)](../디자인패턴/singleton_pattern.md)

가끔 전체 프로그램에서 단 하나의 객체만 만들도록 보장해야 하는 경우가 있다. 단 하나만 생성된다고 해서 이 객체를 **싱글톤**이라고 한다.

- 클래스 외부에서 `new`연산자로 생성자를 호출할 수 없도록 막아야한다.
    -  `private`접근 제한자를 붙여 외부에서 호출할 수 없도록 한다.
- 자신의 타입인 정적 필드를 하나 선언하고 자신의 객체를 생성해 초기화한다.( 클래스 내부에서는 `new` 연산자로 생성자 호출 가능)
    - 정적 필드도 `private` 접근제한자 붙여 외부에서 필드값 변경 못하도록 막기
- 외부에서 호출 할 수 있는 정적 메소드 만들기

```java
public class 클래스{
    //정적 필드
    private static 클래스 singleton = new 클래스();

    //생성자
    private 클래스(){}

    //정적 메소드
    static class getInstance(){
        return singleton;
    }
}
```
```java
// 호출하는 방법
클래스 변수1 = 클래스.getInstance();
클래스 변수2 = 클래스.getInstance();
```

<h2 id="finalField"> final 필드와 상수</h2>

### final 필드

final 필드는 초기값이 저장되면 이것이 최종적인 값이 되어서 프로그램 실행 도중에 수정할 수 없다는 것이다.

```java
final 타입 필드 [=초기값];
```

**초기값 주는 방법**
1. 필드 선언시에 초기화하는 방법 : 단순 값인 경우
2. 생성자에서 주는 방법 : 복잡하거나 외부 데이터로 초기화해야하는 경우

초기화되자 않은 fianl필드를 그대로 남겨두면 컴파일 에러가 발생한다.

### 상수(static final)

일반적으로 불변의 값을 **상수**라고 부른다.(ex) 원주율, 지구의 무게, 둘레 등등

상수는 객체마다 저장할 필요가 없는 공용성을 띠고 있으며, 여러 가지 값으로 초기화될 수 없다.
final필드는 객체마다 저장되고, 생성자의 매개값을 통해서 여러가지 값을 가질 수 있기 때문에 상수가 될 수 없다.

```java
static final 타입 상수 [=초기값];
```
```java
static final 타입 상수;
static{
    상수 = 초기값;
}
```

상수이름은 모두 **대문자**로 작성하는 것이 관례이다. 서로 다른 단어가 혼합된 이름이면 (`_`)로 연결해준다.

```java
static final double PI = 3.14159;
```

## 패키지

프로젝트를 개발하다 보면 적게는 수십 개, 많게는 수백 개의 클래스를 작성해야 한다. 클래스를 체계적으로 관리하지 않으면 클래스 간의 관계가 뒤엉켜서  복잡하고 난해한 프로그램이 되어 결국 유지보수가 어렵게 된다.

자바에서는 클래스를 체계적으로 관리하기 위해 **패키지**를 사용한다. 패키지는 단순히 파일 시스템의 폴더 기능만 하는 것이 아니라 클래스의 일부분이다. 패키지는 클래스를 유일하게 만들어주는 식별자 역할을 한다.

```
상위패키지.하위패키지.클래스
```

### 패키지 선언

패키지는 클래스를 컴파일하는 과정에서 자동적으로 생성되는 폴더이다.

```java
package 상위패키지.하위패키지;

public class ClassName {...}
```

지켜야할 규칙
1. 숫자로 시작해서는 안 되고, `_`,`$`를 제외한 특수 문자를 사용해서는 안된다.
2. java로 시작하는 패키지는 자바 표준 API에서만 사용하므로 사용해서는 안된다.
3. 모두 소문자로 작성하는 것이 관례이다.

### 패키지 선언이 포함된 클래스 컴파일

패키지 선언이 포함된 클래스를 명령 프롬프트에서 컴파일할 경우, 단순히 `javac`으로 컴파일해서는 패키지 폴더가 생성되지 않는다. 명령어 옵션을 추가해줘야한다.

```
$ javac -d .
$ javac -d ../bin
$ javac -d C:/Temp/bin
```

### import문

다른 패키지에 속하는 클래스를 사용하는 방법

- 패키지와 클래스를 모두 기술하는 것 : 패키지 이름이 길거나 사용해야할 클래스 수가 많다면 난잡해짐

```java
package com.mycompany;

public class Car{
    com.hankook.Tire tire = new com.hankook.Tire();
}
```

- 사용하고자 하는 패키지를 `import`문으로 선언

```java
package com.mycompany;

import com.hankook.Tire;
// or import com.hankook.*;

public class Car{
    Tire tire = new Tire();
}
```

`import`문은 패키지 선언과 클래스 선언 사이에 작성된다.
주의할 점은 import문으로 지정된 패키지의 하위 패키지는 import 대상이 아니다. 만약 하위 패키지에 있는 클래스도 사용하려면 두개의 import문이 필요하다.

## 접근 제한자

|접근 제한|적용 대상|접근할 수 없는 클래스|
|-----|-----|-----|
|public|클래스, 필드, 생성자, 메소드 | 없음 |
|protected|필드, 생성자, 메소드 | 자식 클래스가 아닌 다른 패키지에 소속된 클래스 |
|default|클래스, 필드, 생성자, 메소드 | 다른 패키지에 소속된 클래스 |
|private|필드, 생성자, 메소드 | 모든 외부 클래스 |

### 생성자의 접근 제한

클래스에 생성자를 선언하지 않으면 컴파일러에 의해 자동적으로 기본 생성자가 추가된다. 이때 접근 제한은 클래스의 접근 제한과 동일하다.

## Getter와 Setter 메소드

일반적으로 객체 지향 프로그래밍에서 객체의 데이터는 객체 외부에서 직접적으로 접근하는 것을 막는다. 왜냐하면 객체의 데이터를 외부에서 맘대로 읽고 변경할 경우 객체의 무결성이 깨질 수 있기 때문이다.

이러한 문제점을 해결하기 위해 객체 지향 프로그래밍에서는 메소드를 통해서 데이터를 변경하는 방법을 선호한다.
메소드는 매개값을 검증해서 유효한 값만 데이터로 저장할 수 있기 때문이다.

### 예시

```java
void setSpeed(double speed){
    if(speed<0){
        this.speed = 0;
        return;
    }else{
        this.speed = speed;
    }
}
```
```java
double getSpeed(){
    double km = speed*1.6;
    return km;
}
```

**클래스 선언시 가능하다면 필드를 `private`로 선언해 외부로부터 보호하고, 필드에 대한 `Setter`와 `Getter`메소드를 작성해서 필드 값을 안전하게 변경/사용하는 것이 좋다.**

### 메소드 선언방법

```java
private 타입 fieldName; //필드 접근 제한자(private)

//Getter
public 리턴타입 getFieldName(){
    return fieldName;
}

//Setter
public void setFieldName(타입 fieldName){
    this.fieldName =  fieldName;
}
```

만약 필드타입이 `boolean`인 경우에는 Getter는 `is`로 시작한느 것이 관례이다.

```java
private boolean stop;

public boolean isStop(){
    return stop;
}
```

## 어노테이션(Annotation)

- [Spring Annotation 바로가기](https://dahye-jeong.gitbook.io/spring/)

어노테이션은 메타데이터라고 볼 수 있다. 메타데이터란 애플리케이션이 처리해야 할 데이터가 아니라, **컴파일 과정과 실행 과정에서 코드를 어떻게 컴파일하고 처리할 것인지 알려주는 정보**이다.


1. 컴파일러에게 코드 문법 에러를 체크하도록 정보를 제공
2. 소프트웨어 개발 툴이 빌드나 배치 시 코드를 자동으로 생성할 수 있도록 정보를 제공
3. 실행 시(런타임 시) 특정 기능을 실행하도록 정보를 제공

대표적인 예시는 `@Override`어노테이션이다. 어노테이션은 빌드 시 자동으로 XML설정 파일을 생성하거나, 배포를 위해 JAR압축 파일을 생성하는데에도 사용된다.


### 정의

```java
public @interface AnnotationName{
    // 엘리먼트 선언
    타입 elementName() [default 값];
}
```

### 사용

```java
@AnnotationName
@AnnotationName(elementName="값");
```

```java
//예시

public @interface AnnotationName{
    String value();
    int elementName() default 5;
}

@AnnotationName("값");

@AnnotationName(value = "값", elementName=3);
```