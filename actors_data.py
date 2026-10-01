# ---------------- ACTORS GONE BY — DATA FILE ----------------
# One entry per actor. This is the only file you need to touch to add,
# edit or remove someone — re-run build_actors_site.py afterwards and
# every page (Home, Portfolio, and that actor's own Biography page)
# updates automatically.
#
# Fields:
#   slug       - used for the filename (actors/<slug>.html) and must be
#                unique; lowercase, hyphens only.
#   name       - display name.
#   years      - "born–died" string, e.g. "1913–1976".
#   born       - "<date>, <place>" — kept separate from 'years' so the
#                Biography page can show full dates while the Portfolio
#                grid just shows the years.
#   died       - "<date>, <place>" (and cause/circumstances if notable
#                and well documented — kept factual and brief).
#   categories - list of show/franchise names this person appears under
#                in the Portfolio filters. A name not already in
#                CATEGORY_ORDER below gets its own new filter heading
#                automatically.
#   known_for  - short strapline of their most notable roles.
#   bio        - 3-5 sentence original biography (written for this site,
#                not copied from any source) covering their career and
#                what they're remembered for.
#   photo      - path under images/actors/, or None for a "photo coming
#                soon" placeholder. Left as None throughout for now —
#                photos of this era are almost always still in copyright
#                even though the person has passed away, so each needs a
#                specific public-domain or Creative-Commons-licensed
#                source checked by eye before it's added. commons_hint
#                below is a shortcut for that search, not a chosen photo.
#   commons_hint - a Wikimedia Commons category URL that may have a
#                freely-licensed photo worth checking (verify the exact
#                license shown on the file's own page before using it —
#                being in this category is not itself a license).
#
# NOTE ON DATES: three people on the original name list had slightly
# different years than Wikipedia's own infobox gives. This file uses the
# Wikipedia-verified dates: Harry Secombe born 1921 (not 1919), Leslie
# Dwyer born 1906 (not 1905), Pete Postlethwaite 1946-2011 (not 1945-2010,
# he died 2 January 2011, very early in the year).
#
# NOTE ON MICHAEL CAINE: not included. He is still alive — a 2025 social
# media rumour about his death was false and widely debunked at the time.
# This site is specifically for actors who have passed away, so he
# doesn't belong here unless that changes.

CATEGORY_ORDER = [
    "Carry On Legends",
    "Sitcom and Comedy Icons",
    "Oliver!",
    "Zulu",
    "British Film and TV Legends",
]

ACTORS = [
    # ==================== THE CARRY ON LEGENDS ====================
    {
        "slug": "sid-james",
        "name": "Sid James",
        "years": "1913–1976",
        "born": "8 May 1913, Johannesburg, South Africa",
        "died": "26 April 1976, Sunderland, England — suffered a fatal heart attack on stage",
        "categories": ["Carry On Legends"],
        "known_for": "Star of 19 Carry On films (Carry On Camping, Carry On Cleo); Hancock's Half Hour",
        "bio": (
            "Sid James arrived in Britain from South Africa in the 1940s and built a career "
            "on his gravelly voice, distinctive cackling laugh and easy comic timing. He "
            "first found wide fame as Tony Hancock's co-star in Hancock's Half Hour on radio "
            "and television through the 1950s, before becoming one of the most recognisable "
            "faces in British comedy as a mainstay of the Carry On series, appearing in 19 "
            "films — including Carry On Camping and Carry On Cleo — and taking top billing "
            "in most of them. He kept working right up to the end of his life, starring in "
            "the sitcom Bless This House until 1976, when he collapsed and died of a heart "
            "attack while performing on stage in Sunderland."
        ),
        "photo": "sid-james.jpg",
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Sid_James",
    },
    {
        "slug": "kenneth-williams",
        "name": "Kenneth Williams",
        "years": "1926–1988",
        "born": "22 February 1926, King's Cross, London, England",
        "died": "15 April 1988, Bloomsbury, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "Appeared in 26 of the 31 Carry On films (Carry On Up the Khyber); Round the Horne",
        "bio": (
            "Kenneth Williams's nasal, high-camp voice and gift for outrage made him one "
            "of British comedy's most instantly recognisable performers. He built a following "
            "through radio comedy, including Hancock's Half Hour and the innuendo-laden Round "
            "the Horne, before becoming the most prolific cast member of the Carry On series "
            "by a wide margin, appearing in 26 of its 31 films — among them Carry On Up the "
            "Khyber — even as he privately dismissed the films as beneath him in his diaries. "
            "For two decades he was also a fixture of BBC Radio 4's Just a Minute, where his "
            "quick wit and theatrical indignation were given free rein. He remains one of the "
            "most quoted and impersonated British comic voices of the twentieth century."
        ),
        "photo": "kenneth-williams.jpg",
        "photo_credit": (
            "Kenneth Williams by Godfrey Argent, bromide print, 2 December 1968, "
            "NPG x165576 © National Portrait Gallery, London. Used with permission, "
            "non-commercial licence."
        ),
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Kenneth_Williams",
    },
    {
        "slug": "joan-sims",
        "name": "Joan Sims",
        "years": "1930–2001",
        "born": "9 May 1930, Laindon, Essex, England",
        "died": "27 June 2001, Chelsea, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "Appeared in 24 Carry On films — more than any other actress; As Time Goes By; One Foot in the Grave",
        "bio": (
            "Joan Sims trained at RADA and began her career in 1950, going on to appear in "
            "more Carry On films than any other actress — 24 in total, with an unbroken run "
            "of roles from 1964 to 1978. Her range extended well beyond comedy: she played "
            "Gran in Till Death Us Do Part, Madge Kettlewell in Sykes, Madge Hardcastle in As "
            "Time Goes By, and made memorable guest appearances in One Foot in the Grave, "
            "alongside dramatic television work and regular pantomime performances. Across a "
            "five-decade career she became one of the most reliably funny and versatile "
            "character actresses of British film and television."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Joan_Sims",
    },
    {
        "slug": "charles-hawtrey",
        "name": "Charles Hawtrey",
        "years": "1914–1988",
        "born": "30 November 1914, Hounslow, Middlesex, England",
        "died": "27 October 1988, Deal, Kent, England",
        "categories": ["Carry On Legends"],
        "known_for": "23 Carry On films (Carry On Cabby, Carry On Camping), instantly recognisable in his round glasses",
        "bio": (
            "Charles Hawtrey started out as a boy soprano before moving into theatre, radio "
            "and film, supporting comedian Will Hay in a string of 1930s and '40s comedies. "
            "He found lasting fame from Carry On Sergeant (1958) onward, appearing in 23 "
            "films in the series — including Carry On Cabby and Carry On Camping — as a "
            "string of wimpish, effete and instantly recognisable characters, always "
            "identifiable by his round glasses and reedy voice. After being dropped from the "
            "series in 1972 he continued in pantomime and regional theatre, his later years "
            "increasingly overshadowed by ill health."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Charles_Hawtrey_(actor,_born_1914)",
    },
    {
        "slug": "hattie-jacques",
        "name": "Hattie Jacques",
        "years": "1922–1980",
        "born": "7 February 1922, Sandgate, Kent, England",
        "died": "6 October 1980, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "Matron in the Carry On films; Eric Sykes's on-screen sister in Sykes",
        "bio": (
            "Hattie Jacques came up through radio comedy, appearing in It's That Man Again, "
            "Educating Archie and Hancock's Half Hour, before becoming one of the most "
            "beloved faces of the Carry On series. Across 14 films between 1958 and 1974 "
            "she was most often cast as a formidable hospital matron, playing the role five "
            "times and becoming inseparable from it in the public imagination. Alongside her "
            "film work she formed a long and much-loved television partnership with Eric "
            "Sykes, playing his on-screen sister in the sitcom Sykes, and was widely regarded "
            "off-screen as a warm, maternal presence among her Carry On co-stars."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Hattie_Jacques",
    },
    {
        "slug": "barbara-windsor",
        "name": "Dame Barbara Windsor",
        "years": "1937–2020",
        "born": "6 August 1937, Shoreditch, London, England",
        "died": "10 December 2020, Stanmore, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "Nine Carry On films (Carry On Camping); Peggy Mitchell in EastEnders",
        "bio": (
            "Dame Barbara Windsor's six-decade career began with a BAFTA-nominated dramatic "
            "turn in Joan Littlewood's Sparrows Can't Sing (1963), but it was as the "
            "quick-witted, good-time girl of nine Carry On films between 1964 and 1974 — "
            "including Carry On Camping — that she became a national favourite. She found a "
            "second wave of fame late in life as Peggy Mitchell, landlady of the Queen Vic, "
            "in the BBC soap EastEnders, a role she played on and off from 1994 for over two "
            "decades, winning the 1999 British Soap Award for Best Actress. In her final "
            "years she became a prominent campaigner for dementia research and awareness."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Barbara_Windsor",
    },
    {
        "slug": "leslie-phillips",
        "name": "Leslie Phillips",
        "years": "1924–2022",
        "born": "20 April 1924, Tottenham, Middlesex, England",
        "died": "7 November 2022, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "“Ding dong!” in the early Carry On and Doctor films; the Sorting Hat's voice in Harry Potter",
        "bio": (
            "Leslie Phillips rose to prominence in the 1950s as a smooth, upper-class comic "
            "actor known for catchphrases like “Ding dong!” and “Well, hello.” He appeared "
            "in the early Carry On films and starred throughout the Doctor comedy series across "
            "the 1960s and '70s. In his later career he moved into more dramatic roles, "
            "earning BAFTA recognition for Venus (2006) alongside Peter O'Toole, and "
            "introduced himself to an entirely new audience by voicing the Sorting Hat in "
            "three Harry Potter films. His career spanned an extraordinary eight decades, "
            "right up to his death at 98."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Leslie_Phillips",
    },
    {
        "slug": "kenneth-connor",
        "name": "Kenneth Connor",
        "years": "1918–1993",
        "born": "6 June 1918, Highbury, Islington, London, England",
        "died": "28 November 1993, Harrow, Middlesex, England",
        "categories": ["Carry On Legends"],
        "known_for": "Seventeen Carry On films (Carry On Teacher); Monsieur Alphonse in 'Allo 'Allo!",
        "bio": (
            "Kenneth Connor was a stage, film and broadcasting actor who became a familiar "
            "face of British comedy through the Carry On series, appearing in seventeen of "
            "the original thirty films between 1958 and 1978 — including Carry On Teacher — "
            "in roles ranging from nervy romantic leads to broad comic turns. Outside the "
            "series he built a long career in London theatre and on television, including "
            "memorable appearances as Monsieur Alphonse in 'Allo 'Allo! and in Blackadder "
            "the Third. He was appointed MBE in 1991 in recognition of his contribution to "
            "entertainment."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Kenneth_Connor",
    },
    {
        "slug": "peter-butterworth",
        "name": "Peter Butterworth",
        "years": "1915–1979",
        "born": "4 February 1915, Bramhall, Cheshire, England",
        "died": "17 January 1979, Coventry, West Midlands, England",
        "categories": ["Carry On Legends"],
        "known_for": "Sixteen Carry On films (Carry On Abroad, Carry On Screaming!)",
        "bio": (
            "Peter Butterworth became a familiar presence in the Carry On film series, "
            "appearing in sixteen films — including Carry On Abroad and Carry On Screaming! "
            "— typically playing quiet, subtly eccentric characters in support of the "
            "series' bigger personalities. He was also known as the Meddling Monk in "
            "Doctor Who. Before his acting career took off he served as a Royal Navy pilot "
            "during the Second World War and was held as a prisoner of war at Stalag Luft "
            "III, where he met the screenwriter Talbot Rothwell, who would go on to write "
            "many of the Carry On scripts. He worked steadily across film, television and "
            "pantomime throughout his career, including with major stars such as Sean "
            "Connery and Audrey Hepburn."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Peter_Butterworth",
    },
    {
        "slug": "bernard-bresslaw",
        "name": "Bernard Bresslaw",
        "years": "1934–1993",
        "born": "25 February 1934, Stepney, London, England",
        "died": "11 June 1993, Regent's Park, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "Fourteen Carry On films (Carry On Up the Khyber, Carry On Camping)",
        "bio": (
            "Standing at 6 feet 7 inches, Bernard Bresslaw was the tallest member of the "
            "Carry On cast and became best known for his appearances across fourteen films "
            "in the series through the 1960s and '70s, including memorable turns as Bung-Dit-"
            "Din in Carry On Up the Khyber and Bernie Lugg in Carry On Camping. Beyond film, "
            "he worked extensively in theatre with major companies including the Royal "
            "Shakespeare Company and Young Vic. His catchphrase “I only arsked”, from the "
            "earlier television series The Army Game, followed him throughout his career and "
            "became one of British comedy's most quoted lines."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Bernard_Bresslaw",
    },
    {
        "slug": "patsy-rowlands",
        "name": "Patsy Rowlands",
        "years": "1931–2005",
        "born": "19 January 1931, Palmers Green, Middlesex, England",
        "died": "22 January 2005, Hove, East Sussex, England",
        "categories": ["Carry On Legends"],
        "known_for": "Nine Carry On films (Carry On at Your Convenience); Bless This House",
        "bio": (
            "Patsy Rowlands rose to prominence in the Carry On film series, appearing in "
            "nine films between 1969 and 1975 — including Carry On at Your Convenience — "
            "typically playing the dowdy, put-upon wife or the long-suffering secretary. She "
            "achieved further recognition as Betty Lewis in the ITV sitcom Bless This House "
            "(1971–1976), alongside Sid James. Beyond comedy film and television, she had an "
            "extensive stage career in West End productions and later appeared in major "
            "musical revivals including Oliver! and My Fair Lady, across a versatile career "
            "spanning from 1959 to 2001."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Patsy_Rowlands",
    },
    {
        "slug": "june-whitfield",
        "name": "Dame June Whitfield",
        "years": "1925–2018",
        "born": "11 November 1925, Streatham, London, England",
        "died": "29 December 2018, London, England",
        "categories": ["Carry On Legends"],
        "known_for": "Four Carry On films; Terry and June; Mother in Absolutely Fabulous",
        "bio": (
            "Dame June Whitfield had a remarkably prolific seven-decade career spanning "
            "radio, television and film. She gained early prominence as Eth in the BBC radio "
            "comedy Take It from Here, appeared in four Carry On films, and starred opposite "
            "Terry Scott in the long-running sitcoms Happy Ever After and Terry and June. "
            "Her most enduring role came late in her career as Mother in Jennifer Saunders's "
            "Absolutely Fabulous, which she played from 1992 to 2012, becoming a comedy icon "
            "who, by her own account, never wanted the lead role yet remained in constant "
            "demand throughout her working life."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:June_Whitfield",
    },

    # ==================== SITCOM AND COMEDY ICONS ====================
    {
        "slug": "wilfrid-brambell",
        "name": "Wilfrid Brambell",
        "years": "1912–1985",
        "born": "22 March 1912, Dublin, Ireland",
        "died": "18 January 1985, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Albert Steptoe in Steptoe and Son; Paul McCartney's grandfather in A Hard Day's Night",
        "bio": (
            "Wilfrid Brambell was an Irish character actor whose career ran from the 1930s "
            "right up to his death, taking in repertory theatre, film and television. He "
            "became a household name playing the cantankerous rag-and-bone man Albert "
            "Steptoe opposite Harry H. Corbett in the BBC sitcom Steptoe and Son (1962–1974), "
            "a role so vivid that audiences struggled to picture him any other way. That "
            "same year the show made him famous, he took a very different part as Paul "
            "McCartney's tidy, respectable grandfather in the Beatles' film A Hard Day's "
            "Night (1964). He continued working in theatre and film into the early 1980s, "
            "including a well-received silent performance in Terence Davies's short film "
            "Death and Transfiguration shortly before his death."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Wilfrid_Brambell",
    },
    {
        "slug": "harry-h-corbett",
        "name": "Harry H. Corbett",
        "years": "1925–1982",
        "born": "28 February 1925, Rangoon, British Burma",
        "died": "21 March 1982, Hastings, East Sussex, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Harold Steptoe in Steptoe and Son",
        "bio": (
            "Harry H. Corbett trained as a serious stage actor before finding the role "
            "that would define his career: Harold Steptoe, the frustrated, socially "
            "aspiring half of the father-and-son rag-and-bone business in Steptoe and Son "
            "(1962–1974), played alongside Wilfrid Brambell. The show's huge popularity "
            "brought him national fame but also a typecasting he never fully escaped, "
            "despite his own ambitions for more varied, dramatic work. His film credits "
            "included the comedy The Bargee (1964), Carry On Screaming! (1966) and Terry "
            "Gilliam's Jabberwocky (1977). He remained, to the end, inseparable in the "
            "public mind from the character that made him famous."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Harry_H._Corbett",
    },
    {
        "slug": "paul-shane",
        "name": "Paul Shane",
        "years": "1940–2013",
        "born": "19 June 1940, Thrybergh, West Riding of Yorkshire, England",
        "died": "16 May 2013, Rotherham, South Yorkshire, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Ted Bovis in Hi-de-Hi!",
        "bio": (
            "Paul Shane worked as a miner before turning to entertainment, first as a "
            "singer and then as a comedian on the northern club circuit. He was discovered "
            "performing in Coronation Street, a break that led to his best-known role: the "
            "wheeler-dealing holiday camp entertainer Ted Bovis in the BBC sitcom Hi-de-Hi! "
            "through the 1980s. Following that success he starred in the period sitcom You "
            "Rang, M'Lord?, and continued to appear in stage productions and television "
            "guest roles for the rest of his career."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Paul_Shane",
    },
    {
        "slug": "simon-cadell",
        "name": "Simon Cadell",
        "years": "1950–1996",
        "born": "19 July 1950, London, England",
        "died": "6 March 1996, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Jeffrey Fairbrother in Hi-de-Hi!",
        "bio": (
            "A classically trained actor, Simon Cadell gained prominence playing the "
            "well-meaning, faintly hapless holiday camp entertainment manager Jeffrey "
            "Fairbrother in the BBC sitcom Hi-de-Hi! from 1980 to 1984. His theatrical "
            "background led to early television work, including roles in Simon Gray "
            "productions and voice work for the animated film Watership Down, and he later "
            "showed his range in Blott on the Landscape and Life Without George, alongside "
            "guest appearances in Minder and Bergerac. Despite a serious heart attack in "
            "1993 and a subsequent lymphoma diagnosis, he continued working until his death "
            "at 45."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Simon_Cadell",
    },
    {
        "slug": "ruth-madoc",
        "name": "Ruth Madoc",
        "years": "1943–2022",
        "born": "16 April 1943, Norwich, Norfolk, England",
        "died": "9 December 2022, Torquay, Devon, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "“Hi-de-Hi, campers!” — Gladys Pugh in Hi-de-Hi!",
        "bio": (
            "Ruth Madoc was a Welsh actress whose career spanned over six decades on stage "
            "and screen. She achieved her greatest recognition playing Gladys Pugh, the "
            "lovelorn Yellowcoat entertainer with her catchphrase greeting “Hi-de-Hi, "
            "campers!”, in the BBC sitcom Hi-de-Hi! (1980–1988), earning a BAFTA nomination "
            "for the role. Beyond that iconic part, she appeared in numerous theatrical "
            "productions, films including Fiddler on the Roof (1971), and television "
            "programmes ranging from Little Britain to Casualty, with a career in pantomime, "
            "musical theatre and drama that continued almost to the end of her life."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Ruth_Madoc",
    },
    {
        "slug": "leslie-dwyer",
        "name": "Leslie Dwyer",
        "years": "1906–1986",
        "born": "28 August 1906, Catford, London, England",
        "died": "26 December 1986, Truro, Cornwall, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Mr Partridge, the Punch and Judy man, in Hi-de-Hi!",
        "bio": (
            "Leslie Dwyer began acting as a child, appearing in his first film in 1921, and "
            "built an extensive career across several decades of British cinema, including "
            "notable roles in In Which We Serve (1942) and The Way Ahead (1944), and a scene "
            "opposite Brigitte Bardot in Act of Love (1953). He is best remembered today for "
            "television, playing the miserable, hard-drinking Punch and Judy man Mr "
            "Partridge, with his trademark dislike of children, in the BBC sitcom Hi-de-Hi! "
            "He also made guest appearances across popular British series including Doctor "
            "Who, The Sweeney and Steptoe and Son."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Leslie_Dwyer",
    },
    {
        "slug": "arthur-lowe",
        "name": "Arthur Lowe",
        "years": "1915–1982",
        "born": "22 September 1915, Hayfield, Derbyshire, England",
        "died": "15 April 1982, Birmingham, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Captain Mainwaring in Dad's Army",
        "bio": (
            "Arthur Lowe worked across theatre, film and television for 37 years, first "
            "reaching a wide audience as Leonard Swindley in the early years of Coronation "
            "Street. He became one of the best-loved figures in British sitcom history as "
            "the pompous, self-important Captain Mainwaring in Dad's Army (1968–1977), a "
            "performance nominated for seven BAFTAs. His sole BAFTA win came for Best "
            "Supporting Actor in Lindsay Anderson's O Lucky Man! (1973). He continued "
            "working right up until his death from a stroke in 1982, despite failing health "
            "in his later years."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Arthur_Lowe",
    },
    {
        "slug": "john-le-mesurier",
        "name": "John Le Mesurier",
        "years": "1912–1983",
        "born": "5 April 1912, Bedford, England",
        "died": "15 November 1983, Ramsgate, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Sergeant Arthur Wilson in Dad's Army",
        "bio": (
            "John Le Mesurier appeared in well over a hundred films across his career, "
            "almost always in supporting roles — typically mild-mannered authority figures "
            "undone by their own diffidence. He found his most enduring role as the "
            "languid, unflappable Sergeant Arthur Wilson in Dad's Army (1968–1977), whose "
            "genteel bewilderment played perfectly off Arthur Lowe's blustering Captain "
            "Mainwaring. His single major award came for a very different kind of role, "
            "winning the 1971 BAFTA for Best Television Actor for Dennis Potter's play "
            "Traitor. He remained devoted throughout his career to understated, generous "
            "character work rather than leading parts."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:John_Le_Mesurier",
    },
    {
        "slug": "clive-dunn",
        "name": "Clive Dunn",
        "years": "1920–2012",
        "born": "9 January 1920, Brixton, London, England",
        "died": "6 November 2012, Boliqueime, Portugal",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "“Don't panic!” — Lance Corporal Jones in Dad's Army",
        "bio": (
            "Clive Dunn's stage career began in 1935 and was interrupted by wartime service, "
            "which included over four years as a prisoner of war — an experience he later "
            "said helped him understand elderly characters, having watched older prisoners "
            "cope with hardship. He made a speciality of playing much older men, most "
            "famously as the excitable Lance Corporal Jones in Dad's Army (1968–1977), "
            "despite being one of the show's youngest cast members at just 48. In 1971, at "
            "the height of the show's popularity, his novelty song “Grandad” reached number "
            "one on the UK Singles Chart, and he went on to star in his own children's "
            "television series, Grandad, in the early 1980s."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Clive_Dunn",
    },
    {
        "slug": "frank-thornton",
        "name": "Frank Thornton",
        "years": "1921–2013",
        "born": "15 January 1921, Dulwich, London, England",
        "died": "16 March 2013, Barnes, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Captain Peacock in Are You Being Served?",
        "bio": (
            "Frank Thornton became a familiar face on British television from the 1950s "
            "onward, specialising in comedy roles across film and television. He achieved "
            "his greatest fame playing the pompous floorwalker Captain Peacock in the "
            "long-running BBC comedy Are You Being Served? from 1972 to 1985, reprising the "
            "role in its sequel series Grace & Favour. Beyond his iconic department store "
            "character, Thornton appeared in numerous films and television programmes "
            "throughout his career, ranging from Carry On comedies to dramatic roles, and "
            "later joined Last of the Summer Wine in 1997 as Herbert “Truly” Truelove."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Frank_Thornton",
    },
    {
        "slug": "mollie-sugden",
        "name": "Mollie Sugden",
        "years": "1922–2009",
        "born": "21 July 1922, Keighley, Yorkshire, England",
        "died": "1 July 2009, Guildford, Surrey, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Mrs Slocombe in Are You Being Served?",
        "bio": (
            "Mollie Sugden became an international star playing Mrs Slocombe, the "
            "department store saleswoman with a socially superior attitude and a repertoire "
            "of double entendres, in the beloved sitcom Are You Being Served? (1972–1985). "
            "Before landing the role at age 50, she had already spent eight years in "
            "repertory theatre alongside performers including Eric Sykes and appeared in "
            "numerous television shows. Beyond Mrs Slocombe, she played memorable characters "
            "including Nellie Harvey in Coronation Street and Mrs Hutchinson in The Liver "
            "Birds, continuing to work in television, including a Little Britain sketch, "
            "well into her eighties."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Mollie_Sugden",
    },
    {
        "slug": "john-inman",
        "name": "John Inman",
        "years": "1935–2007",
        "born": "28 June 1935, Preston, Lancashire, England",
        "died": "8 March 2007, Paddington, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "“I'm free!” — Mr Humphries in Are You Being Served?",
        "bio": (
            "John Inman became a household name through his iconic portrayal of Mr "
            "Wilberforce Claybourne Humphries in the sitcom Are You Being Served? "
            "(1972–1985). He created the character's signature mincing walk and catchphrase "
            "“I'm free!”, which entered popular culture as the show attracted audiences of "
            "up to 22 million viewers at its peak. Beyond television, Inman had a successful "
            "stage career in pantomime and West End productions, and remained the only "
            "original cast member to reprise his role in the Australian adaptation of the "
            "series. His performance later made him a recognised figure in gay culture, "
            "particularly in the United States."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:John_Inman",
    },
    {
        "slug": "wendy-richard",
        "name": "Wendy Richard",
        "years": "1943–2009",
        "born": "20 July 1943, Middlesbrough, North Riding of Yorkshire, England",
        "died": "26 February 2009, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Miss Brahms in Are You Being Served?; Pauline Fowler in EastEnders",
        "bio": (
            "Wendy Richard's career spanned nearly five decades. She first found fame with "
            "her distinctive Cockney vocals on the 1962 number-one single “Come Outside”, "
            "before becoming best known as the sharp-witted shop assistant Miss Shirley "
            "Brahms in Are You Being Served? (1972–1985), appearing in all 69 episodes. Her "
            "most iconic role came as Pauline Fowler, matriarch of the Fowler family, in "
            "EastEnders from its very first episode in 1985 through to 2006, amassing over "
            "2,000 appearances. She was appointed MBE in 2000 and received a Lifetime "
            "Achievement Award at the 2007 British Soap Awards."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Wendy_Richard",
    },
    {
        "slug": "ronnie-barker",
        "name": "Ronnie Barker",
        "years": "1929–2005",
        "born": "25 September 1929, Bedford, Bedfordshire, England",
        "died": "3 October 2005, Adderbury, Oxfordshire, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "The Two Ronnies; Fletcher in Porridge; Arkwright in Open All Hours",
        "bio": (
            "Ronnie Barker became a cornerstone of British television comedy, achieving "
            "major success as one half of the sketch duo The Two Ronnies (1971–1987), which "
            "became a national institution drawing 15 to 20 million viewers. He also earned "
            "acclaim for his solo roles, particularly as the cunning prisoner Norman Stanley "
            "Fletcher in Porridge (1974–1977) and the stammering shopkeeper Arkwright in "
            "Open All Hours (1976–1985). A master of language and precise comic timing, "
            "Barker wrote much of his own material under pseudonyms such as “Gerald Wiley”, "
            "and retired from acting at 58 to pursue his passion for antiques."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Ronnie_Barker",
    },
    {
        "slug": "ronnie-corbett",
        "name": "Ronnie Corbett",
        "years": "1930–2016",
        "born": "4 December 1930, Edinburgh, Scotland",
        "died": "31 March 2016, Shirley, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "The Two Ronnies; Timothy Lumsden in Sorry!",
        "bio": (
            "Ronnie Corbett was a Scottish comedian and actor best known for his long "
            "partnership with Ronnie Barker on the BBC sketch show The Two Ronnies "
            "(1971–1987), where his meandering, shaggy-dog monologues delivered from a "
            "large armchair became one of British comedy's most familiar sights. He also "
            "demonstrated real range as a solo performer, starring as the mother-dominated "
            "Timothy Lumsden in the sitcom Sorry! (1981–1988) and, earlier, in No — That's "
            "Me Over Here! (1967–1970). Across a career running from 1952 to 2014, he turned "
            "his famously short stature into a source of both visual comedy and gentle "
            "self-deprecation."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Ronnie_Corbett",
    },
    {
        "slug": "leonard-rossiter",
        "name": "Leonard Rossiter",
        "years": "1926–1984",
        "born": "21 October 1926, Wavertree, Liverpool, England",
        "died": "5 October 1984, Lyric Theatre, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Rigsby in Rising Damp; the title role in The Fall and Rise of Reginald Perrin",
        "bio": (
            "Leonard Rossiter established himself as a distinguished character actor across "
            "theatre, film and television, built on decades of repertory work and acclaimed "
            "performances in classic and contemporary plays. He achieved his greatest "
            "prominence through two iconic television comedies: the lecherous, penny-pinching "
            "landlord Rupert Rigsby in Rising Damp (1974–1978), and the title character of "
            "The Fall and Rise of Reginald Perrin (1976–1979). He collapsed from heart "
            "failure at 57 while preparing to perform in Joe Orton's play Loot, at the "
            "height of a career that never slowed down."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Leonard_Rossiter",
    },
    {
        "slug": "richard-briers",
        "name": "Richard Briers",
        "years": "1934–2013",
        "born": "14 January 1934, Raynes Park, Surrey, England",
        "died": "17 February 2013, Bedford Park, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Tom Good in The Good Life",
        "bio": (
            "Richard Briers enjoyed a distinguished five-decade career spanning film, "
            "television, stage and radio. He first gained prominence in the 1960s sitcom "
            "Marriage Lines, but became a household name as Tom Good, the draughtsman who "
            "abandons the rat race to pursue self-sufficiency, in the BBC comedy The Good "
            "Life (1975–1978). Beyond comedy, he collaborated extensively with Kenneth "
            "Branagh on Shakespearean stage and film productions, playing roles including "
            "Polonius in Hamlet and Leonato in Much Ado About Nothing — work that showed a "
            "range far beyond the gentle sitcom character audiences most associated him with."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Richard_Briers",
    },
    {
        "slug": "yootha-joyce",
        "name": "Yootha Joyce",
        "years": "1927–1980",
        "born": "20 August 1927, Wandsworth, London, England",
        "died": "24 August 1980, Marylebone, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Mildred Roper in Man About the House and George and Mildred",
        "bio": (
            "Yootha Joyce came up through Joan Littlewood's Theatre Workshop before moving "
            "into television and film. She became best known for playing Mildred Roper, the "
            "socially aspiring wife of landlord George, in the sitcom Man About the House "
            "(1973–1976), which regularly drew audiences of over 24 million. The character's "
            "popularity led to the spin-off George and Mildred (1976–1979), built around "
            "Mildred's relentless efforts to climb the social ladder. Despite this huge "
            "success, Joyce struggled with typecasting and ill health in her final years, "
            "dying from liver failure at just 53."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Yootha_Joyce",
    },
    {
        "slug": "peter-sallis",
        "name": "Peter Sallis",
        "years": "1921–2017",
        "born": "1 February 1921, Twickenham, Middlesex, England",
        "died": "2 June 2017, Northwood, London, England",
        "categories": ["Sitcom and Comedy Icons"],
        "known_for": "Cleggy in Last of the Summer Wine; the voice of Wallace in Wallace & Gromit",
        "bio": (
            "Peter Sallis achieved remarkable longevity in British entertainment, remembered "
            "for two enduring roles. As Norman “Cleggy” Clegg in Last of the Summer Wine, he "
            "was the only actor to appear in all 295 episodes across the show's run from "
            "1973 to 2010, making him a constant presence in British sitcom for almost four "
            "decades. He was equally beloved as the original voice of the cheese-loving "
            "inventor Wallace in Aardman Animations' Wallace & Gromit films, beginning with "
            "A Grand Day Out in 1989 and winning an Annie Award for The Curse of the "
            "Were-Rabbit in 2005."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Peter_Sallis",
    },

    # ==================== STARS OF OLIVER! (1968) ====================
    {
        "slug": "ron-moody",
        "name": "Ron Moody",
        "years": "1924–2015",
        "born": "8 January 1924, Tottenham, Middlesex, England",
        "died": "11 June 2015, London, England",
        "categories": ["Oliver!"],
        "known_for": "Fagin in Oliver! (stage and 1968 film) — Oscar-nominated",
        "bio": (
            "Ron Moody's career spanned sixty years, but he will always be most closely "
            "associated with one role: Fagin in Lionel Bart's musical Oliver!, which he "
            "originated in the 1960 West End production and reprised for the 1968 film "
            "adaptation, earning a Golden Globe and an Academy Award nomination for his "
            "performance. He returned to the role again in stage revivals through the "
            "1980s and beyond. Beyond Oliver!, he appeared in comedies including The Mouse "
            "on the Moon (1963) and Mel Brooks's The Twelve Chairs (1970), and worked in "
            "children's television as both actor and voice artist."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Ron_Moody",
    },
    {
        "slug": "oliver-reed",
        "name": "Oliver Reed",
        "years": "1938–1999",
        "born": "13 February 1938, Wimbledon, Surrey, England",
        "died": "2 May 1999, Valletta, Malta — suffered a fatal heart attack",
        "categories": ["Oliver!", "Zulu"],
        "known_for": "Bill Sikes in Oliver! (1968); a young officer in Zulu; Proximo in Gladiator",
        "bio": (
            "Oliver Reed built a screen career spanning more than forty years, moving from "
            "Hammer horror pictures to acclaimed collaborations with directors Ken Russell "
            "and Michael Winner. Early in his career he appeared in Zulu (1964), and his "
            "most celebrated role was the menacing Bill Sikes in his uncle Carol Reed's "
            "Oliver! (1968), winner of the Academy Award for Best Picture. He died suddenly "
            "of a heart attack in Malta in 1999 while taking a break from filming Gladiator; "
            "the production was completed around his unfinished scenes using a body double "
            "and early CGI, and his performance as the ageing gladiator trainer Proximo "
            "earned him a posthumous BAFTA nomination."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Oliver_Reed",
    },
    {
        "slug": "jack-wild",
        "name": "Jack Wild",
        "years": "1952–2006",
        "born": "30 September 1952, Royton, Lancashire, England",
        "died": "1 March 2006, Tebworth, Bedfordshire, England",
        "categories": ["Oliver!"],
        "known_for": "The Artful Dodger in Oliver! (1968) — Oscar-nominated at 16",
        "bio": (
            "Jack Wild is best remembered for playing the Artful Dodger in the 1968 film "
            "Oliver!, a role that earned him an Academy Award nomination for Best "
            "Supporting Actor at just 16 years old, along with BAFTA and Golden Globe "
            "nominations for the same performance. Off the back of that breakout success he "
            "starred in the American children's television series H.R. Pufnstuf (1969) and "
            "its film adaptation, and went on to appear in Melody (1971) and Robin Hood: "
            "Prince of Thieves (1991). He also pursued a recording career in the early "
            "1970s before focusing mainly on theatre work in his later years."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Jack_Wild",
    },
    {
        "slug": "harry-secombe",
        "name": "Sir Harry Secombe",
        "years": "1921–2001",
        "born": "8 September 1921, St Thomas, Swansea, Wales",
        "died": "11 April 2001, Guildford, Surrey, England",
        "categories": ["Oliver!"],
        "known_for": "The Goon Show; Mr Bumble in Oliver! (1968)",
        "bio": (
            "Sir Harry Secombe was a Welsh entertainer best known as a founding member of "
            "the groundbreaking BBC radio comedy The Goon Show, in which he played the "
            "accident-prone Neddie Seagoon at the centre of the show's absurd plots. "
            "Alongside his comedy work he was a genuinely accomplished tenor, a talent he "
            "put to use across numerous musicals and films, including a memorable turn as "
            "the pompous Mr Bumble in the 1968 film of Oliver!. Later in his career he "
            "became a familiar face presenting religious television programmes, combining "
            "his singing voice with a warm, sincere screen presence."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Harry_Secombe",
    },
    {
        "slug": "peggy-mount",
        "name": "Peggy Mount",
        "years": "1915–2001",
        "born": "2 May 1915, Southend-on-Sea, Essex, England",
        "died": "13 November 2001, Northwood, London, England",
        "categories": ["Oliver!"],
        "known_for": "Mrs Bumble in Oliver! (1968); The Larkins",
        "bio": (
            "Peggy Mount became a celebrated British actress known for playing domineering, "
            "formidable women across stage, film and television. Her breakthrough came in "
            "1955 as Emma Hornett in Sailor Beware!, a performance the critic Kenneth Tynan "
            "praised for its unforgettable “savage impatience.” She found television "
            "popularity opposite David Kossoff in The Larkins (1958–1964), and went on to "
            "play Mrs Bumble in Oliver! (1968). Her career later embraced more serious "
            "dramatic work, including an acclaimed performance as the title character in "
            "Brecht's Mother Courage, before she retired after losing her sight during her "
            "final stage performance in 1996."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Peggy_Mount",
    },

    # ==================== STARS OF ZULU (1964) ====================
    {
        "slug": "stanley-baker",
        "name": "Sir Stanley Baker",
        "years": "1928–1976",
        "born": "28 February 1928, Ferndale, Glamorgan, Wales",
        "died": "28 June 1976, Málaga, Spain",
        "categories": ["Zulu"],
        "known_for": "Lieutenant John Chard VC in Zulu (also producer); The Guns of Navarone",
        "bio": (
            "Stanley Baker rose to become one of Britain's leading male film stars in the "
            "late 1950s, known for playing tough anti-heroes and working-class characters "
            "quite unlike the typical leading men of the era. He appeared in significant "
            "productions including The Guns of Navarone (1961), but his most memorable "
            "performance was as Lieutenant John Chard in Zulu (1964), a film he also "
            "produced and fought hard to get made. He moved into film production more "
            "broadly as his acting career continued, and was knighted in 1976, though he "
            "died of lung cancer shortly before his investiture could take place."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Stanley_Baker",
    },
    {
        "slug": "nigel-green",
        "name": "Nigel Green",
        "years": "1924–1972",
        "born": "15 October 1924, Pretoria, South Africa",
        "died": "15 May 1972, Brighton, Sussex, England",
        "categories": ["Zulu"],
        "known_for": "Colour Sergeant Bourne in Zulu; The Ipcress File",
        "bio": (
            "Nigel Green's commanding height and imposing build made him a natural fit for "
            "military and action roles throughout the 1960s. He is best remembered for "
            "playing the steady, unflappable Colour Sergeant Frank Bourne in Zulu (1964), "
            "as well as Hercules in Jason and the Argonauts (1963) and Major Dalby in The "
            "Ipcress File (1965) opposite Michael Caine. Beyond film, he worked extensively "
            "in television and on stage, establishing himself as a dependable and versatile "
            "performer across both dramatic and action roles before his death at 47."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Nigel_Green",
    },
    {
        "slug": "jack-hawkins",
        "name": "Jack Hawkins",
        "years": "1910–1973",
        "born": "14 September 1910, Wood Green, Middlesex, England",
        "died": "18 July 1973, Chelsea, London, England",
        "categories": ["Zulu"],
        "known_for": "Reverend Otto Witt in Zulu; The Bridge on the River Kwai; Ben-Hur",
        "bio": (
            "Jack Hawkins worked extensively in stage and film from the 1930s through the "
            "1970s, becoming one of Britain's most popular screen stars of the 1950s, "
            "prized for a formidable presence in military and authority roles. His most "
            "celebrated performances included supporting William Holden and Alec Guinness "
            "in The Bridge on the River Kwai (1957), playing the Roman admiral Quintus "
            "Arrius in Ben-Hur (1959), and appearing as the conflicted missionary Reverend "
            "Otto Witt in Zulu (1964). After losing his voice to throat cancer surgery in "
            "1966, he continued acting with his dialogue dubbed by other performers, right "
            "up until his death."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Jack_Hawkins",
    },

    # ==================== BRITISH FILM AND TV LEGENDS ====================
    {
        "slug": "john-thaw",
        "name": "John Thaw",
        "years": "1942–2002",
        "born": "3 January 1942, Gorton, Manchester, England",
        "died": "21 February 2002, Luckington, Wiltshire, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "Inspector Morse; Jack Regan in The Sweeney",
        "bio": (
            "John Thaw defined two of British television's most iconic detectives. He "
            "first made his name as the hard-bitten, tough-talking Detective Inspector Jack "
            "Regan in the police drama The Sweeney (1975–1978), before finding his most "
            "celebrated role as the classical-music-loving, real-ale-drinking Detective "
            "Chief Inspector Morse in Inspector Morse (1987–2000). The series brought him "
            "international recognition and multiple BAFTA awards, reaching peak audiences "
            "of 18 million viewers in the mid-1990s. Alongside his television work, Thaw "
            "maintained an extensive career in theatre and film throughout his life."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:John_Thaw",
    },
    {
        "slug": "dennis-waterman",
        "name": "Dennis Waterman",
        "years": "1948–2022",
        "born": "24 February 1948, Clapham, London, England",
        "died": "8 May 2022, La Manga, Murcia, Spain",
        "categories": ["British Film and TV Legends"],
        "known_for": "George Carter in The Sweeney; Terry McCann in Minder; New Tricks",
        "bio": (
            "Dennis Waterman's acting career spanned six decades, beginning with child "
            "roles and extending through film, television and West End theatre. He found "
            "household fame in the 1970s as Detective Sergeant George Carter in The "
            "Sweeney, and from 1979 starred as small-time crook Terry McCann in the "
            "comedy-drama Minder, for which he also performed the theme song. His final "
            "major television role came in New Tricks (2003–2014), another series for "
            "which he sang the opening theme — a fitting note for a career that mixed "
            "drama, comedy and music in equal measure."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Dennis_Waterman",
    },
    {
        "slug": "george-cole",
        "name": "George Cole",
        "years": "1925–2015",
        "born": "22 April 1925, Tooting, London, England",
        "died": "5 August 2015, Reading, Berkshire, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "Arthur Daley in Minder; “Flash Harry” in the St Trinian's films",
        "bio": (
            "George Cole enjoyed a remarkable 75-year acting career that began at 15 in "
            "Cottage to Let (1941), opposite Alastair Sim, who became his lifelong mentor. "
            "He became well known for playing the charming rogue “Flash Harry” across the "
            "St Trinian's comedy films of the 1950s and '60s, but his most iconic role by "
            "far was the wheeler-dealing Arthur Daley in the long-running ITV series Minder "
            "(1979–1994), a character that came to define his later career despite his own "
            "mixed feelings about it. He also collaborated with Laurence Olivier in "
            "prestigious film work, and kept working in television comedy into his eighties."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:George_Cole",
    },
    {
        "slug": "pete-postlethwaite",
        "name": "Pete Postlethwaite",
        "years": "1946–2011",
        "born": "7 February 1946, Warrington, Lancashire, England",
        "died": "2 January 2011, Shrewsbury, Shropshire, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "In the Name of the Father; Brassed Off; The Usual Suspects",
        "bio": (
            "Pete Postlethwaite emerged as one of Britain's most respected character actors "
            "following his breakthrough in Distant Voices, Still Lives (1988). He earned an "
            "Academy Award nomination for his portrayal of Giuseppe Conlon in In the Name of "
            "the Father (1993), and gained widespread acclaim for his enigmatic Mr Kobayashi "
            "in The Usual Suspects (1995). His range extended across films including Brassed "
            "Off, The Constant Gardener and Inception, and he was famously described by "
            "Steven Spielberg as “the best actor in the world” — high praise from a director "
            "who cast him twice."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Pete_Postlethwaite",
    },
    {
        "slug": "bob-hoskins",
        "name": "Bob Hoskins",
        "years": "1942–2014",
        "born": "26 October 1942, Bury St Edmunds, Suffolk, England",
        "died": "29 April 2014, London, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "The Long Good Friday; Who Framed Roger Rabbit; Mona Lisa",
        "bio": (
            "Bob Hoskins began acting on stage in 1968 before his breakthrough in the 1978 "
            "BBC serial Pennies from Heaven. He became known for tough yet sensitive "
            "characters, earning critical acclaim for The Long Good Friday (1980) and Mona "
            "Lisa (1986) — for which he won a Cannes Award, BAFTA and Golden Globe, and "
            "received an Academy Award nomination. He reached his widest audience in the "
            "live-action/animated blockbuster Who Framed Roger Rabbit (1988). He retired "
            "from acting in 2012 following a diagnosis of Parkinson's disease, after a "
            "prolific career stretching over four decades."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Bob_Hoskins",
    },
    {
        "slug": "john-hurt",
        "name": "Sir John Hurt",
        "years": "1940–2017",
        "born": "22 January 1940, Chesterfield, Derbyshire, England",
        "died": "25 January 2017, Cromer, Norfolk, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "The Elephant Man; Alien; Midnight Express; the War Doctor in Doctor Who",
        "bio": (
            "Sir John Hurt enjoyed a distinguished career spanning over five decades, "
            "becoming one of Britain's most accomplished and instantly recognisable "
            "performers. He gained prominence through landmark roles including Kane in "
            "Alien (1979), the title role in David Lynch's The Elephant Man (1980), and an "
            "Oscar-nominated performance in Midnight Express (1978). His range extended to "
            "television, notably as Caligula in the BBC's I, Claudius (1976), and he later "
            "introduced a new generation to his distinctive voice as the War Doctor in "
            "Doctor Who (2013). He received four BAFTAs, a Golden Globe and two Academy "
            "Award nominations across his career."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:John_Hurt",
    },
    {
        "slug": "alan-rickman",
        "name": "Alan Rickman",
        "years": "1946–2016",
        "born": "21 February 1946, Brentford, London, England",
        "died": "14 January 2016, London, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "Severus Snape in Harry Potter; Hans Gruber in Die Hard",
        "bio": (
            "Alan Rickman was renowned for his deep, distinctive voice and commanding "
            "presence on both stage and screen. He gained international acclaim through "
            "iconic villain roles, most notably as Hans Gruber in Die Hard (1988) and the "
            "Sheriff of Nottingham in Robin Hood: Prince of Thieves (1991). His portrayal "
            "of Severus Snape across the entire Harry Potter film series (2001–2011) became "
            "perhaps his most celebrated role, widely praised for bringing real complexity "
            "and depth to the character. Beyond villains, he showed considerable range in "
            "dramatic and romantic roles, earning a BAFTA, a Golden Globe, a Primetime Emmy "
            "and a Screen Actors Guild Award over his career."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Alan_Rickman",
    },
    {
        "slug": "robbie-coltrane",
        "name": "Robbie Coltrane",
        "years": "1950–2022",
        "born": "31 March 1950, Rutherglen, Lanarkshire, Scotland",
        "died": "14 October 2022, Larbert, Falkirk, Scotland",
        "categories": ["British Film and TV Legends"],
        "known_for": "Hagrid in Harry Potter; Fitz in Cracker",
        "bio": (
            "Robbie Coltrane established himself as a versatile performer in British comedy "
            "and drama long before achieving worldwide recognition as the gentle giant "
            "Rubeus Hagrid across the entire Harry Potter film series (2001–2011). He earned "
            "three consecutive BAFTA Television Awards for his role as forensic psychologist "
            "Dr Eddie “Fitz” Fitzgerald in the crime series Cracker, one of only two actors "
            "ever to win that award three times running. His film career also included a "
            "memorable turn as the Russian gangster Valentin Zukovsky across several James "
            "Bond films, part of a body of work spanning theatre, television and cinema."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Robbie_Coltrane",
    },
    {
        "slug": "maggie-smith",
        "name": "Dame Maggie Smith",
        "years": "1934–2024",
        "born": "28 December 1934, Ilford, Essex, England",
        "died": "27 September 2024, London, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "The Prime of Miss Jean Brodie; Downton Abbey; Professor McGonagall in Harry Potter",
        "bio": (
            "Dame Maggie Smith's acting career spanned over 70 years, from her stage debut "
            "in 1952 to becoming one of Britain's most garlanded performers, winning two "
            "Academy Awards, seven BAFTAs and a Tony along the way. She won her first Oscar "
            "for the title role in The Prime of Miss Jean Brodie (1969), a performance that "
            "became one of the defining roles of her career. Late in life she found huge new "
            "audiences as the acid-tongued Dowager Countess of Grantham in Downton Abbey and "
            "as the formidable Professor McGonagall in the Harry Potter films, cementing her "
            "as one of the most beloved British actresses of any generation."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Maggie_Smith",
    },
    {
        "slug": "diana-rigg",
        "name": "Dame Diana Rigg",
        "years": "1938–2020",
        "born": "20 July 1938, Doncaster, West Riding of Yorkshire, England",
        "died": "10 September 2020, London, England",
        "categories": ["British Film and TV Legends"],
        "known_for": "Emma Peel in The Avengers; On Her Majesty's Secret Service; Olenna Tyrell in Game of Thrones",
        "bio": (
            "Dame Diana Rigg became a legendary performer across theatre, television and "
            "film. She achieved international fame as the iconic secret agent Emma Peel in "
            "the 1960s television series The Avengers, a role that made her a sex symbol "
            "even though she found the attention that came with it uncomfortable. Her film "
            "work included playing James Bond's wife, Tracy, in On Her Majesty's Secret "
            "Service (1969), and she later won a Tony Award for her Broadway performance as "
            "Medea in 1994. She found renewed popularity among younger audiences late in "
            "life as the sharp-tongued Olenna Tyrell in HBO's Game of Thrones (2013–2017), "
            "earning multiple Emmy nominations for the role."
        ),
        "photo": None,
        "commons_hint": "https://commons.wikimedia.org/wiki/Category:Diana_Rigg",
    },
]
