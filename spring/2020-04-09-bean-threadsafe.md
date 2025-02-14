# Is Spring Bean Thread-Safe?

Spring Bean의 기본 scope는 싱글톤이며, 스프링은 멀티 쓰레드 환경이다. 그렇다면 singleton scope로 생성된 bean들은 Thread Safe 할까?? Spring Container내에서 하나만 존재하도록 보장하지만 그것이 Thread-Safe 를 말하는 것은 아니며, 이러한 부분은 오히려 개발자가 직접 핸들링해줘야한다.

**싱글톤이 멀티스레드 환경에서 서비스 형태의 오브젝트로 사용되는 경우에는 stateless 방식으로 만들어져야한다.** 이때는 읽기전용 값이라면 초기화 시점에 인스턴스 변수에 저장해두고 공유하는 것은 문제 없다. 만약 각 요청에 대한 정보나, DB 서버의 리소스로 부터 생성한 정보는 파라미터와 로컬 변수, 리턴 값을 이용하면 된다. 메소드 파라미터나, 메소드 안에서 생성되는 로컬 변수는 매번 새로운 값을 저장할 독립적인 공간이 만들어지기 때문에 싱글톤이라고 해도 문제없다.

JVM에서 각각의 **쓰레드는 자신의 stack 영역을 가지고 있지만 heap 영역은 쓰레드간에 공유**를 하고 있다.

| 변수                                                    | 저장영역         |
| ------------------------------------------------------- | ---------------- |
| Static 변수, 전역 변수, 코드에서 사용되는 class 정보 등 | Java 메모리 영역 |
| 지역변수, 함수                                          | Stack            |
| 동적할당된 객체                                         | Heap             |

그러므로 Stack 이외의 공간에 저장되는 경우에는 문제가 발생하게 된다. 즉, **스프링 빈의 상태를 변경할 수 있게 만든다면, thread-safe하지 않으며** 이러한 부분에 대해서 인지하고, 개발을 해야한다.

그렇다면, 만약 자주 읽어오는 동적할당되는 객체를 singleton과 같이 만들고 싶으면 어떻게 해야할까??[Cache](./2020-04-19-cache.md)를 사용하면된다! 



## 참고

- [AlwaysPr](https://alwayspr.tistory.com/11)
- [https://groups.google.com/forum/#!topic/ksug/Z1bhFNJcw9Q](https://groups.google.com/forum/#!topic/ksug/Z1bhFNJcw9Q)



