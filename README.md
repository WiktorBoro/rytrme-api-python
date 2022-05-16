# Rytrme api python

Easy way to handle the rytrme API with python 

Oficial Rytr-me page: https://rytr.me/

Oficial Rytr-me git documentation: https://github.com/rytr-me/documentation

### To get started

```
pip install rytrme-api-python
```

### Next 

```
from rytrme_api_python import get_text_from_rytr_me_api
```

## All attributes with basic parametrs:
```api_key=<"YOUR API KEY">``` - **required**

```language="🇺🇸 English"``` - language in which the texts will be generated - **change optional**

```tone="Casual"``` - tons in which the text will be - **change optional**

```use_case="Blog Section Writing"``` - type of text that will be generated - **change optional**

```input_contexts = {"SECTION_TOPIC_LABEL": "Your topic", 'SECTION_KEYWORDS_LABEL': "Your keywords"}``` - required - dictionary with your parametr, more information below

```variations = 1``` - number of texts in response - **change optional**

```user_id='USER1'``` - "*For userId you need to supply user ID from your database, eg: primary key for users database table.*" - **change optional**

```formats='html'``` - html or text - **change optional**

```creativity_level='default'``` - fault | none | low | medium | high | max - **change optional**

## Example of use

```
input_contexts = {"SECTION_TOPIC_LABEL": "Role of AI Writers in the Future of Copywriting", 'SECTION_KEYWORDS_LABEL': 'ai writer, blog generator, best writing software'}

response = get_text_from_rytr_me_api(api_key=<"YOUR API KEY">, input_contexts=input_contexts)

print(response)
```

response (list with dictionary):
```
[{'text': '<p>AI writers can help to generate content ideas at scale. They also get rid of writer’s block and are not a replacement for human copywriters.</p><p>AI writing assistants are increasingly getting popular in the workplace. Some companies use them when they need to generate content for a specific topic or niche. While digital agencies use them to generate all kinds of content for their clients.</p>', 'isUnsafe': False}]
```

**If you want to write a blog section in English, the only parameter you need to complete is the input_contexts above**
**If you want to write something else, change use-case and complete the appropriate dictionary**

### All languages list

(Name) - (ID) - you can use name or ID, but with more calls it is recommended to use ID

```
🇦🇪 Arabic  -  60c4eb424660040013ca8a9f
🇧🇬 Bulgarian  -  60eddd5676319d000c81dfc5
🇨🇳 Chinese (S)  -  607ae6531208a9000cb1141c
🇹🇼 Chinese (T)  -  60f853a39bb0df0013c6a588
🇨🇿 Czech  -  60d014e9d6e910001341493a
🇩🇰 Danish  -  60c653b4bca5d4000cc679e3
🇳🇱 Dutch  -  607adbdf6f8fe5000c1e6378
🇺🇸 English  -  607adac76f8fe5000c1e636d
🇮🇷 Farsi  -  60ebc3e06f90af000c8b15f3
🇵🇭 Filipino  -  6159af6d56a355691567ec9d
🇫🇮 Finnish  -  60c65338bca5d4000cc679dd
🇫🇷 French  -  607adb7b6f8fe5000c1e6375
🇩🇪 German  -  607adb536f8fe5000c1e6374
🇬🇷 Greek  -  607adc966f8fe5000c1e637d
🇮🇱 Hebrew  -  607c7c211ebe15000cbbc7b8
🇮🇳 Hindi  -  60ce30891d63cb0013838dfb
🇭🇺 Hungarian  -  6102aa33280cab000c673c2f
🇮🇩 Indonesian  -  6094f9b4addddd000c04c94b
🇮🇹 Italian  -  607adb996f8fe5000c1e6376
🇯🇵 Japanese  -  607adc3d6f8fe5000c1e637b
🇰🇷 Korean  -  607adc716f8fe5000c1e637c
🇱🇹 Lithuanian  -  6198d279d3a709c29634bb26
🇲🇾 Malay  -  60ef33e9c218d0000c2eb058
🇳🇴 Norwegian  -  607db96c182478000c9ac2d9
🇵🇱 Polish  -  607adc056f8fe5000c1e6379
🇵🇹 Portuguese  -  607adbb56f8fe5000c1e6377
🇷🇴 Romanian  -  609fdbec6cc23d000c7c5e84
🇷🇺 Russian  -  607adc2f6f8fe5000c1e637a
🇸🇰 Slovak  -  614a2cc9c1babef3e4008d48
🇪🇸 Spanish  -  607adad66f8fe5000c1e636e
🇸🇪 Swedish  -  6081b157f580d2000c1baf2c
🇹🇭 Thai  -  607c7bec1ebe15000cbbc7b7
🇹🇷 Turkish  -  60a4c3d60b2ef9000ce86d01
🇻🇳 Vietnamese  -  60c65522bca5d4000cc679fa
```

### All tone list

(Name) - (ID) - you can use name or ID, but with more calls it is recommended to use ID

```
Appreciative  -  6058207530f7b1000c1c4f86
Assertive  -  6058209c30f7b1000c1c4f88
Awestruck  -  6058223630f7b1000c1c4f96
Candid  -  605820c030f7b1000c1c4f89
Casual  -  60572a639bdd4272b8fe358a
Cautionary  -  605820d430f7b1000c1c4f8a
Compassionate  -  605820e330f7b1000c1c4f8b
Convincing  -  60572a639bdd4272b8fe358b
Critical  -  60e96f6992161b0013c6ae4a
Earnest  -  6058212830f7b1000c1c4f8d
Enthusiastic  -  6058213830f7b1000c1c4f8e
Formal  -  6058200830f7b1000c1c4f85
Funny  -  60572a649bdd4272b8fe358c
Humble  -  6058215930f7b1000c1c4f8f
Humorous  -  6058216730f7b1000c1c4f90
Informative  -  60ff8d3afc873e000c08e8b2
Inspirational  -  6064c6679bde74000cea994c
Joyful  -  6058219030f7b1000c1c4f92
Passionate  -  6058208730f7b1000c1c4f87
Thoughtful  -  605821c030f7b1000c1c4f93
Urgent  -  605821cc30f7b1000c1c4f94
Worried  -  605821e030f7b1000c1c4f95
```

### All use-case list

(Name) - (ID) - (input_contexts=dictyou need to complete for a given use-case) - you can use name or ID, but with more calls it is recommended to use ID

```
Blog Idea & Outline  -  60a40cf5da9d76000ccc2828 - input_contexts={'PRIMARY_KEYWORD_LABEL': 'Your parametrs'}
Blog Section Writing  -  60584cf2c2cdaa000c2a7954 - input_contexts={'SECTION_TOPIC_LABEL': 'Your parametrs', 'SECTION_KEYWORDS_LABEL': 'Your parametrs'}
Brand Name  -  61e0224822cc129b33031a80 - input_contexts={'BRAND_DESCRIPTION_LABEL': 'Your parametrs'}
Business Idea Pitch  -  6062df03e20e7d000c15609b - input_contexts={'BUSINESS_IDEA_LABEL': 'Your parametrs'}
Business Ideas  -  61e1167527174a50fdcb55e3 - input_contexts={'INTEREST_LABEL': 'Your parametrs', 'SKILLS_LABEL': 'Your parametrs'}
Call To Action  -  61e01c2d5b9c5f0d9d795319 - input_contexts={'DESCRIPTION_LABEL': 'Your parametrs'}
Copywriting Framework: AIDA  -  60d19b16d63485000cab8c15 - input_contexts={'PRODUCT_OR_BRAND_DESCRIPTION_LABEL': 'Your parametrs'}
Copywriting Framework: PAS  -  60d1ac3e548c6b000c8fce5b - input_contexts={'PRODUCT_OR_BRAND_DESCRIPTION_LABEL': 'Your parametrs'}
Email  -  60572a629bdd4272b8fe3588 - input_contexts={'KEY_POINTS_LABEL': 'Your parametrs'}
Facebook, Twitter, LinkedIn Ads  -  60572a629bdd4272b8fe3585 - input_contexts={'PRODUCT_NAME_LABEL': 'Your parametrs', 'PRODUCT_DESCRIPTION_LABEL': 'Your parametrs'}
Google Search Ads  -  6163f3445bb5990332c018b1 - input_contexts={'PRODUCT_NAME_LABEL': 'Your parametrs', 'PRODUCT_DESCRIPTION_LABEL': 'Your parametrs', 'TARGET_KEYWORD_LABEL': 'Your parametrs'}
Interview Questions  -  6058693ccdebbb000c210588 - input_contexts={'INTERVIEWEE_BIO_LABEL': 'Your parametrs', 'INTERVIEW_CONTEXT_LABEL': 'Your parametrs'}
Job Description  -  60586b31cdebbb000c21058d - input_contexts={'JOB_ROLE_LABEL': 'Your parametrs'}
Landing Page & Website Copies  -  605835258c0a4a000c69c962 - input_contexts={'WEBSITE_NAME_LABEL': 'Your parametrs', 'ABOUT_WEBSITE_LABEL': 'Your parametrs', 'FEATURES_LABEL': 'Your parametrs'}
Magic Command  -  60ed7113732a5b000cf99e8e - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Post & Caption Ideas  -  6062d819be972a000c6a05a3 - input_contexts={'POST_TOPIC_LABEL': 'Your parametrs'}
Product Description  -  605832f78c0a4a000c69c960 - input_contexts={'PRODUCT_NAME_LABEL': 'Your parametrs', 'ABOUT_PRODUCT_LABEL': 'Your parametrs'}
Product Description (bullet points)  -  60bb65ca12ba07000cdc8f64 - input_contexts={'PRODUCT_NAME_LABEL': 'Your parametrs', 'PRODUCT_FEATURES_LABEL': 'Your parametrs'}
Profile Bio  -  60633095de064b000c8f5cc8 - input_contexts={'ABOUT_YOU_LABEL': 'Your parametrs'}
Question & Answer  -  611e2a98045b460ef10242ce - input_contexts={'TOPIC_DESCRIPTION_LABEL': 'Your parametrs'}
Reply to Reviews & Messages  -  611e40d404b47fc3a2297a37 - input_contexts={'MESSAGE_LABEL': 'Your parametrs'}
SEO Meta Description  -  60583ac98c0a4a000c69c96f - input_contexts={'PAGE_META_TITLE_LABEL': 'Your parametrs'}
SEO Meta Title  -  60583a058c0a4a000c69c96d - input_contexts={'TARGET_KEYWORDS_LABEL': 'Your parametrs'}
SMS & Notifications  -  6163fe7b1d5d06c1e9693346 - input_contexts={'CONTEXT_LABEL': 'Your parametrs'}
Song Lyrics  -  60e6f4316ab0b5000c848c51 - input_contexts={'SONG_IDEA_LABEL': 'Your parametrs'}
Story Plot  -  60cdad891d63cb00138240d3 - input_contexts={'STORY_IDEA_LABEL': 'Your parametrs'}
Tagline & Headline  -  605838118c0a4a000c69c968 - input_contexts={'DESCRIPTION_LABEL': 'Your parametrs'}
Testimonial & Review  -  607c7ae91ebe15000cbbc7af - input_contexts={'NAME_LABEL': 'Your parametrs', 'REVIEW_TITLE_LABEL': 'Your parametrs'}
Text Editing: Append Content  -  6092917aa9c7620013304f43 - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Text Editing: Continue Ryting  -  6223abf9ea8eb61e65b4e691 - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Text Editing: Expand Content  -  60928e45a9c7620013304f11 - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Text Editing: Improve Content  -  60cdd8b61d63cb001382a390 - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Text Editing: Paragraph Content  -  60b877a110f2fb000cb004eb - input_contexts={'TOPIC_LABEL': 'Your parametrs'}
Text Editing: Reword Content  -  60928476a9c7620013304e89 - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Text Editing: Shorten Content  -  60928752a9c7620013304ea1 - input_contexts={'INPUT_TEXT_LABEL': 'Your parametrs'}
Video Channel Description  -  605856eec2cdaa000c2a7965 - input_contexts={'CHANNEL_PURPOSE_LABEL': 'Your parametrs'}
Video Description  -  6058536ec2cdaa000c2a795e - input_contexts={'VIDEO_TITLE_LABEL': 'Your parametrs'}
Video Idea  -  60584ffdc2cdaa000c2a7957 - input_contexts={'KEYWORDS_LABEL': 'Your parametrs'}
```
