# Сколько сезонов
# Чтобы узнать, насколько продуктивно работает режиссер
# Alastair Fothergill, мы решили посчитать,
# сколько сезонов сериалов он всего снял.
#
# Пример результата:
#
# Длительность всех сериалов режисcера Alastair Fothergill составляет x сезона.
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("SELECT SUM(duration) "
                "FROM netflix "
                "WHERE director='Alastair Fothergill' "
                "AND type='TV Show' "
                "")
cur.execute(sqlite_query)
seazons = cur.fetchall()[0][0]

result = ('Длительность всех сериалов режиссера Alastair Fothergill'
          f' составляет {seazons} сезона.')
con.close()

if __name__ == '__main__':
    print(result)
