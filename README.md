# WordAnalysis
Десктопное приложение Python под Windows для анализа word документов. 

Пользователь загружает файл .doc, приложение исправляет пунктуацию и орфографию, исправляет оформление в соответствии с заранее заданными настройками. 

Чтобы исправление оформления работало правильно, необходимо правильно разметить документ. 

* Заголовок - Заголовок без нумерации
* Подзаголовок - Heading 2
* Пункт Стиль - Heading 3
* Подпункт - Heading 4
* Обычный - Normal

## Использованные технологии

* Yandex спеллер (https://yandex.ru/dev/speller/).
* SbertPuncCase (https://huggingface.co/kontur-ai/sbert_punc_case_ru).

Для использования SbertPuncCase необходимо:
1. установить git-lfs командой `pip install git-lfs`;
2. установить модель командой `pip install git+https://huggingface.co/kontur-ai/sbert_punc_case_ru`. 

## Использованные библиотеки
|Lib|Version|
|---|-------|
|transformers|4.42.4|
|python-docx|1.1.2|
|git-lfs|1.6|



