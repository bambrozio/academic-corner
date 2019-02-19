#%%[markdown]
# # An easy introduction to Natural Language Processing
# ## Using computers to understand human language
# By George Seif. Oct 2, 2018
# Extracted From: https://towardsdatascience.com/an-easy-introduction-to-natural-language-processing-b1e2801291c1
#
# # entity analysis
#%%
# coding: utf-8
import spacy

#%%

### Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')

### The text we want to examine
text = "Amazon.com, Inc., doing business as Amazon, is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after Alibaba Group in terms of total sales. The amazon.com website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also produces consumer electronics - Kindle e-readers, Fire tablets, Fire TV, and Echo - and is the world's largest provider of cloud infrastructure services (IaaS and PaaS). Amazon also sells certain low-end products under its in-house brand AmazonBasics."

### Parse the text with spaCy
### Our 'document' variable now contains a parsed version of text.
document = nlp(text)

### print out all the named entities that were detected
for entity in document.ents:
    print(entity.text, entity.label_)

#%%
# ..."remove the names of all people and organisations automatically, for privacy concerns..."
# Using a scrub function:
import spacy

### Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')

### The text we want to examine
text = "Amazon.com, Inc., doing business as Amazon, is an American electronic commerce and cloud computing company based in Seattle, Washington, that was founded by Jeff Bezos on July 5, 1994. The tech giant is the largest Internet retailer in the world as measured by revenue and market capitalization, and second largest after Alibaba Group in terms of total sales. The amazon.com website started as an online bookstore and later diversified to sell video downloads/streaming, MP3 downloads/streaming, audiobook downloads/streaming, software, video games, electronics, apparel, furniture, food, toys, and jewelry. The company also produces consumer electronics - Kindle e-readers, Fire tablets, Fire TV, and Echo - and is the world's largest provider of cloud infrastructure services (IaaS and PaaS). Amazon also sells certain low-end products under its in-house brand AmazonBasics."


### Replace a specific entity with the word "PRIVATE"
def replace_entity_with_placeholder(token):
    if token.ent_iob != 0 and (token.ent_type_ == "PERSON" or token.ent_type_ == "ORG"):
        return "[PRIVATE] "
    else:
        return token.string

### Loop through all the entities in a piece of text and apply entity replacement
def scrub(text):
    doc = nlp(text)
    for ent in doc.ents:
        ent.merge()
    tokens = map(replace_entity_with_placeholder, doc)
    return "".join(tokens)


print(scrub(text))

#%% 
# Extracting information from text (with textacy)
# Algorithms: Semi-structured Statement Extraction.
# ... we can extract certain “facts” about the entity of our choice.
# e.g: ... we’re going to take the entire summary of Washington D.C’s Wikipedia page.


import spacy
import textacy.extract

### Load spaCy's English NLP model
nlp = spacy.load('en_core_web_lg')

### The text we want to examine
text = """Washington, D.C., formally the District of Columbia and commonly referred to as Washington or D.C., is the capital of the United States of America.[4] Founded after the American Revolution as the seat of government of the newly independent country, Washington was named after George Washington, first President of the United States and Founding Father.[5] Washington is the principal city of the Washington metropolitan area, which has a population of 6,131,977.[6] As the seat of the United States federal government and several international organizations, the city is an important world political capital.[7] Washington is one of the most visited cities in the world, with more than 20 million annual tourists.[8][9]
The signing of the Residence Act on July 16, 1790, approved the creation of a capital district located along the Potomac River on the country's East Coast. The U.S. Constitution provided for a federal district under the exclusive jurisdiction of the Congress and the District is therefore not a part of any state. The states of Maryland and Virginia each donated land to form the federal district, which included the pre-existing settlements of Georgetown and Alexandria. Named in honor of President George Washington, the City of Washington was founded in 1791 to serve as the new national capital. In 1846, Congress returned the land originally ceded by Virginia; in 1871, it created a single municipal government for the remaining portion of the District.
Washington had an estimated population of 693,972 as of July 2017, making it the 20th largest American city by population. Commuters from the surrounding Maryland and Virginia suburbs raise the city's daytime population to more than one million during the workweek. The Washington metropolitan area, of which the District is the principal city, has a population of over 6 million, the sixth-largest metropolitan statistical area in the country.
All three branches of the U.S. federal government are centered in the District: U.S. Congress (legislative), President (executive), and the U.S. Supreme Court (judicial). Washington is home to many national monuments and museums, which are primarily situated on or around the National Mall. The city hosts 177 foreign embassies as well as the headquarters of many international organizations, trade unions, non-profit, lobbying groups, and professional associations, including the Organization of American States, AARP, the National Geographic Society, the Human Rights Campaign, the International Finance Corporation, and the American Red Cross.
A locally elected mayor and a 13‑member council have governed the District since 1973. However, Congress maintains supreme authority over the city and may overturn local laws. D.C. residents elect a non-voting, at-large congressional delegate to the House of Representatives, but the District has no representation in the Senate. The District receives three electoral votes in presidential elections as permitted by the Twenty-third Amendment to the United States Constitution, ratified in 1961."""
### Parse the text with spaCy
### Our 'document' variable now contains a parsed version of text.
document = nlp(text)

### Extracting semi-structured statements
statements = textacy.extract.semistructured_statements(document, "Washington")

print("**** Information from Washington's Wikipedia page ****")
count = 1
for statement in statements:
    subject, verb, fact = statement
    print(str(count) + " - Statement: ", statement)
    print(str(count) + " - Fact: ", fact)
    count += 1