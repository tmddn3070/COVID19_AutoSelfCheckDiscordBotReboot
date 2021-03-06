# 자동자가진단 디스코드 봇
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ftmddn3070%2FCOVID19_AutoSelfCheckDiscordBotReboot.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ftmddn3070%2FCOVID19_AutoSelfCheckDiscordBotReboot?ref=badge_shield)


## 설명
아침에 자동으로 자가진단을 해주는 봇 입니다. (NEW자동자가진단)

## 라이선스

본 봇의 기본 라이선스는 `MIT`이지만 아래 주의사항을 지킨 후 사용해주시기 바랍니다.

### 주의사항
모든 코드가 공개되어 있으며, 영리적 사용 및 코드의 수정이 가능하지만, 출처(개발자)를 명확하게 밝혀야 합니다.

코드를 사용하실 경우 `discord : white201#0201`로 통보 및 `Github Star` 부탁드립니다.

또한 출력 Embed 하단 개발자명은 수정하시면 안됩니다.

## 기능

- 자동 자가진단 (?정보등록)
- 수동 자가진단 (?진단참여)
- 학사일정, 급식, 시간표, 코로나 확진자 수 알림

## 명령어

### ?명령어
- 모든 명령어를 보여줍니다.

### ?정보등록 [이름] [생년월일] [지역] [학교이름] [학교타입] [비밀번호]
- ?정보등록 홍길동 050201 서울시 ■■고 고등학교 1234 의 형식으로 입력해주세요.
- 지역은 `'서울시','부산시','대구시','인천시','광주시','대전시','울산시','세종시','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주도'`가 가능합니다.

### ?정보확인
- 현재 등록된 정보를 확인합니다. (서버에서 명령어를 실행했더라도 개인DM으로 전송됩니다.)
- 디스코드 아이디를 기준으로 확인합니다.

### ?정보삭제
- 현재 등록된 정보를 완벽하게 삭제합니다. (삭제 후 복구가 불가능하니 신중하게 삭제해주세요.)

### ?진단참여
- 수동으로 자가진단에 참여하는 명령어 입니다. (등록된 정보가 없을 경우 작동하지 않습니다.)

### ?자가진단중지
- 실시되고 있는 자동자가진단을 중지합니다.
- 학사일정에 개학식이 포함되어 있을 경우 자동으로 실시됩니다.

### ?자가진단실시
- 중지된 자가진단을 실시합니다.
- 학사일정에 방학식이 포함되어있을 경우 자동으로 중지될 수 있습니다.
- 자가진단이 중지되는 경우는 `학사일정에 방학식이 포함되어있을 경우`, `사용자가 직접 ?자가진단중지 명령어를 사용` 했을 때 입니다.

### ?급식 <날짜>
- 날짜에 해당하는 급식을 확인해서 전송합니다. (날짜가 없을 경우 자동으로 오늘의 날짜에 해당하는 급식을 전송합니다.)

### ?학사일정 <날짜>
- 날짜에 해당하는 학사일정을 확인해서 전송합니다. (날짜가 없을 경우 자동으로 오늘의 날짜에 해당하는 학사일정을 전송합니다.)

### ?시간표 <날짜>
- 날짜에 해당하는 시간표을 확인해서 전송합니다. (날짜가 없을 경우 자동으로 오늘의 날짜에 해당하는 시간표을 전송합니다.)

## 세팅
### env 세팅
`.env` 파일을 생성해주세요.
그 후 `.env` 파일 내에 아래 형식으로 작성해주세요.
```
TOKEN = 디스코드 봇 토큰
JSON_FILE_NAME = 유저 데이터가 저장될 JSON 파일명 (확장자 포함)
PREFIX = 봇의 명령어 접두사
ADMIN_ID = 봇 관리자의 디스코드 ID
KOR_TOKEN = 한국 디스코드 리스트의 토큰
COVID_API_KEY = 공공데이터 포털 API KEY (시도 확진자 수 API가 활용 신청이 되어있는 KEY)
NEIS_API_KEY = 나이스 오픈데이터 API KEY
```

※한디리 토큰에 경우 [한디리](https://koreanbots.dev/bots/)를 이용하지 않으신다면, KOR_TOKEN이 들어가는 모든 코드를 지우셔도 됩니다.

### 파일 생성
`main.py` 와 같은 경로에 위 env 세팅에서 `JSON_FILE_NAME`으로 지정한 파일 이름으로 파일을 생성해주세요.

## 기타
### 서포트
[초대링크](https://discord.com/api/oauth2/authorize?client_id=846650618701283359&permissions=2184703040&scope=bot) ,[공식 서포트 서버](https://discord.gg/bhJEbEgHED)
### 모듈
사용 모듈 : [hcskr](https://pypi.org/project/hcskr/), [discord.py](https://pypi.org/project/discord.py/), [asyncio](https://pypi.org/project/asyncio/), [requests](https://pypi.org/project/requests/), [xmltodict](https://pypi.org/project/xmltodict3/) 등


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ftmddn3070%2FCOVID19_AutoSelfCheckDiscordBotReboot.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Ftmddn3070%2FCOVID19_AutoSelfCheckDiscordBotReboot?ref=badge_large)