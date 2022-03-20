# CeneoScraper

## Analiza struktury opinii w serwisie [Ceneo.pl]

|Składowa|Selektor|Zmienna|
---------------------------
|opinia|div.js_product-review|review|

|identyfikator opinii|\[data-entry-id\]|review_id|

|autor|.user-post_author-name|author|

|rekomendacja|span.user-post__author-recomendation > em|recommendation|

|liczba gwiazdek|span.user-post__score-count|stars|

|treść|user-post__text|content|

|data wystawienia|span.user-post__published > time:nth-child(1)\[datetime\]|publish_date|

|data zakupu|span.user-post__published > time:nth-child(2)\[datetime\]|purchase_date|

|dla ilu przydatna|button.vote-yes[data-total-vote]|useful|

|dla ilu nieprzydatna|button.vote-no[data-total-vote]|useless|

|lista zalet|div.review-feature__col:has( >review-feature__title review-feature__title--positives) > div.review-feature__item|pros|

|lista wad||cons| 

## inne metody
|dla ilu przydatna|button.vote-yes > span||
|dla ilu przydatna|span[id^=votes-yes]||

