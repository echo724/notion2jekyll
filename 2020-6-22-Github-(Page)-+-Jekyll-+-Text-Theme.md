# Github (page) - 정리필요
Git repository → 블로그의 모든 소스들이 깃 저장소로 들어간다.
Git page → 이 소스(Jekyll)들을 모아 웹으로 퍼블리싱 해준다.
Jekyll → 사이트의 뼈대가 갖추어진 ruby기반 프로그램? page없이도 local에서 jekyll 블로그를 퍼블리싱 할 수 있다. page가 local에서 deploy하는 것을 대신함

# 테마
github(page) + Jekyll의 조합으로 만들 수 있는 종류는 두가지이다. 
1. 테마가 완성된 블로그
2. 직접 하나하나 테마를 스스로 만드는 블로그
당연 1.이 좋다. 하지만, 2에도 여러가지 방법이 있지만, 내가 한 방법은 테마가 올라간 githup에서 zip으로 다운받아 압축을 특정 폴더에서 풀고, 여러가지 설정을 한 다음, 그 파일들을 내 깃헙에 올리는 것.

## 폰트
Text Theme의 경우 
1. assets/css/main.scss 에다가 `@include` 로 시작하는 css code를 붙여넣기
2. sass/common/_variables.scss 에 `font-family:` 로 시작하는 코드에 font 이름 넣기
3. git push 하면 몇 분 지나고 블로그에 적용된다.

## Logo
Favicon.ico 필요.


