# Map Collection

Map Collection은 **키(key)와 값(value)로 구성된 Entry 객체를 저장**하는 구조를 가지고 있다. 여기서 key와 value는 모두 객체이다. **key는 중복 저장될 수 없지만 value는 중복 저장될 수 있다.** 만약 기존에 저장된 key와 동일한 key로 value을 저장하면 기존의 value은 없어지고 새로운 값으로 대치된다.

| 기능      | 메소드                              | 설명                                                         |
| --------- | ----------------------------------- | ------------------------------------------------------------ |
| 객체 추가 | V put(K key,V value)                | 주어진 키와 값을 추가, 저장되면 값을  return                 |
| 객체 검색 | boolean containsKey(Object key)     | 주어진 키가 있는지 여부                                      |
|           | boolean containsValue(Object value) | 주어진 값이 있는지 여부                                      |
|           | Set<Map.Entry<K,V>> entrySet()      | 키와 값의 쌍으로 구성된 모든 Map.Entry 객체를 Set에 담아서 return |
|           | V get(Object key)                   | 주어진 키가 있는 값을 리턴                                   |
|           | boolean isEmpty()                   | Collection이 비어있는지 여부                                 |
|           | `Set<K> keySet()`                   | 모든 키를 Set 객체에 담아서 return                           |
|           | int size()                          | 저장된 키의 총 수를 return                                   |
|           | `Collection<V> values()`            | 저장된 모든 값을 Collection에 담아서 return                  |
| 객체 삭제 | void clear()                        | 모든 Map.Entry(키와 값) 삭제                                 |
|           | V remove(Object key)                | 주어진 키와 일치하는 Map.Entry 삭제하고 값을 return          |

```java
Map<String, Integer> map = ~;
map.put("정다혜",24);
int score = map.get("정다혜");
map.remove("정다혜");
```

 key를 알고 있으면 get()으로 간단하게 객체를 찾아오면되지만, 저장된 전체 객체를 대상으로 하나씩 얻고 싶은 경우에는 두가지 방법이 있다.

```java
Map<K,V> map = ~;
Set<K> keySet = map.keySet();
Iterator<K> keyIterator = keySet.iterator();
while(keyIterator.hasNext()){
    K key = keyIterator.next();
    V value = map.get(key);
}
```

```java
Set<Map.Entry<K,V>> entrySet = map.entrySet();
Iterator<Map.Entry<K,V>> entryIterator = entrySet.iterator();
while(entrySet.hasNext()){
    Map.Entry<K,V> entry = entryIterator.next();
    K key = entry.getKey();
    V value = entry.getValue();
}
```

## HashMap

HashMap은 연관 배열(Key-Value)을 저장하기 위한 자료 구조이다. 키를 통해 쉽게 값을 저장하거나 얻을 수 있다.

HashMap의 키로 사용될 객체는 hashCode()와 equals() 메소드를 재정의해서 동등 객체가 될 조건을 정해야한다.
동일한 키가 될 조건은 hashCode()의 return값이 같아야하고, equals() 메소드가 true를 return해야한다.

```java
Map<K,V> map = new HashMap<K, V>();
```

키와 값의 타입은 기본타입(byte, short, int, float, double, boolean, char)을 사용할 수 없고, 클래스 및 인터페이스 타입만 가능하다.

```java
Map<String,Integer> map = new HashMap<String, Integer>();
```

```java
import java.util.*;

public class HashMapEx{
    public static void main(String[] args){
        //Map Collection
        Map<String, Integer> map = new HashMap<String, Integer>();
        
        // 객체저장
        map.put("정다혜",100);
        map.put("정미래",99);
        map.put("김하영",98);
        
        // 객체 찾기
        System.out.println(map.get("김하영"));
        
        // 객체 한개씩 처리
        Set<String> keySet = map.keySet();
        Iterator<String> keyIterator = keySet.iterator();
        while(keyIterator.hasNext()){
            String key = keyIterator.next();
            Integer value = map.get(key);
        }
        
        // 객체 삭제
        map.remove("정다혜");
    }
}
```
`HashMap.keySet()` 을 통하여 Set을 꺼내게 되는데, 이 반환되는 Set의 동작에서 HashMap의 데이터 입력의 순서가 보장되지 않는다.

```java
class Student{
    public int sno;
    public String name; 
    
    public Student(int sno, String name){
        this.sno = sno;
        this.name = name;
    }
    
    public boolean equals(Object obj){
        if(obj instanceof Student){
            Student student = (Student)obj;
            return (sno==student.sno) && (name.equals(student.name));
        }else{
            return false;
        }
    }
    
    public int hashCode(){
        return sno + name.hashCode();
    }
}
```

```java
public class HashMapEx{
    public static void main(String[] args){
        Map<Student, Integer> map = new HashMap<Student,Integer>();
        
        // 동일한 key를 저장했으므로 map.size()는 1이다.
        map.put(new Student(1,"정다혜"),95);
        map.put(new Student(1,"정다혜"),95);
    }
}
```

## LinkedHashMap

LinkedHashMap은 HashMap을 확장하는 클래스로 **자료가 입력된 순서를 기억**한다는 특징이 있다.

- key-value 값이 필요한 경우
- 전체크기는 알지 못하는 경우
- 순서를 알아야 하는 경우

이러한 경우에 간편하게 쓸 수 있는 자료구조이다.
즉, HashMap을 통해 자료를 보관할 필요가 있지만, 순서대로 가져와야하는 경우에 사용하면된다.
HashMap을 확장했으므로, HashMap의 모든 기능을 사용할 수 있으며, [Doubly-Linked List](https://dh00023.github.io/algorithm/ds/2018/04/23/algorithm-8/)를 내부에 유지함으로써 입력된 자료 순서를 기억할 수 있다.

```java
LinkedHashMap<String, String> map = new LinkedHashMap<String, String>();
map.put("map", "LinkedHashMap");
map.put("array", "ArrayList");

map.get("map"); // "LinkedHashMap"
map.get("array"); // "ArrayList"

map.forEach((key, value) -> {
	System.out.println(key + " : " + value);
});
```

## Hashtable

HashMap과의 차이점은 **Hashtable은 동기화된(synchronized) 메소드로 구성**되어 있기 때문에 멀티 스레드가 동시에 이 메소드들을 실행할 수 없고, 하나의 스레드가 실행을 완료해야만 다른 스레드를 실행할 수 있다. 그래서 멀티 스레드 환경에서 안전하게 객체를 추가, 삭제할 수 있다.

```java
Map<K,V> map = new Hashtable<K,V>();
```


## Properties

Properties는 Hashtable의 하위 클래스이기 때문에 Hashtable의 모든 특징을 그대로 가지고 있다. 차이점은 **Hashtable은 키와 값을 다양한 타입으로 지정이 가능한데 비해 Properties는 키와 값을 String 타입으로 제한한 Collection**이다.

Properties는 애플리케이션의 옵션정보, 데이터베이스 연결 정보, 국제화 정보가 저장된 (`~.properties`)파일을 읽을 때 주로 사용한다.

```properties
driver = oracle.jdbc.OracleDriver
url = jdbc:oracle:thin:@localhost:1521:orcl
username=name
password=password
```

```java
Properties properties = new Properties();
// 데이터 읽어오기
properties.load(new FileReader("properties 파일경로"));
```

## 참고

- [[Java] LinkedHashMap — 순서를 유지하는 해시맵](https://medium.com/@igniter.yoo/java-linkedhashmap-%EC%88%9C%EC%84%9C%EB%A5%BC-%EC%9C%A0%EC%A7%80%ED%95%98%EB%8A%94-%ED%95%B4%EC%8B%9C%EB%A7%B5-11a7846d8893)
- [Map - LinkedHashMap 사용하는 방법](https://developer-syubrofo.tistory.com/13)