# Collection Framework - List, Set

자바는 자료구조(Data Structure)를 바탕으로 객체들을 효율적으로 추가, 삭제, 검색할 수 있도록 `java.util` 패키지에 컬랙션과 관련된 인터페이스와 클래스들이 포함되어 있으며, 이들을 총칭해서 Collection Framework라고 부른다.

**Collection** 은 객체를 수집해서 저장하는 역할을 하며, **Framework** 란 사용 방법을 미리 정해 놓은 라이브러리를 말한다.

![](https://t1.daumcdn.net/cfile/tistory/175466144CC11C2755)

| 인터페이스 분류  | 특징                                               | 구현 클래스                                      |
| ---------------- | -------------------------------------------------- | ------------------------------------------------ |
| Collection(List) | - 순서를 유지하고 저장<br>- 중복 저장 가능         | ArrayList<br>Vector<br>LinkedList                |
| Collection(Set)  | - 순서를 유지하지않고 저장<br/>- 중복 저장 안 됨   | HashSet<br/>TreeSet                              |
| Map              | - 키와 값의 쌍으로 저장<br/>- 키는 중복 저장 안 됨 | HashMap<br/>Hashtable<br/>TreeMap<br/>Properties |

## List Collection

List는 객체를 일렬로 늘어놓은 구조를 가지고 있다. 객체를 저장하면 자동 인덱스가 부여되고 인덱스로 객체를 검색, 삭제할 수 잇는 기능을 제공한다. List Collection 은 객체 자체를 저장하는 것이 아니라 객체 번지를 참조한다. 동일한 객체를 중복 저장할 수도 있다.

([[자료구조 List](https://dh00023.github.io/algorithm/ds/2018/04/23/algorithm-8/)]에 자세한 설명이 있다.)

List 인터페이스는 제네릭 타입이다.

| 기능      | 메소드                         | 설명                                             |
| --------- | ------------------------------ | ------------------------------------------------ |
| 객체 추가 | boolean add(E e)               | 주어진 객체를 맨 끝에 추가                       |
|           | void add(int index, E element) | 주어진 인덱스에 객체 추가                        |
|           | set(int index, E element)      | 주어진 인덱스에 저장된 객체를 주어진 객체로 변경 |
| 객체 검색 | boolean contains(Object o)     | 주어진 객체가 저장되어 있는지 여부               |
|           | E get(int index)               | 주어진 인덱스에 저장된 객체를 리턴               |
|           | isEmpty()                      | 컬렉션이 비어있는지 조사                         |
|           | int size()                     | 저장되어 있는 전체 객체 수를 리턴                |
| 객체 삭제 | void clear()                   | 저장된 모든 객체 삭제                            |
|           | E remove(int index)            | 주어진 인덱스에 저장된 객체 삭제                 |
|           | boolean remove(Object o)       | 주어진 객체를 삭제                               |

```java
List<String> list = ...;
list.add("정다혜");
list.add(1,"정미래"); 
String str = list.get(1);
list.remove(0);
list.remove("정미래");
```

```java
for(int i=0;i<list.size();i++){
    String str = list.get(i);
}
for(String str : list){
}
```

### ArrayList

ArrayList는 List 인터페이스의 구현 클래스로, ArrayList에 객체를 추가하면 객체가 인덱스로 관리된다. 배열은 생성할 때 크기가 고정되고 사용 중에 크기를 변경할 수 없지만, ArrayList는 capacity(저장 용량)를 초과한 객체들이 들어오면 자동으로 capacity가 증가한다.

```java
List<E> list = new ArrayList<E>();
```

기본 생성자로 ArrayList 객체를 생성하면 내부에 10ㄱ의 객체를 저장할 수 있는 초기 용량을 가진다. 저장되는 객체 수가 늘어나면 자동으로 증가하지만, 처음부터 용량을 크게 하고 싶다면 용량의 크기를 매개값으로 받는 생성자를 이용하면된다.

```java
List<String> list = new ArrayList<String>(30);
```

ArrayList에 객체를 추가하면 인덱스 0부터 차례대로 저장된다. 특정 인덱스의 객체를 제거하면 바로 뒤 인덱스부터 마지막 인덱스까지 모두 앞으로 1씩 당겨진다. 또한 특정 인덱스에 객체를 생성하면 해당 인덱스부터 1씩 밀려난다. 따라서 **빈번한 객체 삭제와 삽입을 일어나는 곳에서는 ArrayList를 사용하는 것은 바람직하지 않다.** 이러한 경우는 LinkedList를 사용하는 것이 좋다.

**ArrayList는 맨 마지막에 객체를 추가하는 경우에 더 좋은 성능**을 보인다.

ArrayList를 생성하고 런타임 시 필요에 의해 객체들을 추가하는 것이 일반적이지만, 고정된 객체들로 구성된 List를 생성하는 경우에는 `ArrayList.asList(T...a)` 메소드를 사용하는 것이 간편하다.

```java
List<T> list = Arrays.asList(T...a);
```

T 타입 파라미터에 맞게 asList()의 매개값을 순차적으로 입력하거나, T[] 배열을 매개값으로 주면된다.

```java
import java.util.Arrays;
import java.util.list;

public class ArraysAsListEx {
    public static void main(String[] args){
        List<String> list = Arrays.asList("정다혜", "정미래", "정서영");
        for(String name : list){
            System.out.println(name);
        }
    }
}
```

### Vector

Vector는 ArrayList와 동일한 내부 구조를 가지고 있다.

```java
List<E> list = new Vector<E>();
```

ArrayList와 다른 점은 Vector는 동기화된(synchronized) 메소드로 구성되어 있기 때문에 멀티 스레드가 동시에 이 메소드들을 실행할 수 없고, **하나의 스레드가 실행을 완료해야만 다른 스레드를 실행**할 수 있다. 그래서 **멀티 스레드 환경에서 안전하게 객체를 추가, 삭제**할 수 있다. 

([Vector(C++) 살펴보기](https://dh00023.github.io/stl/2018/05/26/cpp-vector))



### Linked List

ArrayList와 사용 방법은 똑같지만 내부 구조는 완전 다르다. ArrayList는 내부 배열에 객체를 저장해서 인덱스로 관리하지만, **LinkedList는 인접 참조를 링크해서 체인처럼 관리**한다.

LinkedList에서 특정 인덱스의 객체를 제거하면 앞뒤 link만 변경되고 나머지 link는 변경되지 않는다. 객체를 삽입할때도 마찬가지이다. 그러므로 **빈번한 객체 삭제와 삽입이 일어나는 곳에서는 LinkedList가 좋은 성능**을 발휘한다.

```java
List<E> list = new LinkedList<E>();
```

([ Linked List 자료구조 살펴보기](https://dh00023.github.io/algorithm/ds/2018/04/23/algorithm-8/) )



| 구분       | 순차적으로 추가/삭제 | 중간에 추가/삭제 | 검색   |
| ---------- | -------------------- | ---------------- | ------ |
| ArrayLIst  | 빠르다               | 느리다           | 빠르다 |
| LinkedList | 느리다               | 빠르다           | 느리다 |

### sychronizedList

Collection 프레임워크의 대부분의 클래스(ArrayList)는 Single Thread 환경에서 사용할 수 있도록 설계되었다. 그러므로 멀티 스레드 환경에서 안전하지않다.
Single Thread환경에서 Multi Thread환경으로 전달할 경우에 대비해 비동기화된 메소드를 동기화된 메소드로 Wrapping하는 synchronizedList()메소드를 제공하고 있다.

| 리턴타입      | 메소드                     | 설명                                                         |
| --------- | -------------------------- | ------------------------------------------------------------ |
| List<T> | synchronizedList(List<T> list)           | List를 동기화된 List로 리턴 |

```java
List<T> list = Collections.synchronizedList(new ArrayList<T>());
```

## Set Collection

List Collection은 저장순서를 유지하지만, **Set Collection은 저장 순서가 유지되지 않는다**. 또한 **객체를 중복해서 저장할 수 없고, 하나의 null만 저장할 수 있다**. 즉, 수학의 집합에 비유할 수 있다.

| 기능      | 메소드                     | 설명                                                         |
| --------- | -------------------------- | ------------------------------------------------------------ |
| 객체 추가 | boolean add(E e)           | 주어진 객체를 저장, 객체가 성공적으로 저장되면 true, 중복이면 false return |
| 객체 검색 | boolean contains(Object o) | 주어진 객체가 저장되어 있는지 여부                           |
|           | isEmpty()                  | 컬렉션이 비어있는지 조사                                     |
|           | `Iterator<E> iterator`     | 저장된 객체를 한번씩 가져오는 반복자 return                  |
|           | int size()                 | 저장되어 있는 전체 객체 수 리턴                              |
| 객체 삭제 | void clear()               | 저장된 모든 객체 삭제                                        |
|           | boolean remove(Object o)   | 주어진 객체를 삭제                                           |

Set Collection은 Generic Type으로 구체적인 타입은 구현 객체를 생성할 때 결정된다.

```java
Set<String> set = ...;
set.add("홍길동");
set.add("정미래");
set.remove("정미래");
```

Set Collection은 인덱스로 객체를 검색해서 가져오는 메소드가 없다. 대신, 전체 객체를 대상으로 한번 씩 반복해서 가져오는 반복자(Iterator)를 제공한다.

```java
Iterator<String> iterator = set.iterator();
```

| 리턴 타입 | 메소드명  | 설명                                           |
| --------- | --------- | ---------------------------------------------- |
| boolean   | hasNext() | 가져올 객체가 있으면 true, 없으면 false return |
| E         | next()    | 컬렉션에서 하나의 객체를 가져온다.             |
| void      | remove()  | Set 컬렉션에서 객체를 제거                     |

```java
Set<String> set = ...;
Iterator<String> iterator = set.iterator();
while(iterator.hasNext()){
    String str = iterator.next();
}
```

```java
Set<String> set = ...;
for(String str : set){
}
```

### HashSet

HashSet은 Set인터페이스의 구현 클래스이다.

```java
Set<E> set = new HashSet<E>();
```

HashSet은 **객체들을 순서 없이 저장하고 동일한 객체는 중복 저장하지 않는다.** 여기서 동일한 객체란 꼭 같은 인스턴스를 뜻하지 않는다. HashSet은 객체를 저장하기 전에 먼저 객체의 hashCode() 메소드를 호출해 해시코드를 얻어낸다. 그리고 이미 저장된 객체들의 hashcode와 비교한다. 동일한 hashcode가 있다면 다시 equals() 메소드로 두 객체를 비교해 true가 나오면 동일한 객체로 판딘헤 저장하지 않는다.

문자열을 HashSet에 저장할 경우, 같은 문자열을 갖는 String 객체는 동등한 객체, 다른 문자열은 다른 객체로 간주된다. 이는 String 클래스가 hashCode()와 equals() 메소드를 재정의하기 때문이다.

```java
public class Member{
    public String name;
    public int age;
    
    public Member(String name, int age){
        this.name = name;
        this.age = age;
    }
    
    @Override
    public boolean equals(Object obj){
        if(obj instanceof Member){
            Member member = (Member)obj;
            return member.name.equals(name) && (memeber.age==age);
        }else{
            return false;
        }
    }
    
    @Override
    public int hashCode(){
        // name과 age가 같으면 동일한 hashCode리턴
        return name.hashCode()+age;
    }
}
```

```java
import java.util.*;

public class HashSetEx{
    public static void main(String[] args){
        Set<Member> set = HashSet<Member>();
        
        set.add(new Member("정다혜",24));
        set.add(new Member("정다혜",24)); // 인스턴스는 다르지만 내부 데이터가 동일하므로 1개저장
    }
}
```

### sychronizedSet

Collection 프레임워크의 대부분의 클래스(HashSet)는 Single Thread 환경에서 사용할 수 있도록 설계되었다. 그러므로 멀티 스레드 환경에서 안전하지않다.
Single Thread환경에서 Multi Thread환경으로 전달할 경우에 대비해 비동기화된 메소드를 동기화된 메소드로 Wrapping하는 synchronizedSet()메소드를 제공하고 있다.

| 리턴타입      | 메소드                     | 설명                                                         |
| --------- | -------------------------- | ------------------------------------------------------------ |
| Set<T> | synchronizedSet(Set<T> s)           | Set를 동기화된 Set로 리턴 |

```java
Set<T> s = Collections.synchronizedSet(new HashSet<T>());
```