Title: Scrape a Reddit AMA
Date: 2012-12-27 
Tags: reddit, programming, python
Slug: scrape-reddit-ama
Author: Snehasish
Summary: Reddit AMA Scraper using PRAW


Sometime late last year I came across an Ask Me Anything (AMA) thread a someone from Intel Corp. Before the 2012 US Presidential election, President Obama had performed a similar AMA thread on Reddit which quickly became a viral hit. Anyway, while browsing the Intel thread I encountered a lot of comments from users which did not add to the topic of discussion. So I wrote a scraper using Python Reddit API Wrapper which picks out the top level comment threads which have replies from the original poster (OP) and following discussions. This is quick and eliminates almost all of the useless cruft. I realise I may be missing some insightful comments by other users, but it's a tradeoff I am willing to make. Below is an excerpt from the AMA. The code is available on [github](https://github.com/snehasish/AMAScraper).

------------------


#### Question
Favourite branch predictor?

#### Answer
Bimodal.

------------------

#### Question
What is your educational and work experience background? I'm an EE undergrad and working for a place like intel sounds extremely interesting, what kind of knowledge would I need for a job like yours?

#### Answer
I have a BS and MS and have mostly worked in circuit design. Interest for the most part, willingness to learn helps a lot. We have a ton of internships every summer and you can start there as an undergrad. PM me if you want to send me your resume.

Personally, my EE coursework was very circuits-heavy. Particularly VLSI, but analog is essential to ace interviews. Comp. Arch. and device physics concentrations also help. And please, be sure you can code (any C-like language at least) and understand statistics. Skills beyond the technical are necessary to get more interesting work as well so be sure to also develop those.

#### Question
I take it you do a lot of work in Verilog? I got a taste of Computer Architecture and Chip design in my Masters program this fall as a Computer Engineer, granted it was all VHDL and just FPGAs.

But learning all about the packaging methods, development, and life-cycle planning was a blast. It was a course that was a big eye opener for me as a Software Engineer, so thanks for all your hardwork on these low levels so guys like me can keep our abstractions :P

#### Answer
Glad to have helped. Verilog and FPGAs is how I started. So you're getting there.

------------------

#### Question
How often do you get feedback from software developers concerning possible improvements in  the architecture?

#### Answer
Often. We get benchmark traces even more often. Google and Microsoft are some of the most prolific. Google on power-perf and Microsoft on compatibility issues.

------------------

#### Question
How do you feel about AMD?
(No really, let it out :))

#### Answer
They have fantastic people. I cannot underscore this enough, with the resources they have the fact that they're able to compete in the same ballpark we do shows their quality. Sadly for all of us, execution is key. We want to see an exciting marketplace as much as you do.

#### Question
You mean something like selling all of your fabrication capacity is a bad idea?

Or do they have design issues now and are falling behind?

#### Answer
AMD had to sell their fabs, otherwise they wouldn't be in business today. There are advantages to having fabs. You'll see many things, especially with Broadwell, that you cannot do without owning a fab.

The design issues we see today are things that happened a year, maybe a year-and-a-half, ago. But they were falling behind behind and it's hard to recover.

#### Question
Can you elaborate on the benefits expected for consumers using Broadwell that would not be possible without Intel owning a fab?

#### Answer
That surprise is not mine to divulge, at least not today. Sorry.

#### Question
Thanks for this :). We at AMD (especially on the GPU side) have a intense amount of respect for the engineers over at Intel. What Intel has done with their recent CPU architecture, along with the _constant_ advances in fabrication technology, they deserve a lot of credit for "keeping the ball moving forward" in our industry. 

To support jecb's argument, you often hear of negative press going on between the two companies, but that kind of animosity is largely isolated to the legal, marketing, and upper management levels. The engineers at most companies tend to have many good friends working for competitors, and while we might throw in a friendly jab every now and then, it's almost a universally friendly community. 

Thanks for this AMA. It's always cool to hear what it's like on the blue team :). 

#### Answer
Appreciate the thoughts and echo them back.

