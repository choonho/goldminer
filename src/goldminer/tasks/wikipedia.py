import wikipediaapi 

def wiki_page(search, lang='ko'):
    try:
        wiki = wikipediaapi.Wikipedia('Digital Goldminier (dg@example.com)', lang)
        page = wiki.page(search)
        result = {}
        result['title'] = page.title
        result['summary'] = page.summary
        result['fullurl'] = page.fullurl
        return result
    except Exception as e:
        return False

def search_wikipedia(keyword):
   r = wiki_page(keyword, 'ko')
   if r:
      return r
   r = wiki_page(keyword, 'en')
   if r:
      return r
   return False


if __name__ == "__main__":
    a = search_wikipedia("채권")
    print(a)
