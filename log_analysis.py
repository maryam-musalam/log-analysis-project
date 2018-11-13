#!/usr/bin/env python
# impoert psycopg2 moduale
import psycopg2


def query_connect(sql):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(sql)
    result = c.fetchall()
    db.close()
    return result


# function to find the most popular thre articles which get most view.
def most_popular_three_articles():
    result = query_connect(
                           """ SELECT articles.title , COUNT(*) AS views FROM
                           log JOIN articles ON log.path LIKE
                           CONCAT('%', articles.slug, '%')
                           GROUP BY path , title ORDER BY views DESC
                           LIMIT 3 """
                           )
    print " What are the most popular three articles of all time? "
    for row in result:
        print "\" " + row[0] + "\" -- " + str(row[1]) + " viwes."
    print " "


# find the most three authours who got most views on there articles.
def most_popular_authors():
    result = query_connect(
                           """ SELECT authors.name ,COUNT(*) AS views FROM
                           authors JOIN articles ON authors.id =
                           articles.author JOIN log ON log.path LIKE
                           CONCAT('%', articles.slug, '%') GROUP
                           BY authors.name
                           ORDER BY views DESC """
                           )
    print "Who are the most popular article authors of all time?"
    for row in result:
        print row[0] + " -- " + str(row[1]) + " viwes."
    print ""


# function to find requests which lead to more than 1% of errors.
def request_lead_to_more_than_one_persentage_error():
    result = query_connect(
                           """select error_precentage.date ,
                           error_precentage.error from
                           error_precentage where error > 1"""
                           )
    print "On which days did more than 1% of requests lead to errors?"
    for row in result:
        r = row[0].strftime('%B %d, %Y')
        print str(r) + " - " + str("%.1f" % (row[1])) + "% error."


if __name__ == "__main__":
    most_popular_three_articles()
    most_popular_authors()
    request_lead_to_more_than_one_persentage_error()
