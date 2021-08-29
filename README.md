# covid19-automatic-visit-logger

요즘은 COVID-19로 인해 방문하는 곳 마다 명부에 연락처를 기록하거나, QR코드 또는 ARS를 이용하여 전자출입명부에 기록을 남겨야 합니다.  
전자출입명부가 기존의 수기로 명부를 작성하는 방법보다 많이 편리한 것은 사실이지만, COVID-19가 발생하기 전과 비교하면 여전히 번거롭습니다.  
비콘을 이용하면 이러한 과정 없이 명부에 기록을 남기는 것이 가능하여 더욱 편리할 것 같아 한번 POC를 만들어 보았습니다.  

## 소스 코드

### Sketch
주변의 비콘을 스캔하기 위한 장치로 아두이노와 HM-10 블루투스 모듈을 사용하였으며, sketch 폴더 안에는 아두이노를 제어하기 위한 코드가 있습니다.  
컴퓨터로부터 요청이 들어올 경우 주변의 비콘을 스캔한 결과값을 반환하고, 필요에따라 LED와 부저로 피드백을 발생시키는 역할만 합니다.  

### Python

#### app.py
아두이노로부터 수집한 데이터를 가공하여 주변에 지나간 사람이 있는지 확인하고, 지나간 사람이 있을 경우 그 사람이 DB에 등록되었는지 확인합니다.  
만약 DB에 등록되어 있다면 DB에 방문자의 정보와 방문한 장소, 시각을 기록합니다.

#### db.py
DB에 방문기록을 기록하거나, 사용자나 장소를 등록하고 검색하는 것을 쉽게 하기 위해 만들었습니다.

#### beacon.py
아두이노로부터 받은 주변 비콘의 정보를 가공하고, 거리를 계산하는 것을 쉽게 하기 위해 만들었습니다.

## 문제점
간단하게 POC를 구현한 것이라 실제로 사용하기에는 문제점이 있습니다.

- 현실적인 문제: 실제 전자출입명부에 기록을 남길 수 없습니다. 이 POC는 단지 비콘으로도 기록을 남길 수 있다는 것을 확인하기 위함입니다.
- 정확도: 아두이노로 POC를 구현했는데, 처리 속도가 많이 느려(스캔 한번에 약 3.5초) 사람이 지나간 것을 감지하지 못할 수 있습니다.
- 조작: 비콘에서 송신하는 값을 조작해도 잡아낼 방법이 없습니다.
