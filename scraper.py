import json
import requests
from bs4 import BeautifulSoup


url = "https://www.ceneo.pl/96798189#tab=reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

reviews = page_dom.select("div.js_product-review")

all_reviews = []

for review in reviews:
    review_id = review["data-entry-id"]
    #print(review_id)

    author = review.select("span.user-post__author-name").pop(0).text.strip()
    #print(type(author))
    #print(author)
    try:
        recommendation = review.select("span.user-post__author-recomendation > em").pop(0).text
        recommendation = True if recommendation == "Polecam" else False if recommendation == "Nie polecam" else None
        #print(type(recommendation))
        #print(recommendation)
    except IndexError: recommendation = None

    stars = review.select("span.user-post__score-count").pop(0).text
    stars = float(stars.split("/").pop(0).replace(",", "."))
    #print(type(stars))
    #print(stars)

    content = review.select("div.user-post__text").pop(0).get_text(0)
    content = content.replace("\n", " ")
    #print(type(content))
    #print(content)

    publish_date = review.select("span.user-post__published > time:nth-child(1)").pop(0)["datetime"]
    publish_date = publish_date.split("  ").pop(0)
    #print(type(publish_date))
    #print(publish_date)

    purchase_date = review.select("span.user-post__published > time:nth-child(2)").pop(0)["datetime"]
    purchase_date = purchase_date.split("  ").pop(0)
    #print(type(purchase_date))
    #print(purchase_date)

    useful = review.select("button.vote-yes[data-total-vote]").pop(0).text
    useful = int(useful)
    #print(type(useful))
    #print(useful)

    useless = review.select("button.vote-no[data-total-vote]").pop(0).text
    useless = int(useless)
    #print(type(useless))
    #print(useless)

    pros = review.select("div.review-feature__title--positives ~ div.review-feature__item")
    pros = [item.text.strip() for item in pros]
    pros = ", ".join(pros)
    #print(type(pros))
    #print(pros)

    cons = review.select("div.review-feature__title--negatives ~ div.review-feature__item")
    cons = [item.text.strip() for item in cons]
    cons = ", ".join(cons)
    #print(type(cons))
    #print(cons)

    single_review = {
        "review_id": review_id,
        "author": author,
        "recommendation": recommendation,
        "stars": stars,
        "content": content,
        "publish_date": publish_date,
        "purchase_date": purchase_date,
        "useful": useful,
        "useless": useless,
        "pros": pros,
        "cons": cons
    }
    all_reviews.append(single_review)
print(json.dumps(all_reviews, indent=4, ensure_ascii=False))
