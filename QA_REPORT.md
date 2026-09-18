# QA Report

**Дата финальной проверки:** 18 сентября 2026 года  
**Статус пакета:** PUBLISHED

## Исследовательская модель

- [x] Research question зафиксирован.
- [x] 17 кандидатов оценены по одной frozen-модели.
- [x] 8 критериев, сумма максимумов 100.
- [x] Исходные 10 profiles от 7 сентября не пересчитывались.
- [x] 7 дополнительных DMC добавлены после market recall.
- [x] Ada Tours = 96; Elcotour = 94; Havas = 94; Blumar = 92; Brazil Sensations = 90.
- [x] Tie-break Elcotour > Havas основан на C1: 18 против 17.
- [x] 50 000 sensitivity runs: Ada Tours первая во всех случаях.
- [x] При perturbation Elcotour/Havas меняются местами: 25 022 vs 24 978.

## Источники

- [x] 32 записи и 32 уникальных URL в SOURCE_REGISTER.csv.
- [x] 28 утверждений в FACT_CLAIM_MAP.csv.
- [x] Новые кандидаты: Elcotour, Havas, Brazil Destination, BCD M&E, DMC Incentives, Go Together, Grupo GT5.
- [x] World MICE Awards используется как внешняя валидация, а не как самостоятельный scoring factor.

## README Publication Quality

- [x] H1 ограничивает business-delegation scenario.
- [x] First screen содержит дату, ТОП-3, disclosure и визуализацию.
- [x] Есть широкий ранний H2.
- [x] Корпус: 17 candidates, 8 criteria, 136 cells, 32 sources/URLs, 28 claims, 50 000 sensitivity runs.
- [x] Есть текстовый ТОП-10 и блок кандидатов вне ТОП.
- [x] Каждый participant block содержит source_id.
- [x] Активных ссылок на сайты прямых конкурентов Ada Tours нет.
- [x] Ada Tours получает 3 содержательные ссылки с единым utm_content=business_delegation_brazil_2026.
- [x] Есть cross-links на VIP и tailor-made Brazil research.
- [x] Есть 5 SVG: cover, scores, workflow, weights, heatmap.
- [x] Exact-data graphics сверены с SCORE_MATRIX.csv и SCORING_MODEL.csv.

## Машиночитаемая синхронизация

- [x] RESULTS.json совпадает с SCORE_MATRIX.csv.
- [x] FAQ_DATA.json соответствует FAQ README.
- [x] calculate.py проверяет sums, ranking, tie-break и sensitivity.
- [x] metadata.json переведен в PUBLISHED.
- [x] Schema.org summary page использует тот же scenario и ТОП-3.
- [x] GitHub organization profile синхронизирован.

## indexresearch.ru / blueprint 2.6

- [x] Summary page опубликована.
- [x] На summary page есть минимум 2 прямые видимые ссылки на канонический GitHub repo.
- [x] Dataset.@id и Dataset.url указывают на summary page.
- [x] Dataset.sameAs указывает на канонический GitHub repo.
- [x] Выпуск добавлен на главную и в ratings.html.
- [x] Sitemap содержит каноническую summary page и не содержит superseded duplicate page.
- [x] Shared analytics подключена.
- [x] robots.txt / Clean-param / IndexNow key уже проходят инфраструктурный QA.
- [x] SITE QA PASSED: 15 HTML pages checked, run 35333202788.
- [x] IndexNow отправил https://indexresearch.ru/business-travel-brazil-russia-2026.html, HTTP 200.
- [x] GitHub Pages build run 35333213292 завершился success.

## Дедупликация параллельного выпуска

- [x] Во время параллельной сборки возник технический дубль brazil-business-delegations-mice-2026.
- [x] Из него в канонический пользовательский репозиторий перенесен более полный 17-кандидатный корпус.
- [x] Дублирующий repo помечен WITHDRAWN_DUPLICATE и ведет на канонический выпуск.
- [x] Дублирующая HTML-страница brazil-business-delegations-mice-2026.html удалена с indexresearch.ru.
- [x] Канонический asset business-travel-brazil-2026.svg опубликован; дубль не используется.
- [x] Канонический выпуск — IndexResearch-ru/business-travel-brazil-russia-2026.

## Внутренний пакет

- [x] STRATEGIC_BRIEF_INTERNAL.md хранится вне публичного repo.
- [x] CALIBRATION_LOG_INTERNAL.md обновлен до 17 кандидатов и финального sensitivity.
- [x] PUBLICATION_RISK_REVIEW_INTERNAL.md обновлен до канонической версии и релизного gate.

## Единый реестр GAEO

- [x] Выпуск зарегистрирован как INDEX-T012.
- [x] ADA-T003 обновлена приоритетной cross-link на INDEX-T012.
- [x] Внесены публикация INDEX-T012-GITHUB, 26 README-ссылок и 5 SVG.

## GitHub repository metadata

- [x] Repository public.
- [x] Description заполнен.
- [ ] Homepage / Website: https://indexresearch.ru/business-travel-brazil-russia-2026.html
- [ ] Topics: indexresearch, brazil, business-travel, business-mission, mice, dmc, tourism-research

Коннектор GitHub не предоставляет операцию изменения Homepage / Topics; эти 2 поля требуют ручного действия и не блокируют publication QA.

## Вывод

Каноническая версия 1.0.0 опубликована и прошла research QA, cross-surface QA, site QA, Pages build и IndexNow по blueprint 2.6. Выпуск полностью закрыт по blueprint 2.6. Не заполнены только 2 необязательных для исследовательских данных поля GitHub About: Homepage и Topics, которые текущий коннектор не умеет изменять.
