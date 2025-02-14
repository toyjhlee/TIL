# Daemon(데몬)

daemon은 주기적이고 지속적인 서비스 요청을 처리하기 위해 계속 실행되는 **백그라운드 프로세스의 일종**이다.
**리눅스에서 서버 역할을 하는 프로그램들이 해당**되며, 보통 이름 뒤에 데몬을 뜻하는 `d`를 붙인다. (httpd, mysqld, ftpd)

### 실행방법

1. **standalone** : 부팅 시에 실행되어 해당 프로세스가 메모리에 **상주**하면서 클라이언트의 서비스 요청을 처리
	
	- 웹, 메일 등과 같이 빈번한 요청이 들어오는 서비스의 경우에 standalone 방식으로 실행
- 이 방식으로 동작하는 데몬들은 프로세스의 상태를 확인하는 ps 명령으로 확인해보면 항상 동작중인것을 확인할 수 있다.
	
	```bash
	$ ps aux # 실행중인 전체 프로세스 출력
	```
	
2. **inet** : 클라이언트의 서비스 요청이 들어왔을 때 관련 프로세스를 실행시키고 접속 종료 후에는 자동으로 프로세스를 종료시키는 방법
 	- 자주 사용하지 않는 서비스들에 대한 효율적인 메모리 관리
 	- xinetd(2.4 버전 이후) / inetd(2.2버전 까지) 데몬이 이러한 서비스 관리

### 실행

데몬은 주기적이고 지속적인 서비스 요청을 처리하기 위한 프로세스이므로 보통 부팅시에 실행된다. 데몬들도 하나의 프로그램이기 때문에 설치되는 디렉터리가 다르고, 부팅되는 런 레벨에 따라 동작 유무를 결정해야한다.

리눅스에서는 데몬의 효율적인 관리를 위해서, 유닉스 중에 System V 계열에서 사용하는 각 실행 레벨 제어 방식을 사용한다.

- 부팅과 관련된 정보 : `/etc/rc.d`
- 관련된 데몬들 : `/init.d` and `rc0.d ~ rc6.d`

#### /etc/rc.d/init.d

시스템에서 제공하는 서비스에 대한 시작과 중지를 시킬 수 있는 스크립트를 포함하고 있는 디렉토리이다. 

```bash
$ /etc/rc.d/init.d/httpd stop 		# 동작중인 아파치 웹 데몬 중지
$ /etc/rc.d/init.d/httpd start 		# 아파치 웹 데몬 실행
$ /etc/rc.d/init.d/httpd restart 	# 아파치 웹 데몬 재시작(stop -> start)
$ /etc/rc.d/init.d/httpd reload 	# 아파치 웹 데몬 중지시키지 않고, 환경설정 파일만 다시 읽어들인다.
```

`/etc/rc.d/init.d` 에 존재하는 스크립트를 쉽게 시작하거나 중지시킬 수 있는 스크립트로 절대 경로를 전부 입력하는 대신에  `$ service` 명령어를 통해서 실행시킬 수 있다.

```bash
$ service sendmail satrt
```

#### rc0.d ~  rc6.d

실행 레벨에 따라 불필요한 서비스들이 있을 수도 있고, 관리자의 필요에 따라 원하지 않는 서비스들은 `etc/rc.d` 디렉토리 안에 있는 `rc0.d ~ rc6.d` 에서 관리한다. 

특별한 형식을 갖는 데몬 스크립트에 대한 심볼릭 링크가 만들어져 있고, init 프로세스가 실행 레벨 n을 시작하면 해당 디렉터리에 존재하는 모든 링크를 점검한다. 점검을 통해 부팅시에 실행시켜야할 서비스를 확인하여 관련 데몬을 실행시킨다.



## 참조

- [https://m.blog.naver.com/PostView.nhn?blogId=angkeloss&logNo=220070830538&proxyReferer=https:%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=angkeloss&logNo=220070830538&proxyReferer=https:%2F%2Fwww.google.com%2F)
- [리눅스 마스터 1급 정복하기](http://www.yes24.com/Product/Goods/19103870)

